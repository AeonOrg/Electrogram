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


class UpdatePrivacy(TLObject):  # type: ignore
    """Privacy rules were changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``EE3B272A``

    Parameters:
        key (:obj:`PrivacyKey <pyrogram.raw.base.PrivacyKey>`):
            Peers to which the privacy rules apply

        rules (List of :obj:`PrivacyRule <pyrogram.raw.base.PrivacyRule>`):
            New privacy rules

    """

    __slots__: List[str] = ["key", "rules"]

    ID = 0xee3b272a
    QUALNAME = "types.UpdatePrivacy"

    def __init__(self, *, key: "raw.base.PrivacyKey", rules: List["raw.base.PrivacyRule"]) -> None:
        self.key = key  # PrivacyKey
        self.rules = rules  # Vector<PrivacyRule>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePrivacy":
        # No flags

        key = TLObject.read(b)

        rules = TLObject.read(b)

        return UpdatePrivacy(key=key, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.key.write())

        b.write(Vector(self.rules))

        return b.getvalue()
