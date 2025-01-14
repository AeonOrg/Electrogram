from __future__ import annotations

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import raw, types, utils
from pyrogram.types.object import Object

if TYPE_CHECKING:
    from datetime import datetime


class ChatInviteLink(Object):
    """An invite link for a chat.

    Parameters:
        invite_link (``str``):
            The invite link. If the link was created by another chat administrator, then the second part of the
            link will be replaced with "...".

        date (:py:obj:`~datetime.datetime`):
            The date when the link was created.

        is_primary (``bool``):
            True, if the link is primary.

        is_revoked (``bool``):
            True, if the link is revoked.

        creator (:obj:`~pyrogram.types.User`, *optional*):
            Creator of the link.

        name (``str``, *optional*):
            Invite link name

        creates_join_request (``bool``, *optional*):
            True, if users joining the chat via the link need to be approved by chat administrators.

        start_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the link has been edited.

        expire_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the link will expire or has been expired.

        member_limit (``int``, *optional*):
            Maximum number of users that can be members of the chat simultaneously after joining the chat via this
            invite link; 1-99999.

        member_count (``int``, *optional*):
            Number of users that joined via this link and are currently member of the chat.

        pending_join_request_count (``int``, *optional*):
            Number of pending join requests created using this link

        subscription_expired (``int``, *optional*):
            Number of subscription which already expired.

        subscription_period (``int``, *optional*):
            The period of Subscription.

        subscription_price (``int``, *optional*):
            The price of Subscription (stars).
    """

    def __init__(
        self,
        *,
        invite_link: str,
        date: datetime,
        is_primary: bool | None = None,
        is_revoked: bool | None = None,
        creator: types.User = None,
        name: str | None = None,
        creates_join_request: bool | None = None,
        start_date: datetime | None = None,
        expire_date: datetime | None = None,
        member_limit: int | None = None,
        member_count: int | None = None,
        pending_join_request_count: int | None = None,
        subscription_expired: int | None = None,
        subscription_period: int | None = None,
        subscription_price: int | None = None,
    ) -> None:
        super().__init__()

        self.invite_link = invite_link
        self.date = date
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.creator = creator
        self.name = name
        self.creates_join_request = creates_join_request
        self.start_date = start_date
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.member_count = member_count
        self.pending_join_request_count = pending_join_request_count
        self.subscription_expired = subscription_expired
        self.subscription_period = subscription_period
        self.subscription_price = subscription_price

    @staticmethod
    def _parse(
        client: pyrogram.Client,
        invite: raw.base.ExportedChatInvite,
        users: dict[int, raw.types.User] | None = None,
    ) -> ChatInviteLink | None:
        if not isinstance(invite, raw.types.ChatInviteExported):
            return None

        creator = (
            types.User._parse(client, users[invite.admin_id])
            if users is not None
            else None
        )
        subscription_pricing = getattr(invite, "subscription_pricing", None)

        return ChatInviteLink(
            invite_link=invite.link,
            date=utils.timestamp_to_datetime(invite.date),
            is_primary=invite.permanent,
            is_revoked=invite.revoked,
            creator=creator,
            name=invite.title,
            creates_join_request=invite.request_needed,
            start_date=utils.timestamp_to_datetime(invite.start_date),
            expire_date=utils.timestamp_to_datetime(invite.expire_date),
            member_limit=invite.usage_limit,
            member_count=invite.usage,
            pending_join_request_count=invite.requested,
            subscription_expired=invite.subscription_expired,
            subscription_period=subscription_pricing.period
            if subscription_pricing is not None
            else None,
            subscription_price=subscription_pricing.amount
            if subscription_pricing is not None
            else None,
        )
