from __future__ import annotations

from typing import cast

import pyrogram
from pyrogram import enums, raw, types, utils


class SendMessageDraft:
    async def send_message_draft(
        self: pyrogram.Client,
        chat_id: int | str,
        draft_id: int,
        text: str,
        parse_mode: enums.ParseMode | None = None,
        entities: list[types.MessageEntity] | None = None,
        message_thread_id: int | None = None,
        business_connection_id: str | None = None,
    ) -> bool:
        """Stream a drafted text message to a user while the message is being generated.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            draft_id (``int``):
                Unique identifier of the message draft; must be non-zero.
                Changes of drafts with the same identifier are animated.

            text (``str``):
                Text of the message to be sent.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.
                for forum supergroups only.

            business_connection_id (``str``, *optional*):
                Business connection identifier.
                for business bots only.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.send_message_draft(chat_id, 12345, "Hello, I am thinking...")
        """
        parsed_text = await utils.parse_text_entities(
            self, text, parse_mode, entities
        )

        rpc = raw.functions.messages.SetTyping(
            peer=utils.get_input_peer(await self.resolve_peer(chat_id)),
            action=raw.types.SendMessageTextDraftAction(
                random_id=draft_id,
                text=raw.types.TextWithEntities(
                    text=cast("str", parsed_text["message"]),
                    entities=parsed_text.get("entities") or [],
                ),
            ),
            top_msg_id=message_thread_id,
        )

        if business_connection_id:
            return await self.invoke(
                raw.functions.InvokeWithBusinessConnection(
                    connection_id=business_connection_id,
                    query=rpc,
                ),
            )

        return await self.invoke(rpc)
