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


class ImportedContact(TLObject):  # type: ignore
    """Successfully imported contact.

    Constructor of :obj:`~pyrogram.raw.base.ImportedContact`.

    Details:
        - Layer: ``224``
        - ID: ``C13E3C50``

    Parameters:
        user_id (``int`` ``64-bit``):
            User identifier

        client_id (``int`` ``64-bit``):
            The contact's client identifier (passed to one of the InputContact constructors)

    """

    __slots__: List[str] = ["user_id", "client_id"]

    ID = 0xc13e3c50
    QUALNAME = "types.ImportedContact"

    def __init__(self, *, user_id: int, client_id: int) -> None:
        self.user_id = user_id  # long
        self.client_id = client_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportedContact":
        # No flags

        user_id = Long.read(b)

        client_id = Long.read(b)

        return ImportedContact(user_id=user_id, client_id=client_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(Long(self.client_id))

        return b.getvalue()
