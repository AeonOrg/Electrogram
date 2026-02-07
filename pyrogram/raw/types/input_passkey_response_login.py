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


class InputPasskeyResponseLogin(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPasskeyResponse`.

    Details:
        - Layer: ``224``
        - ID: ``C31FC14A``

    Parameters:
        client_data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        authenticator_data (``bytes``):
            N/A

        signature (``bytes``):
            N/A

        user_handle (``str``):
            N/A

    """

    __slots__: List[str] = ["client_data", "authenticator_data", "signature", "user_handle"]

    ID = 0xc31fc14a
    QUALNAME = "types.InputPasskeyResponseLogin"

    def __init__(self, *, client_data: "raw.base.DataJSON", authenticator_data: bytes, signature: bytes, user_handle: str) -> None:
        self.client_data = client_data  # DataJSON
        self.authenticator_data = authenticator_data  # bytes
        self.signature = signature  # bytes
        self.user_handle = user_handle  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPasskeyResponseLogin":
        # No flags

        client_data = TLObject.read(b)

        authenticator_data = Bytes.read(b)

        signature = Bytes.read(b)

        user_handle = String.read(b)

        return InputPasskeyResponseLogin(client_data=client_data, authenticator_data=authenticator_data, signature=signature, user_handle=user_handle)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.client_data.write())

        b.write(Bytes(self.authenticator_data))

        b.write(Bytes(self.signature))

        b.write(String(self.user_handle))

        return b.getvalue()
