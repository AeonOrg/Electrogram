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


class GetSavedStarGifts(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A319E569``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        exclude_unsaved (``bool``, *optional*):
            N/A

        exclude_saved (``bool``, *optional*):
            N/A

        exclude_unlimited (``bool``, *optional*):
            N/A

        exclude_unique (``bool``, *optional*):
            N/A

        sort_by_value (``bool``, *optional*):
            N/A

        exclude_upgradable (``bool``, *optional*):
            N/A

        exclude_unupgradable (``bool``, *optional*):
            N/A

        peer_color_available (``bool``, *optional*):
            N/A

        exclude_hosted (``bool``, *optional*):
            N/A

        collection_id (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`payments.SavedStarGifts <pyrogram.raw.base.payments.SavedStarGifts>`
    """

    __slots__: List[str] = ["peer", "offset", "limit", "exclude_unsaved", "exclude_saved", "exclude_unlimited", "exclude_unique", "sort_by_value", "exclude_upgradable", "exclude_unupgradable", "peer_color_available", "exclude_hosted", "collection_id"]

    ID = 0xa319e569
    QUALNAME = "functions.payments.GetSavedStarGifts"

    def __init__(self, *, peer: "raw.base.InputPeer", offset: str, limit: int, exclude_unsaved: Optional[bool] = None, exclude_saved: Optional[bool] = None, exclude_unlimited: Optional[bool] = None, exclude_unique: Optional[bool] = None, sort_by_value: Optional[bool] = None, exclude_upgradable: Optional[bool] = None, exclude_unupgradable: Optional[bool] = None, peer_color_available: Optional[bool] = None, exclude_hosted: Optional[bool] = None, collection_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset = offset  # string
        self.limit = limit  # int
        self.exclude_unsaved = exclude_unsaved  # flags.0?true
        self.exclude_saved = exclude_saved  # flags.1?true
        self.exclude_unlimited = exclude_unlimited  # flags.2?true
        self.exclude_unique = exclude_unique  # flags.4?true
        self.sort_by_value = sort_by_value  # flags.5?true
        self.exclude_upgradable = exclude_upgradable  # flags.7?true
        self.exclude_unupgradable = exclude_unupgradable  # flags.8?true
        self.peer_color_available = peer_color_available  # flags.9?true
        self.exclude_hosted = exclude_hosted  # flags.10?true
        self.collection_id = collection_id  # flags.6?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedStarGifts":

        flags = Int.read(b)

        exclude_unsaved = True if flags & (1 << 0) else False
        exclude_saved = True if flags & (1 << 1) else False
        exclude_unlimited = True if flags & (1 << 2) else False
        exclude_unique = True if flags & (1 << 4) else False
        sort_by_value = True if flags & (1 << 5) else False
        exclude_upgradable = True if flags & (1 << 7) else False
        exclude_unupgradable = True if flags & (1 << 8) else False
        peer_color_available = True if flags & (1 << 9) else False
        exclude_hosted = True if flags & (1 << 10) else False
        peer = TLObject.read(b)

        collection_id = Int.read(b) if flags & (1 << 6) else None
        offset = String.read(b)

        limit = Int.read(b)

        return GetSavedStarGifts(peer=peer, offset=offset, limit=limit, exclude_unsaved=exclude_unsaved, exclude_saved=exclude_saved, exclude_unlimited=exclude_unlimited, exclude_unique=exclude_unique, sort_by_value=sort_by_value, exclude_upgradable=exclude_upgradable, exclude_unupgradable=exclude_unupgradable, peer_color_available=peer_color_available, exclude_hosted=exclude_hosted, collection_id=collection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_unsaved else 0
        flags |= (1 << 1) if self.exclude_saved else 0
        flags |= (1 << 2) if self.exclude_unlimited else 0
        flags |= (1 << 4) if self.exclude_unique else 0
        flags |= (1 << 5) if self.sort_by_value else 0
        flags |= (1 << 7) if self.exclude_upgradable else 0
        flags |= (1 << 8) if self.exclude_unupgradable else 0
        flags |= (1 << 9) if self.peer_color_available else 0
        flags |= (1 << 10) if self.exclude_hosted else 0
        flags |= (1 << 6) if self.collection_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.collection_id is not None:
            b.write(Int(self.collection_id))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
