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


class DcOption(TLObject):  # type: ignore
    """Data center

    Constructor of :obj:`~pyrogram.raw.base.DcOption`.

    Details:
        - Layer: ``224``
        - ID: ``18B7A10D``

    Parameters:
        id (``int`` ``32-bit``):
            DC ID

        ip_address (``str``):
            IP address of DC

        port (``int`` ``32-bit``):
            Port

        ipv6 (``bool``, *optional*):
            Whether the specified IP is an IPv6 address

        media_only (``bool``, *optional*):
            Whether this DC should only be used to download or upload files

        tcpo_only (``bool``, *optional*):
            Whether this DC only supports connection with transport obfuscation

        cdn (``bool``, *optional*):
            Whether this is a CDN DC.

        static (``bool``, *optional*):
            If set, this IP should be used when connecting through a proxy

        this_port_only (``bool``, *optional*):
            If set, clients must connect using only the specified port, without trying any other port.

        secret (``bytes``, *optional*):
            If the tcpo_only flag is set, specifies the secret to use when connecting using transport obfuscation

    """

    __slots__: List[str] = ["id", "ip_address", "port", "ipv6", "media_only", "tcpo_only", "cdn", "static", "this_port_only", "secret"]

    ID = 0x18b7a10d
    QUALNAME = "types.DcOption"

    def __init__(self, *, id: int, ip_address: str, port: int, ipv6: Optional[bool] = None, media_only: Optional[bool] = None, tcpo_only: Optional[bool] = None, cdn: Optional[bool] = None, static: Optional[bool] = None, this_port_only: Optional[bool] = None, secret: Optional[bytes] = None) -> None:
        self.id = id  # int
        self.ip_address = ip_address  # string
        self.port = port  # int
        self.ipv6 = ipv6  # flags.0?true
        self.media_only = media_only  # flags.1?true
        self.tcpo_only = tcpo_only  # flags.2?true
        self.cdn = cdn  # flags.3?true
        self.static = static  # flags.4?true
        self.this_port_only = this_port_only  # flags.5?true
        self.secret = secret  # flags.10?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DcOption":

        flags = Int.read(b)

        ipv6 = True if flags & (1 << 0) else False
        media_only = True if flags & (1 << 1) else False
        tcpo_only = True if flags & (1 << 2) else False
        cdn = True if flags & (1 << 3) else False
        static = True if flags & (1 << 4) else False
        this_port_only = True if flags & (1 << 5) else False
        id = Int.read(b)

        ip_address = String.read(b)

        port = Int.read(b)

        secret = Bytes.read(b) if flags & (1 << 10) else None
        return DcOption(id=id, ip_address=ip_address, port=port, ipv6=ipv6, media_only=media_only, tcpo_only=tcpo_only, cdn=cdn, static=static, this_port_only=this_port_only, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ipv6 else 0
        flags |= (1 << 1) if self.media_only else 0
        flags |= (1 << 2) if self.tcpo_only else 0
        flags |= (1 << 3) if self.cdn else 0
        flags |= (1 << 4) if self.static else 0
        flags |= (1 << 5) if self.this_port_only else 0
        flags |= (1 << 10) if self.secret is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(String(self.ip_address))

        b.write(Int(self.port))

        if self.secret is not None:
            b.write(Bytes(self.secret))

        return b.getvalue()
