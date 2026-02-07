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


class SetBotPrecheckoutResults(TLObject):  # type: ignore
    """Once the user has confirmed their payment and shipping details, the bot receives an updateBotPrecheckoutQuery update.
Use this method to respond to such pre-checkout queries.
Note: Telegram must receive an answer within 10 seconds after the pre-checkout query was sent.


    Details:
        - Layer: ``224``
        - ID: ``9C2DD95``

    Parameters:
        query_id (``int`` ``64-bit``):
            Unique identifier for the query to be answered

        success (``bool``, *optional*):
            Set this flag if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order, otherwise do not set it, and set the error field, instead

        error (``str``, *optional*):
            Required if the success isn't set. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "success", "error"]

    ID = 0x9c2dd95
    QUALNAME = "functions.messages.SetBotPrecheckoutResults"

    def __init__(self, *, query_id: int, success: Optional[bool] = None, error: Optional[str] = None) -> None:
        self.query_id = query_id  # long
        self.success = success  # flags.1?true
        self.error = error  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotPrecheckoutResults":

        flags = Int.read(b)

        success = True if flags & (1 << 1) else False
        query_id = Long.read(b)

        error = String.read(b) if flags & (1 << 0) else None
        return SetBotPrecheckoutResults(query_id=query_id, success=success, error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.success else 0
        flags |= (1 << 0) if self.error is not None else 0
        b.write(Int(flags))

        b.write(Long(self.query_id))

        if self.error is not None:
            b.write(String(self.error))

        return b.getvalue()
