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


class GetContentSettings(TLObject):  # type: ignore
    """Get sensitive content settings


    Details:
        - Layer: ``224``
        - ID: ``8B9B4DAE``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.ContentSettings <pyrogram.raw.base.account.ContentSettings>`
    """

    __slots__: List[str] = []

    ID = 0x8b9b4dae
    QUALNAME = "functions.account.GetContentSettings"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetContentSettings":
        # No flags

        return GetContentSettings()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
