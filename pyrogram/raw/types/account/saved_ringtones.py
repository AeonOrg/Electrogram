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


class SavedRingtones(TLObject):  # type: ignore
    """A list of saved notification sounds

    Constructor of :obj:`~pyrogram.raw.base.account.SavedRingtones`.

    Details:
        - Layer: ``224``
        - ID: ``C1E92CC5``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        ringtones (List of :obj:`Document <pyrogram.raw.base.Document>`):
            Saved notification sounds

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetSavedRingtones
    """

    __slots__: List[str] = ["hash", "ringtones"]

    ID = 0xc1e92cc5
    QUALNAME = "types.account.SavedRingtones"

    def __init__(self, *, hash: int, ringtones: List["raw.base.Document"]) -> None:
        self.hash = hash  # long
        self.ringtones = ringtones  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedRingtones":
        # No flags

        hash = Long.read(b)

        ringtones = TLObject.read(b)

        return SavedRingtones(hash=hash, ringtones=ringtones)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        b.write(Vector(self.ringtones))

        return b.getvalue()
