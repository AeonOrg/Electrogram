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


class UpdatePinnedMessage(TLObject):  # type: ignore
    """Pin a message


    Details:
        - Layer: ``224``
        - ID: ``D2AAF7EC``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer where to pin the message

        id (``int`` ``32-bit``):
            The message to pin or unpin

        silent (``bool``, *optional*):
            Pin the message silently, without triggering a notification

        unpin (``bool``, *optional*):
            Whether the message should unpinned or pinned

        pm_oneside (``bool``, *optional*):
            Whether the message should only be pinned on the local side of a one-to-one chat

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "silent", "unpin", "pm_oneside"]

    ID = 0xd2aaf7ec
    QUALNAME = "functions.messages.UpdatePinnedMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, silent: Optional[bool] = None, unpin: Optional[bool] = None, pm_oneside: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.silent = silent  # flags.0?true
        self.unpin = unpin  # flags.1?true
        self.pm_oneside = pm_oneside  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedMessage":

        flags = Int.read(b)

        silent = True if flags & (1 << 0) else False
        unpin = True if flags & (1 << 1) else False
        pm_oneside = True if flags & (1 << 2) else False
        peer = TLObject.read(b)

        id = Int.read(b)

        return UpdatePinnedMessage(peer=peer, id=id, silent=silent, unpin=unpin, pm_oneside=pm_oneside)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.silent else 0
        flags |= (1 << 1) if self.unpin else 0
        flags |= (1 << 2) if self.pm_oneside else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.id))

        return b.getvalue()
