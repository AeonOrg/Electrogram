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


class SavedStarGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SavedStarGift`.

    Details:
        - Layer: ``224``
        - ID: ``41DF43FC``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        name_hidden (``bool``, *optional*):
            N/A

        unsaved (``bool``, *optional*):
            N/A

        refunded (``bool``, *optional*):
            N/A

        can_upgrade (``bool``, *optional*):
            N/A

        pinned_to_top (``bool``, *optional*):
            N/A

        upgrade_separate (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

        saved_id (``int`` ``64-bit``, *optional*):
            N/A

        convert_stars (``int`` ``64-bit``, *optional*):
            N/A

        upgrade_stars (``int`` ``64-bit``, *optional*):
            N/A

        can_export_at (``int`` ``32-bit``, *optional*):
            N/A

        transfer_stars (``int`` ``64-bit``, *optional*):
            N/A

        can_transfer_at (``int`` ``32-bit``, *optional*):
            N/A

        can_resell_at (``int`` ``32-bit``, *optional*):
            N/A

        collection_id (List of ``int`` ``32-bit``, *optional*):
            N/A

        prepaid_upgrade_hash (``str``, *optional*):
            N/A

        drop_original_details_stars (``int`` ``64-bit``, *optional*):
            N/A

        gift_num (``int`` ``32-bit``, *optional*):
            N/A

        can_craft_at (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["date", "gift", "name_hidden", "unsaved", "refunded", "can_upgrade", "pinned_to_top", "upgrade_separate", "from_id", "message", "msg_id", "saved_id", "convert_stars", "upgrade_stars", "can_export_at", "transfer_stars", "can_transfer_at", "can_resell_at", "collection_id", "prepaid_upgrade_hash", "drop_original_details_stars", "gift_num", "can_craft_at"]

    ID = 0x41df43fc
    QUALNAME = "types.SavedStarGift"

    def __init__(self, *, date: int, gift: "raw.base.StarGift", name_hidden: Optional[bool] = None, unsaved: Optional[bool] = None, refunded: Optional[bool] = None, can_upgrade: Optional[bool] = None, pinned_to_top: Optional[bool] = None, upgrade_separate: Optional[bool] = None, from_id: "raw.base.Peer" = None, message: "raw.base.TextWithEntities" = None, msg_id: Optional[int] = None, saved_id: Optional[int] = None, convert_stars: Optional[int] = None, upgrade_stars: Optional[int] = None, can_export_at: Optional[int] = None, transfer_stars: Optional[int] = None, can_transfer_at: Optional[int] = None, can_resell_at: Optional[int] = None, collection_id: Optional[List[int]] = None, prepaid_upgrade_hash: Optional[str] = None, drop_original_details_stars: Optional[int] = None, gift_num: Optional[int] = None, can_craft_at: Optional[int] = None) -> None:
        self.date = date  # int
        self.gift = gift  # StarGift
        self.name_hidden = name_hidden  # flags.0?true
        self.unsaved = unsaved  # flags.5?true
        self.refunded = refunded  # flags.9?true
        self.can_upgrade = can_upgrade  # flags.10?true
        self.pinned_to_top = pinned_to_top  # flags.12?true
        self.upgrade_separate = upgrade_separate  # flags.17?true
        self.from_id = from_id  # flags.1?Peer
        self.message = message  # flags.2?TextWithEntities
        self.msg_id = msg_id  # flags.3?int
        self.saved_id = saved_id  # flags.11?long
        self.convert_stars = convert_stars  # flags.4?long
        self.upgrade_stars = upgrade_stars  # flags.6?long
        self.can_export_at = can_export_at  # flags.7?int
        self.transfer_stars = transfer_stars  # flags.8?long
        self.can_transfer_at = can_transfer_at  # flags.13?int
        self.can_resell_at = can_resell_at  # flags.14?int
        self.collection_id = collection_id  # flags.15?Vector<int>
        self.prepaid_upgrade_hash = prepaid_upgrade_hash  # flags.16?string
        self.drop_original_details_stars = drop_original_details_stars  # flags.18?long
        self.gift_num = gift_num  # flags.19?int
        self.can_craft_at = can_craft_at  # flags.20?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedStarGift":

        flags = Int.read(b)

        name_hidden = True if flags & (1 << 0) else False
        unsaved = True if flags & (1 << 5) else False
        refunded = True if flags & (1 << 9) else False
        can_upgrade = True if flags & (1 << 10) else False
        pinned_to_top = True if flags & (1 << 12) else False
        upgrade_separate = True if flags & (1 << 17) else False
        from_id = TLObject.read(b) if flags & (1 << 1) else None

        date = Int.read(b)

        gift = TLObject.read(b)

        message = TLObject.read(b) if flags & (1 << 2) else None

        msg_id = Int.read(b) if flags & (1 << 3) else None
        saved_id = Long.read(b) if flags & (1 << 11) else None
        convert_stars = Long.read(b) if flags & (1 << 4) else None
        upgrade_stars = Long.read(b) if flags & (1 << 6) else None
        can_export_at = Int.read(b) if flags & (1 << 7) else None
        transfer_stars = Long.read(b) if flags & (1 << 8) else None
        can_transfer_at = Int.read(b) if flags & (1 << 13) else None
        can_resell_at = Int.read(b) if flags & (1 << 14) else None
        collection_id = TLObject.read(b, Int) if flags & (1 << 15) else []

        prepaid_upgrade_hash = String.read(b) if flags & (1 << 16) else None
        drop_original_details_stars = Long.read(b) if flags & (1 << 18) else None
        gift_num = Int.read(b) if flags & (1 << 19) else None
        can_craft_at = Int.read(b) if flags & (1 << 20) else None
        return SavedStarGift(date=date, gift=gift, name_hidden=name_hidden, unsaved=unsaved, refunded=refunded, can_upgrade=can_upgrade, pinned_to_top=pinned_to_top, upgrade_separate=upgrade_separate, from_id=from_id, message=message, msg_id=msg_id, saved_id=saved_id, convert_stars=convert_stars, upgrade_stars=upgrade_stars, can_export_at=can_export_at, transfer_stars=transfer_stars, can_transfer_at=can_transfer_at, can_resell_at=can_resell_at, collection_id=collection_id, prepaid_upgrade_hash=prepaid_upgrade_hash, drop_original_details_stars=drop_original_details_stars, gift_num=gift_num, can_craft_at=can_craft_at)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.name_hidden else 0
        flags |= (1 << 5) if self.unsaved else 0
        flags |= (1 << 9) if self.refunded else 0
        flags |= (1 << 10) if self.can_upgrade else 0
        flags |= (1 << 12) if self.pinned_to_top else 0
        flags |= (1 << 17) if self.upgrade_separate else 0
        flags |= (1 << 1) if self.from_id is not None else 0
        flags |= (1 << 2) if self.message is not None else 0
        flags |= (1 << 3) if self.msg_id is not None else 0
        flags |= (1 << 11) if self.saved_id is not None else 0
        flags |= (1 << 4) if self.convert_stars is not None else 0
        flags |= (1 << 6) if self.upgrade_stars is not None else 0
        flags |= (1 << 7) if self.can_export_at is not None else 0
        flags |= (1 << 8) if self.transfer_stars is not None else 0
        flags |= (1 << 13) if self.can_transfer_at is not None else 0
        flags |= (1 << 14) if self.can_resell_at is not None else 0
        flags |= (1 << 15) if self.collection_id else 0
        flags |= (1 << 16) if self.prepaid_upgrade_hash is not None else 0
        flags |= (1 << 18) if self.drop_original_details_stars is not None else 0
        flags |= (1 << 19) if self.gift_num is not None else 0
        flags |= (1 << 20) if self.can_craft_at is not None else 0
        b.write(Int(flags))

        if self.from_id is not None:
            b.write(self.from_id.write())

        b.write(Int(self.date))

        b.write(self.gift.write())

        if self.message is not None:
            b.write(self.message.write())

        if self.msg_id is not None:
            b.write(Int(self.msg_id))

        if self.saved_id is not None:
            b.write(Long(self.saved_id))

        if self.convert_stars is not None:
            b.write(Long(self.convert_stars))

        if self.upgrade_stars is not None:
            b.write(Long(self.upgrade_stars))

        if self.can_export_at is not None:
            b.write(Int(self.can_export_at))

        if self.transfer_stars is not None:
            b.write(Long(self.transfer_stars))

        if self.can_transfer_at is not None:
            b.write(Int(self.can_transfer_at))

        if self.can_resell_at is not None:
            b.write(Int(self.can_resell_at))

        if self.collection_id is not None:
            b.write(Vector(self.collection_id, Int))

        if self.prepaid_upgrade_hash is not None:
            b.write(String(self.prepaid_upgrade_hash))

        if self.drop_original_details_stars is not None:
            b.write(Long(self.drop_original_details_stars))

        if self.gift_num is not None:
            b.write(Int(self.gift_num))

        if self.can_craft_at is not None:
            b.write(Int(self.can_craft_at))

        return b.getvalue()
