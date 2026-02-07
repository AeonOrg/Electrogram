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


class ExportedContactToken(TLObject):  # type: ignore
    """Describes a temporary profile link.

    Constructor of :obj:`~pyrogram.raw.base.ExportedContactToken`.

    Details:
        - Layer: ``224``
        - ID: ``41BF109B``

    Parameters:
        url (``str``):
            The temporary profile link.

        expires (``int`` ``32-bit``):
            Its expiration date

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ExportContactToken
    """

    __slots__: List[str] = ["url", "expires"]

    ID = 0x41bf109b
    QUALNAME = "types.ExportedContactToken"

    def __init__(self, *, url: str, expires: int) -> None:
        self.url = url  # string
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedContactToken":
        # No flags

        url = String.read(b)

        expires = Int.read(b)

        return ExportedContactToken(url=url, expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Int(self.expires))

        return b.getvalue()
