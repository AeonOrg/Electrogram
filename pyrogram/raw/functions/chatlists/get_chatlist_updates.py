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


class GetChatlistUpdates(TLObject):  # type: ignore
    """Fetch new chats associated with an imported chat folder deep link ». Must be invoked at most every chatlist_update_period seconds (as per the related client configuration parameter »).


    Details:
        - Layer: ``224``
        - ID: ``89419521``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            The folder

    Returns:
        :obj:`chatlists.ChatlistUpdates <pyrogram.raw.base.chatlists.ChatlistUpdates>`
    """

    __slots__: List[str] = ["chatlist"]

    ID = 0x89419521
    QUALNAME = "functions.chatlists.GetChatlistUpdates"

    def __init__(self, *, chatlist: "raw.base.InputChatlist") -> None:
        self.chatlist = chatlist  # InputChatlist

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatlistUpdates":
        # No flags

        chatlist = TLObject.read(b)

        return GetChatlistUpdates(chatlist=chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.chatlist.write())

        return b.getvalue()
