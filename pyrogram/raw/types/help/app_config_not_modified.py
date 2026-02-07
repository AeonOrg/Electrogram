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


class AppConfigNotModified(TLObject):  # type: ignore
    """The client configuration parameters haven't changed

    Constructor of :obj:`~pyrogram.raw.base.help.AppConfig`.

    Details:
        - Layer: ``224``
        - ID: ``7CDE641D``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppConfig
    """

    __slots__: List[str] = []

    ID = 0x7cde641d
    QUALNAME = "types.help.AppConfigNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppConfigNotModified":
        # No flags

        return AppConfigNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
