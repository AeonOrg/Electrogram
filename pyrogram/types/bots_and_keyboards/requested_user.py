from __future__ import annotations

from pyrogram import raw, types
from pyrogram.types.object import Object


class RequestedUser(Object):
    """Contains information about a requested user.

    Parameters:
        user_id (``int``):
            Identifier of the user.

        first_name (``str``, *optional*):
            First name of the user.

        last_name (``str``, *optional*):
            Last name of the user.

        username (``str``, *optional*):
            Username of the user.

        photo (``types.Photo``, *optional*):
            User photo.

        full_name (``str``, *optional*):
            User's full name.
    """

    def __init__(
        self,
        user_id: int,
        first_name: str | None = None,
        last_name: str | None = None,
        username: str | None = None,
        photo: types.Photo | None = None,
    ) -> None:
        super().__init__()

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo

    @staticmethod
    async def _parse(
        client,
        request: raw.base.RequestedPeer | raw.base.Peer,
    ) -> RequestedUser:
        photo = None
        if getattr(request, "photo", None):
            photo = types.Photo._parse(client, getattr(request, "photo", None))

        return RequestedUser(
            user_id=getattr(request, "user_id", 0),
            first_name=getattr(request, "first_name", None),
            last_name=getattr(request, "last_name", None),
            username=getattr(request, "username", None),
            photo=photo,
        )

    @property
    def full_name(self) -> str | None:
        return " ".join(filter(None, [self.first_name, self.last_name])) or None
