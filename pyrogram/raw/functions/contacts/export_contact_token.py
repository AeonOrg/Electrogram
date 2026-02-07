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


class ExportContactToken(TLObject):  # type: ignore
    """Generates a temporary profile link for the currently logged-in user.


    Details:
        - Layer: ``224``
        - ID: ``F8654027``

    Parameters:
        No parameters required.

    Returns:
        :obj:`ExportedContactToken <pyrogram.raw.base.ExportedContactToken>`
    """

    __slots__: List[str] = []

    ID = 0xf8654027
    QUALNAME = "functions.contacts.ExportContactToken"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportContactToken":
        # No flags

        return ExportContactToken()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
