from __future__ import annotations

from pyrogram import raw, types
from pyrogram.types.object import Object


class FactCheck(Object):
    """A fact-check.

    Parameters:
        need_check (``bool``):
            True, if the message needs to be fact-checked.

        country (``str``, *optional*):
            ISO 3166-1 alpha-2 country code for which the fact-check is relevant.

        text (:obj:`~pyrogram.types.TextWithEntities`, *optional*):
            Fact-check text.

        hash (``int``):
            Fact-check hash.
    """

    def __init__(
        self,
        *,
        need_check: bool,
        country: str | None = None,
        text: types.TextWithEntities | None = None,
        hash: int,
    ) -> None:
        super().__init__(None)

        self.need_check = need_check
        self.country = country
        self.text = text
        self.hash = hash

    @staticmethod
    def _parse(client, fact_check: raw.types.FactCheck | None) -> FactCheck | None:
        if not fact_check:
            return None

        return FactCheck(
            need_check=fact_check.need_check,
            country=fact_check.country,
            text=types.TextWithEntities(
                text=fact_check.text.text,
                entities=types.List(
                    [
                        types.MessageEntity._parse(client, entity, {})
                        for entity in fact_check.text.entities
                    ],
                ),
            )
            if fact_check.text
            else None,
            hash=fact_check.hash,
        )
