from __future__ import annotations

from typing import cast

from .object import Object


class List(list):
    __slots__ = []

    def __str__(self) -> str:
        return Object.__str__(cast(Object, self))

    def __repr__(self) -> str:
        return f"pyrogram.types.List([{','.join(repr(i) for i in self)}])"
