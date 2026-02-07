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


class ChannelDifferenceTooLong(TLObject):  # type: ignore
    """The provided pts + limit < remote pts. Simply, there are too many updates to be fetched (more than limit), the client has to resolve the update gap in one of the following ways (assuming the existence of a persistent database to locally store messages):

    Constructor of :obj:`~pyrogram.raw.base.updates.ChannelDifference`.

    Details:
        - Layer: ``224``
        - ID: ``A4BCC6FE``

    Parameters:
        dialog (:obj:`Dialog <pyrogram.raw.base.Dialog>`):
            Dialog containing the latest PTS that can be used to reset the channel state

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            The latest messages

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats from messages

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users from messages

        final (``bool``, *optional*):
            Whether there are more updates that must be fetched (always false)

        timeout (``int`` ``32-bit``, *optional*):
            Clients are supposed to refetch the channel difference after timeout seconds have elapsed

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetChannelDifference
    """

    __slots__: List[str] = ["dialog", "messages", "chats", "users", "final", "timeout"]

    ID = 0xa4bcc6fe
    QUALNAME = "types.updates.ChannelDifferenceTooLong"

    def __init__(self, *, dialog: "raw.base.Dialog", messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"], final: Optional[bool] = None, timeout: Optional[int] = None) -> None:
        self.dialog = dialog  # Dialog
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.final = final  # flags.0?true
        self.timeout = timeout  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelDifferenceTooLong":

        flags = Int.read(b)

        final = True if flags & (1 << 0) else False
        timeout = Int.read(b) if flags & (1 << 1) else None
        dialog = TLObject.read(b)

        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return ChannelDifferenceTooLong(dialog=dialog, messages=messages, chats=chats, users=users, final=final, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final else 0
        flags |= (1 << 1) if self.timeout is not None else 0
        b.write(Int(flags))

        if self.timeout is not None:
            b.write(Int(self.timeout))

        b.write(self.dialog.write())

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
