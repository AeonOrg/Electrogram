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


class GetParticipants(TLObject):  # type: ignore
    """Get the participants of a supergroup/channel


    Details:
        - Layer: ``224``
        - ID: ``77CED9D0``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel

        filter (:obj:`ChannelParticipantsFilter <pyrogram.raw.base.ChannelParticipantsFilter>`):
            Which participant types to fetch

        offset (``int`` ``32-bit``):
            Offset

        limit (``int`` ``32-bit``):
            Limit

        hash (``int`` ``64-bit``):
            Hash

    Returns:
        :obj:`channels.ChannelParticipants <pyrogram.raw.base.channels.ChannelParticipants>`
    """

    __slots__: List[str] = ["channel", "filter", "offset", "limit", "hash"]

    ID = 0x77ced9d0
    QUALNAME = "functions.channels.GetParticipants"

    def __init__(self, *, channel: "raw.base.InputChannel", filter: "raw.base.ChannelParticipantsFilter", offset: int, limit: int, hash: int) -> None:
        self.channel = channel  # InputChannel
        self.filter = filter  # ChannelParticipantsFilter
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetParticipants":
        # No flags

        channel = TLObject.read(b)

        filter = TLObject.read(b)

        offset = Int.read(b)

        limit = Int.read(b)

        hash = Long.read(b)

        return GetParticipants(channel=channel, filter=filter, offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.filter.write())

        b.write(Int(self.offset))

        b.write(Int(self.limit))

        b.write(Long(self.hash))

        return b.getvalue()
