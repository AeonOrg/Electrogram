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


class DialogFilters(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.messages.DialogFilters`.

    Details:
        - Layer: ``224``
        - ID: ``2AD93719``

    Parameters:
        filters (List of :obj:`DialogFilter <pyrogram.raw.base.DialogFilter>`):


        tags_enabled (``bool``, *optional*):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogFilters
    """

    __slots__: List[str] = ["filters", "tags_enabled"]

    ID = 0x2ad93719
    QUALNAME = "types.messages.DialogFilters"

    def __init__(self, *, filters: List["raw.base.DialogFilter"], tags_enabled: Optional[bool] = None) -> None:
        self.filters = filters  # Vector<DialogFilter>
        self.tags_enabled = tags_enabled  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilters":

        flags = Int.read(b)

        tags_enabled = True if flags & (1 << 0) else False
        filters = TLObject.read(b)

        return DialogFilters(filters=filters, tags_enabled=tags_enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.tags_enabled else 0
        b.write(Int(flags))

        b.write(Vector(self.filters))

        return b.getvalue()
