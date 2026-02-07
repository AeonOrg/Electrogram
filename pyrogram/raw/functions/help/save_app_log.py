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


class SaveAppLog(TLObject):  # type: ignore
    """Saves logs of application on the server.


    Details:
        - Layer: ``224``
        - ID: ``6F02F748``

    Parameters:
        events (List of :obj:`InputAppEvent <pyrogram.raw.base.InputAppEvent>`):
            List of input events

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["events"]

    ID = 0x6f02f748
    QUALNAME = "functions.help.SaveAppLog"

    def __init__(self, *, events: List["raw.base.InputAppEvent"]) -> None:
        self.events = events  # Vector<InputAppEvent>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAppLog":
        # No flags

        events = TLObject.read(b)

        return SaveAppLog(events=events)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.events))

        return b.getvalue()
