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


class ExportGroupCallInvite(TLObject):  # type: ignore
    """Get an invite link for a group call or livestream


    Details:
        - Layer: ``224``
        - ID: ``E6AA647F``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            The group call

        can_self_unmute (``bool``, *optional*):
            For livestreams or muted group chats, if set, users that join using this link will be able to speak without explicitly requesting permission by (for example by raising their hand).

    Returns:
        :obj:`phone.ExportedGroupCallInvite <pyrogram.raw.base.phone.ExportedGroupCallInvite>`
    """

    __slots__: List[str] = ["call", "can_self_unmute"]

    ID = 0xe6aa647f
    QUALNAME = "functions.phone.ExportGroupCallInvite"

    def __init__(self, *, call: "raw.base.InputGroupCall", can_self_unmute: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.can_self_unmute = can_self_unmute  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportGroupCallInvite":

        flags = Int.read(b)

        can_self_unmute = True if flags & (1 << 0) else False
        call = TLObject.read(b)

        return ExportGroupCallInvite(call=call, can_self_unmute=can_self_unmute)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_self_unmute else 0
        b.write(Int(flags))

        b.write(self.call.write())

        return b.getvalue()
