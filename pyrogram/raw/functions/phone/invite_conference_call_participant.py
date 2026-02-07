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


class InviteConferenceCallParticipant(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BCF22685``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        video (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "user_id", "video"]

    ID = 0xbcf22685
    QUALNAME = "functions.phone.InviteConferenceCallParticipant"

    def __init__(self, *, call: "raw.base.InputGroupCall", user_id: "raw.base.InputUser", video: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.user_id = user_id  # InputUser
        self.video = video  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteConferenceCallParticipant":

        flags = Int.read(b)

        video = True if flags & (1 << 0) else False
        call = TLObject.read(b)

        user_id = TLObject.read(b)

        return InviteConferenceCallParticipant(call=call, user_id=user_id, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))

        b.write(self.call.write())

        b.write(self.user_id.write())

        return b.getvalue()
