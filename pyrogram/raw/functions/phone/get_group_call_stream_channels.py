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


class GetGroupCallStreamChannels(TLObject):  # type: ignore
    """Get info about RTMP streams in a group call or livestream.
This method should be invoked to the same group/channel-related DC used for downloading livestream chunks.
As usual, the media DC is preferred, if available.


    Details:
        - Layer: ``224``
        - ID: ``1AB21940``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call or livestream

    Returns:
        :obj:`phone.GroupCallStreamChannels <pyrogram.raw.base.phone.GroupCallStreamChannels>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x1ab21940
    QUALNAME = "functions.phone.GetGroupCallStreamChannels"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call  # InputGroupCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStreamChannels":
        # No flags

        call = TLObject.read(b)

        return GetGroupCallStreamChannels(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        return b.getvalue()
