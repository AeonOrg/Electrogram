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


class SentEncryptedFile(TLObject):  # type: ignore
    """Message with a file enclosure sent to a protected chat

    Constructor of :obj:`~pyrogram.raw.base.messages.SentEncryptedMessage`.

    Details:
        - Layer: ``224``
        - ID: ``9493FF32``

    Parameters:
        date (``int`` ``32-bit``):
            Sending date

        file (:obj:`EncryptedFile <pyrogram.raw.base.EncryptedFile>`):
            Attached file

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SendEncrypted
            messages.SendEncryptedFile
            messages.SendEncryptedService
    """

    __slots__: List[str] = ["date", "file"]

    ID = 0x9493ff32
    QUALNAME = "types.messages.SentEncryptedFile"

    def __init__(self, *, date: int, file: "raw.base.EncryptedFile") -> None:
        self.date = date  # int
        self.file = file  # EncryptedFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEncryptedFile":
        # No flags

        date = Int.read(b)

        file = TLObject.read(b)

        return SentEncryptedFile(date=date, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.date))

        b.write(self.file.write())

        return b.getvalue()
