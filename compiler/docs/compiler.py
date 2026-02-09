from __future__ import annotations

import ast
import os
import re
import shutil
from pathlib import Path

# Paths
HOME = "compiler/docs"
DESTINATION = "docs/source/telegram"
PYROGRAM_API_DEST = "docs/source/api"

FUNCTIONS_PATH = "pyrogram/raw/functions"
TYPES_PATH = "pyrogram/raw/types"
BASE_PATH = "pyrogram/raw/base"

FUNCTIONS_BASE = "functions"
TYPES_BASE = "types"
BASE_BASE = "base"

METHODS_PATH = "pyrogram/methods"
TYPES_LIB_PATH = "pyrogram/types"
ENUMS_LIB_PATH = "pyrogram/enums"

# Titles mapping for categories that need a pretty name
METHODS_TITLES = {
    "auth": "Authorization",
    "business": "Telegram Business",
}

TYPES_TITLES = {
    "bots_and_keyboards": "Bot keyboards",
    "bot_commands": "Bot commands",
    "business": "Telegram Business",
    "messages_and_media": "Messages & Media",
    "user_and_chats": "Users & Chats",
    "input_message_content": "Input Message Content",
    "input_privacy_rule": "Input Privacy Rule",
}


def snake(s: str):
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def generate_raw(source_path, base) -> None:
    all_entities = {}

    def build(path, level=0) -> None:
        last = path.split("/")[-1]

        for i in os.listdir(path):
            try:
                if not i.startswith("__"):
                    build("/".join([path, i]), level=level + 1)
            except NotADirectoryError:
                with Path(path, i).open(encoding="utf-8") as f:
                    p = ast.parse(f.read())

                for node in ast.walk(p):
                    if isinstance(node, ast.ClassDef):
                        name = node.name
                        break
                else:
                    continue

                full_path = (
                    Path(path).name + "/" + snake(name).replace("_", "-") + ".rst"
                )

                if level:
                    full_path = base + "/" + full_path

                namespace = path.split("/")[-1]
                if namespace in ["base", "types", "functions"]:
                    namespace = ""

                full_name = f"{(namespace + '.') if namespace else ''}{name}"

                Path(DESTINATION, full_path).parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                with Path(DESTINATION, full_path).open("w", encoding="utf-8") as f:
                    f.write(
                        page_template.format(
                            title=full_name,
                            title_markup="=" * len(full_name),
                            full_class_path="pyrogram.raw.{}".format(
                                ".".join(full_path.split("/")[:-1]) + "." + name,
                            ),
                        ),
                    )

                if last not in all_entities:
                    all_entities[last] = []

                all_entities[last].append(name)

    build(source_path)

    for k, v in sorted(all_entities.items()):
        v = sorted(v)
        entities = [f"{i} <{snake(i).replace('_', '-')}>" for i in v]

        if k != base:
            inner_path = base + "/" + k + "/index" + ".rst"
            module = f"pyrogram.raw.{base}.{k}"
        else:
            for i in sorted(all_entities, reverse=True):
                if i != base:
                    entities.insert(0, f"{i}/index")

            inner_path = base + "/index" + ".rst"
            module = f"pyrogram.raw.{base}"

        with Path(DESTINATION, inner_path).open("w", encoding="utf-8") as f:
            if k == base:
                f.write(":tocdepth: 1\n\n")
                k = "Raw " + k

            f.write(
                toctree.format(
                    title=k.title(),
                    title_markup="=" * len(k),
                    module=module,
                    entities="\n    ".join(entities),
                ),
            )

            f.write("\n")


def pyrogram_api() -> None:
    # Discovery logic

    methods_categories = {}
    methods_path = Path(METHODS_PATH)
    if not methods_path.exists():
        methods_path = Path("../../") / METHODS_PATH

    for entry in sorted(methods_path.iterdir()):
        if entry.is_dir() and entry.name != "decorators":
            category_name = entry.name
            methods = []
            for file in sorted(entry.glob("*.py")):
                if file.name == "__init__.py":
                    continue

                # Check if it defines a class or is special function (idle, compose)
                with open(file, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())

                has_class = any(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
                is_special = file.stem in ["idle", "compose"]

                if has_class or is_special:
                    methods.append(file.stem)

            if methods:
                title = METHODS_TITLES.get(
                    category_name,
                    category_name.replace("_", " ").title(),
                )
                methods_categories[category_name] = (title, methods)

    types_categories = {}
    types_lib_path = Path(TYPES_LIB_PATH)
    if not types_lib_path.exists():
        types_lib_path = Path("../../") / TYPES_LIB_PATH

    for entry in sorted(types_lib_path.iterdir()):
        if entry.is_dir():
            category_name = entry.name
            types = []
            for file in sorted(entry.glob("*.py")):
                if file.name == "__init__.py":
                    continue
                with Path(file).open(encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read())
                    except Exception:
                        continue
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        types.append(node.name)
            if types:
                title = TYPES_TITLES.get(
                    category_name,
                    category_name.replace("_", " ").title(),
                )
                types_categories[category_name] = (title, sorted(types))

    bound_methods_categories = {}
    for file in sorted(types_lib_path.rglob("*.py")):
        if file.name == "__init__.py":
            continue
        with Path(file).open(encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read())
            except Exception:
                continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                class_bound_methods = []
                for item in node.body:
                    if isinstance(item, (ast.AsyncFunctionDef, ast.FunctionDef)):
                        docstring = ast.get_docstring(item)
                        if docstring and "Bound method" in docstring:
                            class_bound_methods.append(f"{class_name}.{item.name}")
                if class_bound_methods:
                    if class_name not in bound_methods_categories:
                        bound_methods_categories[class_name] = []
                    bound_methods_categories[class_name].extend(
                        sorted(class_bound_methods),
                    )

    enums_lib_path = Path(ENUMS_LIB_PATH)
    if not enums_lib_path.exists():
        enums_lib_path = Path("../../") / ENUMS_LIB_PATH

    enums_list = []
    for file in sorted(enums_lib_path.glob("*.py")):
        if file.name in ["__init__.py", "auto_name.py"]:
            continue
        with Path(file).open(encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read())
            except Exception:
                continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                enums_list.append(node.name)

    # Methods Generation

    root = PYROGRAM_API_DEST + "/methods"
    shutil.rmtree(root, ignore_errors=True)
    Path(root).mkdir(parents=True, exist_ok=True)

    with Path(root, "index.rst").open("w", encoding="utf-8") as f:
        f.write("Available Methods\n=================\n\n")
        f.write(
            "This page is about Electrogram methods. All the methods listed here are bound to a :class:`~pyrogram.Client` instance,\n",
        )
        f.write(
            "except for :meth:`~pyrogram.idle()` and :meth:`~pyrogram.compose()`, which are special functions that can be found in\n",
        )
        f.write("the main package directly.\n\n")
        f.write(".. code-block:: python\n\n")
        f.write("    from pyrogram import Client\n\n")
        f.write('    app = Client("my_account")\n\n')
        f.write("    with app:\n")
        f.write('        app.send_message("me", "hi")\n\n')
        f.write("-----\n\n")

        for cat_name, (title, methods) in methods_categories.items():
            if cat_name == "utilities":
                f.write(".. currentmodule:: pyrogram.Client\n\n")
                f.write(f"{title}\n" + "-" * len(title) + "\n\n")
                f.write(".. autosummary::\n    :nosignatures:\n\n")
                for m in sorted(methods):
                    if m not in ["idle", "compose"]:
                        f.write(f"    {m}\n")
                f.write("\n.. toctree::\n    :hidden:\n\n")
                for m in sorted(methods):
                    if m not in ["idle", "compose"]:
                        f.write(f"    {m} <{m}>\n")
                f.write("\n.. currentmodule:: pyrogram\n\n")
                f.write(".. autosummary::\n    :nosignatures:\n\n")
                if "idle" in methods:
                    f.write("    idle\n")
                if "compose" in methods:
                    f.write("    compose\n")
                f.write("\n.. toctree::\n    :hidden:\n\n")
                if "idle" in methods:
                    f.write("    idle <idle>\n")
                if "compose" in methods:
                    f.write("    compose <compose>\n")
                f.write("\n")
            else:
                f.write(".. currentmodule:: pyrogram.Client\n\n")
                f.write(f"{title}\n" + "-" * len(title) + "\n\n")
                if cat_name == "advanced":
                    f.write(
                        "Methods used only when dealing with the raw Telegram API.\n",
                    )
                    f.write(
                        "Learn more about how to use the raw API at :doc:`Advanced Usage <../../topics/advanced-usage>`.\n\n",
                    )
                f.write(".. autosummary::\n    :nosignatures:\n\n")
                for m in sorted(methods):
                    f.write(f"    {m}\n")
                f.write("\n.. toctree::\n    :hidden:\n\n")
                for m in sorted(methods):
                    f.write(f"    {m} <{m}>\n")
                f.write("\n")

            for m in methods:
                with Path(root, f"{m}.rst").open("w", encoding="utf-8") as f2:
                    title_m = f"{m}()"
                    f2.write(title_m + "\n" + "=" * len(title_m) + "\n\n")
                    if m in ["idle", "compose"]:
                        f2.write(f".. autofunction:: pyrogram.{m}()")
                    else:
                        f2.write(f".. automethod:: pyrogram.Client.{m}()")

    # Types Generation

    root = PYROGRAM_API_DEST + "/types"
    shutil.rmtree(root, ignore_errors=True)
    Path(root).mkdir(parents=True, exist_ok=True)

    with Path(root, "index.rst").open("w", encoding="utf-8") as f:
        f.write("Available Types\n===============\n\n")
        f.write(
            "This page is about Electrogram Types. All types listed here are available through the ``pyrogram.types`` package.\n",
        )
        f.write(
            "Unless required as argument to a client method, most of the types don't need to be manually instantiated because they\n",
        )
        f.write(
            "are only returned by other methods. You also don't need to import them, unless you want to type-hint your variables.\n\n",
        )
        f.write(".. code-block:: python\n\n")
        f.write("    from pyrogram.types import User, Message, ...\n\n")
        f.write(".. note::\n\n")
        f.write(
            "    Optional fields always exist inside the object, but they could be empty and contain the value of ``None``.\n",
        )
        f.write(
            "    Empty fields aren't shown when, for example, using ``print(message)`` and this means that\n",
        )
        f.write(
            '    ``hasattr(message, "photo")`` always returns ``True``.\n\n',
        )
        f.write(
            "    To tell whether a field is set or not, do a simple boolean check: ``if message.photo: ...``.\n\n"
        )
        f.write("-----\n\n")
        f.write(".. currentmodule:: pyrogram.types\n\n")

        for cat_name, (title, t_list) in sorted(types_categories.items()):
            f.write(f"{title}\n" + "-" * len(title) + "\n\n")
            f.write(".. autosummary::\n    :nosignatures:\n\n")
            for t in sorted(t_list):
                f.write(f"    {t}\n")
            f.write("\n.. toctree::\n    :hidden:\n\n")
            for t in sorted(t_list):
                f.write(f"    {t} <{t}>\n")
            f.write("\n")

            for t in t_list:
                with Path(root, f"{t}.rst").open("w", encoding="utf-8") as f2:
                    f2.write(t + "\n" + "=" * len(t) + "\n\n")
                    f2.write(f".. autoclass:: pyrogram.types.{t}()\n")

    # Bound Methods Generation

    root = PYROGRAM_API_DEST + "/bound-methods"
    shutil.rmtree(root, ignore_errors=True)
    Path(root).mkdir(parents=True, exist_ok=True)

    with Path(root, "index.rst").open("w", encoding="utf-8") as f:
        f.write("Bound Methods\n=============\n\n")
        f.write(
            "Some Electrogram types define what are called bound methods. Bound methods are functions attached to a type which are\n",
        )
        f.write(
            "accessed via an instance of that type. They make it even easier to call specific methods by automatically inferring\n",
        )
        f.write("some of the required arguments.\n\n")
        f.write(".. code-block:: python\n\n")
        f.write("    from pyrogram import Client\n\n")
        f.write('    app = Client("my_account")\n\n\n')
        f.write("    @app.on_message()\n")
        f.write("    def hello(client, message)\n")
        f.write('        message.reply("hi")\n\n\n')
        f.write("    app.run()\n\n")
        f.write("-----\n\n")
        f.write(".. currentmodule:: pyrogram.types\n\n")

        for class_name, bound_methods in sorted(bound_methods_categories.items()):
            f.write(f"{class_name}\n" + "-" * len(class_name) + "\n\n")
            f.write(".. hlist::\n    :columns: 1\n\n")
            for bm in sorted(bound_methods):
                f.write(f"    - :meth:`~{bm}`\n")
            f.write("\n.. toctree::\n    :hidden:\n\n")
            for bm in sorted(bound_methods):
                f.write(f"    {bm.split('.')[1]} <{bm}>\n")
            f.write("\n")

            for bm in bound_methods:
                with Path(root, f"{bm}.rst").open("w", encoding="utf-8") as f2:
                    title_bm = f"{bm}()"
                    f2.write(title_bm + "\n" + "=" * len(title_bm) + "\n\n")
                    f2.write(f".. automethod:: pyrogram.types.{bm}()")

    # Enums Generation

    if enums_list:
        root = PYROGRAM_API_DEST + "/enums"
        shutil.rmtree(root, ignore_errors=True)
        Path(root).mkdir(parents=True, exist_ok=True)

        with Path(root, "index.rst").open("w", encoding="utf-8") as f:
            f.write("Available Enums\n===============\n\n")
            f.write(".. currentmodule:: pyrogram.enums\n\n")
            f.write(".. autosummary::\n    :nosignatures:\n\n")
            for e in sorted(enums_list):
                f.write(f"    {e}\n")
            f.write("\n.. toctree::\n    :hidden:\n\n")
            for e in sorted(enums_list):
                f.write(f"    {e} <{e}>\n")

        for e in enums_list:
            with Path(root, f"{e}.rst").open("w", encoding="utf-8") as f2:
                f2.write(e + "\n" + "=" * len(e) + "\n\n")
                f2.write(f".. autoclass:: pyrogram.enums.{e}()\n    :members:\n")


def start() -> None:
    global page_template, toctree  # noqa: PLW0603

    shutil.rmtree(DESTINATION, ignore_errors=True)

    with Path(HOME, "template/page.txt").open(encoding="utf-8") as f:
        page_template = f.read()

    with Path(HOME, "template/toctree.txt").open(encoding="utf-8") as f:
        toctree = f.read()

    generate_raw(TYPES_PATH, TYPES_BASE)
    generate_raw(FUNCTIONS_PATH, FUNCTIONS_BASE)
    generate_raw(BASE_PATH, BASE_BASE)
    pyrogram_api()


if __name__ == "__main__":
    FUNCTIONS_PATH = "../../pyrogram/raw/functions"
    TYPES_PATH = "../../pyrogram/raw/types"
    BASE_PATH = "../../pyrogram/raw/base"
    METHODS_PATH = "../../pyrogram/methods"
    TYPES_LIB_PATH = "../../pyrogram/types"
    ENUMS_LIB_PATH = "../../pyrogram/enums"
    HOME = "."
    DESTINATION = "../../docs/source/telegram"
    PYROGRAM_API_DEST = "../../docs/source/api"

    start()
