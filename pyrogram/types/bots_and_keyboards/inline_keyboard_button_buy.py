from __future__ import annotations

import pyrogram
from pyrogram import raw, types
from pyrogram.types.object import Object


class InlineKeyboardButtonBuy(Object):
    """One button of the inline keyboard.
    For simple invoice buttons.

    Parameters:
        text (``str``):
            Text of the button. If none of the optional fields are used, it will be sent as a message when
            the button is pressed.

        style (:obj:`~pyrogram.types.KeyboardButtonStyle`, *optional*):
            Button style.
    """

    def __init__(
        self,
        text: str,
        style: types.KeyboardButtonStyle | None = None,
    ) -> None:
        super().__init__()

        self.text = str(text)
        self.style = style

    @staticmethod
    def read(b):
        return InlineKeyboardButtonBuy(
            text=b.text,
            style=types.KeyboardButtonStyle.read(getattr(b, "style", None)),
        )

    async def write(self, _: pyrogram.Client):
        return raw.types.KeyboardButtonBuy(
            text=self.text,
            style=self.style.write() if self.style else None,
        )
