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


class BotVerifierSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotVerifierSettings`.

    Details:
        - Layer: ``224``
        - ID: ``B0CD6617``

    Parameters:
        icon (``int`` ``64-bit``):
            N/A

        company (``str``):
            N/A

        can_modify_custom_description (``bool``, *optional*):
            N/A

        custom_description (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["icon", "company", "can_modify_custom_description", "custom_description"]

    ID = 0xb0cd6617
    QUALNAME = "types.BotVerifierSettings"

    def __init__(self, *, icon: int, company: str, can_modify_custom_description: Optional[bool] = None, custom_description: Optional[str] = None) -> None:
        self.icon = icon  # long
        self.company = company  # string
        self.can_modify_custom_description = can_modify_custom_description  # flags.1?true
        self.custom_description = custom_description  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotVerifierSettings":

        flags = Int.read(b)

        can_modify_custom_description = True if flags & (1 << 1) else False
        icon = Long.read(b)

        company = String.read(b)

        custom_description = String.read(b) if flags & (1 << 0) else None
        return BotVerifierSettings(icon=icon, company=company, can_modify_custom_description=can_modify_custom_description, custom_description=custom_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.can_modify_custom_description else 0
        flags |= (1 << 0) if self.custom_description is not None else 0
        b.write(Int(flags))

        b.write(Long(self.icon))

        b.write(String(self.company))

        if self.custom_description is not None:
            b.write(String(self.custom_description))

        return b.getvalue()
