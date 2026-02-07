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


class SetReactionsNotifySettings(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``316CE548``

    Parameters:
        settings (:obj:`ReactionsNotifySettings <pyrogram.raw.base.ReactionsNotifySettings>`):


    Returns:
        :obj:`ReactionsNotifySettings <pyrogram.raw.base.ReactionsNotifySettings>`
    """

    __slots__: List[str] = ["settings"]

    ID = 0x316ce548
    QUALNAME = "functions.account.SetReactionsNotifySettings"

    def __init__(self, *, settings: "raw.base.ReactionsNotifySettings") -> None:
        self.settings = settings  # ReactionsNotifySettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetReactionsNotifySettings":
        # No flags

        settings = TLObject.read(b)

        return SetReactionsNotifySettings(settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.settings.write())

        return b.getvalue()
