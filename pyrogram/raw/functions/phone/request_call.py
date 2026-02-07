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


class RequestCall(TLObject):  # type: ignore
    """Start a telegram phone call


    Details:
        - Layer: ``224``
        - ID: ``42FF96ED``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Destination of the phone call

        random_id (``int`` ``32-bit``):
            Random ID to avoid resending the same object

        g_a_hash (``bytes``):
            Parameter for E2E encryption key exchange »

        protocol (:obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`):
            Phone call settings

        video (``bool``, *optional*):
            Whether to start a video call

    Returns:
        :obj:`phone.PhoneCall <pyrogram.raw.base.phone.PhoneCall>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a_hash", "protocol", "video"]

    ID = 0x42ff96ed
    QUALNAME = "functions.phone.RequestCall"

    def __init__(self, *, user_id: "raw.base.InputUser", random_id: int, g_a_hash: bytes, protocol: "raw.base.PhoneCallProtocol", video: Optional[bool] = None) -> None:
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a_hash = g_a_hash  # bytes
        self.protocol = protocol  # PhoneCallProtocol
        self.video = video  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestCall":

        flags = Int.read(b)

        video = True if flags & (1 << 0) else False
        user_id = TLObject.read(b)

        random_id = Int.read(b)

        g_a_hash = Bytes.read(b)

        protocol = TLObject.read(b)

        return RequestCall(user_id=user_id, random_id=random_id, g_a_hash=g_a_hash, protocol=protocol, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))

        b.write(self.user_id.write())

        b.write(Int(self.random_id))

        b.write(Bytes(self.g_a_hash))

        b.write(self.protocol.write())

        return b.getvalue()
