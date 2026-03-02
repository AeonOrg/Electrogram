from __future__ import annotations

import typing
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyrogram import types

from pyrogram.types.object import Object

if TYPE_CHECKING:
    from pyrogram import raw


class StoryViews(Object):
    """Contains information about a story viewers.


    Parameters:
        view_count (``int``):
            The count of stories viewers.

        forward_count (``int``, *optional*):
            The count of stories forwards.

        reactions (List of :obj:`~pyrogram.types.Reaction`, *optional*):
            List of reactions.

        reactions_count (``int``, *optional*):
            The count of stories reactions.

        recent_viewers (List of ``int``, *optional*):
            List of user_id of recent stories viewers.
    """

    def __init__(
        self,
        *,
        view_count: int,
        forward_count: int | None = None,
        reactions: list[types.Reaction] | None = None,
        reactions_count: int | None = None,
        recent_viewers: list[int] | None = None,
    ) -> None:
        super().__init__()

        self.view_count = view_count
        self.forward_count = forward_count
        self.reactions = reactions
        self.reactions_count = reactions_count
        self.recent_viewers = recent_viewers

    @staticmethod
    def _parse(client, storyviews: raw.types.StoryViews) -> StoryViews:
        from pyrogram import types

        reactions = [
            types.Reaction._parse_count(client, reaction)
            for reaction in getattr(storyviews, "reactions", [])
        ]
        return StoryViews(
            view_count=getattr(storyviews, "views_count", 0),
            forward_count=getattr(storyviews, "forwards_count", None),
            reactions=typing.cast(
                "list[types.Reaction]", [r for r in reactions if r is not None]
            )
            or None,
            reactions_count=getattr(storyviews, "reactions_count", None),
            recent_viewers=getattr(storyviews, "recent_viewers", None),
        )
