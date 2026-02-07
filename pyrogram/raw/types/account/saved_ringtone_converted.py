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


class SavedRingtoneConverted(TLObject):  # type: ignore
    """The notification sound was not in MP3 format and was successfully converted and saved, use the returned Document to refer to the notification sound from now on

    Constructor of :obj:`~pyrogram.raw.base.account.SavedRingtone`.

    Details:
        - Layer: ``224``
        - ID: ``1F307EB7``

    Parameters:
        document (:obj:`Document <pyrogram.raw.base.Document>`):
            The converted notification sound

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.SaveRingtone
    """

    __slots__: List[str] = ["document"]

    ID = 0x1f307eb7
    QUALNAME = "types.account.SavedRingtoneConverted"

    def __init__(self, *, document: "raw.base.Document") -> None:
        self.document = document  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedRingtoneConverted":
        # No flags

        document = TLObject.read(b)

        return SavedRingtoneConverted(document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.document.write())

        return b.getvalue()
