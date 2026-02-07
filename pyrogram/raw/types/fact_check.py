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


class FactCheck(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.FactCheck`.

    Details:
        - Layer: ``224``
        - ID: ``B89BFCCF``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        need_check (``bool``, *optional*):


        country (``str``, *optional*):


        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFactCheck
    """

    __slots__: List[str] = ["hash", "need_check", "country", "text"]

    ID = 0xb89bfccf
    QUALNAME = "types.FactCheck"

    def __init__(self, *, hash: int, need_check: Optional[bool] = None, country: Optional[str] = None, text: "raw.base.TextWithEntities" = None) -> None:
        self.hash = hash  # long
        self.need_check = need_check  # flags.0?true
        self.country = country  # flags.1?string
        self.text = text  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FactCheck":

        flags = Int.read(b)

        need_check = True if flags & (1 << 0) else False
        country = String.read(b) if flags & (1 << 1) else None
        text = TLObject.read(b) if flags & (1 << 1) else None

        hash = Long.read(b)

        return FactCheck(hash=hash, need_check=need_check, country=country, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.need_check else 0
        flags |= (1 << 1) if self.country is not None else 0
        flags |= (1 << 1) if self.text is not None else 0
        b.write(Int(flags))

        if self.country is not None:
            b.write(String(self.country))

        if self.text is not None:
            b.write(self.text.write())

        b.write(Long(self.hash))

        return b.getvalue()
