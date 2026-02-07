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


class PremiumPromo(TLObject):  # type: ignore
    """Telegram Premium promotion information

    Constructor of :obj:`~pyrogram.raw.base.help.PremiumPromo`.

    Details:
        - Layer: ``224``
        - ID: ``5334759C``

    Parameters:
        status_text (``str``):
            Description of the current state of the user's Telegram Premium subscription

        status_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            Message entities for styled text

        video_sections (List of ``str``):
            A list of premium feature identifiers », associated to each video

        videos (List of :obj:`Document <pyrogram.raw.base.Document>`):
            A list of videos

        period_options (List of :obj:`PremiumSubscriptionOption <pyrogram.raw.base.PremiumSubscriptionOption>`):
            Telegram Premium subscription options

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Related user information

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPremiumPromo
    """

    __slots__: List[str] = ["status_text", "status_entities", "video_sections", "videos", "period_options", "users"]

    ID = 0x5334759c
    QUALNAME = "types.help.PremiumPromo"

    def __init__(self, *, status_text: str, status_entities: List["raw.base.MessageEntity"], video_sections: List[str], videos: List["raw.base.Document"], period_options: List["raw.base.PremiumSubscriptionOption"], users: List["raw.base.User"]) -> None:
        self.status_text = status_text  # string
        self.status_entities = status_entities  # Vector<MessageEntity>
        self.video_sections = video_sections  # Vector<string>
        self.videos = videos  # Vector<Document>
        self.period_options = period_options  # Vector<PremiumSubscriptionOption>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumPromo":
        # No flags

        status_text = String.read(b)

        status_entities = TLObject.read(b)

        video_sections = TLObject.read(b, String)

        videos = TLObject.read(b)

        period_options = TLObject.read(b)

        users = TLObject.read(b)

        return PremiumPromo(status_text=status_text, status_entities=status_entities, video_sections=video_sections, videos=videos, period_options=period_options, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.status_text))

        b.write(Vector(self.status_entities))

        b.write(Vector(self.video_sections, String))

        b.write(Vector(self.videos))

        b.write(Vector(self.period_options))

        b.write(Vector(self.users))

        return b.getvalue()
