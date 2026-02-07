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


class UpdateGroupCallParticipants(TLObject):  # type: ignore
    """The participant list of a certain group call has changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F2EBDB4E``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call

        participants (List of :obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            New participant list

        version (``int`` ``32-bit``):
            Version

    """

    __slots__: List[str] = ["call", "participants", "version"]

    ID = 0xf2ebdb4e
    QUALNAME = "types.UpdateGroupCallParticipants"

    def __init__(self, *, call: "raw.base.InputGroupCall", participants: List["raw.base.GroupCallParticipant"], version: int) -> None:
        self.call = call  # InputGroupCall
        self.participants = participants  # Vector<GroupCallParticipant>
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallParticipants":
        # No flags

        call = TLObject.read(b)

        participants = TLObject.read(b)

        version = Int.read(b)

        return UpdateGroupCallParticipants(call=call, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Vector(self.participants))

        b.write(Int(self.version))

        return b.getvalue()
