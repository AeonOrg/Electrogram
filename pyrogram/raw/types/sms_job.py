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


class SmsJob(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.SmsJob`.

    Details:
        - Layer: ``224``
        - ID: ``E6A1EEB8``

    Parameters:
        job_id (``str``):


        phone_number (``str``):


        text (``str``):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            smsjobs.GetSmsJob
    """

    __slots__: List[str] = ["job_id", "phone_number", "text"]

    ID = 0xe6a1eeb8
    QUALNAME = "types.SmsJob"

    def __init__(self, *, job_id: str, phone_number: str, text: str) -> None:
        self.job_id = job_id  # string
        self.phone_number = phone_number  # string
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SmsJob":
        # No flags

        job_id = String.read(b)

        phone_number = String.read(b)

        text = String.read(b)

        return SmsJob(job_id=job_id, phone_number=phone_number, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.job_id))

        b.write(String(self.phone_number))

        b.write(String(self.text))

        return b.getvalue()
