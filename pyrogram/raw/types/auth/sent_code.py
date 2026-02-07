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


class SentCode(TLObject):  # type: ignore
    """Contains info about a sent verification code.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``224``
        - ID: ``5E002502``

    Parameters:
        type (:obj:`auth.SentCodeType <pyrogram.raw.base.auth.SentCodeType>`):
            Phone code type

        phone_code_hash (``str``):
            Phone code hash, to be stored and later re-used with auth.signIn

        next_type (:obj:`auth.CodeType <pyrogram.raw.base.auth.CodeType>`, *optional*):
            Phone code type that will be sent next, if the phone code is not received within timeout seconds: to send it use auth.resendCode

        timeout (``int`` ``32-bit``, *optional*):
            Timeout for reception of the phone code

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    __slots__: List[str] = ["type", "phone_code_hash", "next_type", "timeout"]

    ID = 0x5e002502
    QUALNAME = "types.auth.SentCode"

    def __init__(self, *, type: "raw.base.auth.SentCodeType", phone_code_hash: str, next_type: "raw.base.auth.CodeType" = None, timeout: Optional[int] = None) -> None:
        self.type = type  # auth.SentCodeType
        self.phone_code_hash = phone_code_hash  # string
        self.next_type = next_type  # flags.1?auth.CodeType
        self.timeout = timeout  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCode":

        flags = Int.read(b)

        type = TLObject.read(b)

        phone_code_hash = String.read(b)

        next_type = TLObject.read(b) if flags & (1 << 1) else None

        timeout = Int.read(b) if flags & (1 << 2) else None
        return SentCode(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.next_type is not None else 0
        flags |= (1 << 2) if self.timeout is not None else 0
        b.write(Int(flags))

        b.write(self.type.write())

        b.write(String(self.phone_code_hash))

        if self.next_type is not None:
            b.write(self.next_type.write())

        if self.timeout is not None:
            b.write(Int(self.timeout))

        return b.getvalue()
