# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MsgResendReq = Union["raw.types.MsgResendAnsReq", "raw.types.MsgResendReq"]


class MsgResendReq:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MsgResendAnsReq
            MsgResendReq
    """

    QUALNAME = "pyrogram.raw.base.MsgResendReq"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
