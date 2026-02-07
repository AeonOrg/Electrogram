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


class Status(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.smsjobs.Status`.

    Details:
        - Layer: ``224``
        - ID: ``2AEE9191``

    Parameters:
        recent_sent (``int`` ``32-bit``):


        recent_since (``int`` ``32-bit``):


        recent_remains (``int`` ``32-bit``):


        total_sent (``int`` ``32-bit``):


        total_since (``int`` ``32-bit``):


        terms_url (``str``):


        allow_international (``bool``, *optional*):


        last_gift_slug (``str``, *optional*):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            smsjobs.GetStatus
    """

    __slots__: List[str] = ["recent_sent", "recent_since", "recent_remains", "total_sent", "total_since", "terms_url", "allow_international", "last_gift_slug"]

    ID = 0x2aee9191
    QUALNAME = "types.smsjobs.Status"

    def __init__(self, *, recent_sent: int, recent_since: int, recent_remains: int, total_sent: int, total_since: int, terms_url: str, allow_international: Optional[bool] = None, last_gift_slug: Optional[str] = None) -> None:
        self.recent_sent = recent_sent  # int
        self.recent_since = recent_since  # int
        self.recent_remains = recent_remains  # int
        self.total_sent = total_sent  # int
        self.total_since = total_since  # int
        self.terms_url = terms_url  # string
        self.allow_international = allow_international  # flags.0?true
        self.last_gift_slug = last_gift_slug  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Status":

        flags = Int.read(b)

        allow_international = True if flags & (1 << 0) else False
        recent_sent = Int.read(b)

        recent_since = Int.read(b)

        recent_remains = Int.read(b)

        total_sent = Int.read(b)

        total_since = Int.read(b)

        last_gift_slug = String.read(b) if flags & (1 << 1) else None
        terms_url = String.read(b)

        return Status(recent_sent=recent_sent, recent_since=recent_since, recent_remains=recent_remains, total_sent=total_sent, total_since=total_since, terms_url=terms_url, allow_international=allow_international, last_gift_slug=last_gift_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_international else 0
        flags |= (1 << 1) if self.last_gift_slug is not None else 0
        b.write(Int(flags))

        b.write(Int(self.recent_sent))

        b.write(Int(self.recent_since))

        b.write(Int(self.recent_remains))

        b.write(Int(self.total_sent))

        b.write(Int(self.total_since))

        if self.last_gift_slug is not None:
            b.write(String(self.last_gift_slug))

        b.write(String(self.terms_url))

        return b.getvalue()
