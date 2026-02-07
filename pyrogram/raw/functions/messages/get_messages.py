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


class GetMessages(TLObject):  # type: ignore
    """Returns the list of messages by their IDs.


    Details:
        - Layer: ``224``
        - ID: ``63C66506``

    Parameters:
        id (List of :obj:`InputMessage <pyrogram.raw.base.InputMessage>`):
            Message ID list

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x63c66506
    QUALNAME = "functions.messages.GetMessages"

    def __init__(self, *, id: List["raw.base.InputMessage"]) -> None:
        self.id = id  # Vector<InputMessage>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessages":
        # No flags

        id = TLObject.read(b)

        return GetMessages(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id))

        return b.getvalue()
