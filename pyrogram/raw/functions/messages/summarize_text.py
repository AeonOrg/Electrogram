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


class SummarizeText(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9D4104E2``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        to_lang (``str``, *optional*):
            N/A

    Returns:
        :obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`
    """

    __slots__: List[str] = ["peer", "id", "to_lang"]

    ID = 0x9d4104e2
    QUALNAME = "functions.messages.SummarizeText"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, to_lang: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.to_lang = to_lang  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SummarizeText":

        flags = Int.read(b)

        peer = TLObject.read(b)

        id = Int.read(b)

        to_lang = String.read(b) if flags & (1 << 0) else None
        return SummarizeText(peer=peer, id=id, to_lang=to_lang)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.to_lang is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.id))

        if self.to_lang is not None:
            b.write(String(self.to_lang))

        return b.getvalue()
