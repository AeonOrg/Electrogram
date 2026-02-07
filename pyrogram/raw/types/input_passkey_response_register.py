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


class InputPasskeyResponseRegister(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPasskeyResponse`.

    Details:
        - Layer: ``224``
        - ID: ``3E63935C``

    Parameters:
        client_data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        attestation_data (``bytes``):
            N/A

    """

    __slots__: List[str] = ["client_data", "attestation_data"]

    ID = 0x3e63935c
    QUALNAME = "types.InputPasskeyResponseRegister"

    def __init__(self, *, client_data: "raw.base.DataJSON", attestation_data: bytes) -> None:
        self.client_data = client_data  # DataJSON
        self.attestation_data = attestation_data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPasskeyResponseRegister":
        # No flags

        client_data = TLObject.read(b)

        attestation_data = Bytes.read(b)

        return InputPasskeyResponseRegister(client_data=client_data, attestation_data=attestation_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.client_data.write())

        b.write(Bytes(self.attestation_data))

        return b.getvalue()
