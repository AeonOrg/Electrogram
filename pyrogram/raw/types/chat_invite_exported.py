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


class ChatInviteExported(TLObject):  # type: ignore
    """Exported chat invite

    Constructor of :obj:`~pyrogram.raw.base.ExportedChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``A22CBD96``

    Parameters:
        link (``str``):
            Chat invitation link

        admin_id (``int`` ``64-bit``):
            ID of the admin that created this chat invite

        date (``int`` ``32-bit``):
            When was this chat invite created

        revoked (``bool``, *optional*):
            Whether this chat invite was revoked

        permanent (``bool``, *optional*):
            Whether this chat invite has no expiration

        request_needed (``bool``, *optional*):
            Whether users importing this invite link will have to be approved to join the channel or group

        start_date (``int`` ``32-bit``, *optional*):
            When was this chat invite last modified

        expire_date (``int`` ``32-bit``, *optional*):
            When does this chat invite expire

        usage_limit (``int`` ``32-bit``, *optional*):
            Maximum number of users that can join using this link

        usage (``int`` ``32-bit``, *optional*):
            How many users joined using this link

        requested (``int`` ``32-bit``, *optional*):
            Number of users that have already used this link to join

        subscription_expired (``int`` ``32-bit``, *optional*):
            N/A

        title (``str``, *optional*):
            Custom description for the invite link, visible only to admins

        subscription_pricing (:obj:`StarsSubscriptionPricing <pyrogram.raw.base.StarsSubscriptionPricing>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ExportChatInvite
    """

    __slots__: List[str] = ["link", "admin_id", "date", "revoked", "permanent", "request_needed", "start_date", "expire_date", "usage_limit", "usage", "requested", "subscription_expired", "title", "subscription_pricing"]

    ID = 0xa22cbd96
    QUALNAME = "types.ChatInviteExported"

    def __init__(self, *, link: str, admin_id: int, date: int, revoked: Optional[bool] = None, permanent: Optional[bool] = None, request_needed: Optional[bool] = None, start_date: Optional[int] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, usage: Optional[int] = None, requested: Optional[int] = None, subscription_expired: Optional[int] = None, title: Optional[str] = None, subscription_pricing: "raw.base.StarsSubscriptionPricing" = None) -> None:
        self.link = link  # string
        self.admin_id = admin_id  # long
        self.date = date  # int
        self.revoked = revoked  # flags.0?true
        self.permanent = permanent  # flags.5?true
        self.request_needed = request_needed  # flags.6?true
        self.start_date = start_date  # flags.4?int
        self.expire_date = expire_date  # flags.1?int
        self.usage_limit = usage_limit  # flags.2?int
        self.usage = usage  # flags.3?int
        self.requested = requested  # flags.7?int
        self.subscription_expired = subscription_expired  # flags.10?int
        self.title = title  # flags.8?string
        self.subscription_pricing = subscription_pricing  # flags.9?StarsSubscriptionPricing

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteExported":

        flags = Int.read(b)

        revoked = True if flags & (1 << 0) else False
        permanent = True if flags & (1 << 5) else False
        request_needed = True if flags & (1 << 6) else False
        link = String.read(b)

        admin_id = Long.read(b)

        date = Int.read(b)

        start_date = Int.read(b) if flags & (1 << 4) else None
        expire_date = Int.read(b) if flags & (1 << 1) else None
        usage_limit = Int.read(b) if flags & (1 << 2) else None
        usage = Int.read(b) if flags & (1 << 3) else None
        requested = Int.read(b) if flags & (1 << 7) else None
        subscription_expired = Int.read(b) if flags & (1 << 10) else None
        title = String.read(b) if flags & (1 << 8) else None
        subscription_pricing = TLObject.read(b) if flags & (1 << 9) else None

        return ChatInviteExported(link=link, admin_id=admin_id, date=date, revoked=revoked, permanent=permanent, request_needed=request_needed, start_date=start_date, expire_date=expire_date, usage_limit=usage_limit, usage=usage, requested=requested, subscription_expired=subscription_expired, title=title, subscription_pricing=subscription_pricing)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoked else 0
        flags |= (1 << 5) if self.permanent else 0
        flags |= (1 << 6) if self.request_needed else 0
        flags |= (1 << 4) if self.start_date is not None else 0
        flags |= (1 << 1) if self.expire_date is not None else 0
        flags |= (1 << 2) if self.usage_limit is not None else 0
        flags |= (1 << 3) if self.usage is not None else 0
        flags |= (1 << 7) if self.requested is not None else 0
        flags |= (1 << 10) if self.subscription_expired is not None else 0
        flags |= (1 << 8) if self.title is not None else 0
        flags |= (1 << 9) if self.subscription_pricing is not None else 0
        b.write(Int(flags))

        b.write(String(self.link))

        b.write(Long(self.admin_id))

        b.write(Int(self.date))

        if self.start_date is not None:
            b.write(Int(self.start_date))

        if self.expire_date is not None:
            b.write(Int(self.expire_date))

        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))

        if self.usage is not None:
            b.write(Int(self.usage))

        if self.requested is not None:
            b.write(Int(self.requested))

        if self.subscription_expired is not None:
            b.write(Int(self.subscription_expired))

        if self.title is not None:
            b.write(String(self.title))

        if self.subscription_pricing is not None:
            b.write(self.subscription_pricing.write())

        return b.getvalue()
