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


class Channel(TLObject):  # type: ignore
    """Channel/supergroup info

    Constructor of :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``224``
        - ID: ``1C32B11C``

    Parameters:
        id (``int`` ``64-bit``):
            ID of the channel

        title (``str``):
            Title

        photo (:obj:`ChatPhoto <pyrogram.raw.base.ChatPhoto>`):
            Profile photo

        date (``int`` ``32-bit``):
            Date when the user joined the supergroup/channel, or if the user isn't a member, its creation date

        creator (``bool``, *optional*):
            Whether the current user is the creator of this channel

        left (``bool``, *optional*):
            Whether the current user has left or is not a member of this channel

        broadcast (``bool``, *optional*):
            Is this a channel?

        verified (``bool``, *optional*):
            Is this channel verified by telegram?

        megagroup (``bool``, *optional*):
            Is this a supergroup?

        restricted (``bool``, *optional*):
            Whether viewing/writing in this channel for a reason (see restriction_reason

        signatures (``bool``, *optional*):
            Whether signatures are enabled (channels)

        min (``bool``, *optional*):
            See min

        scam (``bool``, *optional*):
            This channel/supergroup is probably a scam

        has_link (``bool``, *optional*):
            Whether this channel has a private join link

        has_geo (``bool``, *optional*):
            Whether this chanel has a geoposition

        slowmode_enabled (``bool``, *optional*):
            Whether slow mode is enabled for groups to prevent flood in chat

        call_active (``bool``, *optional*):
            Whether a group call or livestream is currently active

        call_not_empty (``bool``, *optional*):
            Whether there's anyone in the group call or livestream

        fake (``bool``, *optional*):
            If set, this supergroup/channel was reported by many users as a fake or scam: be careful when interacting with it.

        gigagroup (``bool``, *optional*):
            Whether this supergroup is a gigagroup

        noforwards (``bool``, *optional*):
            Whether this channel or group is protected, thus does not allow forwarding messages from it

        join_to_send (``bool``, *optional*):
            Whether a user needs to join the supergroup before they can send messages: can be false only for discussion groups », toggle using channels.toggleJoinToSend

        join_request (``bool``, *optional*):
            Whether a user's join request will have to be approved by administrators, toggle using channels.toggleJoinToSend

        forum (``bool``, *optional*):
            Whether this supergroup is a forum

        stories_hidden (``bool``, *optional*):
            Whether we have hidden all stories posted by this channel ».

        stories_hidden_min (``bool``, *optional*):
            If set, indicates that the stories_hidden flag was not populated, and its value must cannot be relied on; use the previously cached value, or re-fetch the constructor using channels.getChannels to obtain the latest value of the stories_hidden flag.

        stories_unavailable (``bool``, *optional*):
            No stories from the channel are visible.

        signature_profiles (``bool``, *optional*):
            N/A

        autotranslation (``bool``, *optional*):
            N/A

        broadcast_messages_allowed (``bool``, *optional*):
            N/A

        monoforum (``bool``, *optional*):
            N/A

        forum_tabs (``bool``, *optional*):
            N/A

        access_hash (``int`` ``64-bit``, *optional*):
            Access hash

        username (``str``, *optional*):
            Username

        restriction_reason (List of :obj:`RestrictionReason <pyrogram.raw.base.RestrictionReason>`, *optional*):
            Contains the reason why access to this channel must be restricted.

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            Admin rights of the user in this channel (see rights)

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`, *optional*):
            Banned rights of the user in this channel (see rights)

        default_banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`, *optional*):
            Default chat rights (see rights)

        participants_count (``int`` ``32-bit``, *optional*):
            Participant count

        usernames (List of :obj:`Username <pyrogram.raw.base.Username>`, *optional*):
            Additional usernames

        stories_max_id (:obj:`RecentStory <pyrogram.raw.base.RecentStory>`, *optional*):
            ID of the maximum read story.

        color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):
            The channel's accent color.

        profile_color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):
            The channel's profile color.

        emoji_status (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`, *optional*):
            Emoji status

        level (``int`` ``32-bit``, *optional*):
            Boost level

        subscription_until_date (``int`` ``32-bit``, *optional*):
            N/A

        bot_verification_icon (``int`` ``64-bit``, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

        linked_monoforum_id (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "title", "photo", "date", "creator", "left", "broadcast", "verified", "megagroup", "restricted", "signatures", "min", "scam", "has_link", "has_geo", "slowmode_enabled", "call_active", "call_not_empty", "fake", "gigagroup", "noforwards", "join_to_send", "join_request", "forum", "stories_hidden", "stories_hidden_min", "stories_unavailable", "signature_profiles", "autotranslation", "broadcast_messages_allowed", "monoforum", "forum_tabs", "access_hash", "username", "restriction_reason", "admin_rights", "banned_rights", "default_banned_rights", "participants_count", "usernames", "stories_max_id", "color", "profile_color", "emoji_status", "level", "subscription_until_date", "bot_verification_icon", "send_paid_messages_stars", "linked_monoforum_id"]

    ID = 0x1c32b11c
    QUALNAME = "types.Channel"

    def __init__(self, *, id: int, title: str, photo: "raw.base.ChatPhoto", date: int, creator: Optional[bool] = None, left: Optional[bool] = None, broadcast: Optional[bool] = None, verified: Optional[bool] = None, megagroup: Optional[bool] = None, restricted: Optional[bool] = None, signatures: Optional[bool] = None, min: Optional[bool] = None, scam: Optional[bool] = None, has_link: Optional[bool] = None, has_geo: Optional[bool] = None, slowmode_enabled: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, fake: Optional[bool] = None, gigagroup: Optional[bool] = None, noforwards: Optional[bool] = None, join_to_send: Optional[bool] = None, join_request: Optional[bool] = None, forum: Optional[bool] = None, stories_hidden: Optional[bool] = None, stories_hidden_min: Optional[bool] = None, stories_unavailable: Optional[bool] = None, signature_profiles: Optional[bool] = None, autotranslation: Optional[bool] = None, broadcast_messages_allowed: Optional[bool] = None, monoforum: Optional[bool] = None, forum_tabs: Optional[bool] = None, access_hash: Optional[int] = None, username: Optional[str] = None, restriction_reason: Optional[List["raw.base.RestrictionReason"]] = None, admin_rights: "raw.base.ChatAdminRights" = None, banned_rights: "raw.base.ChatBannedRights" = None, default_banned_rights: "raw.base.ChatBannedRights" = None, participants_count: Optional[int] = None, usernames: Optional[List["raw.base.Username"]] = None, stories_max_id: "raw.base.RecentStory" = None, color: "raw.base.PeerColor" = None, profile_color: "raw.base.PeerColor" = None, emoji_status: "raw.base.EmojiStatus" = None, level: Optional[int] = None, subscription_until_date: Optional[int] = None, bot_verification_icon: Optional[int] = None, send_paid_messages_stars: Optional[int] = None, linked_monoforum_id: Optional[int] = None) -> None:
        self.id = id  # long
        self.title = title  # string
        self.photo = photo  # ChatPhoto
        self.date = date  # int
        self.creator = creator  # flags.0?true
        self.left = left  # flags.2?true
        self.broadcast = broadcast  # flags.5?true
        self.verified = verified  # flags.7?true
        self.megagroup = megagroup  # flags.8?true
        self.restricted = restricted  # flags.9?true
        self.signatures = signatures  # flags.11?true
        self.min = min  # flags.12?true
        self.scam = scam  # flags.19?true
        self.has_link = has_link  # flags.20?true
        self.has_geo = has_geo  # flags.21?true
        self.slowmode_enabled = slowmode_enabled  # flags.22?true
        self.call_active = call_active  # flags.23?true
        self.call_not_empty = call_not_empty  # flags.24?true
        self.fake = fake  # flags.25?true
        self.gigagroup = gigagroup  # flags.26?true
        self.noforwards = noforwards  # flags.27?true
        self.join_to_send = join_to_send  # flags.28?true
        self.join_request = join_request  # flags.29?true
        self.forum = forum  # flags.30?true
        self.stories_hidden = stories_hidden  # flags2.1?true
        self.stories_hidden_min = stories_hidden_min  # flags2.2?true
        self.stories_unavailable = stories_unavailable  # flags2.3?true
        self.signature_profiles = signature_profiles  # flags2.12?true
        self.autotranslation = autotranslation  # flags2.15?true
        self.broadcast_messages_allowed = broadcast_messages_allowed  # flags2.16?true
        self.monoforum = monoforum  # flags2.17?true
        self.forum_tabs = forum_tabs  # flags2.19?true
        self.access_hash = access_hash  # flags.13?long
        self.username = username  # flags.6?string
        self.restriction_reason = restriction_reason  # flags.9?Vector<RestrictionReason>
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.banned_rights = banned_rights  # flags.15?ChatBannedRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights
        self.participants_count = participants_count  # flags.17?int
        self.usernames = usernames  # flags2.0?Vector<Username>
        self.stories_max_id = stories_max_id  # flags2.4?RecentStory
        self.color = color  # flags2.7?PeerColor
        self.profile_color = profile_color  # flags2.8?PeerColor
        self.emoji_status = emoji_status  # flags2.9?EmojiStatus
        self.level = level  # flags2.10?int
        self.subscription_until_date = subscription_until_date  # flags2.11?int
        self.bot_verification_icon = bot_verification_icon  # flags2.13?long
        self.send_paid_messages_stars = send_paid_messages_stars  # flags2.14?long
        self.linked_monoforum_id = linked_monoforum_id  # flags2.18?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Channel":

        flags = Int.read(b)

        creator = True if flags & (1 << 0) else False
        left = True if flags & (1 << 2) else False
        broadcast = True if flags & (1 << 5) else False
        verified = True if flags & (1 << 7) else False
        megagroup = True if flags & (1 << 8) else False
        restricted = True if flags & (1 << 9) else False
        signatures = True if flags & (1 << 11) else False
        min = True if flags & (1 << 12) else False
        scam = True if flags & (1 << 19) else False
        has_link = True if flags & (1 << 20) else False
        has_geo = True if flags & (1 << 21) else False
        slowmode_enabled = True if flags & (1 << 22) else False
        call_active = True if flags & (1 << 23) else False
        call_not_empty = True if flags & (1 << 24) else False
        fake = True if flags & (1 << 25) else False
        gigagroup = True if flags & (1 << 26) else False
        noforwards = True if flags & (1 << 27) else False
        join_to_send = True if flags & (1 << 28) else False
        join_request = True if flags & (1 << 29) else False
        forum = True if flags & (1 << 30) else False
        flags2 = Int.read(b)

        stories_hidden = True if flags2 & (1 << 1) else False
        stories_hidden_min = True if flags2 & (1 << 2) else False
        stories_unavailable = True if flags2 & (1 << 3) else False
        signature_profiles = True if flags2 & (1 << 12) else False
        autotranslation = True if flags2 & (1 << 15) else False
        broadcast_messages_allowed = True if flags2 & (1 << 16) else False
        monoforum = True if flags2 & (1 << 17) else False
        forum_tabs = True if flags2 & (1 << 19) else False
        id = Long.read(b)

        access_hash = Long.read(b) if flags & (1 << 13) else None
        title = String.read(b)

        username = String.read(b) if flags & (1 << 6) else None
        photo = TLObject.read(b)

        date = Int.read(b)

        restriction_reason = TLObject.read(b) if flags & (1 << 9) else []

        admin_rights = TLObject.read(b) if flags & (1 << 14) else None

        banned_rights = TLObject.read(b) if flags & (1 << 15) else None

        default_banned_rights = TLObject.read(b) if flags & (1 << 18) else None

        participants_count = Int.read(b) if flags & (1 << 17) else None
        usernames = TLObject.read(b) if flags2 & (1 << 0) else []

        stories_max_id = TLObject.read(b) if flags2 & (1 << 4) else None

        color = TLObject.read(b) if flags2 & (1 << 7) else None

        profile_color = TLObject.read(b) if flags2 & (1 << 8) else None

        emoji_status = TLObject.read(b) if flags2 & (1 << 9) else None

        level = Int.read(b) if flags2 & (1 << 10) else None
        subscription_until_date = Int.read(b) if flags2 & (1 << 11) else None
        bot_verification_icon = Long.read(b) if flags2 & (1 << 13) else None
        send_paid_messages_stars = Long.read(b) if flags2 & (1 << 14) else None
        linked_monoforum_id = Long.read(b) if flags2 & (1 << 18) else None
        return Channel(id=id, title=title, photo=photo, date=date, creator=creator, left=left, broadcast=broadcast, verified=verified, megagroup=megagroup, restricted=restricted, signatures=signatures, min=min, scam=scam, has_link=has_link, has_geo=has_geo, slowmode_enabled=slowmode_enabled, call_active=call_active, call_not_empty=call_not_empty, fake=fake, gigagroup=gigagroup, noforwards=noforwards, join_to_send=join_to_send, join_request=join_request, forum=forum, stories_hidden=stories_hidden, stories_hidden_min=stories_hidden_min, stories_unavailable=stories_unavailable, signature_profiles=signature_profiles, autotranslation=autotranslation, broadcast_messages_allowed=broadcast_messages_allowed, monoforum=monoforum, forum_tabs=forum_tabs, access_hash=access_hash, username=username, restriction_reason=restriction_reason, admin_rights=admin_rights, banned_rights=banned_rights, default_banned_rights=default_banned_rights, participants_count=participants_count, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color, emoji_status=emoji_status, level=level, subscription_until_date=subscription_until_date, bot_verification_icon=bot_verification_icon, send_paid_messages_stars=send_paid_messages_stars, linked_monoforum_id=linked_monoforum_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 2) if self.left else 0
        flags |= (1 << 5) if self.broadcast else 0
        flags |= (1 << 7) if self.verified else 0
        flags |= (1 << 8) if self.megagroup else 0
        flags |= (1 << 9) if self.restricted else 0
        flags |= (1 << 11) if self.signatures else 0
        flags |= (1 << 12) if self.min else 0
        flags |= (1 << 19) if self.scam else 0
        flags |= (1 << 20) if self.has_link else 0
        flags |= (1 << 21) if self.has_geo else 0
        flags |= (1 << 22) if self.slowmode_enabled else 0
        flags |= (1 << 23) if self.call_active else 0
        flags |= (1 << 24) if self.call_not_empty else 0
        flags |= (1 << 25) if self.fake else 0
        flags |= (1 << 26) if self.gigagroup else 0
        flags |= (1 << 27) if self.noforwards else 0
        flags |= (1 << 28) if self.join_to_send else 0
        flags |= (1 << 29) if self.join_request else 0
        flags |= (1 << 30) if self.forum else 0
        flags |= (1 << 13) if self.access_hash is not None else 0
        flags |= (1 << 6) if self.username is not None else 0
        flags |= (1 << 9) if self.restriction_reason else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 15) if self.banned_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        flags |= (1 << 17) if self.participants_count is not None else 0
        b.write(Int(flags))
        flags2 = 0
        flags2 |= (1 << 1) if self.stories_hidden else 0
        flags2 |= (1 << 2) if self.stories_hidden_min else 0
        flags2 |= (1 << 3) if self.stories_unavailable else 0
        flags2 |= (1 << 12) if self.signature_profiles else 0
        flags2 |= (1 << 15) if self.autotranslation else 0
        flags2 |= (1 << 16) if self.broadcast_messages_allowed else 0
        flags2 |= (1 << 17) if self.monoforum else 0
        flags2 |= (1 << 19) if self.forum_tabs else 0
        flags2 |= (1 << 0) if self.usernames else 0
        flags2 |= (1 << 4) if self.stories_max_id is not None else 0
        flags2 |= (1 << 7) if self.color is not None else 0
        flags2 |= (1 << 8) if self.profile_color is not None else 0
        flags2 |= (1 << 9) if self.emoji_status is not None else 0
        flags2 |= (1 << 10) if self.level is not None else 0
        flags2 |= (1 << 11) if self.subscription_until_date is not None else 0
        flags2 |= (1 << 13) if self.bot_verification_icon is not None else 0
        flags2 |= (1 << 14) if self.send_paid_messages_stars is not None else 0
        flags2 |= (1 << 18) if self.linked_monoforum_id is not None else 0
        b.write(Int(flags2))

        b.write(Long(self.id))

        if self.access_hash is not None:
            b.write(Long(self.access_hash))

        b.write(String(self.title))

        if self.username is not None:
            b.write(String(self.username))

        b.write(self.photo.write())

        b.write(Int(self.date))

        if self.restriction_reason is not None:
            b.write(Vector(self.restriction_reason))

        if self.admin_rights is not None:
            b.write(self.admin_rights.write())

        if self.banned_rights is not None:
            b.write(self.banned_rights.write())

        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())

        if self.participants_count is not None:
            b.write(Int(self.participants_count))

        if self.usernames is not None:
            b.write(Vector(self.usernames))

        if self.stories_max_id is not None:
            b.write(self.stories_max_id.write())

        if self.color is not None:
            b.write(self.color.write())

        if self.profile_color is not None:
            b.write(self.profile_color.write())

        if self.emoji_status is not None:
            b.write(self.emoji_status.write())

        if self.level is not None:
            b.write(Int(self.level))

        if self.subscription_until_date is not None:
            b.write(Int(self.subscription_until_date))

        if self.bot_verification_icon is not None:
            b.write(Long(self.bot_verification_icon))

        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))

        if self.linked_monoforum_id is not None:
            b.write(Long(self.linked_monoforum_id))

        return b.getvalue()
