from __future__ import annotations

import pyrogram
from pyrogram import raw


class RefundStarsPayment:
    async def refund_stars_payment(
        self: pyrogram.Client,
        user_id: int | str,
        telegram_payment_charge_id: str,
    ) -> bool:
        """Refund the stars to the user.

        Parameters:
            user_id (``int`` | ``str``):
                The user id to refund the stars.

            telegram_payment_charge_id (``str``):
                The charge id to refund the stars.

        Returns:
            `bool`: On success, a True is returned.

        Example:
            .. code-block:: python

                await app.refund_stars_payment(user_id, telegram_payment_charge_id)
        """
        await self.invoke(
            raw.functions.payments.RefundStarsCharge(
                user_id=await self.resolve_peer(user_id),
                charge_id=telegram_payment_charge_id,
            ),
        )

        return True

    refund_star_payment = refund_stars_payment


RefundStarPayment = RefundStarsPayment
