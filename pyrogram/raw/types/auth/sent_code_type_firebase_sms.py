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


class SentCodeTypeFirebaseSms(TLObject):  # type: ignore
    """An authentication code should be delivered via SMS after Firebase attestation, as described in the auth documentation ».

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``9FD736``

    Parameters:
        length (``int`` ``32-bit``):
            Length of the code that will be delivered.

        nonce (``bytes``, *optional*):
            On Android, the nonce to be used as described in the auth documentation »

        play_integrity_project_id (``int`` ``64-bit``, *optional*):
            N/A

        play_integrity_nonce (``bytes``, *optional*):


        receipt (``str``, *optional*):
            On iOS, must be compared with the receipt extracted from the received push notification.

        push_timeout (``int`` ``32-bit``, *optional*):
            On iOS: if a push notification with the ios_push_secret isn't received within push_timeout seconds, the next_type authentication method must be used, with auth.resendCode.

    """

    __slots__: List[str] = ["length", "nonce", "play_integrity_project_id", "play_integrity_nonce", "receipt", "push_timeout"]

    ID = 0x9fd736
    QUALNAME = "types.auth.SentCodeTypeFirebaseSms"

    def __init__(self, *, length: int, nonce: Optional[bytes] = None, play_integrity_project_id: Optional[int] = None, play_integrity_nonce: Optional[bytes] = None, receipt: Optional[str] = None, push_timeout: Optional[int] = None) -> None:
        self.length = length  # int
        self.nonce = nonce  # flags.0?bytes
        self.play_integrity_project_id = play_integrity_project_id  # flags.2?long
        self.play_integrity_nonce = play_integrity_nonce  # flags.2?bytes
        self.receipt = receipt  # flags.1?string
        self.push_timeout = push_timeout  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFirebaseSms":

        flags = Int.read(b)

        nonce = Bytes.read(b) if flags & (1 << 0) else None
        play_integrity_project_id = Long.read(b) if flags & (1 << 2) else None
        play_integrity_nonce = Bytes.read(b) if flags & (1 << 2) else None
        receipt = String.read(b) if flags & (1 << 1) else None
        push_timeout = Int.read(b) if flags & (1 << 1) else None
        length = Int.read(b)

        return SentCodeTypeFirebaseSms(length=length, nonce=nonce, play_integrity_project_id=play_integrity_project_id, play_integrity_nonce=play_integrity_nonce, receipt=receipt, push_timeout=push_timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.nonce is not None else 0
        flags |= (1 << 2) if self.play_integrity_project_id is not None else 0
        flags |= (1 << 2) if self.play_integrity_nonce is not None else 0
        flags |= (1 << 1) if self.receipt is not None else 0
        flags |= (1 << 1) if self.push_timeout is not None else 0
        b.write(Int(flags))

        if self.nonce is not None:
            b.write(Bytes(self.nonce))

        if self.play_integrity_project_id is not None:
            b.write(Long(self.play_integrity_project_id))

        if self.play_integrity_nonce is not None:
            b.write(Bytes(self.play_integrity_nonce))

        if self.receipt is not None:
            b.write(String(self.receipt))

        if self.push_timeout is not None:
            b.write(Int(self.push_timeout))

        b.write(Int(self.length))

        return b.getvalue()
