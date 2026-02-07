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


class BadServerSalt(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BadMsgNotification`.

    Details:
        - Layer: ``224``
        - ID: ``EDAB447B``

    Parameters:
        bad_msg_id (``int`` ``64-bit``):
            N/A

        bad_msg_seqno (``int`` ``32-bit``):
            N/A

        error_code (``int`` ``32-bit``):
            N/A

        new_server_salt (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["bad_msg_id", "bad_msg_seqno", "error_code", "new_server_salt"]

    ID = 0xedab447b
    QUALNAME = "types.BadServerSalt"

    def __init__(self, *, bad_msg_id: int, bad_msg_seqno: int, error_code: int, new_server_salt: int) -> None:
        self.bad_msg_id = bad_msg_id  # long
        self.bad_msg_seqno = bad_msg_seqno  # int
        self.error_code = error_code  # int
        self.new_server_salt = new_server_salt  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BadServerSalt":
        # No flags

        bad_msg_id = Long.read(b)

        bad_msg_seqno = Int.read(b)

        error_code = Int.read(b)

        new_server_salt = Long.read(b)

        return BadServerSalt(bad_msg_id=bad_msg_id, bad_msg_seqno=bad_msg_seqno, error_code=error_code, new_server_salt=new_server_salt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.bad_msg_id))

        b.write(Int(self.bad_msg_seqno))

        b.write(Int(self.error_code))

        b.write(Long(self.new_server_salt))

        return b.getvalue()
