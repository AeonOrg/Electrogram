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


class UpdateSavedRingtones(TLObject):  # type: ignore
    """The list of saved notification sounds has changed, use account.getSavedRingtones to fetch the new list.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``74D8BE99``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x74d8be99
    QUALNAME = "types.UpdateSavedRingtones"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSavedRingtones":
        # No flags

        return UpdateSavedRingtones()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
