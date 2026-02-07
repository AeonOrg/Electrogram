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


class Passkeys(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.Passkeys`.

    Details:
        - Layer: ``224``
        - ID: ``F8E0AA1C``

    Parameters:
        passkeys (List of :obj:`Passkey <pyrogram.raw.base.Passkey>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPasskeys
    """

    __slots__: List[str] = ["passkeys"]

    ID = 0xf8e0aa1c
    QUALNAME = "types.account.Passkeys"

    def __init__(self, *, passkeys: List["raw.base.Passkey"]) -> None:
        self.passkeys = passkeys  # Vector<Passkey>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Passkeys":
        # No flags

        passkeys = TLObject.read(b)

        return Passkeys(passkeys=passkeys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.passkeys))

        return b.getvalue()
