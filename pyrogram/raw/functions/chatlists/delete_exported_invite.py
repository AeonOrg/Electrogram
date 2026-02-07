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


class DeleteExportedInvite(TLObject):  # type: ignore
    """Delete a previously created chat folder deep link ».


    Details:
        - Layer: ``224``
        - ID: ``719C5C5E``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            The related folder

        slug (``str``):
            slug obtained from the chat folder deep link ».

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chatlist", "slug"]

    ID = 0x719c5c5e
    QUALNAME = "functions.chatlists.DeleteExportedInvite"

    def __init__(self, *, chatlist: "raw.base.InputChatlist", slug: str) -> None:
        self.chatlist = chatlist  # InputChatlist
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteExportedInvite":
        # No flags

        chatlist = TLObject.read(b)

        slug = String.read(b)

        return DeleteExportedInvite(chatlist=chatlist, slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.chatlist.write())

        b.write(String(self.slug))

        return b.getvalue()
