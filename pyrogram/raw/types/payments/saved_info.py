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


class SavedInfo(TLObject):  # type: ignore
    """Saved server-side order information

    Constructor of :obj:`~pyrogram.raw.base.payments.SavedInfo`.

    Details:
        - Layer: ``224``
        - ID: ``FB8FE43C``

    Parameters:
        has_saved_credentials (``bool``, *optional*):
            Whether the user has some saved payment credentials

        saved_info (:obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`, *optional*):
            Saved server-side order information

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetSavedInfo
    """

    __slots__: List[str] = ["has_saved_credentials", "saved_info"]

    ID = 0xfb8fe43c
    QUALNAME = "types.payments.SavedInfo"

    def __init__(self, *, has_saved_credentials: Optional[bool] = None, saved_info: "raw.base.PaymentRequestedInfo" = None) -> None:
        self.has_saved_credentials = has_saved_credentials  # flags.1?true
        self.saved_info = saved_info  # flags.0?PaymentRequestedInfo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedInfo":

        flags = Int.read(b)

        has_saved_credentials = True if flags & (1 << 1) else False
        saved_info = TLObject.read(b) if flags & (1 << 0) else None

        return SavedInfo(has_saved_credentials=has_saved_credentials, saved_info=saved_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.has_saved_credentials else 0
        flags |= (1 << 0) if self.saved_info is not None else 0
        b.write(Int(flags))

        if self.saved_info is not None:
            b.write(self.saved_info.write())

        return b.getvalue()
