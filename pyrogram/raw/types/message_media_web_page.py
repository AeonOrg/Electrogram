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


class MessageMediaWebPage(TLObject):  # type: ignore
    """Preview of webpage

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``DDF10C3B``

    Parameters:
        webpage (:obj:`WebPage <pyrogram.raw.base.WebPage>`):
            Webpage preview

        force_large_media (``bool``, *optional*):
            If set, specifies that a large media preview should be used.

        force_small_media (``bool``, *optional*):
            If set, specifies that a small media preview should be used.

        manual (``bool``, *optional*):
            If set, indicates that the URL used for the webpage preview was specified manually using inputMediaWebPage, and may not be related to any of the URLs specified in the message.

        safe (``bool``, *optional*):
            If set, the webpage can be opened directly without user confirmation; otherwise, user confirmation is required, showing the exact URL that will be opened.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["webpage", "force_large_media", "force_small_media", "manual", "safe"]

    ID = 0xddf10c3b
    QUALNAME = "types.MessageMediaWebPage"

    def __init__(self, *, webpage: "raw.base.WebPage", force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, manual: Optional[bool] = None, safe: Optional[bool] = None) -> None:
        self.webpage = webpage  # WebPage
        self.force_large_media = force_large_media  # flags.0?true
        self.force_small_media = force_small_media  # flags.1?true
        self.manual = manual  # flags.3?true
        self.safe = safe  # flags.4?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaWebPage":

        flags = Int.read(b)

        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        manual = True if flags & (1 << 3) else False
        safe = True if flags & (1 << 4) else False
        webpage = TLObject.read(b)

        return MessageMediaWebPage(webpage=webpage, force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force_large_media else 0
        flags |= (1 << 1) if self.force_small_media else 0
        flags |= (1 << 3) if self.manual else 0
        flags |= (1 << 4) if self.safe else 0
        b.write(Int(flags))

        b.write(self.webpage.write())

        return b.getvalue()
