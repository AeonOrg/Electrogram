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


class InputBusinessAwayMessage(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.InputBusinessAwayMessage`.

    Details:
        - Layer: ``224``
        - ID: ``832175E0``

    Parameters:
        shortcut_id (``int`` ``32-bit``):


        schedule (:obj:`BusinessAwayMessageSchedule <pyrogram.raw.base.BusinessAwayMessageSchedule>`):


        recipients (:obj:`InputBusinessRecipients <pyrogram.raw.base.InputBusinessRecipients>`):


        offline_only (``bool``, *optional*):


    """

    __slots__: List[str] = ["shortcut_id", "schedule", "recipients", "offline_only"]

    ID = 0x832175e0
    QUALNAME = "types.InputBusinessAwayMessage"

    def __init__(self, *, shortcut_id: int, schedule: "raw.base.BusinessAwayMessageSchedule", recipients: "raw.base.InputBusinessRecipients", offline_only: Optional[bool] = None) -> None:
        self.shortcut_id = shortcut_id  # int
        self.schedule = schedule  # BusinessAwayMessageSchedule
        self.recipients = recipients  # InputBusinessRecipients
        self.offline_only = offline_only  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessAwayMessage":

        flags = Int.read(b)

        offline_only = True if flags & (1 << 0) else False
        shortcut_id = Int.read(b)

        schedule = TLObject.read(b)

        recipients = TLObject.read(b)

        return InputBusinessAwayMessage(shortcut_id=shortcut_id, schedule=schedule, recipients=recipients, offline_only=offline_only)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.offline_only else 0
        b.write(Int(flags))

        b.write(Int(self.shortcut_id))

        b.write(self.schedule.write())

        b.write(self.recipients.write())

        return b.getvalue()
