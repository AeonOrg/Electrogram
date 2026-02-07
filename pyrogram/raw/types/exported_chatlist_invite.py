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


class ExportedChatlistInvite(TLObject):  # type: ignore
    """Exported chat folder deep link ».

    Constructor of :obj:`~pyrogram.raw.base.ExportedChatlistInvite`.

    Details:
        - Layer: ``224``
        - ID: ``C5181AC``

    Parameters:
        title (``str``):
            Name of the link

        url (``str``):
            The chat folder deep link ».

        peers (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            Peers to import

        revoked (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.EditExportedInvite
    """

    __slots__: List[str] = ["title", "url", "peers", "revoked"]

    ID = 0xc5181ac
    QUALNAME = "types.ExportedChatlistInvite"

    def __init__(self, *, title: str, url: str, peers: List["raw.base.Peer"], revoked: Optional[bool] = None) -> None:
        self.title = title  # string
        self.url = url  # string
        self.peers = peers  # Vector<Peer>
        self.revoked = revoked  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatlistInvite":

        flags = Int.read(b)

        revoked = True if flags & (1 << 0) else False
        title = String.read(b)

        url = String.read(b)

        peers = TLObject.read(b)

        return ExportedChatlistInvite(title=title, url=url, peers=peers, revoked=revoked)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoked else 0
        b.write(Int(flags))

        b.write(String(self.title))

        b.write(String(self.url))

        b.write(Vector(self.peers))

        return b.getvalue()
