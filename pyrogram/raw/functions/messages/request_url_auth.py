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


class RequestUrlAuth(TLObject):  # type: ignore
    """Get more info about a Seamless Telegram Login authorization request, for more info click here »


    Details:
        - Layer: ``224``
        - ID: ``198FB446``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Peer where the message is located

        msg_id (``int`` ``32-bit``, *optional*):
            The message

        button_id (``int`` ``32-bit``, *optional*):
            The ID of the button with the authorization request

        url (``str``, *optional*):
            URL used for link URL authorization, click here for more info »

    Returns:
        :obj:`UrlAuthResult <pyrogram.raw.base.UrlAuthResult>`
    """

    __slots__: List[str] = ["peer", "msg_id", "button_id", "url"]

    ID = 0x198fb446
    QUALNAME = "functions.messages.RequestUrlAuth"

    def __init__(self, *, peer: "raw.base.InputPeer" = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None) -> None:
        self.peer = peer  # flags.1?InputPeer
        self.msg_id = msg_id  # flags.1?int
        self.button_id = button_id  # flags.1?int
        self.url = url  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestUrlAuth":

        flags = Int.read(b)

        peer = TLObject.read(b) if flags & (1 << 1) else None

        msg_id = Int.read(b) if flags & (1 << 1) else None
        button_id = Int.read(b) if flags & (1 << 1) else None
        url = String.read(b) if flags & (1 << 2) else None
        return RequestUrlAuth(peer=peer, msg_id=msg_id, button_id=button_id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.peer is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        flags |= (1 << 1) if self.button_id is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        b.write(Int(flags))

        if self.peer is not None:
            b.write(self.peer.write())

        if self.msg_id is not None:
            b.write(Int(self.msg_id))

        if self.button_id is not None:
            b.write(Int(self.button_id))

        if self.url is not None:
            b.write(String(self.url))

        return b.getvalue()
