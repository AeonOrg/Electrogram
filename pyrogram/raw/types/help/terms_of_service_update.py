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


class TermsOfServiceUpdate(TLObject):  # type: ignore
    """Info about an update of telegram's terms of service. If the terms of service are declined, then the account.deleteAccount method should be called with the reason "Decline ToS update"

    Constructor of :obj:`~pyrogram.raw.base.help.TermsOfServiceUpdate`.

    Details:
        - Layer: ``224``
        - ID: ``28ECF961``

    Parameters:
        expires (``int`` ``32-bit``):
            New TOS updates will have to be queried using help.getTermsOfServiceUpdate in expires seconds

        terms_of_service (:obj:`help.TermsOfService <pyrogram.raw.base.help.TermsOfService>`):
            New terms of service

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    __slots__: List[str] = ["expires", "terms_of_service"]

    ID = 0x28ecf961
    QUALNAME = "types.help.TermsOfServiceUpdate"

    def __init__(self, *, expires: int, terms_of_service: "raw.base.help.TermsOfService") -> None:
        self.expires = expires  # int
        self.terms_of_service = terms_of_service  # help.TermsOfService

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfServiceUpdate":
        # No flags

        expires = Int.read(b)

        terms_of_service = TLObject.read(b)

        return TermsOfServiceUpdate(expires=expires, terms_of_service=terms_of_service)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.expires))

        b.write(self.terms_of_service.write())

        return b.getvalue()
