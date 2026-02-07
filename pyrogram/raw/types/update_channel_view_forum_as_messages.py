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


class UpdateChannelViewForumAsMessages(TLObject):  # type: ignore
    """Users may also choose to display messages from all topics as if they were sent to a normal group, using a "View as messages" setting in the local client.
This setting only affects the current account, and is synced to other logged in sessions using the channels.toggleViewForumAsMessages method; invoking this method will update the value of the view_forum_as_messages flag of channelFull or dialog and emit an updateChannelViewForumAsMessages.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7B68920``

    Parameters:
        channel_id (``int`` ``64-bit``):
            The forum ID

        enabled (``bool``):
            The new value of the toggle.

    """

    __slots__: List[str] = ["channel_id", "enabled"]

    ID = 0x7b68920
    QUALNAME = "types.UpdateChannelViewForumAsMessages"

    def __init__(self, *, channel_id: int, enabled: bool) -> None:
        self.channel_id = channel_id  # long
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelViewForumAsMessages":
        # No flags

        channel_id = Long.read(b)

        enabled = Bool.read(b)

        return UpdateChannelViewForumAsMessages(channel_id=channel_id, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Bool(self.enabled))

        return b.getvalue()
