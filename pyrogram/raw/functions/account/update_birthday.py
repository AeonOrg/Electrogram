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


class UpdateBirthday(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``CC6E0C11``

    Parameters:
        birthday (:obj:`Birthday <pyrogram.raw.base.Birthday>`, *optional*):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["birthday"]

    ID = 0xcc6e0c11
    QUALNAME = "functions.account.UpdateBirthday"

    def __init__(self, *, birthday: "raw.base.Birthday" = None) -> None:
        self.birthday = birthday  # flags.0?Birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBirthday":

        flags = Int.read(b)

        birthday = TLObject.read(b) if flags & (1 << 0) else None

        return UpdateBirthday(birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.birthday is not None else 0
        b.write(Int(flags))

        if self.birthday is not None:
            b.write(self.birthday.write())

        return b.getvalue()
