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


class GetUserPhotos(TLObject):  # type: ignore
    """Returns the list of user photos.


    Details:
        - Layer: ``224``
        - ID: ``91CD32A8``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User ID

        offset (``int`` ``32-bit``):
            Number of list elements to be skipped

        max_id (``int`` ``64-bit``):
            If a positive value was transferred, the method will return only photos with IDs less than the set one. This parameter is often useful when refetching file references », as in conjuction with limit=1 and offset=-1 the photo object with the id specified in max_id can be fetched.

        limit (``int`` ``32-bit``):
            Number of list elements to be returned

    Returns:
        :obj:`photos.Photos <pyrogram.raw.base.photos.Photos>`
    """

    __slots__: List[str] = ["user_id", "offset", "max_id", "limit"]

    ID = 0x91cd32a8
    QUALNAME = "functions.photos.GetUserPhotos"

    def __init__(self, *, user_id: "raw.base.InputUser", offset: int, max_id: int, limit: int) -> None:
        self.user_id = user_id  # InputUser
        self.offset = offset  # int
        self.max_id = max_id  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserPhotos":
        # No flags

        user_id = TLObject.read(b)

        offset = Int.read(b)

        max_id = Long.read(b)

        limit = Int.read(b)

        return GetUserPhotos(user_id=user_id, offset=offset, max_id=max_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.user_id.write())

        b.write(Int(self.offset))

        b.write(Long(self.max_id))

        b.write(Int(self.limit))

        return b.getvalue()
