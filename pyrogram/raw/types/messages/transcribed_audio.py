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


class TranscribedAudio(TLObject):  # type: ignore
    """Transcribed text from a voice message »

    Constructor of :obj:`~pyrogram.raw.base.messages.TranscribedAudio`.

    Details:
        - Layer: ``224``
        - ID: ``CFB9D957``

    Parameters:
        transcription_id (``int`` ``64-bit``):
            Transcription ID

        text (``str``):
            Transcripted text

        pending (``bool``, *optional*):
            Whether the transcription is partial because audio transcription is still in progress, if set the user may receive further updateTranscribedAudio updates with the updated transcription.

        trial_remains_num (``int`` ``32-bit``, *optional*):
            For non-Premium users, this flag will be set, indicating the remaining transcriptions in the free trial period.

        trial_remains_until_date (``int`` ``32-bit``, *optional*):
            For non-Premium users, this flag will be set, indicating the date when the trial_remains_num counter will be reset to the maximum value of transcribe_audio_trial_weekly_number.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.TranscribeAudio
    """

    __slots__: List[str] = ["transcription_id", "text", "pending", "trial_remains_num", "trial_remains_until_date"]

    ID = 0xcfb9d957
    QUALNAME = "types.messages.TranscribedAudio"

    def __init__(self, *, transcription_id: int, text: str, pending: Optional[bool] = None, trial_remains_num: Optional[int] = None, trial_remains_until_date: Optional[int] = None) -> None:
        self.transcription_id = transcription_id  # long
        self.text = text  # string
        self.pending = pending  # flags.0?true
        self.trial_remains_num = trial_remains_num  # flags.1?int
        self.trial_remains_until_date = trial_remains_until_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranscribedAudio":

        flags = Int.read(b)

        pending = True if flags & (1 << 0) else False
        transcription_id = Long.read(b)

        text = String.read(b)

        trial_remains_num = Int.read(b) if flags & (1 << 1) else None
        trial_remains_until_date = Int.read(b) if flags & (1 << 1) else None
        return TranscribedAudio(transcription_id=transcription_id, text=text, pending=pending, trial_remains_num=trial_remains_num, trial_remains_until_date=trial_remains_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pending else 0
        flags |= (1 << 1) if self.trial_remains_num is not None else 0
        flags |= (1 << 1) if self.trial_remains_until_date is not None else 0
        b.write(Int(flags))

        b.write(Long(self.transcription_id))

        b.write(String(self.text))

        if self.trial_remains_num is not None:
            b.write(Int(self.trial_remains_num))

        if self.trial_remains_until_date is not None:
            b.write(Int(self.trial_remains_until_date))

        return b.getvalue()
