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


class SecureValueErrorSelfie(TLObject):  # type: ignore
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``224``
        - ID: ``E537CED6``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            One of secureValueTypePassport, secureValueTypeDriverLicense, secureValueTypeIdentityCard, secureValueTypeInternalPassport

        file_hash (``bytes``):
            File hash

        text (``str``):
            Error message

    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0xe537ced6
    QUALNAME = "types.SecureValueErrorSelfie"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: bytes, text: str) -> None:
        self.type = type  # SecureValueType
        self.file_hash = file_hash  # bytes
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorSelfie":
        # No flags

        type = TLObject.read(b)

        file_hash = Bytes.read(b)

        text = String.read(b)

        return SecureValueErrorSelfie(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.type.write())

        b.write(Bytes(self.file_hash))

        b.write(String(self.text))

        return b.getvalue()
