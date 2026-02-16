import re
import os

filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# 1. Add assertions for self.chat in bound methods
# We can find methods and add assert self.chat at the beginning.
methods_needing_chat = [
    "click", "react", "retract_vote", "stop_poll", "reply_text", "reply_animation",
    "reply_audio", "reply_cached_media", "reply_contact", "reply_document",
    "reply_game", "reply_location", "reply_media_group", "reply_photo",
    "reply_poll", "reply_sticker", "reply_venue", "reply_video", "reply_video_note",
    "reply_voice", "edit_text", "edit_caption", "edit_media", "edit_reply_markup",
    "delete", "forward", "copy", "pin", "unpin", "ask", "pay", "translate"
]

for method in methods_needing_chat:
    pattern = r'async def ' + method + r'\(.*?\):'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        insertion_point = match.end()
        # Find docstring end or method start
        doc_match = re.search(r'""".*?迅"""', content[insertion_point:], re.DOTALL) # wait, that's wrong
        # Let's just look for the first line after docstring or if no docstring, first line.
        lines = content[insertion_point:].split('\n')
        in_doc = False
        idx = 0
        for i, line in enumerate(lines):
            if '"""' in line:
                if not in_doc:
                    in_doc = True
                else:
                    in_doc = False
                    idx = i + 1
                    break
        else:
            idx = 1

        new_lines = lines[:idx] + ['        assert self.chat'] + lines[idx:]
        content = content[:insertion_point] + '\n'.join(new_lines)

# 2. Fix the click method button attribute accesses
# This is hard with regex. I'll use string replacement for specific lines.

content = content.replace(
    'if button.callback_data:',
    'if isinstance(button, types.InlineKeyboardButton) and button.callback_data:'
)
content = content.replace(
    'if button.requires_password:',
    'if isinstance(button, types.InlineKeyboardButton) and button.requires_password:'
)
content = content.replace(
    'if button.url:',
    'if isinstance(button, (types.InlineKeyboardButton, types.InlineKeyboardButtonBuy)) and button.url:'
)
content = content.replace(
    'if button.web_app:',
    'if isinstance(button, types.InlineKeyboardButton) and button.web_app:'
)
content = content.replace(
    'if button.user_id:',
    'if isinstance(button, types.InlineKeyboardButton) and button.user_id:'
)
content = content.replace(
    'if button.switch_inline_query:',
    'if isinstance(button, types.InlineKeyboardButton) and button.switch_inline_query:'
)
content = content.replace(
    'if button.switch_inline_query_current_chat:',
    'if isinstance(button, types.InlineKeyboardButton) and button.switch_inline_query_current_chat:'
)

# Fix await self.reply(text=button, quote=quote)
content = content.replace(
    'await self.reply(text=button, quote=quote)',
    'await self.reply(text=cast(str, button), quote=quote)'
)

# 3. Fix download return type and translate return type
content = content.replace(
    ') -> str | BinaryIO:',
    ') -> str | BinaryIO | None:'
)
content = content.replace(
    'return await self._client.translate_message_text(',
    'return cast(types.TranslatedText, await self._client.translate_message_text('
)
# Add closing parenthesis for cast
# This is tricky because it's multi-line.
# Let's try to match the whole block.
content = re.sub(
    r'(return cast\(types\.TranslatedText, await self\._client\.translate_message_text\(.*?\))(\s+)\)',
    r'\1\2))',
    content,
    flags=re.DOTALL
)

with open(filepath, "w") as f:
    f.write(content)
