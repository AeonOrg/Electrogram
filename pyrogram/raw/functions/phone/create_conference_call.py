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


class CreateConferenceCall(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7D0444BB``

    Parameters:
        random_id (``int`` ``32-bit``):
            N/A

        muted (``bool``, *optional*):
            N/A

        video_stopped (``bool``, *optional*):
            N/A

        join (``bool``, *optional*):
            N/A

        public_key (``int`` ``256-bit``, *optional*):
            N/A

        block (``bytes``, *optional*):
            N/A

        params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["random_id", "muted", "video_stopped", "join", "public_key", "block", "params"]

    ID = 0x7d0444bb
    QUALNAME = "functions.phone.CreateConferenceCall"

    def __init__(self, *, random_id: int, muted: Optional[bool] = None, video_stopped: Optional[bool] = None, join: Optional[bool] = None, public_key: Optional[int] = None, block: Optional[bytes] = None, params: "raw.base.DataJSON" = None) -> None:
        self.random_id = random_id  # int
        self.muted = muted  # flags.0?true
        self.video_stopped = video_stopped  # flags.2?true
        self.join = join  # flags.3?true
        self.public_key = public_key  # flags.3?int256
        self.block = block  # flags.3?bytes
        self.params = params  # flags.3?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateConferenceCall":

        flags = Int.read(b)

        muted = True if flags & (1 << 0) else False
        video_stopped = True if flags & (1 << 2) else False
        join = True if flags & (1 << 3) else False
        random_id = Int.read(b)

        public_key = Int256.read(b) if flags & (1 << 3) else None
        block = Bytes.read(b) if flags & (1 << 3) else None
        params = TLObject.read(b) if flags & (1 << 3) else None

        return CreateConferenceCall(random_id=random_id, muted=muted, video_stopped=video_stopped, join=join, public_key=public_key, block=block, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 2) if self.video_stopped else 0
        flags |= (1 << 3) if self.join else 0
        flags |= (1 << 3) if self.public_key is not None else 0
        flags |= (1 << 3) if self.block is not None else 0
        flags |= (1 << 3) if self.params is not None else 0
        b.write(Int(flags))

        b.write(Int(self.random_id))

        if self.public_key is not None:
            b.write(Int256(self.public_key))

        if self.block is not None:
            b.write(Bytes(self.block))

        if self.params is not None:
            b.write(self.params.write())

        return b.getvalue()
