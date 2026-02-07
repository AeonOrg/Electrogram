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


class LangPackLanguage(TLObject):  # type: ignore
    """Identifies a localization pack

    Constructor of :obj:`~pyrogram.raw.base.LangPackLanguage`.

    Details:
        - Layer: ``224``
        - ID: ``EECA5CE3``

    Parameters:
        name (``str``):
            Language name

        native_name (``str``):
            Language name in the language itself

        lang_code (``str``):
            Language code (pack identifier)

        plural_code (``str``):
            A language code to be used to apply plural forms. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info

        strings_count (``int`` ``32-bit``):
            Total number of non-deleted strings from the language pack

        translated_count (``int`` ``32-bit``):
            Total number of translated strings from the language pack

        translations_url (``str``):
            Link to language translation interface; empty for custom local language packs

        official (``bool``, *optional*):
            Whether the language pack is official

        rtl (``bool``, *optional*):
            Is this a localization pack for an RTL language

        beta (``bool``, *optional*):
            Is this a beta localization pack?

        base_lang_code (``str``, *optional*):
            Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it should be fetched from base language pack. Unsupported in custom language packs

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetLanguages
            langpack.GetLanguage
    """

    __slots__: List[str] = ["name", "native_name", "lang_code", "plural_code", "strings_count", "translated_count", "translations_url", "official", "rtl", "beta", "base_lang_code"]

    ID = 0xeeca5ce3
    QUALNAME = "types.LangPackLanguage"

    def __init__(self, *, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int, translated_count: int, translations_url: str, official: Optional[bool] = None, rtl: Optional[bool] = None, beta: Optional[bool] = None, base_lang_code: Optional[str] = None) -> None:
        self.name = name  # string
        self.native_name = native_name  # string
        self.lang_code = lang_code  # string
        self.plural_code = plural_code  # string
        self.strings_count = strings_count  # int
        self.translated_count = translated_count  # int
        self.translations_url = translations_url  # string
        self.official = official  # flags.0?true
        self.rtl = rtl  # flags.2?true
        self.beta = beta  # flags.3?true
        self.base_lang_code = base_lang_code  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackLanguage":

        flags = Int.read(b)

        official = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 2) else False
        beta = True if flags & (1 << 3) else False
        name = String.read(b)

        native_name = String.read(b)

        lang_code = String.read(b)

        base_lang_code = String.read(b) if flags & (1 << 1) else None
        plural_code = String.read(b)

        strings_count = Int.read(b)

        translated_count = Int.read(b)

        translations_url = String.read(b)

        return LangPackLanguage(name=name, native_name=native_name, lang_code=lang_code, plural_code=plural_code, strings_count=strings_count, translated_count=translated_count, translations_url=translations_url, official=official, rtl=rtl, beta=beta, base_lang_code=base_lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.official else 0
        flags |= (1 << 2) if self.rtl else 0
        flags |= (1 << 3) if self.beta else 0
        flags |= (1 << 1) if self.base_lang_code is not None else 0
        b.write(Int(flags))

        b.write(String(self.name))

        b.write(String(self.native_name))

        b.write(String(self.lang_code))

        if self.base_lang_code is not None:
            b.write(String(self.base_lang_code))

        b.write(String(self.plural_code))

        b.write(Int(self.strings_count))

        b.write(Int(self.translated_count))

        b.write(String(self.translations_url))

        return b.getvalue()
