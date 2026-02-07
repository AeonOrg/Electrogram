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


class InputFileStoryDocument(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputFile`.

    Details:
        - Layer: ``224``
        - ID: ``62DC8B48``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0x62dc8b48
    QUALNAME = "types.InputFileStoryDocument"

    def __init__(self, *, id: "raw.base.InputDocument") -> None:
        self.id = id  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFileStoryDocument":
        # No flags

        id = TLObject.read(b)

        return InputFileStoryDocument(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        return b.getvalue()
