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


class AttachMenuBot(TLObject):  # type: ignore
    """Represents a bot mini app that can be launched from the attachment/side menu »

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBot`.

    Details:
        - Layer: ``224``
        - ID: ``D90D8DFE``

    Parameters:
        bot_id (``int`` ``64-bit``):
            Bot ID

        short_name (``str``):
            Attachment menu item name

        icons (List of :obj:`AttachMenuBotIcon <pyrogram.raw.base.AttachMenuBotIcon>`):
            List of platform-specific static icons and animations to use for the attachment menu button

        inactive (``bool``, *optional*):
            If set, before launching the mini app the client should ask the user to add the mini app to the attachment/side menu, and only if the user accepts, after invoking messages.toggleBotInAttachMenu the app should be opened.

        has_settings (``bool``, *optional*):
            Deprecated flag, can be ignored.

        request_write_access (``bool``, *optional*):
            Whether the bot would like to send messages to the user.

        show_in_attach_menu (``bool``, *optional*):
            Whether, when installed, an attachment menu entry should be shown for the Mini App.

        show_in_side_menu (``bool``, *optional*):
            Whether, when installed, an entry in the main view side menu should be shown for the Mini App.

        side_menu_disclaimer_needed (``bool``, *optional*):
            If inactive if set and the user hasn't previously accepted the third-party mini apps Terms of Service for this bot, when showing the mini app installation prompt, an additional mandatory checkbox to accept the mini apps TOS and a disclaimer indicating that this Mini App is not affiliated to Telegram should be shown.

        peer_types (List of :obj:`AttachMenuPeerType <pyrogram.raw.base.AttachMenuPeerType>`, *optional*):
            List of dialog types where this attachment menu entry should be shown

    """

    __slots__: List[str] = ["bot_id", "short_name", "icons", "inactive", "has_settings", "request_write_access", "show_in_attach_menu", "show_in_side_menu", "side_menu_disclaimer_needed", "peer_types"]

    ID = 0xd90d8dfe
    QUALNAME = "types.AttachMenuBot"

    def __init__(self, *, bot_id: int, short_name: str, icons: List["raw.base.AttachMenuBotIcon"], inactive: Optional[bool] = None, has_settings: Optional[bool] = None, request_write_access: Optional[bool] = None, show_in_attach_menu: Optional[bool] = None, show_in_side_menu: Optional[bool] = None, side_menu_disclaimer_needed: Optional[bool] = None, peer_types: Optional[List["raw.base.AttachMenuPeerType"]] = None) -> None:
        self.bot_id = bot_id  # long
        self.short_name = short_name  # string
        self.icons = icons  # Vector<AttachMenuBotIcon>
        self.inactive = inactive  # flags.0?true
        self.has_settings = has_settings  # flags.1?true
        self.request_write_access = request_write_access  # flags.2?true
        self.show_in_attach_menu = show_in_attach_menu  # flags.3?true
        self.show_in_side_menu = show_in_side_menu  # flags.4?true
        self.side_menu_disclaimer_needed = side_menu_disclaimer_needed  # flags.5?true
        self.peer_types = peer_types  # flags.3?Vector<AttachMenuPeerType>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBot":

        flags = Int.read(b)

        inactive = True if flags & (1 << 0) else False
        has_settings = True if flags & (1 << 1) else False
        request_write_access = True if flags & (1 << 2) else False
        show_in_attach_menu = True if flags & (1 << 3) else False
        show_in_side_menu = True if flags & (1 << 4) else False
        side_menu_disclaimer_needed = True if flags & (1 << 5) else False
        bot_id = Long.read(b)

        short_name = String.read(b)

        peer_types = TLObject.read(b) if flags & (1 << 3) else []

        icons = TLObject.read(b)

        return AttachMenuBot(bot_id=bot_id, short_name=short_name, icons=icons, inactive=inactive, has_settings=has_settings, request_write_access=request_write_access, show_in_attach_menu=show_in_attach_menu, show_in_side_menu=show_in_side_menu, side_menu_disclaimer_needed=side_menu_disclaimer_needed, peer_types=peer_types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.inactive else 0
        flags |= (1 << 1) if self.has_settings else 0
        flags |= (1 << 2) if self.request_write_access else 0
        flags |= (1 << 3) if self.show_in_attach_menu else 0
        flags |= (1 << 4) if self.show_in_side_menu else 0
        flags |= (1 << 5) if self.side_menu_disclaimer_needed else 0
        flags |= (1 << 3) if self.peer_types else 0
        b.write(Int(flags))

        b.write(Long(self.bot_id))

        b.write(String(self.short_name))

        if self.peer_types is not None:
            b.write(Vector(self.peer_types))

        b.write(Vector(self.icons))

        return b.getvalue()
