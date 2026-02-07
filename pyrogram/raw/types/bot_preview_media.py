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


class BotPreviewMedia(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotPreviewMedia`.

    Details:
        - Layer: ``224``
        - ID: ``23E91BA3``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.AddPreviewMedia
            bots.EditPreviewMedia
            bots.GetPreviewMedias
    """

    __slots__: List[str] = ["date", "media"]

    ID = 0x23e91ba3
    QUALNAME = "types.BotPreviewMedia"

    def __init__(self, *, date: int, media: "raw.base.MessageMedia") -> None:
        self.date = date  # int
        self.media = media  # MessageMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotPreviewMedia":
        # No flags

        date = Int.read(b)

        media = TLObject.read(b)

        return BotPreviewMedia(date=date, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.date))

        b.write(self.media.write())

        return b.getvalue()
