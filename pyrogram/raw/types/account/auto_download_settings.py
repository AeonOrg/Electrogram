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


class AutoDownloadSettings(TLObject):  # type: ignore
    """Media autodownload settings

    Constructor of :obj:`~pyrogram.raw.base.account.AutoDownloadSettings`.

    Details:
        - Layer: ``224``
        - ID: ``63CACF26``

    Parameters:
        low (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            Low data usage preset

        medium (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            Medium data usage preset

        high (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            High data usage preset

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAutoDownloadSettings
    """

    __slots__: List[str] = ["low", "medium", "high"]

    ID = 0x63cacf26
    QUALNAME = "types.account.AutoDownloadSettings"

    def __init__(self, *, low: "raw.base.AutoDownloadSettings", medium: "raw.base.AutoDownloadSettings", high: "raw.base.AutoDownloadSettings") -> None:
        self.low = low  # AutoDownloadSettings
        self.medium = medium  # AutoDownloadSettings
        self.high = high  # AutoDownloadSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoDownloadSettings":
        # No flags

        low = TLObject.read(b)

        medium = TLObject.read(b)

        high = TLObject.read(b)

        return AutoDownloadSettings(low=low, medium=medium, high=high)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.low.write())

        b.write(self.medium.write())

        b.write(self.high.write())

        return b.getvalue()
