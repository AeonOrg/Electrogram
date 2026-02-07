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


class MessageActionSecureValuesSentMe(TLObject):  # type: ignore
    """Secure telegram passport values were received

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``1B287353``

    Parameters:
        values (List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`):
            Vector with information about documents and other Telegram Passport elements that were shared with the bot

        credentials (:obj:`SecureCredentialsEncrypted <pyrogram.raw.base.SecureCredentialsEncrypted>`):
            Encrypted credentials required to decrypt the data

    """

    __slots__: List[str] = ["values", "credentials"]

    ID = 0x1b287353
    QUALNAME = "types.MessageActionSecureValuesSentMe"

    def __init__(self, *, values: List["raw.base.SecureValue"], credentials: "raw.base.SecureCredentialsEncrypted") -> None:
        self.values = values  # Vector<SecureValue>
        self.credentials = credentials  # SecureCredentialsEncrypted

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSecureValuesSentMe":
        # No flags

        values = TLObject.read(b)

        credentials = TLObject.read(b)

        return MessageActionSecureValuesSentMe(values=values, credentials=credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.values))

        b.write(self.credentials.write())

        return b.getvalue()
