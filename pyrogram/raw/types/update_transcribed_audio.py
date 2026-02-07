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


class UpdateTranscribedAudio(TLObject):  # type: ignore
    """A pending voice message transcription » initiated with messages.transcribeAudio was updated.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``84CD5A``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer of the transcribed message

        msg_id (``int`` ``32-bit``):
            Transcribed message ID

        transcription_id (``int`` ``64-bit``):
            Transcription ID

        text (``str``):
            Transcribed text

        pending (``bool``, *optional*):
            Whether this transcription is still pending and further updateTranscribedAudio about it will be sent in the future.

    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "text", "pending"]

    ID = 0x84cd5a
    QUALNAME = "types.UpdateTranscribedAudio"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, transcription_id: int, text: str, pending: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.transcription_id = transcription_id  # long
        self.text = text  # string
        self.pending = pending  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTranscribedAudio":

        flags = Int.read(b)

        pending = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        msg_id = Int.read(b)

        transcription_id = Long.read(b)

        text = String.read(b)

        return UpdateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, text=text, pending=pending)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pending else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Long(self.transcription_id))

        b.write(String(self.text))

        return b.getvalue()
