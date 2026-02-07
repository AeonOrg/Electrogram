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


class PeerUser(TLObject):  # type: ignore
    """Chat partner

    Constructor of :obj:`~pyrogram.raw.base.Peer`.

    Details:
        - Layer: ``224``
        - ID: ``59511722``

    Parameters:
        user_id (``int`` ``64-bit``):
            User identifier

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.GetLeaveChatlistSuggestions
    """

    __slots__: List[str] = ["user_id"]

    ID = 0x59511722
    QUALNAME = "types.PeerUser"

    def __init__(self, *, user_id: int) -> None:
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerUser":
        # No flags

        user_id = Long.read(b)

        return PeerUser(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        return b.getvalue()
