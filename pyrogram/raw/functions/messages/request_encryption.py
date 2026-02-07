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


class RequestEncryption(TLObject):  # type: ignore
    """Sends a request to start a secret chat to the user.


    Details:
        - Layer: ``224``
        - ID: ``F64DAF43``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User ID

        random_id (``int`` ``32-bit``):
            Unique client request ID required to prevent resending. This also doubles as the chat ID.

        g_a (``bytes``):
            A = g ^ a mod p, see Wikipedia

    Returns:
        :obj:`EncryptedChat <pyrogram.raw.base.EncryptedChat>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a"]

    ID = 0xf64daf43
    QUALNAME = "functions.messages.RequestEncryption"

    def __init__(self, *, user_id: "raw.base.InputUser", random_id: int, g_a: bytes) -> None:
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestEncryption":
        # No flags

        user_id = TLObject.read(b)

        random_id = Int.read(b)

        g_a = Bytes.read(b)

        return RequestEncryption(user_id=user_id, random_id=random_id, g_a=g_a)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.user_id.write())

        b.write(Int(self.random_id))

        b.write(Bytes(self.g_a))

        return b.getvalue()
