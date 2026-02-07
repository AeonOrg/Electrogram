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


class PeerSettings(TLObject):  # type: ignore
    """List of actions that are possible when interacting with this user, to be shown as suggested actions in the chat action bar », see here » for more info.

    Constructor of :obj:`~pyrogram.raw.base.PeerSettings`.

    Details:
        - Layer: ``224``
        - ID: ``F47741F7``

    Parameters:
        report_spam (``bool``, *optional*):
            Whether we can still report the user for spam

        add_contact (``bool``, *optional*):
            Whether we can add the user as contact

        block_contact (``bool``, *optional*):
            Whether we can block the user

        share_contact (``bool``, *optional*):
            Whether we can share the user's contact

        need_contacts_exception (``bool``, *optional*):
            Whether a special exception for contacts is needed

        report_geo (``bool``, *optional*):
            Whether we can report a geogroup as irrelevant for this location

        autoarchived (``bool``, *optional*):
            Whether this peer was automatically archived according to privacy settings and can be unarchived

        invite_members (``bool``, *optional*):
            If set, this is a recently created group chat to which new members can be invited

        request_chat_broadcast (``bool``, *optional*):
            This flag is set if request_chat_title and request_chat_date fields are set and the join request » is related to a channel (otherwise if only the request fields are set, the join request » is related to a chat).

        business_bot_paused (``bool``, *optional*):


        business_bot_can_reply (``bool``, *optional*):


        geo_distance (``int`` ``32-bit``, *optional*):
            Distance in meters between us and this peer

        request_chat_title (``str``, *optional*):
            If set, this is a private chat with an administrator of a chat or channel to which the user sent a join request, and this field contains the chat/channel's title.

        request_chat_date (``int`` ``32-bit``, *optional*):
            If set, this is a private chat with an administrator of a chat or channel to which the user sent a join request, and this field contains the timestamp when the join request » was sent.

        business_bot_id (``int`` ``64-bit``, *optional*):


        business_bot_manage_url (``str``, *optional*):


        charge_paid_message_stars (``int`` ``64-bit``, *optional*):
            N/A

        registration_month (``str``, *optional*):
            N/A

        phone_country (``str``, *optional*):
            N/A

        name_change_date (``int`` ``32-bit``, *optional*):
            N/A

        photo_change_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["report_spam", "add_contact", "block_contact", "share_contact", "need_contacts_exception", "report_geo", "autoarchived", "invite_members", "request_chat_broadcast", "business_bot_paused", "business_bot_can_reply", "geo_distance", "request_chat_title", "request_chat_date", "business_bot_id", "business_bot_manage_url", "charge_paid_message_stars", "registration_month", "phone_country", "name_change_date", "photo_change_date"]

    ID = 0xf47741f7
    QUALNAME = "types.PeerSettings"

    def __init__(self, *, report_spam: Optional[bool] = None, add_contact: Optional[bool] = None, block_contact: Optional[bool] = None, share_contact: Optional[bool] = None, need_contacts_exception: Optional[bool] = None, report_geo: Optional[bool] = None, autoarchived: Optional[bool] = None, invite_members: Optional[bool] = None, request_chat_broadcast: Optional[bool] = None, business_bot_paused: Optional[bool] = None, business_bot_can_reply: Optional[bool] = None, geo_distance: Optional[int] = None, request_chat_title: Optional[str] = None, request_chat_date: Optional[int] = None, business_bot_id: Optional[int] = None, business_bot_manage_url: Optional[str] = None, charge_paid_message_stars: Optional[int] = None, registration_month: Optional[str] = None, phone_country: Optional[str] = None, name_change_date: Optional[int] = None, photo_change_date: Optional[int] = None) -> None:
        self.report_spam = report_spam  # flags.0?true
        self.add_contact = add_contact  # flags.1?true
        self.block_contact = block_contact  # flags.2?true
        self.share_contact = share_contact  # flags.3?true
        self.need_contacts_exception = need_contacts_exception  # flags.4?true
        self.report_geo = report_geo  # flags.5?true
        self.autoarchived = autoarchived  # flags.7?true
        self.invite_members = invite_members  # flags.8?true
        self.request_chat_broadcast = request_chat_broadcast  # flags.10?true
        self.business_bot_paused = business_bot_paused  # flags.11?true
        self.business_bot_can_reply = business_bot_can_reply  # flags.12?true
        self.geo_distance = geo_distance  # flags.6?int
        self.request_chat_title = request_chat_title  # flags.9?string
        self.request_chat_date = request_chat_date  # flags.9?int
        self.business_bot_id = business_bot_id  # flags.13?long
        self.business_bot_manage_url = business_bot_manage_url  # flags.13?string
        self.charge_paid_message_stars = charge_paid_message_stars  # flags.14?long
        self.registration_month = registration_month  # flags.15?string
        self.phone_country = phone_country  # flags.16?string
        self.name_change_date = name_change_date  # flags.17?int
        self.photo_change_date = photo_change_date  # flags.18?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerSettings":

        flags = Int.read(b)

        report_spam = True if flags & (1 << 0) else False
        add_contact = True if flags & (1 << 1) else False
        block_contact = True if flags & (1 << 2) else False
        share_contact = True if flags & (1 << 3) else False
        need_contacts_exception = True if flags & (1 << 4) else False
        report_geo = True if flags & (1 << 5) else False
        autoarchived = True if flags & (1 << 7) else False
        invite_members = True if flags & (1 << 8) else False
        request_chat_broadcast = True if flags & (1 << 10) else False
        business_bot_paused = True if flags & (1 << 11) else False
        business_bot_can_reply = True if flags & (1 << 12) else False
        geo_distance = Int.read(b) if flags & (1 << 6) else None
        request_chat_title = String.read(b) if flags & (1 << 9) else None
        request_chat_date = Int.read(b) if flags & (1 << 9) else None
        business_bot_id = Long.read(b) if flags & (1 << 13) else None
        business_bot_manage_url = String.read(b) if flags & (1 << 13) else None
        charge_paid_message_stars = Long.read(b) if flags & (1 << 14) else None
        registration_month = String.read(b) if flags & (1 << 15) else None
        phone_country = String.read(b) if flags & (1 << 16) else None
        name_change_date = Int.read(b) if flags & (1 << 17) else None
        photo_change_date = Int.read(b) if flags & (1 << 18) else None
        return PeerSettings(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo, autoarchived=autoarchived, invite_members=invite_members, request_chat_broadcast=request_chat_broadcast, business_bot_paused=business_bot_paused, business_bot_can_reply=business_bot_can_reply, geo_distance=geo_distance, request_chat_title=request_chat_title, request_chat_date=request_chat_date, business_bot_id=business_bot_id, business_bot_manage_url=business_bot_manage_url, charge_paid_message_stars=charge_paid_message_stars, registration_month=registration_month, phone_country=phone_country, name_change_date=name_change_date, photo_change_date=photo_change_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        flags |= (1 << 1) if self.add_contact else 0
        flags |= (1 << 2) if self.block_contact else 0
        flags |= (1 << 3) if self.share_contact else 0
        flags |= (1 << 4) if self.need_contacts_exception else 0
        flags |= (1 << 5) if self.report_geo else 0
        flags |= (1 << 7) if self.autoarchived else 0
        flags |= (1 << 8) if self.invite_members else 0
        flags |= (1 << 10) if self.request_chat_broadcast else 0
        flags |= (1 << 11) if self.business_bot_paused else 0
        flags |= (1 << 12) if self.business_bot_can_reply else 0
        flags |= (1 << 6) if self.geo_distance is not None else 0
        flags |= (1 << 9) if self.request_chat_title is not None else 0
        flags |= (1 << 9) if self.request_chat_date is not None else 0
        flags |= (1 << 13) if self.business_bot_id is not None else 0
        flags |= (1 << 13) if self.business_bot_manage_url is not None else 0
        flags |= (1 << 14) if self.charge_paid_message_stars is not None else 0
        flags |= (1 << 15) if self.registration_month is not None else 0
        flags |= (1 << 16) if self.phone_country is not None else 0
        flags |= (1 << 17) if self.name_change_date is not None else 0
        flags |= (1 << 18) if self.photo_change_date is not None else 0
        b.write(Int(flags))

        if self.geo_distance is not None:
            b.write(Int(self.geo_distance))

        if self.request_chat_title is not None:
            b.write(String(self.request_chat_title))

        if self.request_chat_date is not None:
            b.write(Int(self.request_chat_date))

        if self.business_bot_id is not None:
            b.write(Long(self.business_bot_id))

        if self.business_bot_manage_url is not None:
            b.write(String(self.business_bot_manage_url))

        if self.charge_paid_message_stars is not None:
            b.write(Long(self.charge_paid_message_stars))

        if self.registration_month is not None:
            b.write(String(self.registration_month))

        if self.phone_country is not None:
            b.write(String(self.phone_country))

        if self.name_change_date is not None:
            b.write(Int(self.name_change_date))

        if self.photo_change_date is not None:
            b.write(Int(self.photo_change_date))

        return b.getvalue()
