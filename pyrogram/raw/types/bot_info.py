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


class BotInfo(TLObject):  # type: ignore
    """Info about bots (available bot commands, etc)

    Constructor of :obj:`~pyrogram.raw.base.BotInfo`.

    Details:
        - Layer: ``224``
        - ID: ``4D8A0299``

    Parameters:
        has_preview_medias (``bool``, *optional*):
            N/A

        user_id (``int`` ``64-bit``, *optional*):
            ID of the bot

        description (``str``, *optional*):
            Description of the bot

        description_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            Description photo

        description_document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            Description animation in MPEG4 format

        commands (List of :obj:`BotCommand <pyrogram.raw.base.BotCommand>`, *optional*):
            Bot commands that can be used in the chat

        menu_button (:obj:`BotMenuButton <pyrogram.raw.base.BotMenuButton>`, *optional*):
            Indicates the action to execute when pressing the in-UI menu button for bots

        privacy_policy_url (``str``, *optional*):
            N/A

        app_settings (:obj:`BotAppSettings <pyrogram.raw.base.BotAppSettings>`, *optional*):
            N/A

        verifier_settings (:obj:`BotVerifierSettings <pyrogram.raw.base.BotVerifierSettings>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["has_preview_medias", "user_id", "description", "description_photo", "description_document", "commands", "menu_button", "privacy_policy_url", "app_settings", "verifier_settings"]

    ID = 0x4d8a0299
    QUALNAME = "types.BotInfo"

    def __init__(self, *, has_preview_medias: Optional[bool] = None, user_id: Optional[int] = None, description: Optional[str] = None, description_photo: "raw.base.Photo" = None, description_document: "raw.base.Document" = None, commands: Optional[List["raw.base.BotCommand"]] = None, menu_button: "raw.base.BotMenuButton" = None, privacy_policy_url: Optional[str] = None, app_settings: "raw.base.BotAppSettings" = None, verifier_settings: "raw.base.BotVerifierSettings" = None) -> None:
        self.has_preview_medias = has_preview_medias  # flags.6?true
        self.user_id = user_id  # flags.0?long
        self.description = description  # flags.1?string
        self.description_photo = description_photo  # flags.4?Photo
        self.description_document = description_document  # flags.5?Document
        self.commands = commands  # flags.2?Vector<BotCommand>
        self.menu_button = menu_button  # flags.3?BotMenuButton
        self.privacy_policy_url = privacy_policy_url  # flags.7?string
        self.app_settings = app_settings  # flags.8?BotAppSettings
        self.verifier_settings = verifier_settings  # flags.9?BotVerifierSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":

        flags = Int.read(b)

        has_preview_medias = True if flags & (1 << 6) else False
        user_id = Long.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        description_photo = TLObject.read(b) if flags & (1 << 4) else None

        description_document = TLObject.read(b) if flags & (1 << 5) else None

        commands = TLObject.read(b) if flags & (1 << 2) else []

        menu_button = TLObject.read(b) if flags & (1 << 3) else None

        privacy_policy_url = String.read(b) if flags & (1 << 7) else None
        app_settings = TLObject.read(b) if flags & (1 << 8) else None

        verifier_settings = TLObject.read(b) if flags & (1 << 9) else None

        return BotInfo(has_preview_medias=has_preview_medias, user_id=user_id, description=description, description_photo=description_photo, description_document=description_document, commands=commands, menu_button=menu_button, privacy_policy_url=privacy_policy_url, app_settings=app_settings, verifier_settings=verifier_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 6) if self.has_preview_medias else 0
        flags |= (1 << 0) if self.user_id is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 4) if self.description_photo is not None else 0
        flags |= (1 << 5) if self.description_document is not None else 0
        flags |= (1 << 2) if self.commands else 0
        flags |= (1 << 3) if self.menu_button is not None else 0
        flags |= (1 << 7) if self.privacy_policy_url is not None else 0
        flags |= (1 << 8) if self.app_settings is not None else 0
        flags |= (1 << 9) if self.verifier_settings is not None else 0
        b.write(Int(flags))

        if self.user_id is not None:
            b.write(Long(self.user_id))

        if self.description is not None:
            b.write(String(self.description))

        if self.description_photo is not None:
            b.write(self.description_photo.write())

        if self.description_document is not None:
            b.write(self.description_document.write())

        if self.commands is not None:
            b.write(Vector(self.commands))

        if self.menu_button is not None:
            b.write(self.menu_button.write())

        if self.privacy_policy_url is not None:
            b.write(String(self.privacy_policy_url))

        if self.app_settings is not None:
            b.write(self.app_settings.write())

        if self.verifier_settings is not None:
            b.write(self.verifier_settings.write())

        return b.getvalue()
