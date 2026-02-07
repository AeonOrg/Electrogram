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


class DeleteMessages(TLObject):  # type: ignore
    """Deletes messages by their identifiers.


    Details:
        - Layer: ``224``
        - ID: ``E58E95D2``

    Parameters:
        id (List of ``int`` ``32-bit``):
            Message ID list

        revoke (``bool``, *optional*):
            Whether to delete messages for all participants of the chat

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.raw.base.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["id", "revoke"]

    ID = 0xe58e95d2
    QUALNAME = "functions.messages.DeleteMessages"

    def __init__(self, *, id: List[int], revoke: Optional[bool] = None) -> None:
        self.id = id  # Vector<int>
        self.revoke = revoke  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteMessages":

        flags = Int.read(b)

        revoke = True if flags & (1 << 0) else False
        id = TLObject.read(b, Int)

        return DeleteMessages(id=id, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke else 0
        b.write(Int(flags))

        b.write(Vector(self.id, Int))

        return b.getvalue()
