import re
filepath = "pyrogram/types/messages_and_media/message.py"
with open(filepath, "r") as f:
    content = f.read()

# 1. Fix click method button label comparison
content = content.replace(
    'if label == button.text',
    'if not isinstance(button, str) and label == button.text'
)

# 2. Fix InlineKeyboardButtonBuy url access
content = content.replace(
    'if isinstance(button, (types.InlineKeyboardButton, types.InlineKeyboardButtonBuy)) and button.url:',
    'if isinstance(button, types.InlineKeyboardButton) and button.url:'
)

# 3. Fix download/translate return type casts (making sure they are correct)
# I already did some, let's check.

# 4. Fix copy method return types
# The problem is that it returns Message | list[Message] but some branches return None or result of methods that might return None.
# Actually, I should cast the returns in copy().

# 5. Fix venue parameters
content = content.replace(
    'foursquare_id=self.venue.foursquare_id,',
    'foursquare_id=self.venue.foursquare_id or "",'
)
content = content.replace(
    'foursquare_type=self.venue.foursquare_type,',
    'foursquare_type=self.venue.foursquare_type or "",'
)

# 6. Fix more assertions or casts if needed

with open(filepath, "w") as f:
    f.write(content)
