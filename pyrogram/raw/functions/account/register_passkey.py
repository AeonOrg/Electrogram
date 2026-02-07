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


class RegisterPasskey(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``55B41FD6``

    Parameters:
        credential (:obj:`InputPasskeyCredential <pyrogram.raw.base.InputPasskeyCredential>`):
            N/A

    Returns:
        :obj:`Passkey <pyrogram.raw.base.Passkey>`
    """

    __slots__: List[str] = ["credential"]

    ID = 0x55b41fd6
    QUALNAME = "functions.account.RegisterPasskey"

    def __init__(self, *, credential: "raw.base.InputPasskeyCredential") -> None:
        self.credential = credential  # InputPasskeyCredential

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RegisterPasskey":
        # No flags

        credential = TLObject.read(b)

        return RegisterPasskey(credential=credential)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.credential.write())

        return b.getvalue()
