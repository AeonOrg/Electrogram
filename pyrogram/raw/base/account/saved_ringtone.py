# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedRingtone = Union["raw.types.account.SavedRingtone", "raw.types.account.SavedRingtoneConverted"]


class SavedRingtone:  # type: ignore
    """Contains information about a saved notification sound

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.SavedRingtone
            account.SavedRingtoneConverted

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.SaveRingtone
    """

    QUALNAME = "pyrogram.raw.base.account.SavedRingtone"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
