from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class LangPackStringPluralized(TLObject):  # type: ignore
    """A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info

    Constructor of :obj:`~pyrogram.raw.base.LangPackString`.

    Details:
        - Layer: ``224``
        - ID: ``6C47AC9F``

    Parameters:
        key (``str``):
            Localization key

        other_value (``str``):
            Default value

        zero_value (``str``, *optional*):
            Value for zero objects

        one_value (``str``, *optional*):
            Value for one object

        two_value (``str``, *optional*):
            Value for two objects

        few_value (``str``, *optional*):
            Value for a few objects

        many_value (``str``, *optional*):
            Value for many objects

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetStrings
    """

    __slots__: List[str] = ["key", "other_value", "zero_value", "one_value", "two_value", "few_value", "many_value"]

    ID = 0x6c47ac9f
    QUALNAME = "types.LangPackStringPluralized"

    def __init__(self, *, key: str, other_value: str, zero_value: Optional[str] = None, one_value: Optional[str] = None, two_value: Optional[str] = None, few_value: Optional[str] = None, many_value: Optional[str] = None) -> None:
        self.key = key  # string
        self.other_value = other_value  # string
        self.zero_value = zero_value  # flags.0?string
        self.one_value = one_value  # flags.1?string
        self.two_value = two_value  # flags.2?string
        self.few_value = few_value  # flags.3?string
        self.many_value = many_value  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackStringPluralized":

        flags = Int.read(b)

        key = String.read(b)

        zero_value = String.read(b) if flags & (1 << 0) else None
        one_value = String.read(b) if flags & (1 << 1) else None
        two_value = String.read(b) if flags & (1 << 2) else None
        few_value = String.read(b) if flags & (1 << 3) else None
        many_value = String.read(b) if flags & (1 << 4) else None
        other_value = String.read(b)

        return LangPackStringPluralized(key=key, other_value=other_value, zero_value=zero_value, one_value=one_value, two_value=two_value, few_value=few_value, many_value=many_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zero_value is not None else 0
        flags |= (1 << 1) if self.one_value is not None else 0
        flags |= (1 << 2) if self.two_value is not None else 0
        flags |= (1 << 3) if self.few_value is not None else 0
        flags |= (1 << 4) if self.many_value is not None else 0
        b.write(Int(flags))

        b.write(String(self.key))

        if self.zero_value is not None:
            b.write(String(self.zero_value))

        if self.one_value is not None:
            b.write(String(self.one_value))

        if self.two_value is not None:
            b.write(String(self.two_value))

        if self.few_value is not None:
            b.write(String(self.few_value))

        if self.many_value is not None:
            b.write(String(self.many_value))

        b.write(String(self.other_value))

        return b.getvalue()
