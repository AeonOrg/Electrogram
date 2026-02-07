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


class InputPasskeyCredentialFirebasePNV(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPasskeyCredential`.

    Details:
        - Layer: ``224``
        - ID: ``5B1CCB28``

    Parameters:
        pnv_token (``str``):
            N/A

    """

    __slots__: List[str] = ["pnv_token"]

    ID = 0x5b1ccb28
    QUALNAME = "types.InputPasskeyCredentialFirebasePNV"

    def __init__(self, *, pnv_token: str) -> None:
        self.pnv_token = pnv_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPasskeyCredentialFirebasePNV":
        # No flags

        pnv_token = String.read(b)

        return InputPasskeyCredentialFirebasePNV(pnv_token=pnv_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.pnv_token))

        return b.getvalue()
