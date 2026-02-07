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


class StickerSetInstallResultSuccess(TLObject):  # type: ignore
    """The stickerset was installed successfully

    Constructor of :obj:`~pyrogram.raw.base.messages.StickerSetInstallResult`.

    Details:
        - Layer: ``224``
        - ID: ``38641628``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InstallStickerSet
    """

    __slots__: List[str] = []

    ID = 0x38641628
    QUALNAME = "types.messages.StickerSetInstallResultSuccess"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetInstallResultSuccess":
        # No flags

        return StickerSetInstallResultSuccess()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
