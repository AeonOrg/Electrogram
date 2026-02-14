from __future__ import annotations

import pyrogram
from pyrogram import raw


class CanSendMessage:
    async def can_send_message(
        self: pyrogram.Client,
        user_id: int | str,
    ) -> bool:
        """Check whether the specified bot can send you messages.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target bot.

        Returns:
            ``bool``: On success, True is returned, False otherwise.
        """
        return bool(
            await self.invoke(
                raw.functions.bots.CanSendMessage(
                    bot=await self.resolve_peer(user_id)
                )
            )
        )
