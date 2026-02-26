from __future__ import annotations

from typing import Any, cast

from .object import Object


class List(list):
    __slots__ = []

    def __str__(self) -> str:
        # noinspection PyCallByClass
        return Object.__str__(cast(Any, self))

    def __repr__(self) -> str:
        return f"pyrogram.types.List([{','.join(Object.__repr__(i) for i in self)}])"
