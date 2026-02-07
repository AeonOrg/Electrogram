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


class DeleteGroupCallParticipantMessages(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1DBFECA0``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        report_spam (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "participant", "report_spam"]

    ID = 0x1dbfeca0
    QUALNAME = "functions.phone.DeleteGroupCallParticipantMessages"

    def __init__(self, *, call: "raw.base.InputGroupCall", participant: "raw.base.InputPeer", report_spam: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.participant = participant  # InputPeer
        self.report_spam = report_spam  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteGroupCallParticipantMessages":

        flags = Int.read(b)

        report_spam = True if flags & (1 << 0) else False
        call = TLObject.read(b)

        participant = TLObject.read(b)

        return DeleteGroupCallParticipantMessages(call=call, participant=participant, report_spam=report_spam)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        b.write(Int(flags))

        b.write(self.call.write())

        b.write(self.participant.write())

        return b.getvalue()
