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


class NewSessionCreated(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.NewSession`.

    Details:
        - Layer: ``224``
        - ID: ``9EC20908``

    Parameters:
        first_msg_id (``int`` ``64-bit``):
            N/A

        unique_id (``int`` ``64-bit``):
            N/A

        server_salt (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["first_msg_id", "unique_id", "server_salt"]

    ID = 0x9ec20908
    QUALNAME = "types.NewSessionCreated"

    def __init__(self, *, first_msg_id: int, unique_id: int, server_salt: int) -> None:
        self.first_msg_id = first_msg_id  # long
        self.unique_id = unique_id  # long
        self.server_salt = server_salt  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NewSessionCreated":
        # No flags

        first_msg_id = Long.read(b)

        unique_id = Long.read(b)

        server_salt = Long.read(b)

        return NewSessionCreated(first_msg_id=first_msg_id, unique_id=unique_id, server_salt=server_salt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.first_msg_id))

        b.write(Long(self.unique_id))

        b.write(Long(self.server_salt))

        return b.getvalue()
