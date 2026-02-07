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


class PageBlockDetails(TLObject):  # type: ignore
    """A collapsible details block

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``76768BED``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            Block contents

        title (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Always visible heading for the block

        open (``bool``, *optional*):
            Whether the block is open by default

    """

    __slots__: List[str] = ["blocks", "title", "open"]

    ID = 0x76768bed
    QUALNAME = "types.PageBlockDetails"

    def __init__(self, *, blocks: List["raw.base.PageBlock"], title: "raw.base.RichText", open: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.title = title  # RichText
        self.open = open  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockDetails":

        flags = Int.read(b)

        open = True if flags & (1 << 0) else False
        blocks = TLObject.read(b)

        title = TLObject.read(b)

        return PageBlockDetails(blocks=blocks, title=title, open=open)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open else 0
        b.write(Int(flags))

        b.write(Vector(self.blocks))

        b.write(self.title.write())

        return b.getvalue()
