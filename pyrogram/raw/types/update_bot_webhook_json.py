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


class UpdateBotWebhookJSON(TLObject):  # type: ignore
    """A new incoming event; for bots only

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8317C0C3``

    Parameters:
        data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            The event

    """

    __slots__: List[str] = ["data"]

    ID = 0x8317c0c3
    QUALNAME = "types.UpdateBotWebhookJSON"

    def __init__(self, *, data: "raw.base.DataJSON") -> None:
        self.data = data  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotWebhookJSON":
        # No flags

        data = TLObject.read(b)

        return UpdateBotWebhookJSON(data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.data.write())

        return b.getvalue()
