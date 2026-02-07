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


class InputTakeoutFileLocation(TLObject):  # type: ignore
    """Used to download a JSON file that will contain all personal data related to features that do not have a specialized takeout method yet, see here » for more info on the takeout API.

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``29BE5899``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x29be5899
    QUALNAME = "types.InputTakeoutFileLocation"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputTakeoutFileLocation":
        # No flags

        return InputTakeoutFileLocation()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
