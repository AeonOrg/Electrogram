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


class ConnectedBot(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.ConnectedBot`.

    Details:
        - Layer: ``224``
        - ID: ``CD64636C``

    Parameters:
        bot_id (``int`` ``64-bit``):


        recipients (:obj:`BusinessBotRecipients <pyrogram.raw.base.BusinessBotRecipients>`):


        rights (:obj:`BusinessBotRights <pyrogram.raw.base.BusinessBotRights>`):
            N/A

    """

    __slots__: List[str] = ["bot_id", "recipients", "rights"]

    ID = 0xcd64636c
    QUALNAME = "types.ConnectedBot"

    def __init__(self, *, bot_id: int, recipients: "raw.base.BusinessBotRecipients", rights: "raw.base.BusinessBotRights") -> None:
        self.bot_id = bot_id  # long
        self.recipients = recipients  # BusinessBotRecipients
        self.rights = rights  # BusinessBotRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedBot":

        flags = Int.read(b)

        bot_id = Long.read(b)

        recipients = TLObject.read(b)

        rights = TLObject.read(b)

        return ConnectedBot(bot_id=bot_id, recipients=recipients, rights=rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0

        b.write(Int(flags))

        b.write(Long(self.bot_id))

        b.write(self.recipients.write())

        b.write(self.rights.write())

        return b.getvalue()
