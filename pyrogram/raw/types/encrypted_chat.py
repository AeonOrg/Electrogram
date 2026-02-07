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


class EncryptedChat(TLObject):  # type: ignore
    """Encrypted chat

    Constructor of :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``224``
        - ID: ``61F0D4C7``

    Parameters:
        id (``int`` ``32-bit``):
            Chat ID

        access_hash (``int`` ``64-bit``):
            Check sum dependent on the user ID

        date (``int`` ``32-bit``):
            Date chat was created

        admin_id (``int`` ``64-bit``):
            Chat creator ID

        participant_id (``int`` ``64-bit``):
            ID of the second chat participant

        g_a_or_b (``bytes``):
            B = g ^ b mod p, if the currently authorized user is the chat's creator,or A = g ^ a mod p otherwiseSee Wikipedia for more info

        key_fingerprint (``int`` ``64-bit``):
            64-bit fingerprint of received key

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint"]

    ID = 0x61f0d4c7
    QUALNAME = "types.EncryptedChat"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int) -> None:
        self.id = id  # int
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # long
        self.participant_id = participant_id  # long
        self.g_a_or_b = g_a_or_b  # bytes
        self.key_fingerprint = key_fingerprint  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedChat":
        # No flags

        id = Int.read(b)

        access_hash = Long.read(b)

        date = Int.read(b)

        admin_id = Long.read(b)

        participant_id = Long.read(b)

        g_a_or_b = Bytes.read(b)

        key_fingerprint = Long.read(b)

        return EncryptedChat(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.id))

        b.write(Long(self.access_hash))

        b.write(Int(self.date))

        b.write(Long(self.admin_id))

        b.write(Long(self.participant_id))

        b.write(Bytes(self.g_a_or_b))

        b.write(Long(self.key_fingerprint))

        return b.getvalue()
