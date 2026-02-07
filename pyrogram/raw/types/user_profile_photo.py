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


class UserProfilePhoto(TLObject):  # type: ignore
    """User profile photo.

    Constructor of :obj:`~pyrogram.raw.base.UserProfilePhoto`.

    Details:
        - Layer: ``224``
        - ID: ``82D1F706``

    Parameters:
        photo_id (``int`` ``64-bit``):
            Identifier of the respective photo

        dc_id (``int`` ``32-bit``):
            DC ID where the photo is stored

        has_video (``bool``, *optional*):
            Whether an animated profile picture is available for this user

        personal (``bool``, *optional*):
            Whether this profile photo is only visible to us (i.e. it was set using photos.uploadContactProfilePhoto).

        stripped_thumb (``bytes``, *optional*):
            Stripped thumbnail

    """

    __slots__: List[str] = ["photo_id", "dc_id", "has_video", "personal", "stripped_thumb"]

    ID = 0x82d1f706
    QUALNAME = "types.UserProfilePhoto"

    def __init__(self, *, photo_id: int, dc_id: int, has_video: Optional[bool] = None, personal: Optional[bool] = None, stripped_thumb: Optional[bytes] = None) -> None:
        self.photo_id = photo_id  # long
        self.dc_id = dc_id  # int
        self.has_video = has_video  # flags.0?true
        self.personal = personal  # flags.2?true
        self.stripped_thumb = stripped_thumb  # flags.1?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserProfilePhoto":

        flags = Int.read(b)

        has_video = True if flags & (1 << 0) else False
        personal = True if flags & (1 << 2) else False
        photo_id = Long.read(b)

        stripped_thumb = Bytes.read(b) if flags & (1 << 1) else None
        dc_id = Int.read(b)

        return UserProfilePhoto(photo_id=photo_id, dc_id=dc_id, has_video=has_video, personal=personal, stripped_thumb=stripped_thumb)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_video else 0
        flags |= (1 << 2) if self.personal else 0
        flags |= (1 << 1) if self.stripped_thumb is not None else 0
        b.write(Int(flags))

        b.write(Long(self.photo_id))

        if self.stripped_thumb is not None:
            b.write(Bytes(self.stripped_thumb))

        b.write(Int(self.dc_id))

        return b.getvalue()
