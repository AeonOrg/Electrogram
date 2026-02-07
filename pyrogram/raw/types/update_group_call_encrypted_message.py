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


class UpdateGroupCallEncryptedMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``C957A766``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        encrypted_message (``bytes``):
            N/A

    """

    __slots__: List[str] = ["call", "from_id", "encrypted_message"]

    ID = 0xc957a766
    QUALNAME = "types.UpdateGroupCallEncryptedMessage"

    def __init__(self, *, call: "raw.base.InputGroupCall", from_id: "raw.base.Peer", encrypted_message: bytes) -> None:
        self.call = call  # InputGroupCall
        self.from_id = from_id  # Peer
        self.encrypted_message = encrypted_message  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallEncryptedMessage":
        # No flags

        call = TLObject.read(b)

        from_id = TLObject.read(b)

        encrypted_message = Bytes.read(b)

        return UpdateGroupCallEncryptedMessage(call=call, from_id=from_id, encrypted_message=encrypted_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(self.from_id.write())

        b.write(Bytes(self.encrypted_message))

        return b.getvalue()
