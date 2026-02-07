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


class HideChatlistUpdates(TLObject):  # type: ignore
    """Dismiss new pending peers recently added to a chat folder deep link ».


    Details:
        - Layer: ``224``
        - ID: ``66E486FB``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            The folder

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chatlist"]

    ID = 0x66e486fb
    QUALNAME = "functions.chatlists.HideChatlistUpdates"

    def __init__(self, *, chatlist: "raw.base.InputChatlist") -> None:
        self.chatlist = chatlist  # InputChatlist

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HideChatlistUpdates":
        # No flags

        chatlist = TLObject.read(b)

        return HideChatlistUpdates(chatlist=chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.chatlist.write())

        return b.getvalue()
