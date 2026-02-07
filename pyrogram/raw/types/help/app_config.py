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


class AppConfig(TLObject):  # type: ignore
    """Contains various client configuration parameters

    Constructor of :obj:`~pyrogram.raw.base.help.AppConfig`.

    Details:
        - Layer: ``224``
        - ID: ``DD18782E``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        config (:obj:`JSONValue <pyrogram.raw.base.JSONValue>`):
            Client configuration parameters

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppConfig
    """

    __slots__: List[str] = ["hash", "config"]

    ID = 0xdd18782e
    QUALNAME = "types.help.AppConfig"

    def __init__(self, *, hash: int, config: "raw.base.JSONValue") -> None:
        self.hash = hash  # int
        self.config = config  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppConfig":
        # No flags

        hash = Int.read(b)

        config = TLObject.read(b)

        return AppConfig(hash=hash, config=config)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        b.write(self.config.write())

        return b.getvalue()
