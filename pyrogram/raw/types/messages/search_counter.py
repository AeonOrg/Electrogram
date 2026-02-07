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


class SearchCounter(TLObject):  # type: ignore
    """Indicates how many results would be found by a messages.search call with the same parameters

    Constructor of :obj:`~pyrogram.raw.base.messages.SearchCounter`.

    Details:
        - Layer: ``224``
        - ID: ``E844EBFF``

    Parameters:
        filter (:obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`):
            Provided message filter

        count (``int`` ``32-bit``):
            Number of results that were found server-side

        inexact (``bool``, *optional*):
            If set, the results may be inexact

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchCounters
    """

    __slots__: List[str] = ["filter", "count", "inexact"]

    ID = 0xe844ebff
    QUALNAME = "types.messages.SearchCounter"

    def __init__(self, *, filter: "raw.base.MessagesFilter", count: int, inexact: Optional[bool] = None) -> None:
        self.filter = filter  # MessagesFilter
        self.count = count  # int
        self.inexact = inexact  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchCounter":

        flags = Int.read(b)

        inexact = True if flags & (1 << 1) else False
        filter = TLObject.read(b)

        count = Int.read(b)

        return SearchCounter(filter=filter, count=count, inexact=inexact)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact else 0
        b.write(Int(flags))

        b.write(self.filter.write())

        b.write(Int(self.count))

        return b.getvalue()
