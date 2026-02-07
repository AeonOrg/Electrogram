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


class StarsTransaction(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.StarsTransaction`.

    Details:
        - Layer: ``224``
        - ID: ``13659EB0``

    Parameters:
        id (``str``):


        amount (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

        date (``int`` ``32-bit``):


        peer (:obj:`StarsTransactionPeer <pyrogram.raw.base.StarsTransactionPeer>`):


        refund (``bool``, *optional*):


        pending (``bool``, *optional*):
            N/A

        failed (``bool``, *optional*):
            N/A

        gift (``bool``, *optional*):
            N/A

        reaction (``bool``, *optional*):
            N/A

        subscription (``bool``, *optional*):
            N/A

        floodskip (``bool``, *optional*):
            N/A

        stargift_upgrade (``bool``, *optional*):
            N/A

        paid_message (``bool``, *optional*):
            N/A

        premium_gift (``bool``, *optional*):
            N/A

        business_transfer (``bool``, *optional*):
            N/A

        stargift_resale (``bool``, *optional*):
            N/A

        posts_search (``bool``, *optional*):
            N/A

        stargift_prepaid_upgrade (``bool``, *optional*):
            N/A

        stargift_drop_original_details (``bool``, *optional*):
            N/A

        phonegroup_message (``bool``, *optional*):
            N/A

        stargift_auction_bid (``bool``, *optional*):
            N/A

        offer (``bool``, *optional*):
            N/A

        title (``str``, *optional*):


        description (``str``, *optional*):


        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):


        transaction_date (``int`` ``32-bit``, *optional*):
            N/A

        transaction_url (``str``, *optional*):
            N/A

        bot_payload (``bytes``, *optional*):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

        extended_media (List of :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            N/A

        subscription_period (``int`` ``32-bit``, *optional*):
            N/A

        giveaway_post_id (``int`` ``32-bit``, *optional*):
            N/A

        stargift (:obj:`StarGift <pyrogram.raw.base.StarGift>`, *optional*):
            N/A

        floodskip_number (``int`` ``32-bit``, *optional*):
            N/A

        starref_commission_permille (``int`` ``32-bit``, *optional*):
            N/A

        starref_peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        starref_amount (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`, *optional*):
            N/A

        paid_messages (``int`` ``32-bit``, *optional*):
            N/A

        premium_gift_months (``int`` ``32-bit``, *optional*):
            N/A

        ads_proceeds_from_date (``int`` ``32-bit``, *optional*):
            N/A

        ads_proceeds_to_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "amount", "date", "peer", "refund", "pending", "failed", "gift", "reaction", "subscription", "floodskip", "stargift_upgrade", "paid_message", "premium_gift", "business_transfer", "stargift_resale", "posts_search", "stargift_prepaid_upgrade", "stargift_drop_original_details", "phonegroup_message", "stargift_auction_bid", "offer", "title", "description", "photo", "transaction_date", "transaction_url", "bot_payload", "msg_id", "extended_media", "subscription_period", "giveaway_post_id", "stargift", "floodskip_number", "starref_commission_permille", "starref_peer", "starref_amount", "paid_messages", "premium_gift_months", "ads_proceeds_from_date", "ads_proceeds_to_date"]

    ID = 0x13659eb0
    QUALNAME = "types.StarsTransaction"

    def __init__(self, *, id: str, amount: "raw.base.StarsAmount", date: int, peer: "raw.base.StarsTransactionPeer", refund: Optional[bool] = None, pending: Optional[bool] = None, failed: Optional[bool] = None, gift: Optional[bool] = None, reaction: Optional[bool] = None, subscription: Optional[bool] = None, floodskip: Optional[bool] = None, stargift_upgrade: Optional[bool] = None, paid_message: Optional[bool] = None, premium_gift: Optional[bool] = None, business_transfer: Optional[bool] = None, stargift_resale: Optional[bool] = None, posts_search: Optional[bool] = None, stargift_prepaid_upgrade: Optional[bool] = None, stargift_drop_original_details: Optional[bool] = None, phonegroup_message: Optional[bool] = None, stargift_auction_bid: Optional[bool] = None, offer: Optional[bool] = None, title: Optional[str] = None, description: Optional[str] = None, photo: "raw.base.WebDocument" = None, transaction_date: Optional[int] = None, transaction_url: Optional[str] = None, bot_payload: Optional[bytes] = None, msg_id: Optional[int] = None, extended_media: Optional[List["raw.base.MessageMedia"]] = None, subscription_period: Optional[int] = None, giveaway_post_id: Optional[int] = None, stargift: "raw.base.StarGift" = None, floodskip_number: Optional[int] = None, starref_commission_permille: Optional[int] = None, starref_peer: "raw.base.Peer" = None, starref_amount: "raw.base.StarsAmount" = None, paid_messages: Optional[int] = None, premium_gift_months: Optional[int] = None, ads_proceeds_from_date: Optional[int] = None, ads_proceeds_to_date: Optional[int] = None) -> None:
        self.id = id  # string
        self.amount = amount  # StarsAmount
        self.date = date  # int
        self.peer = peer  # StarsTransactionPeer
        self.refund = refund  # flags.3?true
        self.pending = pending  # flags.4?true
        self.failed = failed  # flags.6?true
        self.gift = gift  # flags.10?true
        self.reaction = reaction  # flags.11?true
        self.subscription = subscription  # flags.12?true
        self.floodskip = floodskip  # flags.15?true
        self.stargift_upgrade = stargift_upgrade  # flags.18?true
        self.paid_message = paid_message  # flags.19?true
        self.premium_gift = premium_gift  # flags.20?true
        self.business_transfer = business_transfer  # flags.21?true
        self.stargift_resale = stargift_resale  # flags.22?true
        self.posts_search = posts_search  # flags.24?true
        self.stargift_prepaid_upgrade = stargift_prepaid_upgrade  # flags.25?true
        self.stargift_drop_original_details = stargift_drop_original_details  # flags.26?true
        self.phonegroup_message = phonegroup_message  # flags.27?true
        self.stargift_auction_bid = stargift_auction_bid  # flags.28?true
        self.offer = offer  # flags.29?true
        self.title = title  # flags.0?string
        self.description = description  # flags.1?string
        self.photo = photo  # flags.2?WebDocument
        self.transaction_date = transaction_date  # flags.5?int
        self.transaction_url = transaction_url  # flags.5?string
        self.bot_payload = bot_payload  # flags.7?bytes
        self.msg_id = msg_id  # flags.8?int
        self.extended_media = extended_media  # flags.9?Vector<MessageMedia>
        self.subscription_period = subscription_period  # flags.12?int
        self.giveaway_post_id = giveaway_post_id  # flags.13?int
        self.stargift = stargift  # flags.14?StarGift
        self.floodskip_number = floodskip_number  # flags.15?int
        self.starref_commission_permille = starref_commission_permille  # flags.16?int
        self.starref_peer = starref_peer  # flags.17?Peer
        self.starref_amount = starref_amount  # flags.17?StarsAmount
        self.paid_messages = paid_messages  # flags.19?int
        self.premium_gift_months = premium_gift_months  # flags.20?int
        self.ads_proceeds_from_date = ads_proceeds_from_date  # flags.23?int
        self.ads_proceeds_to_date = ads_proceeds_to_date  # flags.23?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransaction":

        flags = Int.read(b)

        refund = True if flags & (1 << 3) else False
        pending = True if flags & (1 << 4) else False
        failed = True if flags & (1 << 6) else False
        gift = True if flags & (1 << 10) else False
        reaction = True if flags & (1 << 11) else False
        subscription = True if flags & (1 << 12) else False
        floodskip = True if flags & (1 << 15) else False
        stargift_upgrade = True if flags & (1 << 18) else False
        paid_message = True if flags & (1 << 19) else False
        premium_gift = True if flags & (1 << 20) else False
        business_transfer = True if flags & (1 << 21) else False
        stargift_resale = True if flags & (1 << 22) else False
        posts_search = True if flags & (1 << 24) else False
        stargift_prepaid_upgrade = True if flags & (1 << 25) else False
        stargift_drop_original_details = True if flags & (1 << 26) else False
        phonegroup_message = True if flags & (1 << 27) else False
        stargift_auction_bid = True if flags & (1 << 28) else False
        offer = True if flags & (1 << 29) else False
        id = String.read(b)

        amount = TLObject.read(b)

        date = Int.read(b)

        peer = TLObject.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None

        transaction_date = Int.read(b) if flags & (1 << 5) else None
        transaction_url = String.read(b) if flags & (1 << 5) else None
        bot_payload = Bytes.read(b) if flags & (1 << 7) else None
        msg_id = Int.read(b) if flags & (1 << 8) else None
        extended_media = TLObject.read(b) if flags & (1 << 9) else []

        subscription_period = Int.read(b) if flags & (1 << 12) else None
        giveaway_post_id = Int.read(b) if flags & (1 << 13) else None
        stargift = TLObject.read(b) if flags & (1 << 14) else None

        floodskip_number = Int.read(b) if flags & (1 << 15) else None
        starref_commission_permille = Int.read(b) if flags & (1 << 16) else None
        starref_peer = TLObject.read(b) if flags & (1 << 17) else None

        starref_amount = TLObject.read(b) if flags & (1 << 17) else None

        paid_messages = Int.read(b) if flags & (1 << 19) else None
        premium_gift_months = Int.read(b) if flags & (1 << 20) else None
        ads_proceeds_from_date = Int.read(b) if flags & (1 << 23) else None
        ads_proceeds_to_date = Int.read(b) if flags & (1 << 23) else None
        return StarsTransaction(id=id, amount=amount, date=date, peer=peer, refund=refund, pending=pending, failed=failed, gift=gift, reaction=reaction, subscription=subscription, floodskip=floodskip, stargift_upgrade=stargift_upgrade, paid_message=paid_message, premium_gift=premium_gift, business_transfer=business_transfer, stargift_resale=stargift_resale, posts_search=posts_search, stargift_prepaid_upgrade=stargift_prepaid_upgrade, stargift_drop_original_details=stargift_drop_original_details, phonegroup_message=phonegroup_message, stargift_auction_bid=stargift_auction_bid, offer=offer, title=title, description=description, photo=photo, transaction_date=transaction_date, transaction_url=transaction_url, bot_payload=bot_payload, msg_id=msg_id, extended_media=extended_media, subscription_period=subscription_period, giveaway_post_id=giveaway_post_id, stargift=stargift, floodskip_number=floodskip_number, starref_commission_permille=starref_commission_permille, starref_peer=starref_peer, starref_amount=starref_amount, paid_messages=paid_messages, premium_gift_months=premium_gift_months, ads_proceeds_from_date=ads_proceeds_from_date, ads_proceeds_to_date=ads_proceeds_to_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.refund else 0
        flags |= (1 << 4) if self.pending else 0
        flags |= (1 << 6) if self.failed else 0
        flags |= (1 << 10) if self.gift else 0
        flags |= (1 << 11) if self.reaction else 0
        flags |= (1 << 12) if self.subscription else 0
        flags |= (1 << 15) if self.floodskip else 0
        flags |= (1 << 18) if self.stargift_upgrade else 0
        flags |= (1 << 19) if self.paid_message else 0
        flags |= (1 << 20) if self.premium_gift else 0
        flags |= (1 << 21) if self.business_transfer else 0
        flags |= (1 << 22) if self.stargift_resale else 0
        flags |= (1 << 24) if self.posts_search else 0
        flags |= (1 << 25) if self.stargift_prepaid_upgrade else 0
        flags |= (1 << 26) if self.stargift_drop_original_details else 0
        flags |= (1 << 27) if self.phonegroup_message else 0
        flags |= (1 << 28) if self.stargift_auction_bid else 0
        flags |= (1 << 29) if self.offer else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        flags |= (1 << 5) if self.transaction_date is not None else 0
        flags |= (1 << 5) if self.transaction_url is not None else 0
        flags |= (1 << 7) if self.bot_payload is not None else 0
        flags |= (1 << 8) if self.msg_id is not None else 0
        flags |= (1 << 9) if self.extended_media else 0
        flags |= (1 << 12) if self.subscription_period is not None else 0
        flags |= (1 << 13) if self.giveaway_post_id is not None else 0
        flags |= (1 << 14) if self.stargift is not None else 0
        flags |= (1 << 15) if self.floodskip_number is not None else 0
        flags |= (1 << 16) if self.starref_commission_permille is not None else 0
        flags |= (1 << 17) if self.starref_peer is not None else 0
        flags |= (1 << 17) if self.starref_amount is not None else 0
        flags |= (1 << 19) if self.paid_messages is not None else 0
        flags |= (1 << 20) if self.premium_gift_months is not None else 0
        flags |= (1 << 23) if self.ads_proceeds_from_date is not None else 0
        flags |= (1 << 23) if self.ads_proceeds_to_date is not None else 0
        b.write(Int(flags))

        b.write(String(self.id))

        b.write(self.amount.write())

        b.write(Int(self.date))

        b.write(self.peer.write())

        if self.title is not None:
            b.write(String(self.title))

        if self.description is not None:
            b.write(String(self.description))

        if self.photo is not None:
            b.write(self.photo.write())

        if self.transaction_date is not None:
            b.write(Int(self.transaction_date))

        if self.transaction_url is not None:
            b.write(String(self.transaction_url))

        if self.bot_payload is not None:
            b.write(Bytes(self.bot_payload))

        if self.msg_id is not None:
            b.write(Int(self.msg_id))

        if self.extended_media is not None:
            b.write(Vector(self.extended_media))

        if self.subscription_period is not None:
            b.write(Int(self.subscription_period))

        if self.giveaway_post_id is not None:
            b.write(Int(self.giveaway_post_id))

        if self.stargift is not None:
            b.write(self.stargift.write())

        if self.floodskip_number is not None:
            b.write(Int(self.floodskip_number))

        if self.starref_commission_permille is not None:
            b.write(Int(self.starref_commission_permille))

        if self.starref_peer is not None:
            b.write(self.starref_peer.write())

        if self.starref_amount is not None:
            b.write(self.starref_amount.write())

        if self.paid_messages is not None:
            b.write(Int(self.paid_messages))

        if self.premium_gift_months is not None:
            b.write(Int(self.premium_gift_months))

        if self.ads_proceeds_from_date is not None:
            b.write(Int(self.ads_proceeds_from_date))

        if self.ads_proceeds_to_date is not None:
            b.write(Int(self.ads_proceeds_to_date))

        return b.getvalue()
