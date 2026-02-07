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


class GetInviteText(TLObject):  # type: ignore
    """Returns localized text of a text message with an invitation.


    Details:
        - Layer: ``224``
        - ID: ``4D392343``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.InviteText <pyrogram.raw.base.help.InviteText>`
    """

    __slots__: List[str] = []

    ID = 0x4d392343
    QUALNAME = "functions.help.GetInviteText"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInviteText":
        # No flags

        return GetInviteText()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
