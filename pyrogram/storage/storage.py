from __future__ import annotations

import base64
import struct
from abc import ABC, abstractmethod
from typing import Any, NoReturn


class Storage(ABC):
    OLD_SESSION_STRING_FORMAT = ">B?256sI?"
    OLD_SESSION_STRING_FORMAT_64 = ">B?256sQ?"
    SESSION_STRING_SIZE = 351
    SESSION_STRING_SIZE_64 = 356

    SESSION_STRING_FORMAT = ">BI?256sQ?"

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    async def open(self) -> None:
        """Opens the storage engine."""
        raise NotImplementedError

    @abstractmethod
    async def save(self) -> None:
        """Saves the current state of the storage engine."""
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        """Closes the storage engine."""
        raise NotImplementedError

    @abstractmethod
    async def delete(self) -> None:
        """Deletes the storage."""
        raise NotImplementedError

    @abstractmethod
    async def update_peers(
        self,
        peers: list[tuple[int, int, str, str | None, str | None]],
    ) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update_usernames(
        self,
        usernames: list[tuple[int, str]],
    ) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update_state(
        self,
        update_state: Any = object,
    ) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_peer_by_id(self, peer_id: int | str) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_peer_by_username(self, username: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_peer_by_phone_number(self, phone_number: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def dc_id(self, value: Any = object) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def api_id(self, value: Any = object) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def test_mode(self, value: Any = object) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def auth_key(self, value: Any = object) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def date(self, value: Any = object) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def user_id(self, value: Any = object) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def is_bot(self, value: Any = object) -> Any:
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
