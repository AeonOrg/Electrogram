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


class SavedRingtonesNotModified(TLObject):  # type: ignore
    """The notification sound list hasn't changed.

    Constructor of :obj:`~pyrogram.raw.base.account.SavedRingtones`.

    Details:
        - Layer: ``224``
        - ID: ``FBF6E8B1``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetSavedRingtones
    """

    __slots__: List[str] = []

    ID = 0xfbf6e8b1
    QUALNAME = "types.account.SavedRingtonesNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedRingtonesNotModified":
        # No flags

        return SavedRingtonesNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
