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


class TimezonesListNotModified(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.help.TimezonesList`.

    Details:
        - Layer: ``224``
        - ID: ``970708CC``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    __slots__: List[str] = []

    ID = 0x970708cc
    QUALNAME = "types.help.TimezonesListNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TimezonesListNotModified":
        # No flags

        return TimezonesListNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
