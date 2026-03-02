from __future__ import annotations

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import raw, types, utils

if TYPE_CHECKING:
    from collections.abc import Iterable
    from datetime import datetime


class ForwardMessages:
    async def forward_messages(
        self: pyrogram.Client,
        chat_id: int | str,
        from_chat_id: int | str,
        message_ids: int | Iterable[int],
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        schedule_date: datetime | None = None,
        schedule_repeat_period: int | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        allow_paid_stars: int | None = None,
        drop_author: bool | None = None,
        drop_media_captions: bool | None = None,
        background: bool | None = None,
        with_my_score: bool | None = None,
        message_effect_id: int | None = None,
        video_timestamp: int | None = None,
        quick_reply_shortcut: str | int | None = None,
        send_as: int | str | None = None,
        suggested_post: types.SuggestedPost | None = None,
    ) -> types.Message | list[types.Message]:
        """Forward messages of any kind.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            from_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the source chat where the original message was sent.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            message_ids (``int`` | Iterable of ``int``):
                An iterable of message identifiers in the chat specified in *from_chat_id* or a single message id.

            message_thread_id (``int``, *optional*):
                Unique identifier of a message thread to which the message belongs.
                for supergroups only

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            schedule_repeat_period (``int``, *optional*):
                Repeat period of the scheduled message.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            allow_paid_broadcast (``bool``, *optional*):
                Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots only.

            allow_paid_stars (``int``, *optional*):
                Amount of stars to pay for the message; for bots only.

            drop_author (``bool``, *optional*):
                Forwards messages without quoting the original author

            drop_media_captions (``bool``, *optional*):
                Forwards messages without media captions.

            background (``bool``, *optional*):
                Pass True to send the message in the background.

            with_my_score (``bool``, *optional*):
                Forwards games with the user's score.

            message_effect_id (``int`` ``64-bit``, *optional*):
                Unique identifier of the message effect to be added to the message; for private chats only.

            video_timestamp (``int``, *optional*):
                Timestamp for the video.

            quick_reply_shortcut (``str`` | ``int``, *optional*):
                Quick reply shortcut identifier or name.

            send_as (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the chat to send the message as.

            suggested_post (:obj:`~pyrogram.types.SuggestedPost`, *optional*):
                Suggested post information.

        Returns:
            :obj:`~pyrogram.types.Message` | List of :obj:`~pyrogram.types.Message`: In case *message_ids* was not
            a list, a single message is returned, otherwise a list of messages is returned.

        Example:
            .. code-block:: python

                # Forward a single message
                await app.forward_messages(to_chat, from_chat, 123)

                # Forward multiple messages at once
                await app.forward_messages(to_chat, from_chat, [1, 2, 3])
        """

        if isinstance(message_ids, int):
            is_iterable = False
            ids = [message_ids]
        else:
            is_iterable = True
            ids = list(message_ids)

        r = await self.invoke(
            raw.functions.messages.ForwardMessages(
                to_peer=utils.get_input_peer(await self.resolve_peer(chat_id)),
                from_peer=utils.get_input_peer(
                    await self.resolve_peer(from_chat_id)
                ),
                id=ids,
                top_msg_id=message_thread_id,
                silent=disable_notification or None,
                background=background,
                random_id=[self.rnd_id() for _ in ids],
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                noforwards=protect_content,
                allow_paid_floodskip=allow_paid_broadcast,
                drop_author=drop_author,
                drop_media_captions=drop_media_captions,
                with_my_score=with_my_score,
                effect=message_effect_id,
                video_timestamp=video_timestamp,
                quick_reply_shortcut=await utils.get_input_quick_reply_shortcut(
                    quick_reply_shortcut,
                )
                if quick_reply_shortcut
                else None,
                send_as=utils.get_input_peer(await self.resolve_peer(send_as))
                if send_as
                else None,
                allow_paid_stars=allow_paid_stars,
                suggested_post=await suggested_post.write()
                if suggested_post
                else None,
                schedule_repeat_period=schedule_repeat_period,
            ),
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        forwarded_messages = [
            await types.Message._parse(self, i.message, users, chats)
            for i in r.updates
            if isinstance(
                i,
                raw.types.UpdateNewMessage
                | raw.types.UpdateNewChannelMessage
                | raw.types.UpdateNewScheduledMessage
                | raw.types.UpdateBotNewBusinessMessage,
            )
        ]

        return (
            types.List(forwarded_messages) if is_iterable else forwarded_messages[0]
        )
