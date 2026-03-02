from __future__ import annotations

from typing import cast

import pyrogram
from pyrogram import raw, types
from pyrogram.types.object import Object


class MessageReactions(Object):
    """Contains information about a message reactions.

    Parameters:
        reactions (List of :obj:`~pyrogram.types.Reaction`):
            Reactions list.

        top_reactors (List of :obj:`~pyrogram.types.MessageReactor`):
            Top reactors.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client | None = None,
        reactions: list[types.Reaction] | None = None,
        top_reactors: list[types.MessageReactor] | None = None,
    ) -> None:
        super().__init__(client)

        self.reactions = reactions
        self.top_reactors = top_reactors

    @staticmethod
    def _parse(
        client: pyrogram.Client,
        message_reactions: raw.base.MessageReactions | None = None,
        users: dict[int, raw.types.User] | None = None,
    ) -> MessageReactions | None:
        if not message_reactions:
            return None

        reactions = [
            types.Reaction._parse_count(client, reaction)
            for reaction in message_reactions.results
        ]
        top_reactors = [
            types.MessageReactor._parse(client, reactor, users)
            for reactor in message_reactions.top_reactors
        ]

        return MessageReactions(
            client=client,
            reactions=cast(
                "list[types.Reaction]", [r for r in reactions if r is not None]
            ),
            top_reactors=cast(
                "list[types.MessageReactor]",
                [r for r in top_reactors if r is not None],
            ),
        )
