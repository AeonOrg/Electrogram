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


class ConfigSimple(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.ConfigSimple`.

    Details:
        - Layer: ``224``
        - ID: ``5A592A6C``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        expires (``int`` ``32-bit``):
            N/A

        rules (List of :obj:`AccessPointRule <pyrogram.raw.base.AccessPointRule>`):
            N/A

    """

    __slots__: List[str] = ["date", "expires", "rules"]

    ID = 0x5a592a6c
    QUALNAME = "types.help.ConfigSimple"

    def __init__(self, *, date: int, expires: int, rules: List["raw.base.AccessPointRule"]) -> None:
        self.date = date  # int
        self.expires = expires  # int
        self.rules = rules  # vector<AccessPointRule>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfigSimple":
        # No flags

        date = Int.read(b)

        expires = Int.read(b)

        rules = TLObject.read(b)

        return ConfigSimple(date=date, expires=expires, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.date))

        b.write(Int(self.expires))

        b.write(Vector(self.rules))

        return b.getvalue()
