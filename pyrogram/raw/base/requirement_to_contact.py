# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RequirementToContact = Union["raw.types.RequirementToContactEmpty", "raw.types.RequirementToContactPaidMessages", "raw.types.RequirementToContactPremium"]


class RequirementToContact:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            RequirementToContactEmpty
            RequirementToContactPaidMessages
            RequirementToContactPremium

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetRequirementsToContact
    """

    QUALNAME = "pyrogram.raw.base.RequirementToContact"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
