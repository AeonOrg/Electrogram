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


class PhoneConnection(TLObject):  # type: ignore
    """Identifies an endpoint that can be used to connect to the other user in a phone call

    Constructor of :obj:`~pyrogram.raw.base.PhoneConnection`.

    Details:
        - Layer: ``224``
        - ID: ``9CC123C7``

    Parameters:
        id (``int`` ``64-bit``):
            Endpoint ID

        ip (``str``):
            IP address of endpoint

        ipv6 (``str``):
            IPv6 address of endpoint

        port (``int`` ``32-bit``):
            Port ID

        peer_tag (``bytes``):
            Our peer tag

        tcp (``bool``, *optional*):
            Whether TCP should be used

    """

    __slots__: List[str] = ["id", "ip", "ipv6", "port", "peer_tag", "tcp"]

    ID = 0x9cc123c7
    QUALNAME = "types.PhoneConnection"

    def __init__(self, *, id: int, ip: str, ipv6: str, port: int, peer_tag: bytes, tcp: Optional[bool] = None) -> None:
        self.id = id  # long
        self.ip = ip  # string
        self.ipv6 = ipv6  # string
        self.port = port  # int
        self.peer_tag = peer_tag  # bytes
        self.tcp = tcp  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneConnection":

        flags = Int.read(b)

        tcp = True if flags & (1 << 0) else False
        id = Long.read(b)

        ip = String.read(b)

        ipv6 = String.read(b)

        port = Int.read(b)

        peer_tag = Bytes.read(b)

        return PhoneConnection(id=id, ip=ip, ipv6=ipv6, port=port, peer_tag=peer_tag, tcp=tcp)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.tcp else 0
        b.write(Int(flags))

        b.write(Long(self.id))

        b.write(String(self.ip))

        b.write(String(self.ipv6))

        b.write(Int(self.port))

        b.write(Bytes(self.peer_tag))

        return b.getvalue()
