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


class ChannelAdminLogEventsFilter(TLObject):  # type: ignore
    """Filter only certain admin log events

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventsFilter`.

    Details:
        - Layer: ``224``
        - ID: ``EA107AE4``

    Parameters:
        join (``bool``, *optional*):
            Join events, including joins using invite links and join requests.

        leave (``bool``, *optional*):
            Leave events

        invite (``bool``, *optional*):
            Invite events

        ban (``bool``, *optional*):
            Ban events

        unban (``bool``, *optional*):
            Unban events

        kick (``bool``, *optional*):
            Kick events

        unkick (``bool``, *optional*):
            Unkick events

        promote (``bool``, *optional*):
            Admin promotion events

        demote (``bool``, *optional*):
            Admin demotion events

        info (``bool``, *optional*):
            Info change events (when about, linked chat, location, photo, stickerset, title or username, slowmode, history TTL settings of a channel gets modified)

        settings (``bool``, *optional*):
            Settings change events (invites, hidden prehistory, signatures, default banned rights, forum toggle events)

        pinned (``bool``, *optional*):
            Message pin events

        edit (``bool``, *optional*):
            Message edit events

        delete (``bool``, *optional*):
            Message deletion events

        group_call (``bool``, *optional*):
            Group call events

        invites (``bool``, *optional*):
            Invite events

        send (``bool``, *optional*):
            A message was posted in a channel

        forums (``bool``, *optional*):
            Forum-related events

        sub_extend (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["join", "leave", "invite", "ban", "unban", "kick", "unkick", "promote", "demote", "info", "settings", "pinned", "edit", "delete", "group_call", "invites", "send", "forums", "sub_extend"]

    ID = 0xea107ae4
    QUALNAME = "types.ChannelAdminLogEventsFilter"

    def __init__(self, *, join: Optional[bool] = None, leave: Optional[bool] = None, invite: Optional[bool] = None, ban: Optional[bool] = None, unban: Optional[bool] = None, kick: Optional[bool] = None, unkick: Optional[bool] = None, promote: Optional[bool] = None, demote: Optional[bool] = None, info: Optional[bool] = None, settings: Optional[bool] = None, pinned: Optional[bool] = None, edit: Optional[bool] = None, delete: Optional[bool] = None, group_call: Optional[bool] = None, invites: Optional[bool] = None, send: Optional[bool] = None, forums: Optional[bool] = None, sub_extend: Optional[bool] = None) -> None:
        self.join = join  # flags.0?true
        self.leave = leave  # flags.1?true
        self.invite = invite  # flags.2?true
        self.ban = ban  # flags.3?true
        self.unban = unban  # flags.4?true
        self.kick = kick  # flags.5?true
        self.unkick = unkick  # flags.6?true
        self.promote = promote  # flags.7?true
        self.demote = demote  # flags.8?true
        self.info = info  # flags.9?true
        self.settings = settings  # flags.10?true
        self.pinned = pinned  # flags.11?true
        self.edit = edit  # flags.12?true
        self.delete = delete  # flags.13?true
        self.group_call = group_call  # flags.14?true
        self.invites = invites  # flags.15?true
        self.send = send  # flags.16?true
        self.forums = forums  # flags.17?true
        self.sub_extend = sub_extend  # flags.18?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventsFilter":

        flags = Int.read(b)

        join = True if flags & (1 << 0) else False
        leave = True if flags & (1 << 1) else False
        invite = True if flags & (1 << 2) else False
        ban = True if flags & (1 << 3) else False
        unban = True if flags & (1 << 4) else False
        kick = True if flags & (1 << 5) else False
        unkick = True if flags & (1 << 6) else False
        promote = True if flags & (1 << 7) else False
        demote = True if flags & (1 << 8) else False
        info = True if flags & (1 << 9) else False
        settings = True if flags & (1 << 10) else False
        pinned = True if flags & (1 << 11) else False
        edit = True if flags & (1 << 12) else False
        delete = True if flags & (1 << 13) else False
        group_call = True if flags & (1 << 14) else False
        invites = True if flags & (1 << 15) else False
        send = True if flags & (1 << 16) else False
        forums = True if flags & (1 << 17) else False
        sub_extend = True if flags & (1 << 18) else False
        return ChannelAdminLogEventsFilter(join=join, leave=leave, invite=invite, ban=ban, unban=unban, kick=kick, unkick=unkick, promote=promote, demote=demote, info=info, settings=settings, pinned=pinned, edit=edit, delete=delete, group_call=group_call, invites=invites, send=send, forums=forums, sub_extend=sub_extend)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.join else 0
        flags |= (1 << 1) if self.leave else 0
        flags |= (1 << 2) if self.invite else 0
        flags |= (1 << 3) if self.ban else 0
        flags |= (1 << 4) if self.unban else 0
        flags |= (1 << 5) if self.kick else 0
        flags |= (1 << 6) if self.unkick else 0
        flags |= (1 << 7) if self.promote else 0
        flags |= (1 << 8) if self.demote else 0
        flags |= (1 << 9) if self.info else 0
        flags |= (1 << 10) if self.settings else 0
        flags |= (1 << 11) if self.pinned else 0
        flags |= (1 << 12) if self.edit else 0
        flags |= (1 << 13) if self.delete else 0
        flags |= (1 << 14) if self.group_call else 0
        flags |= (1 << 15) if self.invites else 0
        flags |= (1 << 16) if self.send else 0
        flags |= (1 << 17) if self.forums else 0
        flags |= (1 << 18) if self.sub_extend else 0
        b.write(Int(flags))

        return b.getvalue()
