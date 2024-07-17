from typing import Union, Optional, AsyncGenerator

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetChatJoinRequests:
    async def get_chat_join_requests(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        limit: int = 0,
        query: str = "",
    ) -> Optional[AsyncGenerator["types.ChatJoiner", None]]:
        current = 0
        total = abs(limit) or (1 << 31) - 1
        limit = min(100, total)

        offset_date = 0
        offset_user = raw.types.InputUserEmpty()

        while True:
            r = await self.invoke(
                raw.functions.messages.GetChatInviteImporters(
                    peer=await self.resolve_peer(chat_id),
                    limit=limit,
                    offset_date=offset_date,
                    offset_user=offset_user,
                    requested=True,
                    q=query,
                )
            )

            if not r.importers:
                break

            users = {i.id: i for i in r.users}

            offset_date = r.importers[-1].date
            offset_user = await self.resolve_peer(r.importers[-1].user_id)

            for i in r.importers:
                yield types.ChatJoiner._parse(self, i, users)

                current += 1

                if current >= total:
                    return
