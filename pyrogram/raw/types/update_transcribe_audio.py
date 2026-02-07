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


class UpdateTranscribeAudio(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``88617090``

    Parameters:
        transcription_id (``int`` ``64-bit``):
            N/A

        text (``str``):
            N/A

        final (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["transcription_id", "text", "final"]

    ID = 0x88617090
    QUALNAME = "types.UpdateTranscribeAudio"

    def __init__(self, *, transcription_id: int, text: str, final: Optional[bool] = None) -> None:
        self.transcription_id = transcription_id  # long
        self.text = text  # string
        self.final = final  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTranscribeAudio":

        flags = Int.read(b)

        final = True if flags & (1 << 0) else False
        transcription_id = Long.read(b)

        text = String.read(b)

        return UpdateTranscribeAudio(transcription_id=transcription_id, text=text, final=final)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final else 0
        b.write(Int(flags))

        b.write(Long(self.transcription_id))

        b.write(String(self.text))

        return b.getvalue()
