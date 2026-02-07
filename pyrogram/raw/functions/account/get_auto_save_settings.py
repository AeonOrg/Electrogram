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


class GetAutoSaveSettings(TLObject):  # type: ignore
    """Get autosave settings


    Details:
        - Layer: ``224``
        - ID: ``ADCBBCDA``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.AutoSaveSettings <pyrogram.raw.base.account.AutoSaveSettings>`
    """

    __slots__: List[str] = []

    ID = 0xadcbbcda
    QUALNAME = "functions.account.GetAutoSaveSettings"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAutoSaveSettings":
        # No flags

        return GetAutoSaveSettings()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
