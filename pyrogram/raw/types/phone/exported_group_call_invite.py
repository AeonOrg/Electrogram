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


class ExportedGroupCallInvite(TLObject):  # type: ignore
    """An invite to a group call or livestream

    Constructor of :obj:`~pyrogram.raw.base.phone.ExportedGroupCallInvite`.

    Details:
        - Layer: ``224``
        - ID: ``204BD158``

    Parameters:
        link (``str``):
            Invite link

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.ExportGroupCallInvite
    """

    __slots__: List[str] = ["link"]

    ID = 0x204bd158
    QUALNAME = "types.phone.ExportedGroupCallInvite"

    def __init__(self, *, link: str) -> None:
        self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedGroupCallInvite":
        # No flags

        link = String.read(b)

        return ExportedGroupCallInvite(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.link))

        return b.getvalue()
