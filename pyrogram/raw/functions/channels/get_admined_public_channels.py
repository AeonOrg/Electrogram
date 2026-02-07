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


class GetAdminedPublicChannels(TLObject):  # type: ignore
    """Get channels/supergroups/geogroups we're admin in. Usually called when the user exceeds the limit for owned public channels/supergroups/geogroups, and the user is given the choice to remove one of his channels/supergroups/geogroups.


    Details:
        - Layer: ``224``
        - ID: ``F8B036AF``

    Parameters:
        by_location (``bool``, *optional*):
            Get geogroups

        check_limit (``bool``, *optional*):
            If set and the user has reached the limit of owned public channels/supergroups/geogroups, instead of returning the channel list one of the specified errors will be returned.Useful to check if a new public channel can indeed be created, even before asking the user to enter a channel username to use in channels.checkUsername/channels.updateUsername.

        for_personal (``bool``, *optional*):


    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["by_location", "check_limit", "for_personal"]

    ID = 0xf8b036af
    QUALNAME = "functions.channels.GetAdminedPublicChannels"

    def __init__(self, *, by_location: Optional[bool] = None, check_limit: Optional[bool] = None, for_personal: Optional[bool] = None) -> None:
        self.by_location = by_location  # flags.0?true
        self.check_limit = check_limit  # flags.1?true
        self.for_personal = for_personal  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAdminedPublicChannels":

        flags = Int.read(b)

        by_location = True if flags & (1 << 0) else False
        check_limit = True if flags & (1 << 1) else False
        for_personal = True if flags & (1 << 2) else False
        return GetAdminedPublicChannels(by_location=by_location, check_limit=check_limit, for_personal=for_personal)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.by_location else 0
        flags |= (1 << 1) if self.check_limit else 0
        flags |= (1 << 2) if self.for_personal else 0
        b.write(Int(flags))

        return b.getvalue()
