import base64
import struct
from abc import abstractmethod
from typing import List, Tuple


class Storage:
    OLD_SESSION_STRING_FORMAT = ">B?256sI?"
    OLD_SESSION_STRING_FORMAT_64 = ">B?256sQ?"
    SESSION_STRING_SIZE = 351
    SESSION_STRING_SIZE_64 = 356

    SESSION_STRING_FORMAT = ">BI?256sQ?"

    def __init__(self, name: str):
        self.name = name

    async def open(self):
        raise NotImplementedError

    async def save(self):
        raise NotImplementedError

    async def close(self):
        raise NotImplementedError

    async def delete(self):
        raise NotImplementedError

    async def update_peers(self, peers: list[tuple[int, int, str, str, str]]):
        raise NotImplementedError

    async def update_usernames(self, usernames: list[tuple[int, str]]):
        raise NotImplementedError

    @abstractmethod
    async def update_state(self, update_state: tuple[int, int, int, int, int] = object):
        """Get or set the update state of the current session.

        Parameters:
            update_state (``tuple[int, int, int, int, int]``): A tuple containing the update state to set.
                Tuple must contain the following information:
                - ``int``: The id of the entity.
                - ``int``: The pts.
                - ``int``: The qts.
                - ``int``: The date.
                - ``int``: The seq.
        """
        raise NotImplementedError

    async def get_peer_by_id(self, peer_id: int):
        raise NotImplementedError

    async def get_peer_by_username(self, username: str):
        raise NotImplementedError

    async def get_peer_by_phone_number(self, phone_number: str):
        raise NotImplementedError

    async def dc_id(self, value: int = object):
        raise NotImplementedError

    async def api_id(self, value: int = object):
        raise NotImplementedError

    async def test_mode(self, value: bool = object):
        raise NotImplementedError

    async def auth_key(self, value: bytes = object):
        raise NotImplementedError

    async def date(self, value: int = object):
        raise NotImplementedError

    async def user_id(self, value: int = object):
        raise NotImplementedError

    async def is_bot(self, value: bool = object):
        raise NotImplementedError

    async def export_session_string(self):
        packed = struct.pack(
            self.SESSION_STRING_FORMAT,
            await self.dc_id(),
            await self.api_id(),
            await self.test_mode(),
            await self.auth_key(),
            await self.user_id(),
            await self.is_bot(),
        )

        return base64.urlsafe_b64encode(packed).decode().rstrip("=")
