from __future__ import annotations

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import raw, types, utils
from pyrogram.types.object import Object

if TYPE_CHECKING:
    from datetime import datetime


class Gift(Object):
    """Describes a gift that can be sent to another user.

    Parameters:
        id (``int``):
            Unique identifier of the gift.

        sticker (:obj:`~pyrogram.types.Sticker`):
            The sticker representing the gift.

        star_count (``int``):
            Number of Telegram Stars that must be paid for the gift.

        default_sell_star_count (``int``):
            Number of Telegram Stars that can be claimed by the receiver instead of the gift by default. If the gift was paid with just bought Telegram Stars, then full value can be claimed.

        remaining_count (``int``, *optional*):
            Number of remaining times the gift can be purchased by all users; None if not limited or the gift was sold out.

        total_count (``int``, *optional*):
            Number of total times the gift can be purchased by all users; None if not limited.

        first_send_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time (Unix timestamp) when the gift was send for the first time; for sold out gifts only.

        last_send_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time (Unix timestamp) when the gift was send for the last time; for sold out gifts only.

        is_limited (``bool``, *optional*):
            True, if the number of gifts is limited.

        is_sold_out (``bool``, *optional*):
            True, if the star gift is sold out.

        is_birthday (``bool``, *optional*):
            True, if it is a birthday gift.

        can_upgrade (``bool``, *optional*):
            True, if the gift can be upgraded.

        require_premium (``bool``, *optional*):
            True, if the gift requires Telegram Premium to be sent.

        is_limited_per_user (``bool``, *optional*):
            True, if the gift is limited per user.

        is_peer_color_available (``bool``, *optional*):
            True, if peer color is available for this gift.

        is_auction (``bool``, *optional*):
            True, if the gift is an auction gift.

        availability_resale (``int``, *optional*):
            Number of Telegram Stars required to resale the gift.

        upgrade_stars (``int``, *optional*):
            Number of Telegram Stars required to upgrade the gift.

        resell_min_stars (``int``, *optional*):
            Minimum number of Telegram Stars required to resale the gift.

        title (``str``, *optional*):
            Gift title.

        released_by (``int``, *optional*):
            Identifier of the user who released the gift.

        per_user_total (``int``, *optional*):
            Total number of gifts allowed per user.

        per_user_remains (``int``, *optional*):
            Number of remaining gifts allowed per user.

        locked_until_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the gift will be unlocked.

        auction_slug (``str``, *optional*):
            Auction slug.

        gifts_per_round (``int``, *optional*):
            Number of gifts per auction round.

        auction_start_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the auction starts.

        upgrade_variants (``int``, *optional*):
            Number of upgrade variants.

        is_unique (``bool``, *optional*):
            True, if the gift is unique.

        gift_id (``int``, *optional*):
            Unique identifier of the gift.

        slug (``str``, *optional*):
            Gift slug.

        num (``int``, *optional*):
            Gift number.

        owner_id (``int``, *optional*):
            Identifier of the user who owns the gift.

        owner_name (``str``, *optional*):
            Name of the user who owns the gift.

        owner_address (``str``, *optional*):
            Address of the user who owns the gift.

        gift_address (``str``, *optional*):
            Gift address.

        value_amount (``int``, *optional*):
            Gift value amount.

        value_currency (``str``, *optional*):
            Gift value currency.

        value_usd_amount (``int``, *optional*):
            Gift value USD amount.

        craft_chance_permille (``int``, *optional*):
            Craft chance in permille.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client  | None = None,
        id: int,
        sticker: types.Sticker  | None = None,
        star_count: int | None = None,
        default_sell_star_count: int | None = None,
        remaining_count: int | None = None,
        total_count: int | None = None,
        first_send_date: datetime | None = None,
        last_send_date: datetime | None = None,
        is_limited: bool | None = None,
        is_sold_out: bool | None = None,
        is_birthday: bool | None = None,
        can_upgrade: bool | None = None,
        require_premium: bool | None = None,
        is_limited_per_user: bool | None = None,
        is_peer_color_available: bool | None = None,
        is_auction: bool | None = None,
        availability_resale: int | None = None,
        upgrade_stars: int | None = None,
        resell_min_stars: int | None = None,
        title: str | None = None,
        released_by: int | None = None,
        per_user_total: int | None = None,
        per_user_remains: int | None = None,
        locked_until_date: datetime | None = None,
        auction_slug: str | None = None,
        gifts_per_round: int | None = None,
        auction_start_date: datetime | None = None,
        upgrade_variants: int | None = None,
        is_unique: bool | None = None,
        gift_id: int | None = None,
        slug: str | None = None,
        num: int | None = None,
        owner_id: int | None = None,
        owner_name: str | None = None,
        owner_address: str | None = None,
        gift_address: str | None = None,
        value_amount: int | None = None,
        value_currency: str | None = None,
        value_usd_amount: int | None = None,
        craft_chance_permille: int | None = None,
    ) -> None:
        super().__init__(client)

        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.default_sell_star_count = default_sell_star_count
        self.remaining_count = remaining_count
        self.total_count = total_count
        self.first_send_date = first_send_date
        self.last_send_date = last_send_date
        self.is_limited = is_limited
        self.is_sold_out = is_sold_out
        self.is_birthday = is_birthday
        self.can_upgrade = can_upgrade
        self.require_premium = require_premium
        self.is_limited_per_user = is_limited_per_user
        self.is_peer_color_available = is_peer_color_available
        self.is_auction = is_auction
        self.availability_resale = availability_resale
        self.upgrade_stars = upgrade_stars
        self.resell_min_stars = resell_min_stars
        self.title = title
        self.released_by = released_by
        self.per_user_total = per_user_total
        self.per_user_remains = per_user_remains
        self.locked_until_date = locked_until_date
        self.auction_slug = auction_slug
        self.gifts_per_round = gifts_per_round
        self.auction_start_date = auction_start_date
        self.upgrade_variants = upgrade_variants
        self.is_unique = is_unique
        self.gift_id = gift_id
        self.slug = slug
        self.num = num
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.gift_address = gift_address
        self.value_amount = value_amount
        self.value_currency = value_currency
        self.value_usd_amount = value_usd_amount
        self.craft_chance_permille = craft_chance_permille

    @staticmethod
    async def _parse(
        client,
        star_gift: raw.base.StarGift,
    ) -> Gift:
        if isinstance(star_gift, raw.types.StarGift):
            doc = star_gift.sticker
            attributes = {type(i): i for i in doc.attributes}

            return Gift(
                id=star_gift.id,
                sticker=await types.Sticker._parse(client, doc, attributes),
                star_count=star_gift.stars,
                default_sell_star_count=star_gift.convert_stars,
                remaining_count=getattr(star_gift, "availability_remains", None),
                total_count=getattr(star_gift, "availability_total", None),
                first_send_date=utils.timestamp_to_datetime(
                    getattr(star_gift, "first_sale_date", None),
                ),
                last_send_date=utils.timestamp_to_datetime(
                    getattr(star_gift, "last_sale_date", None),
                ),
                is_limited=getattr(star_gift, "limited", None),
                is_sold_out=getattr(star_gift, "sold_out", None),
                is_birthday=getattr(star_gift, "birthday", None),
                can_upgrade=getattr(star_gift, "can_upgrade", None),
                require_premium=getattr(star_gift, "require_premium", None),
                is_limited_per_user=getattr(star_gift, "limited_per_user", None),
                is_peer_color_available=getattr(
                    star_gift,
                    "peer_color_available",
                    None,
                ),
                is_auction=getattr(star_gift, "auction", None),
                availability_resale=getattr(star_gift, "availability_resale", None),
                upgrade_stars=getattr(star_gift, "upgrade_stars", None),
                resell_min_stars=getattr(star_gift, "resell_min_stars", None),
                title=getattr(star_gift, "title", None),
                released_by=utils.get_raw_peer_id(star_gift.released_by)
                if getattr(star_gift, "released_by", None)
                else None,
                per_user_total=getattr(star_gift, "per_user_total", None),
                per_user_remains=getattr(star_gift, "per_user_remains", None),
                locked_until_date=utils.timestamp_to_datetime(
                    getattr(star_gift, "locked_until_date", None),
                ),
                auction_slug=getattr(star_gift, "auction_slug", None),
                gifts_per_round=getattr(star_gift, "gifts_per_round", None),
                auction_start_date=utils.timestamp_to_datetime(
                    getattr(star_gift, "auction_start_date", None),
                ),
                upgrade_variants=getattr(star_gift, "upgrade_variants", None),
                is_unique=False,
                client=client,
            )
        if isinstance(star_gift, raw.types.StarGiftUnique):
            return Gift(
                id=star_gift.id,
                gift_id=star_gift.gift_id,
                title=star_gift.title,
                slug=star_gift.slug,
                num=star_gift.num,
                owner_id=utils.get_raw_peer_id(star_gift.owner_id)
                if star_gift.owner_id
                else None,
                owner_name=star_gift.owner_name,
                owner_address=star_gift.owner_address,
                total_count=star_gift.availability_total,
                gift_address=star_gift.gift_address,
                released_by=utils.get_raw_peer_id(star_gift.released_by)
                if star_gift.released_by
                else None,
                value_amount=star_gift.value_amount,
                value_currency=star_gift.value_currency,
                value_usd_amount=star_gift.value_usd_amount,
                require_premium=star_gift.require_premium,
                craft_chance_permille=star_gift.craft_chance_permille,
                is_unique=True,
                client=client,
            )
        return None
