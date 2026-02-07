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


class StarsTransactionPeerPremiumBot(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.StarsTransactionPeer`.

    Details:
        - Layer: ``224``
        - ID: ``250DBAF8``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x250dbaf8
    QUALNAME = "types.StarsTransactionPeerPremiumBot"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransactionPeerPremiumBot":
        # No flags

        return StarsTransactionPeerPremiumBot()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
