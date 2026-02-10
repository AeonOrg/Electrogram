from __future__ import annotations

from pyrogram import raw
from pyrogram.types.object import Object


class StarsAmount(Object):
    """A stars amount.

    Parameters:
        amount (``int``):
            Amount of stars.

        nanos (``int``, *optional*):
            Amount of nanostars.
    """

    def __init__(
        self,
        *,
        amount: int,
        nanos: int | None = None,
    ) -> None:
        super().__init__(None)

        self.amount = amount
        self.nanos = nanos

    async def write(self) -> raw.base.StarsAmount:
        if self.nanos:
            return raw.types.StarsAmount(amount=self.amount, nanos=self.nanos)
        return raw.types.StarsTonAmount(amount=self.amount)

    @staticmethod
    def _parse(
        stars_amount: raw.types.StarsAmount | raw.types.StarsTonAmount,
    ) -> StarsAmount | None:
        if not stars_amount:
            return None

        return StarsAmount(
            amount=stars_amount.amount,
            nanos=getattr(stars_amount, "nanos", None),
        )
