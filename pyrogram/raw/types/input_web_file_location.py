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


class InputWebFileLocation(TLObject):  # type: ignore
    """Location of a remote HTTP(s) file

    Constructor of :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``C239D686``

    Parameters:
        url (``str``):
            HTTP URL of file

        access_hash (``int`` ``64-bit``):
            Access hash

    """

    __slots__: List[str] = ["url", "access_hash"]

    ID = 0xc239d686
    QUALNAME = "types.InputWebFileLocation"

    def __init__(self, *, url: str, access_hash: int) -> None:
        self.url = url  # string
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileLocation":
        # No flags

        url = String.read(b)

        access_hash = Long.read(b)

        return InputWebFileLocation(url=url, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Long(self.access_hash))

        return b.getvalue()
