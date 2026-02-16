import re
import os

filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# Fix imports
if "from typing import TYPE_CHECKING, BinaryIO" in content:
    content = content.replace("from typing import TYPE_CHECKING, BinaryIO", "from typing import TYPE_CHECKING, Any, BinaryIO, cast")

# 1. Fix get_raw_peer_id calls
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
    'cast(raw.base.InputUser, await client.resolve_peer(from_id)) if from_id else None,'
)
content = content.replace(
    'await client.resolve_peer(peer_id),',
    'cast(raw.base.InputUser, await client.resolve_peer(peer_id)) if peer_id else None,'
)

# 3. Fix Photo._parse call in actions
content = content.replace(
    'new_chat_photo = types.Photo._parse(client, action.photo)',
    'new_chat_photo = types.Photo._parse(client, action.photo) if isinstance(action.photo, raw.types.Photo) else None'
)

# 4. Fix GiveawayLaunched._parse
content = content.replace(
    'giveaway_launched = types.GiveawayLaunched._parse(client, action)',
    'giveaway_launched = types.GiveawayLaunched()'
)

# 5. Fix from_user.id at GIFTED_PREMIUM
content = content.replace(
    'gifted_premium = await types.GiftedPremium._parse(\n                    client,\n                    action,\n                    from_user.id,\n                )',
    'gifted_premium = await types.GiftedPremium._parse(\n                    client,\n                    action,\n                    from_user.id if from_user else 0,\n                )'
)

# 6. Fix chats_shared
content = content.replace(
    'chats_shared=chats_shared,',
    'chats_shared=cast(list[types.RequestedChats], [chats_shared]) if isinstance(chats_shared, types.RequestedChats) else None,'
)

# 7. Fix raw cast in parsed_message
content = content.replace(
    'raw=message,',
    'raw=cast(raw.types.Message, message),'
)

# 8. Fix Poll attributes
# Insert logic before "return parsed_message"
content = content.replace(
    '            return parsed_message',
    '            if parsed_message.poll:\n                parsed_message.poll.chat = parsed_message.chat\n                parsed_message.poll.message_id = parsed_message.id\n            return parsed_message'
)

with open(filepath, "w") as f:
    f.write(content)
