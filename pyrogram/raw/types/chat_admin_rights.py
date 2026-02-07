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


class ChatAdminRights(TLObject):  # type: ignore
    """Represents the rights of an admin in a channel/supergroup.

    Constructor of :obj:`~pyrogram.raw.base.ChatAdminRights`.

    Details:
        - Layer: ``224``
        - ID: ``5FB224D5``

    Parameters:
        change_info (``bool``, *optional*):
            If set, allows the admin to modify the description of the channel/supergroup

        post_messages (``bool``, *optional*):
            If set, allows the admin to post messages in the channel

        edit_messages (``bool``, *optional*):
            If set, allows the admin to also edit messages from other admins in the channel

        delete_messages (``bool``, *optional*):
            If set, allows the admin to also delete messages from other admins in the channel

        ban_users (``bool``, *optional*):
            If set, allows the admin to ban users from the channel/supergroup

        invite_users (``bool``, *optional*):
            If set, allows the admin to invite users in the channel/supergroup

        pin_messages (``bool``, *optional*):
            If set, allows the admin to pin messages in the channel/supergroup

        add_admins (``bool``, *optional*):
            If set, allows the admin to add other admins with the same (or more limited) permissions in the channel/supergroup

        anonymous (``bool``, *optional*):
            Whether this admin is anonymous

        manage_call (``bool``, *optional*):
            If set, allows the admin to change group call/livestream settings

        other (``bool``, *optional*):
            Set this flag if none of the other flags are set, but you still want the user to be an admin: if this or any of the other flags are set, the admin can get the chat admin log, get chat statistics, get message statistics in channels, get channel members, see anonymous administrators in supergroups and ignore slow mode.

        manage_topics (``bool``, *optional*):
            If set, allows the admin to create, delete or modify forum topics ».

        post_stories (``bool``, *optional*):
            If set, allows the admin to post stories as the channel.

        edit_stories (``bool``, *optional*):
            If set, allows the admin to edit stories posted by the other admins of the channel.

        delete_stories (``bool``, *optional*):
            If set, allows the admin to delete stories posted by the other admins of the channel.

        manage_direct_messages (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["change_info", "post_messages", "edit_messages", "delete_messages", "ban_users", "invite_users", "pin_messages", "add_admins", "anonymous", "manage_call", "other", "manage_topics", "post_stories", "edit_stories", "delete_stories", "manage_direct_messages"]

    ID = 0x5fb224d5
    QUALNAME = "types.ChatAdminRights"

    def __init__(self, *, change_info: Optional[bool] = None, post_messages: Optional[bool] = None, edit_messages: Optional[bool] = None, delete_messages: Optional[bool] = None, ban_users: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, add_admins: Optional[bool] = None, anonymous: Optional[bool] = None, manage_call: Optional[bool] = None, other: Optional[bool] = None, manage_topics: Optional[bool] = None, post_stories: Optional[bool] = None, edit_stories: Optional[bool] = None, delete_stories: Optional[bool] = None, manage_direct_messages: Optional[bool] = None) -> None:
        self.change_info = change_info  # flags.0?true
        self.post_messages = post_messages  # flags.1?true
        self.edit_messages = edit_messages  # flags.2?true
        self.delete_messages = delete_messages  # flags.3?true
        self.ban_users = ban_users  # flags.4?true
        self.invite_users = invite_users  # flags.5?true
        self.pin_messages = pin_messages  # flags.7?true
        self.add_admins = add_admins  # flags.9?true
        self.anonymous = anonymous  # flags.10?true
        self.manage_call = manage_call  # flags.11?true
        self.other = other  # flags.12?true
        self.manage_topics = manage_topics  # flags.13?true
        self.post_stories = post_stories  # flags.14?true
        self.edit_stories = edit_stories  # flags.15?true
        self.delete_stories = delete_stories  # flags.16?true
        self.manage_direct_messages = manage_direct_messages  # flags.17?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminRights":

        flags = Int.read(b)

        change_info = True if flags & (1 << 0) else False
        post_messages = True if flags & (1 << 1) else False
        edit_messages = True if flags & (1 << 2) else False
        delete_messages = True if flags & (1 << 3) else False
        ban_users = True if flags & (1 << 4) else False
        invite_users = True if flags & (1 << 5) else False
        pin_messages = True if flags & (1 << 7) else False
        add_admins = True if flags & (1 << 9) else False
        anonymous = True if flags & (1 << 10) else False
        manage_call = True if flags & (1 << 11) else False
        other = True if flags & (1 << 12) else False
        manage_topics = True if flags & (1 << 13) else False
        post_stories = True if flags & (1 << 14) else False
        edit_stories = True if flags & (1 << 15) else False
        delete_stories = True if flags & (1 << 16) else False
        manage_direct_messages = True if flags & (1 << 17) else False
        return ChatAdminRights(change_info=change_info, post_messages=post_messages, edit_messages=edit_messages, delete_messages=delete_messages, ban_users=ban_users, invite_users=invite_users, pin_messages=pin_messages, add_admins=add_admins, anonymous=anonymous, manage_call=manage_call, other=other, manage_topics=manage_topics, post_stories=post_stories, edit_stories=edit_stories, delete_stories=delete_stories, manage_direct_messages=manage_direct_messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.change_info else 0
        flags |= (1 << 1) if self.post_messages else 0
        flags |= (1 << 2) if self.edit_messages else 0
        flags |= (1 << 3) if self.delete_messages else 0
        flags |= (1 << 4) if self.ban_users else 0
        flags |= (1 << 5) if self.invite_users else 0
        flags |= (1 << 7) if self.pin_messages else 0
        flags |= (1 << 9) if self.add_admins else 0
        flags |= (1 << 10) if self.anonymous else 0
        flags |= (1 << 11) if self.manage_call else 0
        flags |= (1 << 12) if self.other else 0
        flags |= (1 << 13) if self.manage_topics else 0
        flags |= (1 << 14) if self.post_stories else 0
        flags |= (1 << 15) if self.edit_stories else 0
        flags |= (1 << 16) if self.delete_stories else 0
        flags |= (1 << 17) if self.manage_direct_messages else 0
        b.write(Int(flags))

        return b.getvalue()
