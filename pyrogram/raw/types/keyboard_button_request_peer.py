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


class KeyboardButtonRequestPeer(TLObject):  # type: ignore
    """Prompts the user to select and share one or more peers with the bot using messages.sendBotRequestedPeer

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``5B0F15F5``

    Parameters:
        text (``str``):
            Button text

        button_id (``int`` ``32-bit``):
            Button ID, to be passed to messages.sendBotRequestedPeer.

        peer_type (:obj:`RequestPeerType <pyrogram.raw.base.RequestPeerType>`):
            Filtering criteria to use for the peer selection list shown to the user. The list should display all existing peers of the specified type, and should also offer an option for the user to create and immediately use one or more (up to max_quantity) peers of the specified type, if needed.

        max_quantity (``int`` ``32-bit``):
            Maximum number of peers that can be chosne.

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "button_id", "peer_type", "max_quantity", "style"]

    ID = 0x5b0f15f5
    QUALNAME = "types.KeyboardButtonRequestPeer"

    def __init__(self, *, text: str, button_id: int, peer_type: "raw.base.RequestPeerType", max_quantity: int, style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text  # string
        self.button_id = button_id  # int
        self.peer_type = peer_type  # RequestPeerType
        self.max_quantity = max_quantity  # int
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPeer":

        flags = Int.read(b)

        style = TLObject.read(b) if flags & (1 << 10) else None

        text = String.read(b)

        button_id = Int.read(b)

        peer_type = TLObject.read(b)

        max_quantity = Int.read(b)

        return KeyboardButtonRequestPeer(text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        b.write(String(self.text))

        b.write(Int(self.button_id))

        b.write(self.peer_type.write())

        b.write(Int(self.max_quantity))

        return b.getvalue()
