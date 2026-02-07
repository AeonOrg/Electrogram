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


class UrlAuthResultAccepted(TLObject):  # type: ignore
    """Details about an accepted authorization request, for more info click here »

    Constructor of :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``224``
        - ID: ``623A8FA0``

    Parameters:
        url (``str``, *optional*):
            The URL name of the website on which the user has logged in.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = ["url"]

    ID = 0x623a8fa0
    QUALNAME = "types.UrlAuthResultAccepted"

    def __init__(self, *, url: Optional[str] = None) -> None:
        self.url = url  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultAccepted":

        flags = Int.read(b)

        url = String.read(b) if flags & (1 << 0) else None
        return UrlAuthResultAccepted(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.url is not None else 0
        b.write(Int(flags))

        if self.url is not None:
            b.write(String(self.url))

        return b.getvalue()
