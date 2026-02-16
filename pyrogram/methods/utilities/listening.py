from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import filters


class Listening:
    async def listen(
        self: pyrogram.Client,
        chat_id: int | str,
        filters: filters.Filter | None = None,
        timeout: int | None = None,
        *args,
        **kwargs,
    ):
        """Wait for a new message in a chat."""
        return await self.wait_for_message(chat_id, filters, timeout)

    async def wait_for_message(
        self: pyrogram.Client,
        chat_id: int | str,
        filters: filters.Filter | None = None,
        timeout: int | None = None,
    ):
        """Wait for a new message in a chat."""
        # This is a stub to satisfy type checker and provide missing functionality
        # In a real implementation, this would interact with self.dispatcher
        raise NotImplementedError("Listening is not implemented in this fork yet.")

    async def ask(
        self: pyrogram.Client,
        chat_id: int | str,
        text: str,
        filters: filters.Filter | None = None,
        timeout: int | None = None,
        *args,
        **kwargs,
    ):
        """Send a message and wait for a reply."""
        await self.send_message(chat_id, text, *args, **kwargs)
        return await self.listen(chat_id, filters, timeout)

    async def stop_listening(
        self: pyrogram.Client,
        chat_id: int | str,
        *args,
        **kwargs,
    ):
        """Stop listening for messages in a chat."""
        raise NotImplementedError("Listening is not implemented in this fork yet.")
