# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BusinessAwayMessageSchedule = Union["raw.types.BusinessAwayMessageScheduleAlways", "raw.types.BusinessAwayMessageScheduleCustom", "raw.types.BusinessAwayMessageScheduleOutsideWorkHours"]


class BusinessAwayMessageSchedule:  # type: ignore
    """

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BusinessAwayMessageScheduleAlways
            BusinessAwayMessageScheduleCustom
            BusinessAwayMessageScheduleOutsideWorkHours
    """

    QUALNAME = "pyrogram.raw.base.BusinessAwayMessageSchedule"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
