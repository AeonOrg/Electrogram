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


class DropTempAuthKeys(TLObject):  # type: ignore
    """Delete all temporary authorization keys except for the ones specified


    Details:
        - Layer: ``224``
        - ID: ``8E48A188``

    Parameters:
        except_auth_keys (List of ``int`` ``64-bit``):
            The auth keys that shouldn't be dropped.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["except_auth_keys"]

    ID = 0x8e48a188
    QUALNAME = "functions.auth.DropTempAuthKeys"

    def __init__(self, *, except_auth_keys: List[int]) -> None:
        self.except_auth_keys = except_auth_keys  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DropTempAuthKeys":
        # No flags

        except_auth_keys = TLObject.read(b, Long)

        return DropTempAuthKeys(except_auth_keys=except_auth_keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.except_auth_keys, Long))

        return b.getvalue()
