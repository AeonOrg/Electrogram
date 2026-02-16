import re
import os

filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# Remove missing attributes from constructor calls
content = re.sub(r'                chat_theme_updated=chat_theme_updated,\n', '', content)
content = re.sub(r'                chat_wallpaper_updated=chat_wallpaper_updated,\n', '', content)
content = re.sub(r'                gift_code=gift_code,\n', '', content)
content = re.sub(r'                star_gift=star_gift,\n', '', content)

# Remove the branches that use these attributes
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionSetChatTheme\):.*?service_type = enums\.MessageServiceType\.CHAT_THEME_UPDATED\n', '', content, flags=re.DOTALL)
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionSetChatWallPaper\):.*?service_type = enums\.MessageServiceType\.CHAT_WALLPAPER_UPDATED\n', '', content, flags=re.DOTALL)
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionGiftCode\):.*?service_type = enums\.MessageServiceType\.GIFT_CODE\n', '', content, flags=re.DOTALL)

# Fix StarGift branches - wait, there were two of them?
content = re.sub(r'            elif isinstance\(action, raw\.types\.MessageActionStarGift\):.*?star_gift = await types\.StarGift\._parse_action\(.*?\) \n                service_type = enums\.MessageServiceType\.STAR_GIFT\n', '', content, flags=re.DOTALL)

# Add assertions before chat usage
content = re.sub(r'if parsed_message\.chat\.type', r'assert parsed_message.chat\n            if parsed_message.chat.type', content)
content = re.sub(r'parsed_message\.chat\.id', r'assert parsed_message.chat\n                        parsed_message.chat.id', content)
content = re.sub(r'parsed_message\.chat\.is_forum', r'assert parsed_message.chat\n            if parsed_message.chat.is_forum', content)

# Fix Poll attributes
# Insert logic before "return parsed_message"
content = re.sub(r'            return parsed_message', r'            if parsed_message.poll:\n                parsed_message.poll.chat = parsed_message.chat\n                parsed_message.poll.message_id = parsed_message.id\n            return parsed_message', content)

with open(filepath, "w") as f:
    f.write(content)
