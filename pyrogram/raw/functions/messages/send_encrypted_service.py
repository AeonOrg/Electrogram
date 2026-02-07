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


class SendEncryptedService(TLObject):  # type: ignore
    """Sends a service message to a secret chat.


    Details:
        - Layer: ``224``
        - ID: ``32D439A4``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            Secret chat ID

        random_id (``int`` ``64-bit``):
            Unique client message ID required to prevent message resending

        data (``bytes``):
            TL-serialization of  DecryptedMessage type, encrypted with a key generated during chat initialization

    Returns:
        :obj:`messages.SentEncryptedMessage <pyrogram.raw.base.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data"]

    ID = 0x32d439a4
    QUALNAME = "functions.messages.SendEncryptedService"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", random_id: int, data: bytes) -> None:
        self.peer = peer  # InputEncryptedChat
        self.random_id = random_id  # long
        self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendEncryptedService":
        # No flags

        peer = TLObject.read(b)

        random_id = Long.read(b)

        data = Bytes.read(b)

        return SendEncryptedService(peer=peer, random_id=random_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Long(self.random_id))

        b.write(Bytes(self.data))

        return b.getvalue()
