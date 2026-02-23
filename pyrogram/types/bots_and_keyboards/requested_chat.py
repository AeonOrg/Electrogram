from __future__ import annotations

from pyrogram import enums, raw, types, utils
from pyrogram.types.object import Object


class RequestedChat(Object):
    """Contains information about a requested chat.

    Parameters:
        chat_id (``int``):
            Identifier of the chat.

        chat_type (``enums.ChatType``):
            Type of the chat.

        name (``str``, *optional*):
            Name of the chat.

        username (``str``, *optional*):
            Username of the chat.

        photo (``types.Photo``, *optional*):
            Chat photo.
    """

    def __init__(
        self,
        chat_id: int,
        chat_type: enums.ChatType,
        name: str | None = None,
        username: str | None = None,
        photo: types.Photo | None = None,
    ) -> None:
        super().__init__()

        self.chat_id = chat_id
        self.chat_type = chat_type
        self.name = name
        self.username = username
        self.photo = photo

    @staticmethod
    async def _parse(
        client,
        request: raw.base.RequestedPeer | raw.base.Peer,
    ) -> RequestedChat:
        if isinstance(
            request,
            raw.types.RequestedPeerChannel | raw.types.PeerChannel,
        ):
            chat_type = enums.ChatType.CHANNEL
        else:
            chat_type = enums.ChatType.GROUP
        photo = None
        if getattr(request, "photo", None):
            photo = types.Photo._parse(client, getattr(request, "photo", None))

        return RequestedChat(
            chat_id=utils.get_channel_id(utils.get_raw_peer_id(request) or 0),
            chat_type=chat_type,
            name=getattr(request, "title", None),
            username=getattr(request, "username", None),
            photo=photo,
        )
