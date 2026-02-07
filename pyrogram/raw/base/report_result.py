# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ReportResult = Union["raw.types.ReportResultAddComment", "raw.types.ReportResultChooseOption", "raw.types.ReportResultReported"]


class ReportResult:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ReportResultAddComment
            ReportResultChooseOption
            ReportResultReported

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.Report
            stories.Report
    """

    QUALNAME = "pyrogram.raw.base.ReportResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
