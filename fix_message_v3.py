import re
import os

filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# Fix imports
if "from typing import TYPE_CHECKING, Any, BinaryIO" in content:
    content = content.replace("from typing import TYPE_CHECKING, Any, BinaryIO", "from typing import TYPE_CHECKING, Any, BinaryIO, cast")
elif "from typing import TYPE_CHECKING, BinaryIO" in content:
    content = content.replace("from typing import TYPE_CHECKING, BinaryIO", "from typing import TYPE_CHECKING, Any, BinaryIO, cast")

# 1. Fix get_raw_peer_id calls at 785-786
content = content.replace(
    'from_id = utils.get_raw_peer_id(message.from_id)',
    'from_id = utils.get_raw_peer_id(message.from_id) if message.from_id else None'
)
content = content.replace(
    'peer_id = utils.get_raw_peer_id(message.peer_id)',
    'peer_id = utils.get_raw_peer_id(message.peer_id) if message.peer_id else None'
)

# 2. Fix resolve_peer calls in GetUsers
content = content.replace(
    'await client.resolve_peer(from_id),',
    'cast(raw.base.InputUser, await client.resolve_peer(from_id)),'
)
content = content.replace(
    'await client.resolve_peer(peer_id),',
    'cast(raw.base.InputUser, await client.resolve_peer(peer_id)),'
)

# 3. Fix line 870 (or similar)
content = content.replace(
    'users[utils.get_raw_peer_id(message.from_id)]',
    'users.get(utils.get_raw_peer_id(message.from_id)) if message.from_id else None'
)

# 4. Fix new_chat_members list parsing
content = content.replace(
    'new_chat_members = [\n                    types.User._parse(client, users[i]) for i in action.users\n                ]',
    'new_chat_members = cast(list[types.User], [types.User._parse(client, users.get(i)) for i in action.users])'
)

# 5. Fix Photo._parse call
content = content.replace(
    'new_chat_photo = types.Photo._parse(client, action.photo)',
    'new_chat_photo = types.Photo._parse(client, action.photo) if isinstance(action.photo, raw.types.Photo) else None'
)

# 6. Fix from_user.id at GIFTED_PREMIUM
content = content.replace(
    'from_user.id,',
    'from_user.id if from_user else 0,'
)

# 7. Fix GiveawayLaunched._parse
content = content.replace(
    'giveaway_launched = types.GiveawayLaunched._parse(client, action)',
    'giveaway_launched = types.GiveawayLaunched()'
)

# 8. Fix chats_shared
content = content.replace(
    'chats_shared=chats_shared,',
    'chats_shared=cast(list[types.RequestedChats], [chats_shared]) if isinstance(chats_shared, types.RequestedChats) else None,'
)

# 9. Fix raw cast in parsed_message
content = content.replace(
    'raw=message,',
    'raw=cast(raw.types.Message, message),'
)

# 10. Add assertions for chat
content = re.sub(r'([ \t]+)if parsed_message\.chat\.type', r'\1assert parsed_message.chat\n\1if parsed_message.chat.type', content)
content = re.sub(r'([ \t]+)parsed_message\.chat\.id', r'\1assert parsed_message.chat\n\1parsed_message.chat.id', content)

# 11. Fix Poll attribute population
# I'll do this by finding where Message is returned and inserting logic before it.
# Actually, it's better to do it right after parsed_message is created.

content = content.replace(
    '            return parsed_message',
    '            if parsed_message.poll:\n                parsed_message.poll.chat = parsed_message.chat\n                parsed_message.poll.message_id = parsed_message.id\n            return parsed_message'
)

with open(filepath, "w") as f:
    f.write(content)
