from __future__ import annotations

from typing import overload

import pyrogram
from pyrogram import enums

from .html import HTML
from .markdown import Markdown


class Parser:
    def __init__(self, client: pyrogram.Client | None) -> None:
        self.client = client
        self.html = HTML(client)
        self.markdown = Markdown(client)

    @overload
    async def parse(
        self,
        text: str,
        mode: enums.ParseMode | str | None = None,
    ) -> dict[str, str | list[pyrogram.raw.base.MessageEntity] | None]: ...

    @overload
    async def parse(
        self,
        text: None,
        mode: enums.ParseMode | str | None = None,
    ) -> dict[str, str | list[pyrogram.raw.base.MessageEntity] | None]: ...

    async def parse(
        self,
        text: str | None,
        mode: enums.ParseMode | str | None = None,
    ) -> dict[str, str | list[pyrogram.raw.base.MessageEntity] | None]:
        text = str(text or "").strip()

        if mode is None:
            mode = self.client.parse_mode if self.client else enums.ParseMode.DEFAULT

        if mode == enums.ParseMode.DEFAULT:
            return await self.markdown.parse(text)

        if mode == enums.ParseMode.MARKDOWN:
            return await self.markdown.parse(text, True)

        if mode == enums.ParseMode.HTML:
            return await self.html.parse(text)

        if mode == enums.ParseMode.DISABLED:
            return {"message": text, "entities": None}

        raise ValueError(f'Invalid parse mode "{mode}"')

    @staticmethod
    def unparse(text: str, entities: list, is_html: bool):
        if is_html:
            return HTML.unparse(text, entities)
        return Markdown.unparse(text, entities)
