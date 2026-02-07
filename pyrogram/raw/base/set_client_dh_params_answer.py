# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SetClientDHParamsAnswer = Union["raw.types.DhGenFail", "raw.types.DhGenOk", "raw.types.DhGenRetry"]


class SetClientDHParamsAnswer:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DhGenFail
            DhGenOk
            DhGenRetry

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            SetClientDHParams
    """

    QUALNAME = "pyrogram.raw.base.SetClientDHParamsAnswer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
