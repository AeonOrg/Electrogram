from __future__ import annotations

from typing import TYPE_CHECKING

from pyrogram import raw, types, utils
from pyrogram.types.object import Object

if TYPE_CHECKING:
    from datetime import datetime


class SuggestedPost(Object):
    """A suggested post.

    Parameters:
        is_accepted (``bool``, *optional*):
            True, if the post was accepted.

        is_rejected (``bool``, *optional*):
            True, if the post was rejected.

        price (:obj:`~pyrogram.types.StarsAmount`, *optional*):
            Price of the post.

        schedule_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the post will be automatically sent.
    """

    def __init__(
        self,
        *,
        is_accepted: bool | None = None,
        is_rejected: bool | None = None,
        price: types.StarsAmount | None = None,
        schedule_date: datetime | None = None,
    ) -> None:
        super().__init__(None)

        self.is_accepted = is_accepted
        self.is_rejected = is_rejected
        self.price = price
        self.schedule_date = schedule_date

    async def write(self) -> raw.types.SuggestedPost:
        return raw.types.SuggestedPost(
            accepted=self.is_accepted or None,
            rejected=self.is_rejected or None,
            price=await self.price.write() if self.price else None,
            schedule_date=utils.datetime_to_timestamp(self.schedule_date),
        )

    @staticmethod
    def _parse(suggested_post: raw.types.SuggestedPost) -> SuggestedPost | None:
        if not suggested_post:
            return None

        return SuggestedPost(
            is_accepted=suggested_post.accepted,
            is_rejected=suggested_post.rejected,
            price=types.StarsAmount._parse(suggested_post.price),
            schedule_date=utils.timestamp_to_datetime(suggested_post.schedule_date),
        )
