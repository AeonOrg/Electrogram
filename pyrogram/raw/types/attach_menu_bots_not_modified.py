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


class AttachMenuBotsNotModified(TLObject):  # type: ignore
    """The list of bot mini apps hasn't changed

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBots`.

    Details:
        - Layer: ``224``
        - ID: ``F1D88A5C``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBots
    """

    __slots__: List[str] = []

    ID = 0xf1d88a5c
    QUALNAME = "types.AttachMenuBotsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsNotModified":
        # No flags

        return AttachMenuBotsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
