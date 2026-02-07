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


class GetPinnedDialogs(TLObject):  # type: ignore
    """Get pinned dialogs


    Details:
        - Layer: ``224``
        - ID: ``D6B94DF2``

    Parameters:
        folder_id (``int`` ``32-bit``):
            Peer folder ID, for more info click here

    Returns:
        :obj:`messages.PeerDialogs <pyrogram.raw.base.messages.PeerDialogs>`
    """

    __slots__: List[str] = ["folder_id"]

    ID = 0xd6b94df2
    QUALNAME = "functions.messages.GetPinnedDialogs"

    def __init__(self, *, folder_id: int) -> None:
        self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPinnedDialogs":
        # No flags

        folder_id = Int.read(b)

        return GetPinnedDialogs(folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.folder_id))

        return b.getvalue()
