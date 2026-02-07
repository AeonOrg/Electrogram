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


class ReactionCount(TLObject):  # type: ignore
    """Reactions

    Constructor of :obj:`~pyrogram.raw.base.ReactionCount`.

    Details:
        - Layer: ``224``
        - ID: ``A3D1CB80``

    Parameters:
        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            The reaction.

        count (``int`` ``32-bit``):
            Number of users that reacted with this emoji.

        chosen_order (``int`` ``32-bit``, *optional*):
            If set, indicates that the current user also sent this reaction. The integer value indicates when was the reaction added: the bigger the value, the newer the reaction.

    """

    __slots__: List[str] = ["reaction", "count", "chosen_order"]

    ID = 0xa3d1cb80
    QUALNAME = "types.ReactionCount"

    def __init__(self, *, reaction: "raw.base.Reaction", count: int, chosen_order: Optional[int] = None) -> None:
        self.reaction = reaction  # Reaction
        self.count = count  # int
        self.chosen_order = chosen_order  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionCount":

        flags = Int.read(b)

        chosen_order = Int.read(b) if flags & (1 << 0) else None
        reaction = TLObject.read(b)

        count = Int.read(b)

        return ReactionCount(reaction=reaction, count=count, chosen_order=chosen_order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chosen_order is not None else 0
        b.write(Int(flags))

        if self.chosen_order is not None:
            b.write(Int(self.chosen_order))

        b.write(self.reaction.write())

        b.write(Int(self.count))

        return b.getvalue()
