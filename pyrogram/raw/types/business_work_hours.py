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


class BusinessWorkHours(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BusinessWorkHours`.

    Details:
        - Layer: ``224``
        - ID: ``8C92B098``

    Parameters:
        timezone_id (``str``):


        weekly_open (List of :obj:`BusinessWeeklyOpen <pyrogram.raw.base.BusinessWeeklyOpen>`):


        open_now (``bool``, *optional*):


    """

    __slots__: List[str] = ["timezone_id", "weekly_open", "open_now"]

    ID = 0x8c92b098
    QUALNAME = "types.BusinessWorkHours"

    def __init__(self, *, timezone_id: str, weekly_open: List["raw.base.BusinessWeeklyOpen"], open_now: Optional[bool] = None) -> None:
        self.timezone_id = timezone_id  # string
        self.weekly_open = weekly_open  # Vector<BusinessWeeklyOpen>
        self.open_now = open_now  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessWorkHours":

        flags = Int.read(b)

        open_now = True if flags & (1 << 0) else False
        timezone_id = String.read(b)

        weekly_open = TLObject.read(b)

        return BusinessWorkHours(timezone_id=timezone_id, weekly_open=weekly_open, open_now=open_now)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open_now else 0
        b.write(Int(flags))

        b.write(String(self.timezone_id))

        b.write(Vector(self.weekly_open))

        return b.getvalue()
