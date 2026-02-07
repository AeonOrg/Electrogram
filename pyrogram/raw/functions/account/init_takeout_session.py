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


class InitTakeoutSession(TLObject):  # type: ignore
    """Initialize a takeout session, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``8EF3EAB0``

    Parameters:
        contacts (``bool``, *optional*):
            Whether to export contacts

        message_users (``bool``, *optional*):
            Whether to export messages in private chats

        message_chats (``bool``, *optional*):
            Whether to export messages in basic groups

        message_megagroups (``bool``, *optional*):
            Whether to export messages in supergroups

        message_channels (``bool``, *optional*):
            Whether to export messages in channels

        files (``bool``, *optional*):
            Whether to export files

        file_max_size (``int`` ``64-bit``, *optional*):
            Maximum size of files to export

    Returns:
        :obj:`account.Takeout <pyrogram.raw.base.account.Takeout>`
    """

    __slots__: List[str] = ["contacts", "message_users", "message_chats", "message_megagroups", "message_channels", "files", "file_max_size"]

    ID = 0x8ef3eab0
    QUALNAME = "functions.account.InitTakeoutSession"

    def __init__(self, *, contacts: Optional[bool] = None, message_users: Optional[bool] = None, message_chats: Optional[bool] = None, message_megagroups: Optional[bool] = None, message_channels: Optional[bool] = None, files: Optional[bool] = None, file_max_size: Optional[int] = None) -> None:
        self.contacts = contacts  # flags.0?true
        self.message_users = message_users  # flags.1?true
        self.message_chats = message_chats  # flags.2?true
        self.message_megagroups = message_megagroups  # flags.3?true
        self.message_channels = message_channels  # flags.4?true
        self.files = files  # flags.5?true
        self.file_max_size = file_max_size  # flags.5?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitTakeoutSession":

        flags = Int.read(b)

        contacts = True if flags & (1 << 0) else False
        message_users = True if flags & (1 << 1) else False
        message_chats = True if flags & (1 << 2) else False
        message_megagroups = True if flags & (1 << 3) else False
        message_channels = True if flags & (1 << 4) else False
        files = True if flags & (1 << 5) else False
        file_max_size = Long.read(b) if flags & (1 << 5) else None
        return InitTakeoutSession(contacts=contacts, message_users=message_users, message_chats=message_chats, message_megagroups=message_megagroups, message_channels=message_channels, files=files, file_max_size=file_max_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts else 0
        flags |= (1 << 1) if self.message_users else 0
        flags |= (1 << 2) if self.message_chats else 0
        flags |= (1 << 3) if self.message_megagroups else 0
        flags |= (1 << 4) if self.message_channels else 0
        flags |= (1 << 5) if self.files else 0
        flags |= (1 << 5) if self.file_max_size is not None else 0
        b.write(Int(flags))

        if self.file_max_size is not None:
            b.write(Long(self.file_max_size))

        return b.getvalue()
