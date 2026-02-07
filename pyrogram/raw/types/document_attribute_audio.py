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


class DocumentAttributeAudio(TLObject):  # type: ignore
    """Represents an audio file

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``9852F9C6``

    Parameters:
        duration (``int`` ``32-bit``):
            Duration in seconds

        voice (``bool``, *optional*):
            Whether this is a voice message

        title (``str``, *optional*):
            Name of song

        performer (``str``, *optional*):
            Performer

        waveform (``bytes``, *optional*):
            Waveform: consists in a series of bitpacked 5-bit values. Example implementation: android.

    """

    __slots__: List[str] = ["duration", "voice", "title", "performer", "waveform"]

    ID = 0x9852f9c6
    QUALNAME = "types.DocumentAttributeAudio"

    def __init__(self, *, duration: int, voice: Optional[bool] = None, title: Optional[str] = None, performer: Optional[str] = None, waveform: Optional[bytes] = None) -> None:
        self.duration = duration  # int
        self.voice = voice  # flags.10?true
        self.title = title  # flags.0?string
        self.performer = performer  # flags.1?string
        self.waveform = waveform  # flags.2?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeAudio":

        flags = Int.read(b)

        voice = True if flags & (1 << 10) else False
        duration = Int.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        performer = String.read(b) if flags & (1 << 1) else None
        waveform = Bytes.read(b) if flags & (1 << 2) else None
        return DocumentAttributeAudio(duration=duration, voice=voice, title=title, performer=performer, waveform=waveform)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.voice else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.performer is not None else 0
        flags |= (1 << 2) if self.waveform is not None else 0
        b.write(Int(flags))

        b.write(Int(self.duration))

        if self.title is not None:
            b.write(String(self.title))

        if self.performer is not None:
            b.write(String(self.performer))

        if self.waveform is not None:
            b.write(Bytes(self.waveform))

        return b.getvalue()
