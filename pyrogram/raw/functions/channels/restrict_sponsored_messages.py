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


class RestrictSponsoredMessages(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``9AE91519``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):


        restricted (``bool``):


    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "restricted"]

    ID = 0x9ae91519
    QUALNAME = "functions.channels.RestrictSponsoredMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", restricted: bool) -> None:
        self.channel = channel  # InputChannel
        self.restricted = restricted  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RestrictSponsoredMessages":
        # No flags

        channel = TLObject.read(b)

        restricted = Bool.read(b)

        return RestrictSponsoredMessages(channel=channel, restricted=restricted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Bool(self.restricted))

        return b.getvalue()
