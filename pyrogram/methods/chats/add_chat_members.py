from __future__ import annotations

import pyrogram
from pyrogram import raw, utils


class AddChatMembers:
    async def add_chat_members(
        self: pyrogram.Client,
        chat_id: int | str,
        user_ids: int | str | list[int | str],
        forward_limit: int = 100,
    ) -> bool:
        """Add new chat members to a group, supergroup or channel

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The group, supergroup or channel id or chat/channel public link

            user_ids (``int`` | ``str`` | List of ``int`` or ``str``):
                Users to add in the chat
                You can pass an ID (int), username (str) or phone number (str).
                Multiple users can be added by passing a list of IDs, usernames or phone numbers.
                You can also use user profile link in form of *t.me/<username>* (str).

            forward_limit (``int``, *optional*):
                How many of the latest messages you want to forward to the new members. Pass 0 to forward none of them.
                Only applicable to basic groups (the argument is ignored for supergroups or channels).
                Defaults to 100 (max amount).

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Add one member to a group or channel
                await app.add_chat_members(chat_id, user_id)

                # Add multiple members to a group or channel
                await app.add_chat_members(chat_id, [user_id1, user_id2, user_id3])

                # Change forward_limit (for basic groups only)
                await app.add_chat_members(chat_id, user_id, forward_limit=25)
        """
        peer = await self.resolve_peer(chat_id)

        if not isinstance(user_ids, list):
            user_ids = [user_ids]

        if isinstance(peer, raw.types.InputPeerChat):
            for user_id in user_ids:
                input_user = utils.get_input_user(await self.resolve_peer(user_id))

                if input_user is not None:
                    await self.invoke(
                        raw.functions.messages.AddChatUser(
                            chat_id=peer.chat_id,
                            user_id=input_user,
                            fwd_limit=forward_limit,
                        ),
                    )
        else:
            input_channel = utils.get_input_channel(peer)

            if input_channel is not None:
                await self.invoke(
                    raw.functions.channels.InviteToChannel(
                        channel=input_channel,
                        users=[
                            u
                            for user_id in user_ids
                            if (
                                u := utils.get_input_user(
                                    await self.resolve_peer(user_id),
                                )
                            )
                            is not None
                        ],
                    ),
                )

        return True
