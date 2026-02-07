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


class AcceptEncryption(TLObject):  # type: ignore
    """Confirms creation of a secret chat


    Details:
        - Layer: ``224``
        - ID: ``3DBC0415``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            Secret chat ID

        g_b (``bytes``):
            B = g ^ b mod p, see Wikipedia

        key_fingerprint (``int`` ``64-bit``):
            64-bit fingerprint of the received key

    Returns:
        :obj:`EncryptedChat <pyrogram.raw.base.EncryptedChat>`
    """

    __slots__: List[str] = ["peer", "g_b", "key_fingerprint"]

    ID = 0x3dbc0415
    QUALNAME = "functions.messages.AcceptEncryption"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", g_b: bytes, key_fingerprint: int) -> None:
        self.peer = peer  # InputEncryptedChat
        self.g_b = g_b  # bytes
        self.key_fingerprint = key_fingerprint  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptEncryption":
        # No flags

        peer = TLObject.read(b)

        g_b = Bytes.read(b)

        key_fingerprint = Long.read(b)

        return AcceptEncryption(peer=peer, g_b=g_b, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Bytes(self.g_b))

        b.write(Long(self.key_fingerprint))

        return b.getvalue()
