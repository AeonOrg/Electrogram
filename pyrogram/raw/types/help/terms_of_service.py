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


class TermsOfService(TLObject):  # type: ignore
    """Info about the latest telegram Terms Of Service

    Constructor of :obj:`~pyrogram.raw.base.help.TermsOfService`.

    Details:
        - Layer: ``224``
        - ID: ``780A0310``

    Parameters:
        id (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            ID of the new terms

        text (``str``):
            Text of the new terms

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            Message entities for styled text

        popup (``bool``, *optional*):
            Whether a prompt must be showed to the user, in order to accept the new terms.

        min_age_confirm (``int`` ``32-bit``, *optional*):
            Minimum age required to sign up to telegram, the user must confirm that they is older than the minimum age.

    """

    __slots__: List[str] = ["id", "text", "entities", "popup", "min_age_confirm"]

    ID = 0x780a0310
    QUALNAME = "types.help.TermsOfService"

    def __init__(self, *, id: "raw.base.DataJSON", text: str, entities: List["raw.base.MessageEntity"], popup: Optional[bool] = None, min_age_confirm: Optional[int] = None) -> None:
        self.id = id  # DataJSON
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>
        self.popup = popup  # flags.0?true
        self.min_age_confirm = min_age_confirm  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfService":

        flags = Int.read(b)

        popup = True if flags & (1 << 0) else False
        id = TLObject.read(b)

        text = String.read(b)

        entities = TLObject.read(b)

        min_age_confirm = Int.read(b) if flags & (1 << 1) else None
        return TermsOfService(id=id, text=text, entities=entities, popup=popup, min_age_confirm=min_age_confirm)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup else 0
        flags |= (1 << 1) if self.min_age_confirm is not None else 0
        b.write(Int(flags))

        b.write(self.id.write())

        b.write(String(self.text))

        b.write(Vector(self.entities))

        if self.min_age_confirm is not None:
            b.write(Int(self.min_age_confirm))

        return b.getvalue()
