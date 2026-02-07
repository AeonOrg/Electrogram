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


class ChannelParticipantsNotModified(TLObject):  # type: ignore
    """No new participant info could be found

    Constructor of :obj:`~pyrogram.raw.base.channels.ChannelParticipants`.

    Details:
        - Layer: ``224``
        - ID: ``F0173FE9``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetParticipants
    """

    __slots__: List[str] = []

    ID = 0xf0173fe9
    QUALNAME = "types.channels.ChannelParticipantsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantsNotModified":
        # No flags

        return ChannelParticipantsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
