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


class CreateBusinessChatLink(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``8851E68E``

    Parameters:
        link (:obj:`InputBusinessChatLink <pyrogram.raw.base.InputBusinessChatLink>`):


    Returns:
        :obj:`BusinessChatLink <pyrogram.raw.base.BusinessChatLink>`
    """

    __slots__: List[str] = ["link"]

    ID = 0x8851e68e
    QUALNAME = "functions.account.CreateBusinessChatLink"

    def __init__(self, *, link: "raw.base.InputBusinessChatLink") -> None:
        self.link = link  # InputBusinessChatLink

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateBusinessChatLink":
        # No flags

        link = TLObject.read(b)

        return CreateBusinessChatLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.link.write())

        return b.getvalue()
