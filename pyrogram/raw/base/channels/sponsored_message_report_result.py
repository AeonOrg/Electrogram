# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SponsoredMessageReportResult = Union["raw.types.channels.SponsoredMessageReportResultAdsHidden", "raw.types.channels.SponsoredMessageReportResultChooseOption", "raw.types.channels.SponsoredMessageReportResultReported"]


class SponsoredMessageReportResult:  # type: ignore
    """

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            channels.SponsoredMessageReportResultAdsHidden
            channels.SponsoredMessageReportResultChooseOption
            channels.SponsoredMessageReportResultReported

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReportSponsoredMessage
    """

    QUALNAME = "pyrogram.raw.base.channels.SponsoredMessageReportResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
