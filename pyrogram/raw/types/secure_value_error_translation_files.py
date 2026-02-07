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


class SecureValueErrorTranslationFiles(TLObject):  # type: ignore
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation changes.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``224``
        - ID: ``34636DD8``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            One of secureValueTypePersonalDetails, secureValueTypePassport, secureValueTypeDriverLicense, secureValueTypeIdentityCard, secureValueTypeInternalPassport, secureValueTypeUtilityBill, secureValueTypeBankStatement, secureValueTypeRentalAgreement, secureValueTypePassportRegistration, secureValueTypeTemporaryRegistration

        file_hash (List of ``bytes``):
            Hash

        text (``str``):
            Error message

    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0x34636dd8
    QUALNAME = "types.SecureValueErrorTranslationFiles"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: List[bytes], text: str) -> None:
        self.type = type  # SecureValueType
        self.file_hash = file_hash  # Vector<bytes>
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorTranslationFiles":
        # No flags

        type = TLObject.read(b)

        file_hash = TLObject.read(b, Bytes)

        text = String.read(b)

        return SecureValueErrorTranslationFiles(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.type.write())

        b.write(Vector(self.file_hash, Bytes))

        b.write(String(self.text))

        return b.getvalue()
