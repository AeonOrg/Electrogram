from __future__ import annotations

from pyrogram import enums, raw
from pyrogram.types.object import Object


class KeyboardButtonStyle(Object):
    """Button style.

    Parameters:
        bg_primary (``bool``, *optional*):
            Whether the button should be primary.

        bg_danger (``bool``, *optional*):
            Whether the button should be danger.

        bg_success (``bool``, *optional*):
            Whether the button should be success.

        icon (``int``, *optional*):
            Custom icon for the button.
    """

    def __init__(
        self,
        *,
        bg_primary: bool | None = None,
        bg_danger: bool | None = None,
        bg_success: bool | None = None,
        icon: int | None = None,
    ) -> None:
        super().__init__()

        self.bg_primary = bg_primary
        self.bg_danger = bg_danger
        self.bg_success = bg_success
        self.icon = icon

    @staticmethod
    def read(b: raw.types.KeyboardButtonStyle) -> KeyboardButtonStyle | None:
        if not b:
            return None

        return KeyboardButtonStyle(
            bg_primary=b.bg_primary,
            bg_danger=b.bg_danger,
            bg_success=b.bg_success,
            icon=b.icon,
        )

    def write(self) -> raw.types.KeyboardButtonStyle:
        return raw.types.KeyboardButtonStyle(
            bg_primary=self.bg_primary,
            bg_danger=self.bg_danger,
            bg_success=self.bg_success,
            icon=self.icon,
        )

    @staticmethod
    def _parse(
        style: KeyboardButtonStyle | enums.ButtonStyle | None,
    ) -> KeyboardButtonStyle | None:
        if style is None:
            return None

        if isinstance(style, enums.ButtonStyle):
            return KeyboardButtonStyle(
                bg_primary=style == enums.ButtonStyle.PRIMARY,
                bg_danger=style == enums.ButtonStyle.DANGER,
                bg_success=style == enums.ButtonStyle.SUCCESS,
            )

        return style
