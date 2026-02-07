from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UserFull(TLObject):  # type: ignore
    """Extended user info

    Constructor of :obj:`~pyrogram.raw.base.UserFull`.

    Details:
        - Layer: ``224``
        - ID: ``A02BC13E``

    Parameters:
        id (``int`` ``64-bit``):
            User ID

        settings (:obj:`PeerSettings <pyrogram.raw.base.PeerSettings>`):
            Peer settings

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            Notification settings

        common_chats_count (``int`` ``32-bit``):
            Chats in common with this user

        blocked (``bool``, *optional*):
            Whether you have blocked this user

        phone_calls_available (``bool``, *optional*):
            Whether this user can make VoIP calls

        phone_calls_private (``bool``, *optional*):
            Whether this user's privacy settings allow you to call them

        can_pin_message (``bool``, *optional*):
            Whether you can pin messages in the chat with this user, you can do this only for a chat with yourself

        has_scheduled (``bool``, *optional*):
            Whether scheduled messages are available

        video_calls_available (``bool``, *optional*):
            Whether the user can receive video calls

        voice_messages_forbidden (``bool``, *optional*):
            Whether this user doesn't allow sending voice messages in a private chat with them

        translations_disabled (``bool``, *optional*):
            Whether the real-time chat translation popup should be hidden.

        stories_pinned_available (``bool``, *optional*):
            Whether this user has some pinned stories.

        blocked_my_stories_from (``bool``, *optional*):
            Whether we've blocked this user, preventing them from seeing our stories ».

        wallpaper_overridden (``bool``, *optional*):
            Whether the other user has chosen a custom wallpaper for us using messages.setChatWallPaper and the for_both flag, see here » for more info.

        contact_require_premium (``bool``, *optional*):


        read_dates_private (``bool``, *optional*):


        sponsored_enabled (``bool``, *optional*):


        can_view_revenue (``bool``, *optional*):
            N/A

        bot_can_manage_emoji_status (``bool``, *optional*):
            N/A

        display_gifts_button (``bool``, *optional*):
            N/A

        about (``str``, *optional*):
            Bio of the user

        personal_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            Personal profile photo, to be shown instead of profile_photo.

        profile_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            Profile photo

        fallback_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            Fallback profile photo, displayed if no photo is present in profile_photo or personal_photo, due to privacy settings.

        bot_info (:obj:`BotInfo <pyrogram.raw.base.BotInfo>`, *optional*):
            For bots, info about the bot (bot commands, etc)

        pinned_msg_id (``int`` ``32-bit``, *optional*):
            Message ID of the last pinned message

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

        ttl_period (``int`` ``32-bit``, *optional*):
            Time To Live of all messages in this chat; once a message is this many seconds old, it must be deleted.

        theme (:obj:`ChatTheme <pyrogram.raw.base.ChatTheme>`, *optional*):
            N/A

        private_forward_name (``str``, *optional*):
            Anonymized text to be shown instead of the user's name on forwarded messages

        bot_group_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            A suggested set of administrator rights for the bot, to be shown when adding the bot as admin to a group, see here for more info on how to handle them ».

        bot_broadcast_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            A suggested set of administrator rights for the bot, to be shown when adding the bot as admin to a channel, see here for more info on how to handle them ».

        wallpaper (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`, *optional*):
            Wallpaper to use in the private chat with the user.

        stories (:obj:`PeerStories <pyrogram.raw.base.PeerStories>`, *optional*):
            Active stories »

        business_work_hours (:obj:`BusinessWorkHours <pyrogram.raw.base.BusinessWorkHours>`, *optional*):


        business_location (:obj:`BusinessLocation <pyrogram.raw.base.BusinessLocation>`, *optional*):


        business_greeting_message (:obj:`BusinessGreetingMessage <pyrogram.raw.base.BusinessGreetingMessage>`, *optional*):


        business_away_message (:obj:`BusinessAwayMessage <pyrogram.raw.base.BusinessAwayMessage>`, *optional*):


        business_intro (:obj:`BusinessIntro <pyrogram.raw.base.BusinessIntro>`, *optional*):


        birthday (:obj:`Birthday <pyrogram.raw.base.Birthday>`, *optional*):


        personal_channel_id (``int`` ``64-bit``, *optional*):


        personal_channel_message (``int`` ``32-bit``, *optional*):


        stargifts_count (``int`` ``32-bit``, *optional*):
            N/A

        starref_program (:obj:`StarRefProgram <pyrogram.raw.base.StarRefProgram>`, *optional*):
            N/A

        bot_verification (:obj:`BotVerification <pyrogram.raw.base.BotVerification>`, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

        disallowed_gifts (:obj:`DisallowedGiftsSettings <pyrogram.raw.base.DisallowedGiftsSettings>`, *optional*):
            N/A

        stars_rating (:obj:`StarsRating <pyrogram.raw.base.StarsRating>`, *optional*):
            N/A

        stars_my_pending_rating (:obj:`StarsRating <pyrogram.raw.base.StarsRating>`, *optional*):
            N/A

        stars_my_pending_rating_date (``int`` ``32-bit``, *optional*):
            N/A

        main_tab (:obj:`ProfileTab <pyrogram.raw.base.ProfileTab>`, *optional*):
            N/A

        saved_music (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        note (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "settings", "notify_settings", "common_chats_count", "blocked", "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled", "video_calls_available", "voice_messages_forbidden", "translations_disabled", "stories_pinned_available", "blocked_my_stories_from", "wallpaper_overridden", "contact_require_premium", "read_dates_private", "sponsored_enabled", "can_view_revenue", "bot_can_manage_emoji_status", "display_gifts_button", "about", "personal_photo", "profile_photo", "fallback_photo", "bot_info", "pinned_msg_id", "folder_id", "ttl_period", "theme", "private_forward_name", "bot_group_admin_rights", "bot_broadcast_admin_rights", "wallpaper", "stories", "business_work_hours", "business_location", "business_greeting_message", "business_away_message", "business_intro", "birthday", "personal_channel_id", "personal_channel_message", "stargifts_count", "starref_program", "bot_verification", "send_paid_messages_stars", "disallowed_gifts", "stars_rating", "stars_my_pending_rating", "stars_my_pending_rating_date", "main_tab", "saved_music", "note"]

    ID = 0xa02bc13e
    QUALNAME = "types.UserFull"

    def __init__(self, *, id: int, settings: "raw.base.PeerSettings", notify_settings: "raw.base.PeerNotifySettings", common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, voice_messages_forbidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, wallpaper_overridden: Optional[bool] = None, contact_require_premium: Optional[bool] = None, read_dates_private: Optional[bool] = None, sponsored_enabled: Optional[bool] = None, can_view_revenue: Optional[bool] = None, bot_can_manage_emoji_status: Optional[bool] = None, display_gifts_button: Optional[bool] = None, about: Optional[str] = None, personal_photo: "raw.base.Photo" = None, profile_photo: "raw.base.Photo" = None, fallback_photo: "raw.base.Photo" = None, bot_info: "raw.base.BotInfo" = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme: "raw.base.ChatTheme" = None, private_forward_name: Optional[str] = None, bot_group_admin_rights: "raw.base.ChatAdminRights" = None, bot_broadcast_admin_rights: "raw.base.ChatAdminRights" = None, wallpaper: "raw.base.WallPaper" = None, stories: "raw.base.PeerStories" = None, business_work_hours: "raw.base.BusinessWorkHours" = None, business_location: "raw.base.BusinessLocation" = None, business_greeting_message: "raw.base.BusinessGreetingMessage" = None, business_away_message: "raw.base.BusinessAwayMessage" = None, business_intro: "raw.base.BusinessIntro" = None, birthday: "raw.base.Birthday" = None, personal_channel_id: Optional[int] = None, personal_channel_message: Optional[int] = None, stargifts_count: Optional[int] = None, starref_program: "raw.base.StarRefProgram" = None, bot_verification: "raw.base.BotVerification" = None, send_paid_messages_stars: Optional[int] = None, disallowed_gifts: "raw.base.DisallowedGiftsSettings" = None, stars_rating: "raw.base.StarsRating" = None, stars_my_pending_rating: "raw.base.StarsRating" = None, stars_my_pending_rating_date: Optional[int] = None, main_tab: "raw.base.ProfileTab" = None, saved_music: "raw.base.Document" = None, note: "raw.base.TextWithEntities" = None) -> None:
        self.id = id  # long
        self.settings = settings  # PeerSettings
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.common_chats_count = common_chats_count  # int
        self.blocked = blocked  # flags.0?true
        self.phone_calls_available = phone_calls_available  # flags.4?true
        self.phone_calls_private = phone_calls_private  # flags.5?true
        self.can_pin_message = can_pin_message  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.12?true
        self.video_calls_available = video_calls_available  # flags.13?true
        self.voice_messages_forbidden = voice_messages_forbidden  # flags.20?true
        self.translations_disabled = translations_disabled  # flags.23?true
        self.stories_pinned_available = stories_pinned_available  # flags.26?true
        self.blocked_my_stories_from = blocked_my_stories_from  # flags.27?true
        self.wallpaper_overridden = wallpaper_overridden  # flags.28?true
        self.contact_require_premium = contact_require_premium  # flags.29?true
        self.read_dates_private = read_dates_private  # flags.30?true
        self.sponsored_enabled = sponsored_enabled  # flags2.7?true
        self.can_view_revenue = can_view_revenue  # flags2.9?true
        self.bot_can_manage_emoji_status = bot_can_manage_emoji_status  # flags2.10?true
        self.display_gifts_button = display_gifts_button  # flags2.16?true
        self.about = about  # flags.1?string
        self.personal_photo = personal_photo  # flags.21?Photo
        self.profile_photo = profile_photo  # flags.2?Photo
        self.fallback_photo = fallback_photo  # flags.22?Photo
        self.bot_info = bot_info  # flags.3?BotInfo
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.folder_id = folder_id  # flags.11?int
        self.ttl_period = ttl_period  # flags.14?int
        self.theme = theme  # flags.15?ChatTheme
        self.private_forward_name = private_forward_name  # flags.16?string
        self.bot_group_admin_rights = bot_group_admin_rights  # flags.17?ChatAdminRights
        self.bot_broadcast_admin_rights = bot_broadcast_admin_rights  # flags.18?ChatAdminRights
        self.wallpaper = wallpaper  # flags.24?WallPaper
        self.stories = stories  # flags.25?PeerStories
        self.business_work_hours = business_work_hours  # flags2.0?BusinessWorkHours
        self.business_location = business_location  # flags2.1?BusinessLocation
        self.business_greeting_message = business_greeting_message  # flags2.2?BusinessGreetingMessage
        self.business_away_message = business_away_message  # flags2.3?BusinessAwayMessage
        self.business_intro = business_intro  # flags2.4?BusinessIntro
        self.birthday = birthday  # flags2.5?Birthday
        self.personal_channel_id = personal_channel_id  # flags2.6?long
        self.personal_channel_message = personal_channel_message  # flags2.6?int
        self.stargifts_count = stargifts_count  # flags2.8?int
        self.starref_program = starref_program  # flags2.11?StarRefProgram
        self.bot_verification = bot_verification  # flags2.12?BotVerification
        self.send_paid_messages_stars = send_paid_messages_stars  # flags2.14?long
        self.disallowed_gifts = disallowed_gifts  # flags2.15?DisallowedGiftsSettings
        self.stars_rating = stars_rating  # flags2.17?StarsRating
        self.stars_my_pending_rating = stars_my_pending_rating  # flags2.18?StarsRating
        self.stars_my_pending_rating_date = stars_my_pending_rating_date  # flags2.18?int
        self.main_tab = main_tab  # flags2.20?ProfileTab
        self.saved_music = saved_music  # flags2.21?Document
        self.note = note  # flags2.22?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserFull":

        flags = Int.read(b)

        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        video_calls_available = True if flags & (1 << 13) else False
        voice_messages_forbidden = True if flags & (1 << 20) else False
        translations_disabled = True if flags & (1 << 23) else False
        stories_pinned_available = True if flags & (1 << 26) else False
        blocked_my_stories_from = True if flags & (1 << 27) else False
        wallpaper_overridden = True if flags & (1 << 28) else False
        contact_require_premium = True if flags & (1 << 29) else False
        read_dates_private = True if flags & (1 << 30) else False
        flags2 = Int.read(b)

        sponsored_enabled = True if flags2 & (1 << 7) else False
        can_view_revenue = True if flags2 & (1 << 9) else False
        bot_can_manage_emoji_status = True if flags2 & (1 << 10) else False
        display_gifts_button = True if flags2 & (1 << 16) else False
        id = Long.read(b)

        about = String.read(b) if flags & (1 << 1) else None
        settings = TLObject.read(b)

        personal_photo = TLObject.read(b) if flags & (1 << 21) else None

        profile_photo = TLObject.read(b) if flags & (1 << 2) else None

        fallback_photo = TLObject.read(b) if flags & (1 << 22) else None

        notify_settings = TLObject.read(b)

        bot_info = TLObject.read(b) if flags & (1 << 3) else None

        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        common_chats_count = Int.read(b)

        folder_id = Int.read(b) if flags & (1 << 11) else None
        ttl_period = Int.read(b) if flags & (1 << 14) else None
        theme = TLObject.read(b) if flags & (1 << 15) else None

        private_forward_name = String.read(b) if flags & (1 << 16) else None
        bot_group_admin_rights = TLObject.read(b) if flags & (1 << 17) else None

        bot_broadcast_admin_rights = TLObject.read(b) if flags & (1 << 18) else None

        wallpaper = TLObject.read(b) if flags & (1 << 24) else None

        stories = TLObject.read(b) if flags & (1 << 25) else None

        business_work_hours = TLObject.read(b) if flags2 & (1 << 0) else None

        business_location = TLObject.read(b) if flags2 & (1 << 1) else None

        business_greeting_message = TLObject.read(b) if flags2 & (1 << 2) else None

        business_away_message = TLObject.read(b) if flags2 & (1 << 3) else None

        business_intro = TLObject.read(b) if flags2 & (1 << 4) else None

        birthday = TLObject.read(b) if flags2 & (1 << 5) else None

        personal_channel_id = Long.read(b) if flags2 & (1 << 6) else None
        personal_channel_message = Int.read(b) if flags2 & (1 << 6) else None
        stargifts_count = Int.read(b) if flags2 & (1 << 8) else None
        starref_program = TLObject.read(b) if flags2 & (1 << 11) else None

        bot_verification = TLObject.read(b) if flags2 & (1 << 12) else None

        send_paid_messages_stars = Long.read(b) if flags2 & (1 << 14) else None
        disallowed_gifts = TLObject.read(b) if flags2 & (1 << 15) else None

        stars_rating = TLObject.read(b) if flags2 & (1 << 17) else None

        stars_my_pending_rating = TLObject.read(b) if flags2 & (1 << 18) else None

        stars_my_pending_rating_date = Int.read(b) if flags2 & (1 << 18) else None
        main_tab = TLObject.read(b) if flags2 & (1 << 20) else None

        saved_music = TLObject.read(b) if flags2 & (1 << 21) else None

        note = TLObject.read(b) if flags2 & (1 << 22) else None

        return UserFull(id=id, settings=settings, notify_settings=notify_settings, common_chats_count=common_chats_count, blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, voice_messages_forbidden=voice_messages_forbidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, blocked_my_stories_from=blocked_my_stories_from, wallpaper_overridden=wallpaper_overridden, contact_require_premium=contact_require_premium, read_dates_private=read_dates_private, sponsored_enabled=sponsored_enabled, can_view_revenue=can_view_revenue, bot_can_manage_emoji_status=bot_can_manage_emoji_status, display_gifts_button=display_gifts_button, about=about, personal_photo=personal_photo, profile_photo=profile_photo, fallback_photo=fallback_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, ttl_period=ttl_period, theme=theme, private_forward_name=private_forward_name, bot_group_admin_rights=bot_group_admin_rights, bot_broadcast_admin_rights=bot_broadcast_admin_rights, wallpaper=wallpaper, stories=stories, business_work_hours=business_work_hours, business_location=business_location, business_greeting_message=business_greeting_message, business_away_message=business_away_message, business_intro=business_intro, birthday=birthday, personal_channel_id=personal_channel_id, personal_channel_message=personal_channel_message, stargifts_count=stargifts_count, starref_program=starref_program, bot_verification=bot_verification, send_paid_messages_stars=send_paid_messages_stars, disallowed_gifts=disallowed_gifts, stars_rating=stars_rating, stars_my_pending_rating=stars_my_pending_rating, stars_my_pending_rating_date=stars_my_pending_rating_date, main_tab=main_tab, saved_music=saved_music, note=note)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 4) if self.phone_calls_available else 0
        flags |= (1 << 5) if self.phone_calls_private else 0
        flags |= (1 << 7) if self.can_pin_message else 0
        flags |= (1 << 12) if self.has_scheduled else 0
        flags |= (1 << 13) if self.video_calls_available else 0
        flags |= (1 << 20) if self.voice_messages_forbidden else 0
        flags |= (1 << 23) if self.translations_disabled else 0
        flags |= (1 << 26) if self.stories_pinned_available else 0
        flags |= (1 << 27) if self.blocked_my_stories_from else 0
        flags |= (1 << 28) if self.wallpaper_overridden else 0
        flags |= (1 << 29) if self.contact_require_premium else 0
        flags |= (1 << 30) if self.read_dates_private else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 21) if self.personal_photo is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 22) if self.fallback_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.ttl_period is not None else 0
        flags |= (1 << 15) if self.theme is not None else 0
        flags |= (1 << 16) if self.private_forward_name is not None else 0
        flags |= (1 << 17) if self.bot_group_admin_rights is not None else 0
        flags |= (1 << 18) if self.bot_broadcast_admin_rights is not None else 0
        flags |= (1 << 24) if self.wallpaper is not None else 0
        flags |= (1 << 25) if self.stories is not None else 0
        b.write(Int(flags))
        flags2 = 0
        flags2 |= (1 << 7) if self.sponsored_enabled else 0
        flags2 |= (1 << 9) if self.can_view_revenue else 0
        flags2 |= (1 << 10) if self.bot_can_manage_emoji_status else 0
        flags2 |= (1 << 16) if self.display_gifts_button else 0
        flags2 |= (1 << 0) if self.business_work_hours is not None else 0
        flags2 |= (1 << 1) if self.business_location is not None else 0
        flags2 |= (1 << 2) if self.business_greeting_message is not None else 0
        flags2 |= (1 << 3) if self.business_away_message is not None else 0
        flags2 |= (1 << 4) if self.business_intro is not None else 0
        flags2 |= (1 << 5) if self.birthday is not None else 0
        flags2 |= (1 << 6) if self.personal_channel_id is not None else 0
        flags2 |= (1 << 6) if self.personal_channel_message is not None else 0
        flags2 |= (1 << 8) if self.stargifts_count is not None else 0
        flags2 |= (1 << 11) if self.starref_program is not None else 0
        flags2 |= (1 << 12) if self.bot_verification is not None else 0
        flags2 |= (1 << 14) if self.send_paid_messages_stars is not None else 0
        flags2 |= (1 << 15) if self.disallowed_gifts is not None else 0
        flags2 |= (1 << 17) if self.stars_rating is not None else 0
        flags2 |= (1 << 18) if self.stars_my_pending_rating is not None else 0
        flags2 |= (1 << 18) if self.stars_my_pending_rating_date is not None else 0
        flags2 |= (1 << 20) if self.main_tab is not None else 0
        flags2 |= (1 << 21) if self.saved_music is not None else 0
        flags2 |= (1 << 22) if self.note is not None else 0
        b.write(Int(flags2))

        b.write(Long(self.id))

        if self.about is not None:
            b.write(String(self.about))

        b.write(self.settings.write())

        if self.personal_photo is not None:
            b.write(self.personal_photo.write())

        if self.profile_photo is not None:
            b.write(self.profile_photo.write())

        if self.fallback_photo is not None:
            b.write(self.fallback_photo.write())

        b.write(self.notify_settings.write())

        if self.bot_info is not None:
            b.write(self.bot_info.write())

        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))

        b.write(Int(self.common_chats_count))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))

        if self.theme is not None:
            b.write(self.theme.write())

        if self.private_forward_name is not None:
            b.write(String(self.private_forward_name))

        if self.bot_group_admin_rights is not None:
            b.write(self.bot_group_admin_rights.write())

        if self.bot_broadcast_admin_rights is not None:
            b.write(self.bot_broadcast_admin_rights.write())

        if self.wallpaper is not None:
            b.write(self.wallpaper.write())

        if self.stories is not None:
            b.write(self.stories.write())

        if self.business_work_hours is not None:
            b.write(self.business_work_hours.write())

        if self.business_location is not None:
            b.write(self.business_location.write())

        if self.business_greeting_message is not None:
            b.write(self.business_greeting_message.write())

        if self.business_away_message is not None:
            b.write(self.business_away_message.write())

        if self.business_intro is not None:
            b.write(self.business_intro.write())

        if self.birthday is not None:
            b.write(self.birthday.write())

        if self.personal_channel_id is not None:
            b.write(Long(self.personal_channel_id))

        if self.personal_channel_message is not None:
            b.write(Int(self.personal_channel_message))

        if self.stargifts_count is not None:
            b.write(Int(self.stargifts_count))

        if self.starref_program is not None:
            b.write(self.starref_program.write())

        if self.bot_verification is not None:
            b.write(self.bot_verification.write())

        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))

        if self.disallowed_gifts is not None:
            b.write(self.disallowed_gifts.write())

        if self.stars_rating is not None:
            b.write(self.stars_rating.write())

        if self.stars_my_pending_rating is not None:
            b.write(self.stars_my_pending_rating.write())

        if self.stars_my_pending_rating_date is not None:
            b.write(Int(self.stars_my_pending_rating_date))

        if self.main_tab is not None:
            b.write(self.main_tab.write())

        if self.saved_music is not None:
            b.write(self.saved_music.write())

        if self.note is not None:
            b.write(self.note.write())

        return b.getvalue()
