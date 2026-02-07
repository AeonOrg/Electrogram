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


class ChangeAuthorizationSettings(TLObject):  # type: ignore
    """Change settings related to a session.


    Details:
        - Layer: ``224``
        - ID: ``40F48462``

    Parameters:
        hash (``int`` ``64-bit``):
            Session ID from the authorization constructor, fetchable using account.getAuthorizations

        confirmed (``bool``, *optional*):
            If set, confirms a newly logged in session ».

        encrypted_requests_disabled (``bool``, *optional*):
            Whether to enable or disable receiving encrypted chats: if the flag is not set, the previous setting is not changed

        call_requests_disabled (``bool``, *optional*):
            Whether to enable or disable receiving calls: if the flag is not set, the previous setting is not changed

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hash", "confirmed", "encrypted_requests_disabled", "call_requests_disabled"]

    ID = 0x40f48462
    QUALNAME = "functions.account.ChangeAuthorizationSettings"

    def __init__(self, *, hash: int, confirmed: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None) -> None:
        self.hash = hash  # long
        self.confirmed = confirmed  # flags.3?true
        self.encrypted_requests_disabled = encrypted_requests_disabled  # flags.0?Bool
        self.call_requests_disabled = call_requests_disabled  # flags.1?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeAuthorizationSettings":

        flags = Int.read(b)

        confirmed = True if flags & (1 << 3) else False
        hash = Long.read(b)

        encrypted_requests_disabled = Bool.read(b) if flags & (1 << 0) else None
        call_requests_disabled = Bool.read(b) if flags & (1 << 1) else None
        return ChangeAuthorizationSettings(hash=hash, confirmed=confirmed, encrypted_requests_disabled=encrypted_requests_disabled, call_requests_disabled=call_requests_disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.confirmed else 0
        flags |= (1 << 0) if self.encrypted_requests_disabled is not None else 0
        flags |= (1 << 1) if self.call_requests_disabled is not None else 0
        b.write(Int(flags))

        b.write(Long(self.hash))

        if self.encrypted_requests_disabled is not None:
            b.write(Bool(self.encrypted_requests_disabled))

        if self.call_requests_disabled is not None:
            b.write(Bool(self.call_requests_disabled))

        return b.getvalue()
