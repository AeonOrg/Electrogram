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


class SponsoredMessagesEmpty(TLObject):  # type: ignore
    """No sponsored messages are available.

    Constructor of :obj:`~pyrogram.raw.base.messages.SponsoredMessages`.

    Details:
        - Layer: ``224``
        - ID: ``1839490F``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSponsoredMessages
    """

    __slots__: List[str] = []

    ID = 0x1839490f
    QUALNAME = "types.messages.SponsoredMessagesEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessagesEmpty":
        # No flags

        return SponsoredMessagesEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
