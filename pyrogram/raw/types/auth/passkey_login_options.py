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


class PasskeyLoginOptions(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.PasskeyLoginOptions`.

    Details:
        - Layer: ``224``
        - ID: ``E2037789``

    Parameters:
        options (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.InitPasskeyLogin
    """

    __slots__: List[str] = ["options"]

    ID = 0xe2037789
    QUALNAME = "types.auth.PasskeyLoginOptions"

    def __init__(self, *, options: "raw.base.DataJSON") -> None:
        self.options = options  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasskeyLoginOptions":
        # No flags

        options = TLObject.read(b)

        return PasskeyLoginOptions(options=options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.options.write())

        return b.getvalue()
