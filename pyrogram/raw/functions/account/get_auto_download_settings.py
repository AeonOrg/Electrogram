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


class GetAutoDownloadSettings(TLObject):  # type: ignore
    """Get media autodownload settings


    Details:
        - Layer: ``224``
        - ID: ``56DA0B3F``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.AutoDownloadSettings <pyrogram.raw.base.account.AutoDownloadSettings>`
    """

    __slots__: List[str] = []

    ID = 0x56da0b3f
    QUALNAME = "functions.account.GetAutoDownloadSettings"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAutoDownloadSettings":
        # No flags

        return GetAutoDownloadSettings()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
