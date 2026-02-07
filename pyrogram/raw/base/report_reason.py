# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ReportReason = Union["raw.types.InputReportReasonChildAbuse", "raw.types.InputReportReasonCopyright", "raw.types.InputReportReasonFake", "raw.types.InputReportReasonGeoIrrelevant", "raw.types.InputReportReasonIllegalDrugs", "raw.types.InputReportReasonOther", "raw.types.InputReportReasonPersonalDetails", "raw.types.InputReportReasonPornography", "raw.types.InputReportReasonSpam", "raw.types.InputReportReasonViolence"]


class ReportReason:  # type: ignore
    """Report reason

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputReportReasonChildAbuse
            InputReportReasonCopyright
            InputReportReasonFake
            InputReportReasonGeoIrrelevant
            InputReportReasonIllegalDrugs
            InputReportReasonOther
            InputReportReasonPersonalDetails
            InputReportReasonPornography
            InputReportReasonSpam
            InputReportReasonViolence
    """

    QUALNAME = "pyrogram.raw.base.ReportReason"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
