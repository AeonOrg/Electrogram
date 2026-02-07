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


class GetBirthdays(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``DAEDA864``

    Parameters:
        No parameters required.

    Returns:
        :obj:`contacts.ContactBirthdays <pyrogram.raw.base.contacts.ContactBirthdays>`
    """

    __slots__: List[str] = []

    ID = 0xdaeda864
    QUALNAME = "functions.contacts.GetBirthdays"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBirthdays":
        # No flags

        return GetBirthdays()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
