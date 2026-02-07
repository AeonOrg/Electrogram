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


class UpdatePersonalChannel(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``D94305E0``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel"]

    ID = 0xd94305e0
    QUALNAME = "functions.account.UpdatePersonalChannel"

    def __init__(self, *, channel: "raw.base.InputChannel") -> None:
        self.channel = channel  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePersonalChannel":
        # No flags

        channel = TLObject.read(b)

        return UpdatePersonalChannel(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        return b.getvalue()
