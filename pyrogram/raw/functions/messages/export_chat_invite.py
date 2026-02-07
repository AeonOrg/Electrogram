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


class ExportChatInvite(TLObject):  # type: ignore
    """Export an invite link for a chat


    Details:
        - Layer: ``224``
        - ID: ``A455DE90``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Chat

        legacy_revoke_permanent (``bool``, *optional*):
            Legacy flag, reproducing legacy behavior of this method: if set, revokes all previous links before creating a new one. Kept for bot API BC, should not be used by modern clients.

        request_needed (``bool``, *optional*):
            Whether admin confirmation is required before admitting each separate user into the chat

        expire_date (``int`` ``32-bit``, *optional*):
            Expiration date

        usage_limit (``int`` ``32-bit``, *optional*):
            Maximum number of users that can join using this link

        title (``str``, *optional*):
            Description of the invite link, visible only to administrators

        subscription_pricing (:obj:`StarsSubscriptionPricing <pyrogram.raw.base.StarsSubscriptionPricing>`, *optional*):
            N/A

    Returns:
        :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "legacy_revoke_permanent", "request_needed", "expire_date", "usage_limit", "title", "subscription_pricing"]

    ID = 0xa455de90
    QUALNAME = "functions.messages.ExportChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", legacy_revoke_permanent: Optional[bool] = None, request_needed: Optional[bool] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, title: Optional[str] = None, subscription_pricing: "raw.base.StarsSubscriptionPricing" = None) -> None:
        self.peer = peer  # InputPeer
        self.legacy_revoke_permanent = legacy_revoke_permanent  # flags.2?true
        self.request_needed = request_needed  # flags.3?true
        self.expire_date = expire_date  # flags.0?int
        self.usage_limit = usage_limit  # flags.1?int
        self.title = title  # flags.4?string
        self.subscription_pricing = subscription_pricing  # flags.5?StarsSubscriptionPricing

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportChatInvite":

        flags = Int.read(b)

        legacy_revoke_permanent = True if flags & (1 << 2) else False
        request_needed = True if flags & (1 << 3) else False
        peer = TLObject.read(b)

        expire_date = Int.read(b) if flags & (1 << 0) else None
        usage_limit = Int.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 4) else None
        subscription_pricing = TLObject.read(b) if flags & (1 << 5) else None

        return ExportChatInvite(peer=peer, legacy_revoke_permanent=legacy_revoke_permanent, request_needed=request_needed, expire_date=expire_date, usage_limit=usage_limit, title=title, subscription_pricing=subscription_pricing)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.legacy_revoke_permanent else 0
        flags |= (1 << 3) if self.request_needed else 0
        flags |= (1 << 0) if self.expire_date is not None else 0
        flags |= (1 << 1) if self.usage_limit is not None else 0
        flags |= (1 << 4) if self.title is not None else 0
        flags |= (1 << 5) if self.subscription_pricing is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.expire_date is not None:
            b.write(Int(self.expire_date))

        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))

        if self.title is not None:
            b.write(String(self.title))

        if self.subscription_pricing is not None:
            b.write(self.subscription_pricing.write())

        return b.getvalue()
