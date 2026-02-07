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


class AcceptUrlAuth(TLObject):  # type: ignore
    """Use this to accept a Seamless Telegram Login authorization request, for more info click here »


    Details:
        - Layer: ``224``
        - ID: ``B12C7125``

    Parameters:
        write_allowed (``bool``, *optional*):
            Set this flag to allow the bot to send messages to you (if requested)

        share_phone_number (``bool``, *optional*):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            The location of the message

        msg_id (``int`` ``32-bit``, *optional*):
            Message ID of the message with the login button

        button_id (``int`` ``32-bit``, *optional*):
            ID of the login button

        url (``str``, *optional*):
            URL used for link URL authorization, click here for more info »

    Returns:
        :obj:`UrlAuthResult <pyrogram.raw.base.UrlAuthResult>`
    """

    __slots__: List[str] = ["write_allowed", "share_phone_number", "peer", "msg_id", "button_id", "url"]

    ID = 0xb12c7125
    QUALNAME = "functions.messages.AcceptUrlAuth"

    def __init__(self, *, write_allowed: Optional[bool] = None, share_phone_number: Optional[bool] = None, peer: "raw.base.InputPeer" = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None) -> None:
        self.write_allowed = write_allowed  # flags.0?true
        self.share_phone_number = share_phone_number  # flags.3?true
        self.peer = peer  # flags.1?InputPeer
        self.msg_id = msg_id  # flags.1?int
        self.button_id = button_id  # flags.1?int
        self.url = url  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptUrlAuth":

        flags = Int.read(b)

        write_allowed = True if flags & (1 << 0) else False
        share_phone_number = True if flags & (1 << 3) else False
        peer = TLObject.read(b) if flags & (1 << 1) else None

        msg_id = Int.read(b) if flags & (1 << 1) else None
        button_id = Int.read(b) if flags & (1 << 1) else None
        url = String.read(b) if flags & (1 << 2) else None
        return AcceptUrlAuth(write_allowed=write_allowed, share_phone_number=share_phone_number, peer=peer, msg_id=msg_id, button_id=button_id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.write_allowed else 0
        flags |= (1 << 3) if self.share_phone_number else 0
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
