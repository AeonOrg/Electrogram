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


class InputPasskeyCredentialPublicKey(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPasskeyCredential`.

    Details:
        - Layer: ``224``
        - ID: ``3C27B78F``

    Parameters:
        id (``str``):
            N/A

        raw_id (``str``):
            N/A

        response (:obj:`InputPasskeyResponse <pyrogram.raw.base.InputPasskeyResponse>`):
            N/A

    """

    __slots__: List[str] = ["id", "raw_id", "response"]

    ID = 0x3c27b78f
    QUALNAME = "types.InputPasskeyCredentialPublicKey"

    def __init__(self, *, id: str, raw_id: str, response: "raw.base.InputPasskeyResponse") -> None:
        self.id = id  # string
        self.raw_id = raw_id  # string
        self.response = response  # InputPasskeyResponse

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPasskeyCredentialPublicKey":
        # No flags

        id = String.read(b)

        raw_id = String.read(b)

        response = TLObject.read(b)

        return InputPasskeyCredentialPublicKey(id=id, raw_id=raw_id, response=response)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.id))

        b.write(String(self.raw_id))

        b.write(self.response.write())

        return b.getvalue()
