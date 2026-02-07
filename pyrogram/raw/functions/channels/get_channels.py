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


class GetChannels(TLObject):  # type: ignore
    """Get info about channels/supergroups


    Details:
        - Layer: ``224``
        - ID: ``A7F6BBB``

    Parameters:
        id (List of :obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            IDs of channels/supergroups to get info about

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xa7f6bbb
    QUALNAME = "functions.channels.GetChannels"

    def __init__(self, *, id: List["raw.base.InputChannel"]) -> None:
        self.id = id  # Vector<InputChannel>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannels":
        # No flags

        id = TLObject.read(b)

        return GetChannels(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id))

        return b.getvalue()
