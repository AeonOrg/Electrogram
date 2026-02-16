import re
filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# Fix parameters with None default but no | None in annotation
content = content.replace('reply_markup: types.InlineKeyboardMarkup = None', 'reply_markup: types.InlineKeyboardMarkup | None = None')
content = content.replace('explanation_parse_mode: enums.ParseMode = None', 'explanation_parse_mode: enums.ParseMode | None = None')

# Fix complex types in parameters
# reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply = None
# This occurs in many methods.
content = re.sub(
    r'(reply_markup: types\.InlineKeyboardMarkup\s+\| types\.ReplyKeyboardMarkup\s+\| types\.ReplyKeyboardRemove\s+\| types\.ForceReply) = None',
    r'\1 | None = None',
    content
)

# Fix copy method specifically
content = content.replace(
    'reply_markup: types.InlineKeyboardMarkup\n        | types.ReplyKeyboardMarkup\n        | types.ReplyKeyboardRemove\n        | types.ForceReply = object,',
    'reply_markup: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove | types.ForceReply | Any = object,'
)

# Cast returns in copy() and edit_media()
content = content.replace(
    'return await self._client.edit_message_media(',
    'return cast(Message, await self._client.edit_message_media('
)
# Note: I'll need to make sure I add 'from pyrogram.types.messages_and_media.message import Message' or just use 'Message' if it's already there.
# But it's in the same file.

with open(filepath, "w") as f:
    f.write(content)
