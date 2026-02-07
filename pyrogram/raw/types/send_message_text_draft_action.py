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


class SendMessageTextDraftAction(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``376D975C``

    Parameters:
        random_id (``int`` ``64-bit``):
            N/A

        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    """

    __slots__: List[str] = ["random_id", "text"]

    ID = 0x376d975c
    QUALNAME = "types.SendMessageTextDraftAction"

    def __init__(self, *, random_id: int, text: "raw.base.TextWithEntities") -> None:
        self.random_id = random_id  # long
        self.text = text  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageTextDraftAction":
        # No flags

        random_id = Long.read(b)

        text = TLObject.read(b)

        return SendMessageTextDraftAction(random_id=random_id, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.random_id))

        b.write(self.text.write())

        return b.getvalue()
