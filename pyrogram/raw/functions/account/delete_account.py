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


class DeleteAccount(TLObject):  # type: ignore
    """Delete the user's account from the telegram servers.


    Details:
        - Layer: ``224``
        - ID: ``A2C0CF74``

    Parameters:
        reason (``str``):
            Why is the account being deleted, can be empty

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`, *optional*):
            2FA password: this field can be omitted even for accounts with 2FA enabled: in this case account account deletion will be delayed by 7 days as specified in the docs »

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reason", "password"]

    ID = 0xa2c0cf74
    QUALNAME = "functions.account.DeleteAccount"

    def __init__(self, *, reason: str, password: "raw.base.InputCheckPasswordSRP" = None) -> None:
        self.reason = reason  # string
        self.password = password  # flags.0?InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteAccount":

        flags = Int.read(b)

        reason = String.read(b)

        password = TLObject.read(b) if flags & (1 << 0) else None

        return DeleteAccount(reason=reason, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.password is not None else 0
        b.write(Int(flags))

        b.write(String(self.reason))

        if self.password is not None:
            b.write(self.password.write())

        return b.getvalue()
