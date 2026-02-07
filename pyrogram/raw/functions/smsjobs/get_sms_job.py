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


class GetSmsJob(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``778D902F``

    Parameters:
        job_id (``str``):


    Returns:
        :obj:`SmsJob <pyrogram.raw.base.SmsJob>`
    """

    __slots__: List[str] = ["job_id"]

    ID = 0x778d902f
    QUALNAME = "functions.smsjobs.GetSmsJob"

    def __init__(self, *, job_id: str) -> None:
        self.job_id = job_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSmsJob":
        # No flags

        job_id = String.read(b)

        return GetSmsJob(job_id=job_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.job_id))

        return b.getvalue()
