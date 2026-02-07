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


class TimezonesList(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.help.TimezonesList`.

    Details:
        - Layer: ``224``
        - ID: ``7B74ED71``

    Parameters:
        timezones (List of :obj:`Timezone <pyrogram.raw.base.Timezone>`):


        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    __slots__: List[str] = ["timezones", "hash"]

    ID = 0x7b74ed71
    QUALNAME = "types.help.TimezonesList"

    def __init__(self, *, timezones: List["raw.base.Timezone"], hash: int) -> None:
        self.timezones = timezones  # Vector<Timezone>
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TimezonesList":
        # No flags

        timezones = TLObject.read(b)

        hash = Int.read(b)

        return TimezonesList(timezones=timezones, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.timezones))

        b.write(Int(self.hash))

        return b.getvalue()
