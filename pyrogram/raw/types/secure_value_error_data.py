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


class SecureValueErrorData(TLObject):  # type: ignore
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``224``
        - ID: ``E8A40BD9``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            The section of the user's Telegram Passport which has the error, one of secureValueTypePersonalDetails, secureValueTypePassport, secureValueTypeDriverLicense, secureValueTypeIdentityCard, secureValueTypeInternalPassport, secureValueTypeAddress

        data_hash (``bytes``):
            Data hash

        field (``str``):
            Name of the data field which has the error

        text (``str``):
            Error message

    """

    __slots__: List[str] = ["type", "data_hash", "field", "text"]

    ID = 0xe8a40bd9
    QUALNAME = "types.SecureValueErrorData"

    def __init__(self, *, type: "raw.base.SecureValueType", data_hash: bytes, field: str, text: str) -> None:
        self.type = type  # SecureValueType
        self.data_hash = data_hash  # bytes
        self.field = field  # string
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorData":
        # No flags

        type = TLObject.read(b)

        data_hash = Bytes.read(b)

        field = String.read(b)

        text = String.read(b)

        return SecureValueErrorData(type=type, data_hash=data_hash, field=field, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.type.write())

        b.write(Bytes(self.data_hash))

        b.write(String(self.field))

        b.write(String(self.text))

        return b.getvalue()
