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


class GetNotifyExceptions(TLObject):  # type: ignore
    """Returns list of chats with non-default notification settings


    Details:
        - Layer: ``224``
        - ID: ``53577479``

    Parameters:
        compare_sound (``bool``, *optional*):
            If set, chats with non-default sound will be returned

        compare_stories (``bool``, *optional*):
            If set, chats with non-default notification settings for stories will be returned

        peer (:obj:`InputNotifyPeer <pyrogram.raw.base.InputNotifyPeer>`, *optional*):
            If specified, only chats of the specified category will be returned

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["compare_sound", "compare_stories", "peer"]

    ID = 0x53577479
    QUALNAME = "functions.account.GetNotifyExceptions"

    def __init__(self, *, compare_sound: Optional[bool] = None, compare_stories: Optional[bool] = None, peer: "raw.base.InputNotifyPeer" = None) -> None:
        self.compare_sound = compare_sound  # flags.1?true
        self.compare_stories = compare_stories  # flags.2?true
        self.peer = peer  # flags.0?InputNotifyPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNotifyExceptions":

        flags = Int.read(b)

        compare_sound = True if flags & (1 << 1) else False
        compare_stories = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 0) else None

        return GetNotifyExceptions(compare_sound=compare_sound, compare_stories=compare_stories, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.compare_sound else 0
        flags |= (1 << 2) if self.compare_stories else 0
        flags |= (1 << 0) if self.peer is not None else 0
        b.write(Int(flags))

        if self.peer is not None:
            b.write(self.peer.write())

        return b.getvalue()
