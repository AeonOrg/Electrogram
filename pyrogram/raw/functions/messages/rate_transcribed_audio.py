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


class RateTranscribedAudio(TLObject):  # type: ignore
    """Rate transcribed voice message


    Details:
        - Layer: ``224``
        - ID: ``7F1D072F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the voice message was sent

        msg_id (``int`` ``32-bit``):
            Message ID

        transcription_id (``int`` ``64-bit``):
            Transcription ID

        good (``bool``):
            Whether the transcription was correct

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "good"]

    ID = 0x7f1d072f
    QUALNAME = "functions.messages.RateTranscribedAudio"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, transcription_id: int, good: bool) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.transcription_id = transcription_id  # long
        self.good = good  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RateTranscribedAudio":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        transcription_id = Long.read(b)

        good = Bool.read(b)

        return RateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, good=good)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Long(self.transcription_id))

        b.write(Bool(self.good))

        return b.getvalue()
