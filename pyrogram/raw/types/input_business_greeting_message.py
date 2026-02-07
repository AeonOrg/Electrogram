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


class InputBusinessGreetingMessage(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.InputBusinessGreetingMessage`.

    Details:
        - Layer: ``224``
        - ID: ``194CB3B``

    Parameters:
        shortcut_id (``int`` ``32-bit``):


        recipients (:obj:`InputBusinessRecipients <pyrogram.raw.base.InputBusinessRecipients>`):


        no_activity_days (``int`` ``32-bit``):


    """

    __slots__: List[str] = ["shortcut_id", "recipients", "no_activity_days"]

    ID = 0x194cb3b
    QUALNAME = "types.InputBusinessGreetingMessage"

    def __init__(self, *, shortcut_id: int, recipients: "raw.base.InputBusinessRecipients", no_activity_days: int) -> None:
        self.shortcut_id = shortcut_id  # int
        self.recipients = recipients  # InputBusinessRecipients
        self.no_activity_days = no_activity_days  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessGreetingMessage":
        # No flags

        shortcut_id = Int.read(b)

        recipients = TLObject.read(b)

        no_activity_days = Int.read(b)

        return InputBusinessGreetingMessage(shortcut_id=shortcut_id, recipients=recipients, no_activity_days=no_activity_days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.shortcut_id))

        b.write(self.recipients.write())

        b.write(Int(self.no_activity_days))

        return b.getvalue()
