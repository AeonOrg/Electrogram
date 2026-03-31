from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

    import pyrogram
    from pyrogram import enums, types

log = logging.getLogger(__name__)


class CopyMessage:
    async def copy_message(
        self: pyrogram.Client,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        caption: str | None = None,
        parse_mode: enums.ParseMode | None = None,
        caption_entities: list[types.MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        message_thread_id: int | None = None,
        reply_to_message_id: int | None = None,
        reply_to_chat_id: int | None = None,
        schedule_date: datetime | None = None,
        schedule_repeat_period: int | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        allow_paid_stars: int | None = None,
        message_effect_id: int | None = None,
        invert_media: bool | None = None,
        quick_reply_shortcut: str | int | None = None,
        send_as: int | str | None = None,
        background: bool | None = None,
        clear_draft: bool | None = None,
        update_stickersets_order: bool | None = None,
        suggested_post: types.SuggestedPost | None = None,
        reply_markup: types.InlineKeyboardMarkup
        | None
        | types.ReplyKeyboardMarkup
        | types.ReplyKeyboardRemove
        | types.ForceReply = None,
    ) -> types.Message | list[types.Message] | None:
        """Copy messages of any kind.

        The method is analogous to the method :meth:`~Client.forward_messages`, but the copied message doesn't have a
        link to the original message.

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

            message_id (``int``):
                Message identifier in the chat specified in *from_chat_id*.

            caption (``string``, *optional*):
                New caption for media, 0-1024 characters after entities parsing.
                If not specified, the original caption is kept.
                Pass "" (empty string) to remove the caption.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the new caption, which can be specified instead of *parse_mode*.

            has_spoiler (``bool``, *optional*):
                Pass True if the photo needs to be covered with a spoiler animation.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.
                for forum supergroups only.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            reply_to_chat_id (``int``, *optional*):
                Unique identifier for the origin chat.
                for reply to message from another chat.
                You can also use chat public link in form of *t.me/<username>* (str).

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

            message_effect_id (``int`` ``64-bit``, *optional*):
                Unique identifier of the message effect to be added to the message; for private chats only.

            invert_media (``bool``, *optional*):
                Inverts the position of the media and caption.

            quick_reply_shortcut (``str`` | ``int``, *optional*):
                Quick reply shortcut identifier or name.

            send_as (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the chat to send the message as.

            background (``bool``, *optional*):
                Pass True to send the message in the background.

            clear_draft (``bool``, *optional*):
                Pass True to clear the draft.

            update_stickersets_order (``bool``, *optional*):
                Pass True to update the stickersets order.

            suggested_post (:obj:`~pyrogram.types.SuggestedPost`, *optional*):
                Suggested post information.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the copied message is returned.

        Example:
            .. code-block:: python

                # Copy a message
                await app.copy_message(to_chat, from_chat, 123)

        """
        message = await self.get_messages(from_chat_id, message_id)

        from pyrogram import types

        if isinstance(message, types.Message):
            return await message.copy(
                chat_id=chat_id,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                has_spoiler=has_spoiler,
                disable_notification=disable_notification,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_to_chat_id=reply_to_chat_id,
                schedule_date=schedule_date,
                schedule_repeat_period=schedule_repeat_period,
                protect_content=protect_content,
                allow_paid_broadcast=allow_paid_broadcast,
                allow_paid_stars=allow_paid_stars,
                message_effect_id=message_effect_id,
                invert_media=invert_media,
                quick_reply_shortcut=quick_reply_shortcut,
                send_as=send_as,
                background=background,
                clear_draft=clear_draft,
                update_stickersets_order=update_stickersets_order,
                suggested_post=suggested_post,
                reply_markup=reply_markup,
            )

        return None
