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


class SetEmojiStickers(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``3CD930B7``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):


        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "stickerset"]

    ID = 0x3cd930b7
    QUALNAME = "functions.channels.SetEmojiStickers"

    def __init__(self, *, channel: "raw.base.InputChannel", stickerset: "raw.base.InputStickerSet") -> None:
        self.channel = channel  # InputChannel
        self.stickerset = stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetEmojiStickers":
        # No flags

        channel = TLObject.read(b)

        stickerset = TLObject.read(b)

        return SetEmojiStickers(channel=channel, stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.stickerset.write())

        return b.getvalue()
