import re
filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# Match methods and insert assertion after docstring
# Pattern matches 'async def method(...):' followed by optional docstring
pattern = r'(async def ([a-zA-Z0-9_]+)\(self,.*?\):\n\s+(?:"""[\s\S]*?""")?)'

def repl(match):
    method_name = match.group(2)
    methods_needing_chat = [
        "click", "react", "retract_vote", "stop_poll", "reply_text", "reply_animation",
        "reply_audio", "reply_cached_media", "reply_contact", "reply_document",
        "reply_game", "reply_location", "reply_media_group", "reply_photo",
        "reply_poll", "reply_sticker", "reply_venue", "reply_video", "reply_video_note",
        "reply_voice", "edit_text", "edit_caption", "edit_media", "edit_reply_markup",
        "delete", "forward", "copy", "pin", "unpin", "ask", "pay", "translate"
    ]
    if method_name in methods_needing_chat:
        if 'assert self.chat' not in content[match.end():match.end()+100]:
             return match.group(1) + '\n        assert self.chat'
    return match.group(1)

content = re.sub(pattern, repl, content)

with open(filepath, "w") as f:
    f.write(content)
