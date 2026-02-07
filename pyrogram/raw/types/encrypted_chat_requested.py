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


class EncryptedChatRequested(TLObject):  # type: ignore
    """Request to create an encrypted chat.

    Constructor of :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``224``
        - ID: ``48F1D94C``

    Parameters:
        id (``int`` ``32-bit``):
            Chat ID

        access_hash (``int`` ``64-bit``):
            Check sum depending on user ID

        date (``int`` ``32-bit``):
            Chat creation date

        admin_id (``int`` ``64-bit``):
            Chat creator ID

        participant_id (``int`` ``64-bit``):
            ID of second chat participant

        g_a (``bytes``):
            A = g ^ a mod p, see Wikipedia

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a", "folder_id"]

    ID = 0x48f1d94c
    QUALNAME = "types.EncryptedChatRequested"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a: bytes, folder_id: Optional[int] = None) -> None:
        self.id = id  # int
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # long
        self.participant_id = participant_id  # long
        self.g_a = g_a  # bytes
        self.folder_id = folder_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedChatRequested":

        flags = Int.read(b)

        folder_id = Int.read(b) if flags & (1 << 0) else None
        id = Int.read(b)

        access_hash = Long.read(b)

        date = Int.read(b)

        admin_id = Long.read(b)

        participant_id = Long.read(b)

        g_a = Bytes.read(b)

        return EncryptedChatRequested(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a=g_a, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        b.write(Int(flags))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        b.write(Int(self.id))

        b.write(Long(self.access_hash))

        b.write(Int(self.date))

        b.write(Long(self.admin_id))

        b.write(Long(self.participant_id))

        b.write(Bytes(self.g_a))

        return b.getvalue()
