from __future__ import annotations

from pyrogram import raw
from pyrogram.types.object import Object


class Restriction(Object):
    """A restriction applied to bots or chats.

    Parameters:
        platform (``str``):
            The platform the restriction is applied to, e.g. "ios", "android"

        reason (``str``):
            The restriction reason, e.g. "porn", "copyright".

        text (``str``):
            The restriction text.
    """

    def __init__(self, *, platform: str, reason: str, text: str) -> None:
        super().__init__(None)

        self.platform = platform
        self.reason = reason
        self.text = text

    @staticmethod
    def _parse(
        restriction: raw.base.RestrictionReason | None,
    ) -> Restriction | None:
        if not isinstance(restriction, raw.types.RestrictionReason):
            return None

        return Restriction(
            platform=restriction.platform,
            reason=restriction.reason,
            text=restriction.text,
        )
