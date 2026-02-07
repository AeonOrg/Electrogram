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


class RequestFirebaseSms(TLObject):  # type: ignore
    """Request an SMS code via Firebase.


    Details:
        - Layer: ``224``
        - ID: ``8E39261E``

    Parameters:
        phone_number (``str``):
            Phone number

        phone_code_hash (``str``):
            Phone code hash returned by auth.sendCode

        safety_net_token (``str``, *optional*):
            On Android, a JWS object obtained as described in the auth documentation »

        play_integrity_token (``str``, *optional*):


        ios_push_secret (``str``, *optional*):
            Secret token received via an apple push notification

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "safety_net_token", "play_integrity_token", "ios_push_secret"]

    ID = 0x8e39261e
    QUALNAME = "functions.auth.RequestFirebaseSms"

    def __init__(self, *, phone_number: str, phone_code_hash: str, safety_net_token: Optional[str] = None, play_integrity_token: Optional[str] = None, ios_push_secret: Optional[str] = None) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.safety_net_token = safety_net_token  # flags.0?string
        self.play_integrity_token = play_integrity_token  # flags.2?string
        self.ios_push_secret = ios_push_secret  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestFirebaseSms":

        flags = Int.read(b)

        phone_number = String.read(b)

        phone_code_hash = String.read(b)

        safety_net_token = String.read(b) if flags & (1 << 0) else None
        play_integrity_token = String.read(b) if flags & (1 << 2) else None
        ios_push_secret = String.read(b) if flags & (1 << 1) else None
        return RequestFirebaseSms(phone_number=phone_number, phone_code_hash=phone_code_hash, safety_net_token=safety_net_token, play_integrity_token=play_integrity_token, ios_push_secret=ios_push_secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.safety_net_token is not None else 0
        flags |= (1 << 2) if self.play_integrity_token is not None else 0
        flags |= (1 << 1) if self.ios_push_secret is not None else 0
        b.write(Int(flags))

        b.write(String(self.phone_number))

        b.write(String(self.phone_code_hash))

        if self.safety_net_token is not None:
            b.write(String(self.safety_net_token))

        if self.play_integrity_token is not None:
            b.write(String(self.play_integrity_token))

        if self.ios_push_secret is not None:
            b.write(String(self.ios_push_secret))

        return b.getvalue()
