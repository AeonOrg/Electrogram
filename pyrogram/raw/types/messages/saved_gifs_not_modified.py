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


class SavedGifsNotModified(TLObject):  # type: ignore
    """No new saved gifs were found

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedGifs`.

    Details:
        - Layer: ``224``
        - ID: ``E8025CA2``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedGifs
    """

    __slots__: List[str] = []

    ID = 0xe8025ca2
    QUALNAME = "types.messages.SavedGifsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedGifsNotModified":
        # No flags

        return SavedGifsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
