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


class UpdateSmsJob(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F16269D4``

    Parameters:
        job_id (``str``):


    """

    __slots__: List[str] = ["job_id"]

    ID = 0xf16269d4
    QUALNAME = "types.UpdateSmsJob"

    def __init__(self, *, job_id: str) -> None:
        self.job_id = job_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSmsJob":
        # No flags

        job_id = String.read(b)

        return UpdateSmsJob(job_id=job_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.job_id))

        return b.getvalue()
