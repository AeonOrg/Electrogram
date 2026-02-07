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


class SendEncrypted(TLObject):  # type: ignore
    """Sends a text message to a secret chat.


    Details:
        - Layer: ``224``
        - ID: ``44FA7A15``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            Secret chat ID

        random_id (``int`` ``64-bit``):
            Unique client message ID, necessary to avoid message resending

        data (``bytes``):
            TL-serialization of DecryptedMessage type, encrypted with a key that was created during chat initialization

        silent (``bool``, *optional*):
            Send encrypted message without a notification

    Returns:
        :obj:`messages.SentEncryptedMessage <pyrogram.raw.base.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data", "silent"]

    ID = 0x44fa7a15
    QUALNAME = "functions.messages.SendEncrypted"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", random_id: int, data: bytes, silent: Optional[bool] = None) -> None:
        self.peer = peer  # InputEncryptedChat
        self.random_id = random_id  # long
        self.data = data  # bytes
        self.silent = silent  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendEncrypted":

        flags = Int.read(b)

        silent = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        random_id = Long.read(b)

        data = Bytes.read(b)

        return SendEncrypted(peer=peer, random_id=random_id, data=data, silent=silent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.silent else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Long(self.random_id))

        b.write(Bytes(self.data))

        return b.getvalue()
