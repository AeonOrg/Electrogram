from __future__ import annotations

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import raw

if TYPE_CHECKING:
    from collections.abc import Iterable


class DeleteScheduledMessages:
    async def delete_scheduled_messages(
        self: pyrogram.Client,
        chat_id: int | str,
        message_ids: int | Iterable[int],
    ) -> int | list[int]:
        """Delete scheduled messages.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).
            message_ids (``int`` | Iterable of ``int``):
                An iterable of message identifiers to delete (integers) or a single message id.

        Returns:
            ``int`` | List of ``int``: In case *message_ids* was not
            a list, a single message id is returned, otherwise a list of messages ids is returned.

        Example:
            .. code-block:: python

                # Delete one message
                await app.delete_scheduled_messages(chat_id, message_id)
                # Delete multiple messages at once
                await app.delete_scheduled_messages(chat_id, list_of_message_ids)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(message_ids, int):
            is_iterable = False
            ids = [message_ids]
        else:
            is_iterable = True
            ids = list(message_ids)

        await self.invoke(
            raw.functions.messages.DeleteScheduledMessages(
                peer=peer,  # type: ignore
                id=ids,
            ),
        )

        return ids if is_iterable else ids[0]
