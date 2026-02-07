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


class RestrictionReason(TLObject):  # type: ignore
    """Restriction reason.

    Constructor of :obj:`~pyrogram.raw.base.RestrictionReason`.

    Details:
        - Layer: ``224``
        - ID: ``D072ACB4``

    Parameters:
        platform (``str``):
            Platform identifier (ios, android, wp, all, etc.), can be concatenated with a dash as separator (android-ios, ios-wp, etc)

        reason (``str``):
            Restriction reason (porno, terms, etc.)

        text (``str``):
            Error message to be shown to the user

    """

    __slots__: List[str] = ["platform", "reason", "text"]

    ID = 0xd072acb4
    QUALNAME = "types.RestrictionReason"

    def __init__(self, *, platform: str, reason: str, text: str) -> None:
        self.platform = platform  # string
        self.reason = reason  # string
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RestrictionReason":
        # No flags

        platform = String.read(b)

        reason = String.read(b)

        text = String.read(b)

        return RestrictionReason(platform=platform, reason=reason, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.platform))

        b.write(String(self.reason))

        b.write(String(self.text))

        return b.getvalue()
