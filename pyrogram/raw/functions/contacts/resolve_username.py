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


class ResolveUsername(TLObject):  # type: ignore
    """Resolve a @username to get peer info


    Details:
        - Layer: ``224``
        - ID: ``725AFBBC``

    Parameters:
        username (``str``):
            @username to resolve

        referer (``str``, *optional*):
            N/A

    Returns:
        :obj:`contacts.ResolvedPeer <pyrogram.raw.base.contacts.ResolvedPeer>`
    """

    __slots__: List[str] = ["username", "referer"]

    ID = 0x725afbbc
    QUALNAME = "functions.contacts.ResolveUsername"

    def __init__(self, *, username: str, referer: Optional[str] = None) -> None:
        self.username = username  # string
        self.referer = referer  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveUsername":

        flags = Int.read(b)

        username = String.read(b)

        referer = String.read(b) if flags & (1 << 0) else None
        return ResolveUsername(username=username, referer=referer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.referer is not None else 0
        b.write(Int(flags))

        b.write(String(self.username))

        if self.referer is not None:
            b.write(String(self.referer))

        return b.getvalue()
