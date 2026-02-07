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


class ClickSponsoredMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8235057E``

    Parameters:
        random_id (``bytes``):
            N/A

        media (``bool``, *optional*):
            N/A

        fullscreen (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["random_id", "media", "fullscreen"]

    ID = 0x8235057e
    QUALNAME = "functions.messages.ClickSponsoredMessage"

    def __init__(self, *, random_id: bytes, media: Optional[bool] = None, fullscreen: Optional[bool] = None) -> None:
        self.random_id = random_id  # bytes
        self.media = media  # flags.0?true
        self.fullscreen = fullscreen  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClickSponsoredMessage":

        flags = Int.read(b)

        media = True if flags & (1 << 0) else False
        fullscreen = True if flags & (1 << 1) else False
        random_id = Bytes.read(b)

        return ClickSponsoredMessage(random_id=random_id, media=media, fullscreen=fullscreen)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.media else 0
        flags |= (1 << 1) if self.fullscreen else 0
        b.write(Int(flags))

        b.write(Bytes(self.random_id))

        return b.getvalue()
