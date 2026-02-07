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


class SetChatTheme(TLObject):  # type: ignore
    """Change the chat theme of a certain chat


    Details:
        - Layer: ``224``
        - ID: ``81202C9``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Private chat where to change theme

        theme (:obj:`InputChatTheme <pyrogram.raw.base.InputChatTheme>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "theme"]

    ID = 0x81202c9
    QUALNAME = "functions.messages.SetChatTheme"

    def __init__(self, *, peer: "raw.base.InputPeer", theme: "raw.base.InputChatTheme") -> None:
        self.peer = peer  # InputPeer
        self.theme = theme  # InputChatTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatTheme":
        # No flags

        peer = TLObject.read(b)

        theme = TLObject.read(b)

        return SetChatTheme(peer=peer, theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.theme.write())

        return b.getvalue()
