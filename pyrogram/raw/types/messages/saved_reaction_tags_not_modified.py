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


class SavedReactionTagsNotModified(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedReactionTags`.

    Details:
        - Layer: ``224``
        - ID: ``889B59EF``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedReactionTags
    """

    __slots__: List[str] = []

    ID = 0x889b59ef
    QUALNAME = "types.messages.SavedReactionTagsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedReactionTagsNotModified":
        # No flags

        return SavedReactionTagsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
