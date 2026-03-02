import re
from pathlib import Path
from typing import List, Dict, Set, NamedTuple

CORE_TYPES = {
    "int", "long", "int128", "int256", "double", "bytes", "string", "Bool", "true"
}

class Argument(NamedTuple):
    name: str
    type: str

class Combinator(NamedTuple):
    section: str
    qualname: str
    id: str
    args: List[Argument]
    qualtype: str
    full_line: str

def camel(s: str):
    return "".join(i[0].upper() + i[1:] for i in s.split("_"))

class TLDocGenerator:
    def __init__(self, tl_files: List[Path]):
        self.combinators = self._parse_tl(tl_files)
        self.name_to_comb = {}
        self.base_to_constructors = {}
        for c in self.combinators:
            ns, name = c.qualname.split(".") if "." in c.qualname else ("", c.qualname)
            camel_name = ".".join([ns, camel(name)]).lstrip(".")
            self.name_to_comb[camel_name] = c
            if c.section == "types":
                base = c.qualtype
                bns, bname = base.split(".") if "." in base else ("", base)
                camel_base = ".".join([bns, camel(bname)]).lstrip(".")
                if camel_base not in self.base_to_constructors:
                    self.base_to_constructors[camel_base] = []
                self.base_to_constructors[camel_base].append(camel_name)

    def _parse_tl(self, tl_files: List[Path]) -> List[Combinator]:
        combinators = []
        section = "types"
        COMBINATOR_RE = re.compile(r"^([\w.]+)#([0-9a-f]+)\s(?:.*)=\s([\w<>.]+);$")
        SECTION_RE = re.compile(r"---(\w+)---")

        for tl_file in tl_files:
            with tl_file.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    if section_match := SECTION_RE.match(line):
                        section = section_match.group(1)
                        continue
                    if line.startswith("//"): continue

                    if combinator_match := COMBINATOR_RE.match(line):
                        qualname, cid, qualtype = combinator_match.groups()
                        parts = line.split(" ")
                        args = []
                        for part in parts[1:]:
                            if part == "=": break
                            if ":" in part:
                                arg_name, arg_type = part.split(":", 1)
                                # Fix reserved keywords
                                if arg_name == "self": arg_name = "is_self"
                                if arg_name == "from": arg_name = "from_peer"
                                args.append(Argument(arg_name, arg_type))
                        combinators.append(Combinator(section, qualname, cid, args, qualtype, line))
        return combinators

    def get_tl_signature(self, name: str) -> str:
        c = self.name_to_comb.get(name)
        if not c: return ""

        line = c.full_line.replace(";", "")
        # Split into name#id parts and result type
        if " = " in line:
            main_part, res_type = line.split(" = ", 1)
            parts = main_part.split(" ")
            res = [parts[0]] # name#id
            for p in parts[1:]:
                if p: res.append("    " + p)
            res.append("= " + res_type)
            return "\n".join(res)
        return line

    def get_full_class_path(self, name: str):
        c = self.name_to_comb.get(name)
        if c:
            directory = "types" if c.section == "types" else "functions"
            return f"pyrogram.raw.{directory}.{name}"
        if name in self.base_to_constructors:
            return f"pyrogram.raw.base.{name}"
        return name

    def get_type_link(self, t: str):
        if t in CORE_TYPES:
            return f"``{t}``"
        if t.startswith("Vector<"):
            inner = t[7:-1]
            return f"``Vector`` < {self.get_type_link(inner)} >"
        full_path = self.get_full_class_path(t)
        return f":obj:`{t} <{full_path}>`"

    def generate_tree(self, name: str) -> str:
        res = [f"| **{name.split('.')[-1]}**"]
        # Check if it is a base type or function/constructor
        is_base = name in self.base_to_constructors and name not in self.name_to_comb
        res.extend(self._generate_tree_recursive(name, 0, "", set(), is_base=is_base))
        return "\n".join(res)

    def _generate_tree_recursive(self, name: str, depth: int, prefix: str, visited: Set[str], is_vector_item: bool = False, is_base: bool = False) -> List[str]:
        if depth > 12: return []

        # Prevent cycles
        if name in visited and depth > 5: return []
        new_visited = visited | {name}

        res = []
        c = self.name_to_comb.get(name)

        if is_vector_item:
            # If it's a vector item, we always want to show its name/type line first
            if name in self.base_to_constructors:
                constrs = self.base_to_constructors[name]
                for i, constr in enumerate(constrs):
                    is_last = (i == len(constrs) - 1)
                    res.append(f"| {prefix}{'└── ' if is_last else '├── '}{self.get_type_link(constr)}")
                    if depth < 4:
                        res.extend(self._generate_tree_recursive(constr, depth + 1, prefix + ("    " if is_last else "│   "), new_visited, is_base=False))
            else:
                res.append(f"| {prefix}└── {self.get_type_link(name)}")
                res.extend(self._generate_tree_recursive(name, depth + 1, prefix + "    ", new_visited, is_base=False))
            return res

        if is_base and name in self.base_to_constructors:
            constrs = self.base_to_constructors[name]
            limit_expansion = name in ["InputPeer", "InputUser", "InputChannel", "InputFile", "InputMedia", "MessageEntity"]

            for i, constr in enumerate(constrs):
                is_last = (i == len(constrs) - 1)
                res.append(f"| {prefix}{'└── ' if is_last else '├── '}{self.get_type_link(constr)}")
                if depth < 4 and (not limit_expansion or depth < 2):
                    res.extend(self._generate_tree_recursive(constr, depth + 1, prefix + ("    " if is_last else "│   "), new_visited, is_base=False))
            return res

        # It's a constructor or function
        if not c: return []

        # Common constructors that we don't want to expand everywhere
        if name in ["InputPeerSelf", "InputPeerEmpty", "InputPeerChat", "InputUserSelf", "InputUserEmpty"] and depth > 2:
            return []

        filtered_args = [a for a in c.args if not (a.name.startswith("flags") and a.type == "#")]
        for i, arg in enumerate(filtered_args):
            is_last = (i == len(filtered_args) - 1)
            arg_type = arg.type
            is_optional = "?" in arg_type
            if is_optional: arg_type = arg_type.split("?")[1]

            line = f"| {prefix}{'└── ' if is_last else '├── '}**{arg.name}** → {self.get_type_link(arg_type)}"
            if is_optional: line += " (*optional*)"
            res.append(line)

            if arg_type.startswith("Vector<"):
                inner = arg_type[7:-1]
                if inner not in CORE_TYPES:
                    res.extend(self._generate_tree_recursive(inner, depth + 1, prefix + ("    " if is_last else "│   "), new_visited, is_vector_item=True))
            elif arg_type not in CORE_TYPES:
                # If the type is a base type, we want to show its constructors
                is_arg_base = arg_type in self.base_to_constructors
                res.extend(self._generate_tree_recursive(arg_type, depth + 1, prefix + ("    " if is_last else "│   "), new_visited, is_base=is_arg_base))

        return res

    def get_default_value(self, arg_name, arg_type, depth=0, visited=None, minimal=False):
        if visited is None: visited = set()
        is_optional = "?" in arg_type
        if is_optional: arg_type = arg_type.split("?")[1]

        if minimal and is_optional:
            return "None"

        if not minimal and is_optional and depth > 0:
            # Prune some to avoid explosion, but keep key ones
            if arg_name not in ["rows", "buttons", "text", "url", "peer", "message", "random_id", "id"]:
                return "None"

        if arg_type == "string":
            if arg_name == "message": return '"Hello"'
            if arg_name == "url": return '"https://google.com"'
            if arg_name == "phone": return '"+1234567890"'
            if arg_name == "text": return '"Open"'
            return '"text"'
        if arg_type == "int": return "0"
        if arg_type == "long":
            if arg_name == "random_id": return "app.rnd_id()"
            return "0"
        if arg_type == "double": return "0.0"
        if arg_type == "bytes": return 'b"data"'
        if arg_type in ["Bool", "true"]:
            if is_optional and depth == 0: return "None"
            return "True"

        if arg_type.startswith("Vector<"):
            inner = arg_type[7:-1]
            val = self.get_default_value(arg_name, inner, depth + 1, visited.copy(), minimal=minimal)
            indent = "    " * (depth + 1)
            item_indent = "    " * (depth + 2)
            if inner not in CORE_TYPES:
                return f"[\n{item_indent}{val.replace('\n', '\n' + '    ')}\n{indent}]"
            return f"[{val}]"

        if arg_type == "InputPeer": return "await app.resolve_peer(chat_id)"
        if arg_type == "InputUser": return "await app.resolve_user(chat_id)"
        if arg_type == "InputChannel": return "await app.resolve_channel(chat_id)"

        if depth > 6: return "None" if is_optional else "None"

        target_type = arg_type
        if target_type in self.base_to_constructors:
            constrs = self.base_to_constructors[target_type]
            mapping = {"ReplyMarkup": "ReplyInlineMarkup", "KeyboardButton": "KeyboardButtonUrl", "KeyboardButtonRow": "KeyboardButtonRow"}
            target_type = mapping.get(target_type, constrs[0])

        c = self.name_to_comb.get(target_type)
        if c:
            args_code = []
            for arg in c.args:
                if arg.name.startswith("flags") and arg.type == "#": continue
                val = self.get_default_value(arg.name, arg.type, depth + 1, visited.copy(), minimal=minimal)
                if minimal and val == "None" and "?" in arg.type:
                    continue
                args_code.append(f"{arg.name}={val}")
            name_only = target_type.split(".")[-1]
            if len(args_code) > 1:
                indent = "    " * (depth + 1)
                inner = (",\n" + indent).join(args_code)
                return f"{name_only}(\n{indent}{inner}\n{'    ' * depth})"
            return f"{name_only}({', '.join(args_code)})"
        return "None" if is_optional else "None"

    def generate_example(self, name: str, minimal: bool = False) -> str:
        c = self.name_to_comb.get(name)
        if not c: return ""
        if c.section != "functions" and c.section != "types": return ""
        name_only = name.split(".")[-1]

        if c.section == "functions":
            res = [".. code-block:: python", "", "    await app.invoke(", f"        {name_only}("]
            indent = "            "
        else:
            res = [".. code-block:: python", "", f"    {name_only}("]
            indent = "        "

        args_lines = []
        filtered_args = [a for a in c.args if not (a.name.startswith("flags") and a.type == "#")]
        for arg in filtered_args:
            is_optional = "?" in arg.type
            if minimal and is_optional:
                continue

            val = self.get_default_value(arg.name, arg.type, 0, minimal=minimal)
            if "\n" in val: val = val.replace("\n", "\n" + indent)
            args_lines.append(f"{indent}{arg.name}={val},")

        res.extend(args_lines)
        if c.section == "functions":
            res.append("        )\n    )")
        else:
            res.append("    )")
        return "\n".join(res)
