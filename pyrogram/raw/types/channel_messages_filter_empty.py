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


class ChannelMessagesFilterEmpty(TLObject):  # type: ignore
    """No filter

    Constructor of :obj:`~pyrogram.raw.base.ChannelMessagesFilter`.

    Details:
        - Layer: ``224``
        - ID: ``94D42EE7``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x94d42ee7
    QUALNAME = "types.ChannelMessagesFilterEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelMessagesFilterEmpty":
        # No flags

        return ChannelMessagesFilterEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
