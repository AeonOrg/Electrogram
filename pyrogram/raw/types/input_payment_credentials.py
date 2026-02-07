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


class InputPaymentCredentials(TLObject):  # type: ignore
    """Payment credentials

    Constructor of :obj:`~pyrogram.raw.base.InputPaymentCredentials`.

    Details:
        - Layer: ``224``
        - ID: ``3417D728``

    Parameters:
        data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            Payment credentials

        save (``bool``, *optional*):
            Save payment credential for future use

    """

    __slots__: List[str] = ["data", "save"]

    ID = 0x3417d728
    QUALNAME = "types.InputPaymentCredentials"

    def __init__(self, *, data: "raw.base.DataJSON", save: Optional[bool] = None) -> None:
        self.data = data  # DataJSON
        self.save = save  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPaymentCredentials":

        flags = Int.read(b)

        save = True if flags & (1 << 0) else False
        data = TLObject.read(b)

        return InputPaymentCredentials(data=data, save=save)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.save else 0
        b.write(Int(flags))

        b.write(self.data.write())

        return b.getvalue()
