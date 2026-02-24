from __future__ import annotations

import pyrogram
from pyrogram import raw, types, utils


class SetChatMenuButton:
    async def set_chat_menu_button(
        self: pyrogram.Client,
        chat_id: int | str | None = None,
        menu_button: types.MenuButton | None = None,
    ) -> bool:
        """Change the bot's menu button in a private chat, or the default menu button.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                If not specified, default bot's menu button will be changed.

            menu_button (:obj:`~pyrogram.types.MenuButton`, *optional*):
                The new bot's menu button.
                Defaults to :obj:`~pyrogram.types.MenuButtonDefault`.
        """

        user_id = utils.get_input_user(await self.resolve_peer(chat_id or "me"))
        if user_id is None:
            raise ValueError(f"Invalid user_id: {chat_id or 'me'}")

        await self.invoke(
            raw.functions.bots.SetBotMenuButton(
                user_id=user_id,
                button=(
                    (await menu_button.write(self))
                    if menu_button
                    else (await types.MenuButtonDefault().write(self))
                ),
            ),
        )

        return True
