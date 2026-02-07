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


class InputMediaWebPage(TLObject):  # type: ignore
    """Specifies options that will be used to generate the link preview for the caption, or even a standalone link preview without an attached message.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``C21B8849``

    Parameters:
        url (``str``):
            The URL to use for the link preview.

        force_large_media (``bool``, *optional*):
            If set, specifies that a large media preview should be used.

        force_small_media (``bool``, *optional*):
            If set, specifies that a small media preview should be used.

        optional (``bool``, *optional*):
            If not set, a WEBPAGE_NOT_FOUND RPC error will be emitted if a webpage preview cannot be generated for the specified url; otherwise, no error will be emitted (unless the provided message is also empty, in which case a MESSAGE_EMPTY will be emitted, instead).

    """

    __slots__: List[str] = ["url", "force_large_media", "force_small_media", "optional"]

    ID = 0xc21b8849
    QUALNAME = "types.InputMediaWebPage"

    def __init__(self, *, url: str, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None) -> None:
        self.url = url  # string
        self.force_large_media = force_large_media  # flags.0?true
        self.force_small_media = force_small_media  # flags.1?true
        self.optional = optional  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaWebPage":

        flags = Int.read(b)

        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        optional = True if flags & (1 << 2) else False
        url = String.read(b)

        return InputMediaWebPage(url=url, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force_large_media else 0
        flags |= (1 << 1) if self.force_small_media else 0
        flags |= (1 << 2) if self.optional else 0
        b.write(Int(flags))

        b.write(String(self.url))

        return b.getvalue()
