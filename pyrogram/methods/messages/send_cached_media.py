from __future__ import annotations

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import enums, raw, types, utils

if TYPE_CHECKING:
    from datetime import datetime


class SendCachedMedia:
    async def send_cached_media(
        self: pyrogram.Client,
        chat_id: int | str,
        file_id: str,
        caption: str = "",
        parse_mode: enums.ParseMode | None = None,
        caption_entities: list[types.MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        message_thread_id: int | None = None,
        reply_to_message_id: int | None = None,
        reply_to_story_id: int | None = None,
        reply_to_chat_id: int | str | None = None,
        quote_text: str | None = None,
        quote_entities: list[types.MessageEntity] | None = None,
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
    ) -> types.Message | None:
        """Send any media stored on the Telegram servers using a file_id.

        This convenience method works with any valid file_id only.
        It does the same as calling the relevant method for sending media using a file_id, thus saving you from the
        hassle of using the correct method for the media the file_id is pointing to.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            file_id (``str``):
                Media to send.
                Pass a file_id as string to send a media that exists on the Telegram servers.

            caption (``str``, *optional*):
                Media caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

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

            reply_to_story_id (``int``, *optional*):
                If the message is a reply, ID of the target story.

            reply_to_chat_id (``int`` | ``str``, *optional*):
                Unique identifier for the origin chat.
                for reply to message from another chat.
                You can also use chat public link in form of *t.me/<username>* (str).

            quote_text (``str``, *optional*):
                Text to quote.
                for reply_to_message only.

            quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
                for reply_to_message only.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            schedule_repeat_period (``int``, *optional*):
                Repeat period of the scheduled message.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            allow_paid_broadcast (``bool``, *optional*):
                Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots only

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
            :obj:`~pyrogram.types.Message`: On success, the sent media message is returned.

        Example:
            .. code-block:: python

                await app.send_cached_media("me", file_id)
        """

        reply_to = await utils.get_reply_to(
            client=self,
            chat_id=chat_id,
            reply_to_message_id=reply_to_message_id,
            reply_to_story_id=reply_to_story_id,
            message_thread_id=message_thread_id,
            reply_to_chat_id=reply_to_chat_id,
            quote_text=quote_text,
            quote_entities=quote_entities,
            parse_mode=parse_mode,
        )

        media = utils.get_input_media_from_file_id(file_id)
        media.spoiler = has_spoiler

        r = await self.invoke(
            raw.functions.messages.SendMedia(
                peer=utils.get_input_peer(await self.resolve_peer(chat_id)),
                media=media,
                silent=disable_notification or None,
                reply_to=reply_to,
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                noforwards=protect_content,
                allow_paid_floodskip=allow_paid_broadcast,
                invert_media=invert_media,
                effect=message_effect_id,
                background=background,
                clear_draft=clear_draft,
                update_stickersets_order=update_stickersets_order,
                schedule_repeat_period=schedule_repeat_period,
                send_as=utils.get_input_peer(await self.resolve_peer(send_as))
                if send_as
                else None,
                quick_reply_shortcut=await utils.get_input_quick_reply_shortcut(
                    quick_reply_shortcut,
                )
                if quick_reply_shortcut
                else None,
                allow_paid_stars=allow_paid_stars,
                suggested_post=await suggested_post.write()
                if suggested_post
                else None,
                reply_markup=await reply_markup.write(self)
                if reply_markup
                else None,
                **await utils.parse_text_entities(
                    self,
                    caption,
                    parse_mode,
                    caption_entities,
                ),
            ),
        )

        for i in r.updates:
            if isinstance(
                i,
                raw.types.UpdateNewMessage
                | raw.types.UpdateNewChannelMessage
                | raw.types.UpdateNewScheduledMessage,
            ):
                return await types.Message._parse(
                    self,
                    i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                )
        return None
