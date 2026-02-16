import re

filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# Remove branches for missing types
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionSetChatTheme\):.*?service_type = enums\.MessageServiceType\.CHAT_THEME_UPDATED\n', '', content, flags=re.DOTALL)
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionSetChatWallPaper\):.*?service_type = enums\.MessageServiceType\.CHAT_WALLPAPER_UPDATED\n', '', content, flags=re.DOTALL)
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionGiftCode\):.*?service_type = enums\.MessageServiceType\.GIFT_CODE\n', '', content, flags=re.DOTALL)

# Remove redundant StarGift branch (keep USER_GIFT)
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionStarGift\):.*?star_gift = await types\.StarGift\._parse_action\(.*?\)\s+service_type = enums\.MessageServiceType\.STAR_GIFT\n', '', content, flags=re.DOTALL)

# Remove attributes from Message call
for attr in ['chat_theme_updated', 'chat_wallpaper_updated', 'gift_code', 'star_gift']:
    content = re.sub(f'                {attr}={attr},\n', '', content)

# Populate Poll attributes
content = content.replace(
    '            return parsed_message',
    '            if parsed_message.poll:\n                parsed_message.poll.chat = parsed_message.chat\n                parsed_message.poll.message_id = parsed_message.id\n            return parsed_message'
)

# Fix some more diagnostics in _parse
content = content.replace(
    'location = types.Location._parse(client, media.geo)',
    'location = types.Location._parse(client, media.geo) if isinstance(media.geo, raw.types.GeoPoint) else None'
)
content = content.replace(
    'poll = await types.Poll._parse(client, media, users)',
    'poll = await types.Poll._parse(client, media, cast(dict, users))'
)
content = content.replace(
    'invoice = types.Invoice._parse(media)',
    'invoice = types.Invoice._parse(client, media)'
)

# Add assertions for chat usage
content = re.sub(r'if parsed_message\.chat\.type', r'assert parsed_message.chat\n            if parsed_message.chat.type', content)
content = re.sub(r'if rtci is not None and parsed_message\.chat\.id', r'assert parsed_message.chat\n                if rtci is not None and parsed_message.chat.id', content)
content = re.sub(r'key = \(\s+parsed_message\.chat\.id,', r'assert parsed_message.chat\n                            key = (\n                                parsed_message.chat.id,', content)

with open(filepath, "w") as f:
    f.write(content)
