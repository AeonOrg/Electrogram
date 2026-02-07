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


class InputCollectibleUsername(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.InputCollectible`.

    Details:
        - Layer: ``224``
        - ID: ``E39460A9``

    Parameters:
        username (``str``):


    """

    __slots__: List[str] = ["username"]

    ID = 0xe39460a9
    QUALNAME = "types.InputCollectibleUsername"

    def __init__(self, *, username: str) -> None:
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputCollectibleUsername":
        # No flags

        username = String.read(b)

        return InputCollectibleUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.username))

        return b.getvalue()
