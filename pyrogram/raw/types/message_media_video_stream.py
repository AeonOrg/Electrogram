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


class MessageMediaVideoStream(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``CA5CAB89``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        rtmp_stream (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["call", "rtmp_stream"]

    ID = 0xca5cab89
    QUALNAME = "types.MessageMediaVideoStream"

    def __init__(self, *, call: "raw.base.InputGroupCall", rtmp_stream: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.rtmp_stream = rtmp_stream  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaVideoStream":

        flags = Int.read(b)

        rtmp_stream = True if flags & (1 << 0) else False
        call = TLObject.read(b)

        return MessageMediaVideoStream(call=call, rtmp_stream=rtmp_stream)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtmp_stream else 0
        b.write(Int(flags))

        b.write(self.call.write())

        return b.getvalue()
