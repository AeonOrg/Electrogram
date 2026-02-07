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


class ConfirmCall(TLObject):  # type: ignore
    """Complete phone call E2E encryption key exchange »


    Details:
        - Layer: ``224``
        - ID: ``2EFE1722``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            The phone call

        g_a (``bytes``):
            Parameter for E2E encryption key exchange »

        key_fingerprint (``int`` ``64-bit``):
            Key fingerprint

        protocol (:obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`):
            Phone call settings

    Returns:
        :obj:`phone.PhoneCall <pyrogram.raw.base.phone.PhoneCall>`
    """

    __slots__: List[str] = ["peer", "g_a", "key_fingerprint", "protocol"]

    ID = 0x2efe1722
    QUALNAME = "functions.phone.ConfirmCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", g_a: bytes, key_fingerprint: int, protocol: "raw.base.PhoneCallProtocol") -> None:
        self.peer = peer  # InputPhoneCall
        self.g_a = g_a  # bytes
        self.key_fingerprint = key_fingerprint  # long
        self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmCall":
        # No flags

        peer = TLObject.read(b)

        g_a = Bytes.read(b)

        key_fingerprint = Long.read(b)

        protocol = TLObject.read(b)

        return ConfirmCall(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Bytes(self.g_a))

        b.write(Long(self.key_fingerprint))

        b.write(self.protocol.write())

        return b.getvalue()
