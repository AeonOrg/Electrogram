from typing import Union, AsyncGenerator, Optional

import pyrogram
from pyrogram import types, raw, utils


class GetChatPhotos:
    async def get_chat_photos(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        limit: int = 0,
    ) -> Optional[
        Union[
            AsyncGenerator["types.Photo", None], AsyncGenerator["types.Animation", None]
        ]
    ]:
        peer_id = await self.resolve_peer(chat_id)

        if isinstance(peer_id, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetFullChannel(channel=peer_id)
            )

            current = types.Photo._parse(self, r.full_chat.chat_photo) or []
            current = [current]
            current_animation = types.Animation._parse_chat_animation(
                self, r.full_chat.chat_photo
            )
            if current_animation:
                current = current + [current_animation]
            extra = []
            if not self.me.is_bot:
                r = await utils.parse_messages(
                    self,
                    await self.invoke(
                        raw.functions.messages.Search(
                            peer=peer_id,
                            q="",
                            filter=raw.types.InputMessagesFilterChatPhotos(),
                            min_date=0,
                            max_date=0,
                            offset_id=0,
                            add_offset=0,
                            limit=limit,
                            max_id=0,
                            min_id=0,
                            hash=0,
                        )
                    ),
                )

                extra = [message.new_chat_photo for message in r]

            if extra:
                if current:
                    photos = (
                        (current + extra)
                        if current[0].file_id != extra[0].file_id
                        else extra
                    )
                else:
                    photos = extra
            else:
                if current:
                    photos = current
                else:
                    photos = []

            current = 0

            for photo in photos:
                yield photo

                current += 1

                if current >= limit:
                    return
        else:
            current = 0
            total = limit or (1 << 31)
            limit = min(100, total)
            offset = 0

            while True:
                r = await self.invoke(
                    raw.functions.photos.GetUserPhotos(
                        user_id=peer_id, offset=offset, max_id=0, limit=limit
                    )
                )

                photos = []
                for photo in r.photos:
                    photos.append(types.Photo._parse(self, photo))
                    current_animation = types.Animation._parse_chat_animation(
                        self, photo
                    )
                    if current_animation:
                        photos.append(current_animation)

                if not photos:
                    return

                offset += len(photos)

                for photo in photos:
                    yield photo

                    current += 1

                    if current >= total:
                        return
