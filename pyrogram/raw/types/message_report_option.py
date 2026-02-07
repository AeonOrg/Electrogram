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


class MessageReportOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageReportOption`.

    Details:
        - Layer: ``224``
        - ID: ``7903E3D9``

    Parameters:
        text (``str``):
            N/A

        option (``bytes``):
            N/A

    """

    __slots__: List[str] = ["text", "option"]

    ID = 0x7903e3d9
    QUALNAME = "types.MessageReportOption"

    def __init__(self, *, text: str, option: bytes) -> None:
        self.text = text  # string
        self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReportOption":
        # No flags

        text = String.read(b)

        option = Bytes.read(b)

        return MessageReportOption(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        b.write(Bytes(self.option))

        return b.getvalue()
