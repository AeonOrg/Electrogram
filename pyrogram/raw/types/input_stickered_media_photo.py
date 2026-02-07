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


class InputStickeredMediaPhoto(TLObject):  # type: ignore
    """A photo with stickers attached

    Constructor of :obj:`~pyrogram.raw.base.InputStickeredMedia`.

    Details:
        - Layer: ``224``
        - ID: ``4A992157``

    Parameters:
        id (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            The photo

    """

    __slots__: List[str] = ["id"]

    ID = 0x4a992157
    QUALNAME = "types.InputStickeredMediaPhoto"

    def __init__(self, *, id: "raw.base.InputPhoto") -> None:
        self.id = id  # InputPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickeredMediaPhoto":
        # No flags

        id = TLObject.read(b)

        return InputStickeredMediaPhoto(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        return b.getvalue()
