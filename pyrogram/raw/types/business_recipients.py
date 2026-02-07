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


class BusinessRecipients(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BusinessRecipients`.

    Details:
        - Layer: ``224``
        - ID: ``21108FF7``

    Parameters:
        existing_chats (``bool``, *optional*):


        new_chats (``bool``, *optional*):


        contacts (``bool``, *optional*):


        non_contacts (``bool``, *optional*):


        exclude_selected (``bool``, *optional*):


        users (List of ``int`` ``64-bit``, *optional*):


    """

    __slots__: List[str] = ["existing_chats", "new_chats", "contacts", "non_contacts", "exclude_selected", "users"]

    ID = 0x21108ff7
    QUALNAME = "types.BusinessRecipients"

    def __init__(self, *, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[int]] = None) -> None:
        self.existing_chats = existing_chats  # flags.0?true
        self.new_chats = new_chats  # flags.1?true
        self.contacts = contacts  # flags.2?true
        self.non_contacts = non_contacts  # flags.3?true
        self.exclude_selected = exclude_selected  # flags.5?true
        self.users = users  # flags.4?Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessRecipients":

        flags = Int.read(b)

        existing_chats = True if flags & (1 << 0) else False
        new_chats = True if flags & (1 << 1) else False
        contacts = True if flags & (1 << 2) else False
        non_contacts = True if flags & (1 << 3) else False
        exclude_selected = True if flags & (1 << 5) else False
        users = TLObject.read(b, Long) if flags & (1 << 4) else []

        return BusinessRecipients(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.existing_chats else 0
        flags |= (1 << 1) if self.new_chats else 0
        flags |= (1 << 2) if self.contacts else 0
        flags |= (1 << 3) if self.non_contacts else 0
        flags |= (1 << 5) if self.exclude_selected else 0
        flags |= (1 << 4) if self.users else 0
        b.write(Int(flags))

        if self.users is not None:
            b.write(Vector(self.users, Long))

        return b.getvalue()
