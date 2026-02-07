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


class InputMessagesFilterPhoneCalls(TLObject):  # type: ignore
    """Return only phone calls

    Constructor of :obj:`~pyrogram.raw.base.MessagesFilter`.

    Details:
        - Layer: ``224``
        - ID: ``80C99768``

    Parameters:
        missed (``bool``, *optional*):
            Return only missed phone calls

    """

    __slots__: List[str] = ["missed"]

    ID = 0x80c99768
    QUALNAME = "types.InputMessagesFilterPhoneCalls"

    def __init__(self, *, missed: Optional[bool] = None) -> None:
        self.missed = missed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagesFilterPhoneCalls":

        flags = Int.read(b)

        missed = True if flags & (1 << 0) else False
        return InputMessagesFilterPhoneCalls(missed=missed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.missed else 0
        b.write(Int(flags))

        return b.getvalue()
