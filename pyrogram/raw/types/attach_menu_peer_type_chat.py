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


class AttachMenuPeerTypeChat(TLObject):  # type: ignore
    """The bot attachment menu entry is available in groups and supergroups

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``509113F``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x509113f
    QUALNAME = "types.AttachMenuPeerTypeChat"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuPeerTypeChat":
        # No flags

        return AttachMenuPeerTypeChat()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
