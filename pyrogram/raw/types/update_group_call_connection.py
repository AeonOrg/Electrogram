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


class UpdateGroupCallConnection(TLObject):  # type: ignore
    """New WebRTC parameters

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``B783982``

    Parameters:
        params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            WebRTC parameters

        presentation (``bool``, *optional*):
            Are these parameters related to the screen capture session currently in progress?

    """

    __slots__: List[str] = ["params", "presentation"]

    ID = 0xb783982
    QUALNAME = "types.UpdateGroupCallConnection"

    def __init__(self, *, params: "raw.base.DataJSON", presentation: Optional[bool] = None) -> None:
        self.params = params  # DataJSON
        self.presentation = presentation  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallConnection":

        flags = Int.read(b)

        presentation = True if flags & (1 << 0) else False
        params = TLObject.read(b)

        return UpdateGroupCallConnection(params=params, presentation=presentation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.presentation else 0
        b.write(Int(flags))

        b.write(self.params.write())

        return b.getvalue()
