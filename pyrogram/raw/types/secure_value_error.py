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


class SecureValueError(TLObject):  # type: ignore
    """Secure value error

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``224``
        - ID: ``869D758F``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            Type of element which has the issue

        hash (``bytes``):
            Hash

        text (``str``):
            Error message

    """

    __slots__: List[str] = ["type", "hash", "text"]

    ID = 0x869d758f
    QUALNAME = "types.SecureValueError"

    def __init__(self, *, type: "raw.base.SecureValueType", hash: bytes, text: str) -> None:
        self.type = type  # SecureValueType
        self.hash = hash  # bytes
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueError":
        # No flags

        type = TLObject.read(b)

        hash = Bytes.read(b)

        text = String.read(b)

        return SecureValueError(type=type, hash=hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.type.write())

        b.write(Bytes(self.hash))

        b.write(String(self.text))

        return b.getvalue()
