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


class DeleteConferenceCallParticipants(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8CA60525``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        ids (List of ``int`` ``64-bit``):
            N/A

        block (``bytes``):
            N/A

        only_left (``bool``, *optional*):
            N/A

        kick (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "ids", "block", "only_left", "kick"]

    ID = 0x8ca60525
    QUALNAME = "functions.phone.DeleteConferenceCallParticipants"

    def __init__(self, *, call: "raw.base.InputGroupCall", ids: List[int], block: bytes, only_left: Optional[bool] = None, kick: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.ids = ids  # Vector<long>
        self.block = block  # bytes
        self.only_left = only_left  # flags.0?true
        self.kick = kick  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteConferenceCallParticipants":

        flags = Int.read(b)

        only_left = True if flags & (1 << 0) else False
        kick = True if flags & (1 << 1) else False
        call = TLObject.read(b)

        ids = TLObject.read(b, Long)

        block = Bytes.read(b)

        return DeleteConferenceCallParticipants(call=call, ids=ids, block=block, only_left=only_left, kick=kick)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_left else 0
        flags |= (1 << 1) if self.kick else 0
        b.write(Int(flags))

        b.write(self.call.write())

        b.write(Vector(self.ids, Long))

        b.write(Bytes(self.block))

        return b.getvalue()
