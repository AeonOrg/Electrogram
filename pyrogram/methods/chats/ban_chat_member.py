from __future__ import annotations

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import raw, types, utils

if TYPE_CHECKING:
    from datetime import datetime


class BanChatMember:
    async def ban_chat_member(
        self: pyrogram.Client,
        chat_id: int | str,
        user_id: int | str,
        until_date: datetime | None = None,
        revoke_messages: bool | None = None,
    ) -> types.Message | bool:
        """Ban a user from a group, a supergroup or a channel.
        In the case of supergroups and channels, the user will not be able to return to the group on their own using
        invite links, etc., unless unbanned first. You must be an administrator in the chat for this to work and must
        have the appropriate admin rights.

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins" setting is
            off in the target group. Otherwise members may only be removed by the group's creator or by the member
            that added them.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                You can also use chat public link in form of *t.me/<username>* (str).

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use user profile link in form of *t.me/<username>* (str).

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

            revoke_messages (``bool``, *optional*):
                Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed.
                Always True for supergroups and channels.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, a service message will be returned (when applicable),
            otherwise, in case a message object couldn't be returned, True is returned.

        Example:
            .. code-block:: python

                from datetime import datetime, timedelta

                # Ban chat member forever
                await app.ban_chat_member(chat_id, user_id)

                # Ban chat member and automatically unban after 24h
                await app.ban_chat_member(chat_id, user_id, datetime.now() + timedelta(days=1))
        """
        if until_date is None:
            until_date = utils.zero_datetime()
        chat_peer = await self.resolve_peer(chat_id)
        user_peer = await self.resolve_peer(user_id)

        if isinstance(chat_peer, raw.types.InputPeerChannel):
            input_channel = utils.get_input_channel(chat_peer)
            participant = utils.get_input_peer(user_peer)

            if input_channel is None or participant is None:
                return False

            r = await self.invoke(
                raw.functions.channels.EditBanned(
                    channel=input_channel,
                    participant=participant,
                    banned_rights=raw.types.ChatBannedRights(
                        until_date=utils.datetime_to_timestamp(until_date) or 0,
                        view_messages=True,
                        send_messages=True,
                        send_media=True,
                        send_stickers=True,
                        send_gifs=True,
                        send_games=True,
                        send_inline=True,
                        embed_links=True,
                        manage_topics=True,
                    ),
                ),
            )
        else:
            input_user = utils.get_input_user(user_peer)

            if input_user is None:
                return False

            chat_id_to_use = 0
            if isinstance(chat_id, (int, float)):
                chat_id_to_use = int(chat_id)
            elif isinstance(chat_peer, raw.types.InputPeerChat):
                chat_id_to_use = chat_peer.chat_id

            r = await self.invoke(
                raw.functions.messages.DeleteChatUser(
                    chat_id=abs(chat_id_to_use),
                    user_id=input_user,
                    revoke_history=revoke_messages,
                ),
            )

        for i in r.updates:
            if isinstance(
                i,
                raw.types.UpdateNewMessage | raw.types.UpdateNewChannelMessage,
            ):
                return await types.Message._parse(
                    self,
                    i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                )
        return True
