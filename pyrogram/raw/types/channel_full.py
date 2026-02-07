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


class ChannelFull(TLObject):  # type: ignore
    """Full info about a channel, supergroup or gigagroup.

    Constructor of :obj:`~pyrogram.raw.base.ChatFull`.

    Details:
        - Layer: ``224``
        - ID: ``E4E0B29D``

    Parameters:
        id (``int`` ``64-bit``):
            ID of the channel

        about (``str``):
            Info about the channel

        read_inbox_max_id (``int`` ``32-bit``):
            Position up to which all incoming messages are read.

        read_outbox_max_id (``int`` ``32-bit``):
            Position up to which all outgoing messages are read.

        unread_count (``int`` ``32-bit``):
            Count of unread messages

        chat_photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            Channel picture

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            Notification settings

        bot_info (List of :obj:`BotInfo <pyrogram.raw.base.BotInfo>`):
            Info about bots in the channel/supergroup

        pts (``int`` ``32-bit``):
            Latest PTS for this channel

        can_view_participants (``bool``, *optional*):
            Can we view the participant list?

        can_set_username (``bool``, *optional*):
            Can we set the channel's username?

        can_set_stickers (``bool``, *optional*):
            Can we associate a stickerpack to the supergroup?

        hidden_prehistory (``bool``, *optional*):
            Is the history before we joined hidden to us?

        can_set_location (``bool``, *optional*):
            Can we set the geolocation of this group (for geogroups)

        has_scheduled (``bool``, *optional*):
            Whether scheduled messages are available

        can_view_stats (``bool``, *optional*):
            Can the user view channel/supergroup statistics

        blocked (``bool``, *optional*):
            Whether any anonymous admin of this supergroup was blocked: if set, you won't receive messages from anonymous group admins in discussion replies via @replies

        can_delete_channel (``bool``, *optional*):
            Can we delete this channel?

        antispam (``bool``, *optional*):
            Whether native antispam functionality is enabled in this supergroup.

        participants_hidden (``bool``, *optional*):
            Whether the participant list is hidden.

        translations_disabled (``bool``, *optional*):
            Whether the real-time chat translation popup should be hidden.

        stories_pinned_available (``bool``, *optional*):
            Whether this user has some pinned stories.

        view_forum_as_messages (``bool``, *optional*):
            Users may also choose to display messages from all topics of a forum as if they were sent to a normal group, using a "View as messages" setting in the local client.  This setting only affects the current account, and is synced to other logged in sessions using the channels.toggleViewForumAsMessages method; invoking this method will update the value of this flag.

        restricted_sponsored (``bool``, *optional*):


        can_view_revenue (``bool``, *optional*):


        paid_media_allowed (``bool``, *optional*):
            N/A

        can_view_stars_revenue (``bool``, *optional*):
            N/A

        paid_reactions_available (``bool``, *optional*):
            N/A

        stargifts_available (``bool``, *optional*):
            N/A

        paid_messages_available (``bool``, *optional*):
            N/A

        participants_count (``int`` ``32-bit``, *optional*):
            Number of participants of the channel

        admins_count (``int`` ``32-bit``, *optional*):
            Number of channel admins

        kicked_count (``int`` ``32-bit``, *optional*):
            Number of users kicked from the channel

        banned_count (``int`` ``32-bit``, *optional*):
            Number of users banned from the channel

        online_count (``int`` ``32-bit``, *optional*):
            Number of users currently online

        exported_invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`, *optional*):
            Invite link

        migrated_from_chat_id (``int`` ``64-bit``, *optional*):
            The chat ID from which this group was migrated

        migrated_from_max_id (``int`` ``32-bit``, *optional*):
            The message ID in the original chat at which this group was migrated

        pinned_msg_id (``int`` ``32-bit``, *optional*):
            Message ID of the last pinned message

        stickerset (:obj:`StickerSet <pyrogram.raw.base.StickerSet>`, *optional*):
            Associated stickerset

        available_min_id (``int`` ``32-bit``, *optional*):
            Identifier of a maximum unavailable message in a channel due to hidden history.

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

        linked_chat_id (``int`` ``64-bit``, *optional*):
            ID of the linked discussion chat for channels

        location (:obj:`ChannelLocation <pyrogram.raw.base.ChannelLocation>`, *optional*):
            Location of the geogroup

        slowmode_seconds (``int`` ``32-bit``, *optional*):
            If specified, users in supergroups will only be able to send one message every slowmode_seconds seconds

        slowmode_next_send_date (``int`` ``32-bit``, *optional*):
            Indicates when the user will be allowed to send another message in the supergroup (unixtime)

        stats_dc (``int`` ``32-bit``, *optional*):
            If set, specifies the DC to use for fetching channel statistics

        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`, *optional*):
            Livestream or group call information

        ttl_period (``int`` ``32-bit``, *optional*):
            Time-To-Live of messages in this channel or supergroup

        pending_suggestions (List of ``str``, *optional*):
            A list of suggested actions for the supergroup admin, see here for more info ».

        groupcall_default_join_as (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            When using phone.getGroupCallJoinAs to get a list of peers that can be used to join a group call, this field indicates the peer that should be selected by default.

        theme_emoticon (``str``, *optional*):
            Emoji representing a specific chat theme

        requests_pending (``int`` ``32-bit``, *optional*):
            Pending join requests »

        recent_requesters (List of ``int`` ``64-bit``, *optional*):
            IDs of users who requested to join recently

        default_send_as (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            Default peer used for sending messages to this channel

        available_reactions (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`, *optional*):
            Allowed message reactions »

        reactions_limit (``int`` ``32-bit``, *optional*):


        stories (:obj:`PeerStories <pyrogram.raw.base.PeerStories>`, *optional*):
            Channel stories

        wallpaper (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`, *optional*):
            Wallpaper

        boosts_applied (``int`` ``32-bit``, *optional*):


        boosts_unrestrict (``int`` ``32-bit``, *optional*):


        emojiset (:obj:`StickerSet <pyrogram.raw.base.StickerSet>`, *optional*):


        bot_verification (:obj:`BotVerification <pyrogram.raw.base.BotVerification>`, *optional*):
            N/A

        stargifts_count (``int`` ``32-bit``, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

        main_tab (:obj:`ProfileTab <pyrogram.raw.base.ProfileTab>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "about", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "chat_photo", "notify_settings", "bot_info", "pts", "can_view_participants", "can_set_username", "can_set_stickers", "hidden_prehistory", "can_set_location", "has_scheduled", "can_view_stats", "blocked", "can_delete_channel", "antispam", "participants_hidden", "translations_disabled", "stories_pinned_available", "view_forum_as_messages", "restricted_sponsored", "can_view_revenue", "paid_media_allowed", "can_view_stars_revenue", "paid_reactions_available", "stargifts_available", "paid_messages_available", "participants_count", "admins_count", "kicked_count", "banned_count", "online_count", "exported_invite", "migrated_from_chat_id", "migrated_from_max_id", "pinned_msg_id", "stickerset", "available_min_id", "folder_id", "linked_chat_id", "location", "slowmode_seconds", "slowmode_next_send_date", "stats_dc", "call", "ttl_period", "pending_suggestions", "groupcall_default_join_as", "theme_emoticon", "requests_pending", "recent_requesters", "default_send_as", "available_reactions", "reactions_limit", "stories", "wallpaper", "boosts_applied", "boosts_unrestrict", "emojiset", "bot_verification", "stargifts_count", "send_paid_messages_stars", "main_tab"]

    ID = 0xe4e0b29d
    QUALNAME = "types.ChannelFull"

    def __init__(self, *, id: int, about: str, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, chat_photo: "raw.base.Photo", notify_settings: "raw.base.PeerNotifySettings", bot_info: List["raw.base.BotInfo"], pts: int, can_view_participants: Optional[bool] = None, can_set_username: Optional[bool] = None, can_set_stickers: Optional[bool] = None, hidden_prehistory: Optional[bool] = None, can_set_location: Optional[bool] = None, has_scheduled: Optional[bool] = None, can_view_stats: Optional[bool] = None, blocked: Optional[bool] = None, can_delete_channel: Optional[bool] = None, antispam: Optional[bool] = None, participants_hidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, view_forum_as_messages: Optional[bool] = None, restricted_sponsored: Optional[bool] = None, can_view_revenue: Optional[bool] = None, paid_media_allowed: Optional[bool] = None, can_view_stars_revenue: Optional[bool] = None, paid_reactions_available: Optional[bool] = None, stargifts_available: Optional[bool] = None, paid_messages_available: Optional[bool] = None, participants_count: Optional[int] = None, admins_count: Optional[int] = None, kicked_count: Optional[int] = None, banned_count: Optional[int] = None, online_count: Optional[int] = None, exported_invite: "raw.base.ExportedChatInvite" = None, migrated_from_chat_id: Optional[int] = None, migrated_from_max_id: Optional[int] = None, pinned_msg_id: Optional[int] = None, stickerset: "raw.base.StickerSet" = None, available_min_id: Optional[int] = None, folder_id: Optional[int] = None, linked_chat_id: Optional[int] = None, location: "raw.base.ChannelLocation" = None, slowmode_seconds: Optional[int] = None, slowmode_next_send_date: Optional[int] = None, stats_dc: Optional[int] = None, call: "raw.base.InputGroupCall" = None, ttl_period: Optional[int] = None, pending_suggestions: Optional[List[str]] = None, groupcall_default_join_as: "raw.base.Peer" = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, default_send_as: "raw.base.Peer" = None, available_reactions: "raw.base.ChatReactions" = None, reactions_limit: Optional[int] = None, stories: "raw.base.PeerStories" = None, wallpaper: "raw.base.WallPaper" = None, boosts_applied: Optional[int] = None, boosts_unrestrict: Optional[int] = None, emojiset: "raw.base.StickerSet" = None, bot_verification: "raw.base.BotVerification" = None, stargifts_count: Optional[int] = None, send_paid_messages_stars: Optional[int] = None, main_tab: "raw.base.ProfileTab" = None) -> None:
        self.id = id  # long
        self.about = about  # string
        self.read_inbox_max_id = read_inbox_max_id  # int
        self.read_outbox_max_id = read_outbox_max_id  # int
        self.unread_count = unread_count  # int
        self.chat_photo = chat_photo  # Photo
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.bot_info = bot_info  # Vector<BotInfo>
        self.pts = pts  # int
        self.can_view_participants = can_view_participants  # flags.3?true
        self.can_set_username = can_set_username  # flags.6?true
        self.can_set_stickers = can_set_stickers  # flags.7?true
        self.hidden_prehistory = hidden_prehistory  # flags.10?true
        self.can_set_location = can_set_location  # flags.16?true
        self.has_scheduled = has_scheduled  # flags.19?true
        self.can_view_stats = can_view_stats  # flags.20?true
        self.blocked = blocked  # flags.22?true
        self.can_delete_channel = can_delete_channel  # flags2.0?true
        self.antispam = antispam  # flags2.1?true
        self.participants_hidden = participants_hidden  # flags2.2?true
        self.translations_disabled = translations_disabled  # flags2.3?true
        self.stories_pinned_available = stories_pinned_available  # flags2.5?true
        self.view_forum_as_messages = view_forum_as_messages  # flags2.6?true
        self.restricted_sponsored = restricted_sponsored  # flags2.11?true
        self.can_view_revenue = can_view_revenue  # flags2.12?true
        self.paid_media_allowed = paid_media_allowed  # flags2.14?true
        self.can_view_stars_revenue = can_view_stars_revenue  # flags2.15?true
        self.paid_reactions_available = paid_reactions_available  # flags2.16?true
        self.stargifts_available = stargifts_available  # flags2.19?true
        self.paid_messages_available = paid_messages_available  # flags2.20?true
        self.participants_count = participants_count  # flags.0?int
        self.admins_count = admins_count  # flags.1?int
        self.kicked_count = kicked_count  # flags.2?int
        self.banned_count = banned_count  # flags.2?int
        self.online_count = online_count  # flags.13?int
        self.exported_invite = exported_invite  # flags.23?ExportedChatInvite
        self.migrated_from_chat_id = migrated_from_chat_id  # flags.4?long
        self.migrated_from_max_id = migrated_from_max_id  # flags.4?int
        self.pinned_msg_id = pinned_msg_id  # flags.5?int
        self.stickerset = stickerset  # flags.8?StickerSet
        self.available_min_id = available_min_id  # flags.9?int
        self.folder_id = folder_id  # flags.11?int
        self.linked_chat_id = linked_chat_id  # flags.14?long
        self.location = location  # flags.15?ChannelLocation
        self.slowmode_seconds = slowmode_seconds  # flags.17?int
        self.slowmode_next_send_date = slowmode_next_send_date  # flags.18?int
        self.stats_dc = stats_dc  # flags.12?int
        self.call = call  # flags.21?InputGroupCall
        self.ttl_period = ttl_period  # flags.24?int
        self.pending_suggestions = pending_suggestions  # flags.25?Vector<string>
        self.groupcall_default_join_as = groupcall_default_join_as  # flags.26?Peer
        self.theme_emoticon = theme_emoticon  # flags.27?string
        self.requests_pending = requests_pending  # flags.28?int
        self.recent_requesters = recent_requesters  # flags.28?Vector<long>
        self.default_send_as = default_send_as  # flags.29?Peer
        self.available_reactions = available_reactions  # flags.30?ChatReactions
        self.reactions_limit = reactions_limit  # flags2.13?int
        self.stories = stories  # flags2.4?PeerStories
        self.wallpaper = wallpaper  # flags2.7?WallPaper
        self.boosts_applied = boosts_applied  # flags2.8?int
        self.boosts_unrestrict = boosts_unrestrict  # flags2.9?int
        self.emojiset = emojiset  # flags2.10?StickerSet
        self.bot_verification = bot_verification  # flags2.17?BotVerification
        self.stargifts_count = stargifts_count  # flags2.18?int
        self.send_paid_messages_stars = send_paid_messages_stars  # flags2.21?long
        self.main_tab = main_tab  # flags2.22?ProfileTab

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelFull":

        flags = Int.read(b)

        can_view_participants = True if flags & (1 << 3) else False
        can_set_username = True if flags & (1 << 6) else False
        can_set_stickers = True if flags & (1 << 7) else False
        hidden_prehistory = True if flags & (1 << 10) else False
        can_set_location = True if flags & (1 << 16) else False
        has_scheduled = True if flags & (1 << 19) else False
        can_view_stats = True if flags & (1 << 20) else False
        blocked = True if flags & (1 << 22) else False
        flags2 = Int.read(b)

        can_delete_channel = True if flags2 & (1 << 0) else False
        antispam = True if flags2 & (1 << 1) else False
        participants_hidden = True if flags2 & (1 << 2) else False
        translations_disabled = True if flags2 & (1 << 3) else False
        stories_pinned_available = True if flags2 & (1 << 5) else False
        view_forum_as_messages = True if flags2 & (1 << 6) else False
        restricted_sponsored = True if flags2 & (1 << 11) else False
        can_view_revenue = True if flags2 & (1 << 12) else False
        paid_media_allowed = True if flags2 & (1 << 14) else False
        can_view_stars_revenue = True if flags2 & (1 << 15) else False
        paid_reactions_available = True if flags2 & (1 << 16) else False
        stargifts_available = True if flags2 & (1 << 19) else False
        paid_messages_available = True if flags2 & (1 << 20) else False
        id = Long.read(b)

        about = String.read(b)

        participants_count = Int.read(b) if flags & (1 << 0) else None
        admins_count = Int.read(b) if flags & (1 << 1) else None
        kicked_count = Int.read(b) if flags & (1 << 2) else None
        banned_count = Int.read(b) if flags & (1 << 2) else None
        online_count = Int.read(b) if flags & (1 << 13) else None
        read_inbox_max_id = Int.read(b)

        read_outbox_max_id = Int.read(b)

        unread_count = Int.read(b)

        chat_photo = TLObject.read(b)

        notify_settings = TLObject.read(b)

        exported_invite = TLObject.read(b) if flags & (1 << 23) else None

        bot_info = TLObject.read(b)

        migrated_from_chat_id = Long.read(b) if flags & (1 << 4) else None
        migrated_from_max_id = Int.read(b) if flags & (1 << 4) else None
        pinned_msg_id = Int.read(b) if flags & (1 << 5) else None
        stickerset = TLObject.read(b) if flags & (1 << 8) else None

        available_min_id = Int.read(b) if flags & (1 << 9) else None
        folder_id = Int.read(b) if flags & (1 << 11) else None
        linked_chat_id = Long.read(b) if flags & (1 << 14) else None
        location = TLObject.read(b) if flags & (1 << 15) else None

        slowmode_seconds = Int.read(b) if flags & (1 << 17) else None
        slowmode_next_send_date = Int.read(b) if flags & (1 << 18) else None
        stats_dc = Int.read(b) if flags & (1 << 12) else None
        pts = Int.read(b)

        call = TLObject.read(b) if flags & (1 << 21) else None

        ttl_period = Int.read(b) if flags & (1 << 24) else None
        pending_suggestions = TLObject.read(b, String) if flags & (1 << 25) else []

        groupcall_default_join_as = TLObject.read(b) if flags & (1 << 26) else None

        theme_emoticon = String.read(b) if flags & (1 << 27) else None
        requests_pending = Int.read(b) if flags & (1 << 28) else None
        recent_requesters = TLObject.read(b, Long) if flags & (1 << 28) else []

        default_send_as = TLObject.read(b) if flags & (1 << 29) else None

        available_reactions = TLObject.read(b) if flags & (1 << 30) else None

        reactions_limit = Int.read(b) if flags2 & (1 << 13) else None
        stories = TLObject.read(b) if flags2 & (1 << 4) else None

        wallpaper = TLObject.read(b) if flags2 & (1 << 7) else None

        boosts_applied = Int.read(b) if flags2 & (1 << 8) else None
        boosts_unrestrict = Int.read(b) if flags2 & (1 << 9) else None
        emojiset = TLObject.read(b) if flags2 & (1 << 10) else None

        bot_verification = TLObject.read(b) if flags2 & (1 << 17) else None

        stargifts_count = Int.read(b) if flags2 & (1 << 18) else None
        send_paid_messages_stars = Long.read(b) if flags2 & (1 << 21) else None
        main_tab = TLObject.read(b) if flags2 & (1 << 22) else None

        return ChannelFull(id=id, about=about, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo, notify_settings=notify_settings, bot_info=bot_info, pts=pts, can_view_participants=can_view_participants, can_set_username=can_set_username, can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory, can_set_location=can_set_location, has_scheduled=has_scheduled, can_view_stats=can_view_stats, blocked=blocked, can_delete_channel=can_delete_channel, antispam=antispam, participants_hidden=participants_hidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, view_forum_as_messages=view_forum_as_messages, restricted_sponsored=restricted_sponsored, can_view_revenue=can_view_revenue, paid_media_allowed=paid_media_allowed, can_view_stars_revenue=can_view_stars_revenue, paid_reactions_available=paid_reactions_available, stargifts_available=stargifts_available, paid_messages_available=paid_messages_available, participants_count=participants_count, admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count, online_count=online_count, exported_invite=exported_invite, migrated_from_chat_id=migrated_from_chat_id, migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id, stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id, linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds, slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc, call=call, ttl_period=ttl_period, pending_suggestions=pending_suggestions, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, default_send_as=default_send_as, available_reactions=available_reactions, reactions_limit=reactions_limit, stories=stories, wallpaper=wallpaper, boosts_applied=boosts_applied, boosts_unrestrict=boosts_unrestrict, emojiset=emojiset, bot_verification=bot_verification, stargifts_count=stargifts_count, send_paid_messages_stars=send_paid_messages_stars, main_tab=main_tab)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.can_view_participants else 0
        flags |= (1 << 6) if self.can_set_username else 0
        flags |= (1 << 7) if self.can_set_stickers else 0
        flags |= (1 << 10) if self.hidden_prehistory else 0
        flags |= (1 << 16) if self.can_set_location else 0
        flags |= (1 << 19) if self.has_scheduled else 0
        flags |= (1 << 20) if self.can_view_stats else 0
        flags |= (1 << 22) if self.blocked else 0
        flags |= (1 << 0) if self.participants_count is not None else 0
        flags |= (1 << 1) if self.admins_count is not None else 0
        flags |= (1 << 2) if self.kicked_count is not None else 0
        flags |= (1 << 2) if self.banned_count is not None else 0
        flags |= (1 << 13) if self.online_count is not None else 0
        flags |= (1 << 23) if self.exported_invite is not None else 0
        flags |= (1 << 4) if self.migrated_from_chat_id is not None else 0
        flags |= (1 << 4) if self.migrated_from_max_id is not None else 0
        flags |= (1 << 5) if self.pinned_msg_id is not None else 0
        flags |= (1 << 8) if self.stickerset is not None else 0
        flags |= (1 << 9) if self.available_min_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.linked_chat_id is not None else 0
        flags |= (1 << 15) if self.location is not None else 0
        flags |= (1 << 17) if self.slowmode_seconds is not None else 0
        flags |= (1 << 18) if self.slowmode_next_send_date is not None else 0
        flags |= (1 << 12) if self.stats_dc is not None else 0
        flags |= (1 << 21) if self.call is not None else 0
        flags |= (1 << 24) if self.ttl_period is not None else 0
        flags |= (1 << 25) if self.pending_suggestions else 0
        flags |= (1 << 26) if self.groupcall_default_join_as is not None else 0
        flags |= (1 << 27) if self.theme_emoticon is not None else 0
        flags |= (1 << 28) if self.requests_pending is not None else 0
        flags |= (1 << 28) if self.recent_requesters else 0
        flags |= (1 << 29) if self.default_send_as is not None else 0
        flags |= (1 << 30) if self.available_reactions is not None else 0
        b.write(Int(flags))
        flags2 = 0
        flags2 |= (1 << 0) if self.can_delete_channel else 0
        flags2 |= (1 << 1) if self.antispam else 0
        flags2 |= (1 << 2) if self.participants_hidden else 0
        flags2 |= (1 << 3) if self.translations_disabled else 0
        flags2 |= (1 << 5) if self.stories_pinned_available else 0
        flags2 |= (1 << 6) if self.view_forum_as_messages else 0
        flags2 |= (1 << 11) if self.restricted_sponsored else 0
        flags2 |= (1 << 12) if self.can_view_revenue else 0
        flags2 |= (1 << 14) if self.paid_media_allowed else 0
        flags2 |= (1 << 15) if self.can_view_stars_revenue else 0
        flags2 |= (1 << 16) if self.paid_reactions_available else 0
        flags2 |= (1 << 19) if self.stargifts_available else 0
        flags2 |= (1 << 20) if self.paid_messages_available else 0
        flags2 |= (1 << 13) if self.reactions_limit is not None else 0
        flags2 |= (1 << 4) if self.stories is not None else 0
        flags2 |= (1 << 7) if self.wallpaper is not None else 0
        flags2 |= (1 << 8) if self.boosts_applied is not None else 0
        flags2 |= (1 << 9) if self.boosts_unrestrict is not None else 0
        flags2 |= (1 << 10) if self.emojiset is not None else 0
        flags2 |= (1 << 17) if self.bot_verification is not None else 0
        flags2 |= (1 << 18) if self.stargifts_count is not None else 0
        flags2 |= (1 << 21) if self.send_paid_messages_stars is not None else 0
        flags2 |= (1 << 22) if self.main_tab is not None else 0
        b.write(Int(flags2))

        b.write(Long(self.id))

        b.write(String(self.about))

        if self.participants_count is not None:
            b.write(Int(self.participants_count))

        if self.admins_count is not None:
            b.write(Int(self.admins_count))

        if self.kicked_count is not None:
            b.write(Int(self.kicked_count))

        if self.banned_count is not None:
            b.write(Int(self.banned_count))

        if self.online_count is not None:
            b.write(Int(self.online_count))

        b.write(Int(self.read_inbox_max_id))

        b.write(Int(self.read_outbox_max_id))

        b.write(Int(self.unread_count))

        b.write(self.chat_photo.write())

        b.write(self.notify_settings.write())

        if self.exported_invite is not None:
            b.write(self.exported_invite.write())

        b.write(Vector(self.bot_info))

        if self.migrated_from_chat_id is not None:
            b.write(Long(self.migrated_from_chat_id))

        if self.migrated_from_max_id is not None:
            b.write(Int(self.migrated_from_max_id))

        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))

        if self.stickerset is not None:
            b.write(self.stickerset.write())

        if self.available_min_id is not None:
            b.write(Int(self.available_min_id))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        if self.linked_chat_id is not None:
            b.write(Long(self.linked_chat_id))

        if self.location is not None:
            b.write(self.location.write())

        if self.slowmode_seconds is not None:
            b.write(Int(self.slowmode_seconds))

        if self.slowmode_next_send_date is not None:
            b.write(Int(self.slowmode_next_send_date))

        if self.stats_dc is not None:
            b.write(Int(self.stats_dc))

        b.write(Int(self.pts))

        if self.call is not None:
            b.write(self.call.write())

        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))

        if self.pending_suggestions is not None:
            b.write(Vector(self.pending_suggestions, String))

        if self.groupcall_default_join_as is not None:
            b.write(self.groupcall_default_join_as.write())

        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))

        if self.requests_pending is not None:
            b.write(Int(self.requests_pending))

        if self.recent_requesters is not None:
            b.write(Vector(self.recent_requesters, Long))

        if self.default_send_as is not None:
            b.write(self.default_send_as.write())

        if self.available_reactions is not None:
            b.write(self.available_reactions.write())

        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))

        if self.stories is not None:
            b.write(self.stories.write())

        if self.wallpaper is not None:
            b.write(self.wallpaper.write())

        if self.boosts_applied is not None:
            b.write(Int(self.boosts_applied))

        if self.boosts_unrestrict is not None:
            b.write(Int(self.boosts_unrestrict))

        if self.emojiset is not None:
            b.write(self.emojiset.write())

        if self.bot_verification is not None:
            b.write(self.bot_verification.write())

        if self.stargifts_count is not None:
            b.write(Int(self.stargifts_count))

        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))

        if self.main_tab is not None:
            b.write(self.main_tab.write())

        return b.getvalue()
