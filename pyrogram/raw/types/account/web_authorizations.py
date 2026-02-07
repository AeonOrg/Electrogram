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


class WebAuthorizations(TLObject):  # type: ignore
    """Web authorizations

    Constructor of :obj:`~pyrogram.raw.base.account.WebAuthorizations`.

    Details:
        - Layer: ``224``
        - ID: ``ED56C9FC``

    Parameters:
        authorizations (List of :obj:`WebAuthorization <pyrogram.raw.base.WebAuthorization>`):
            Web authorization list

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWebAuthorizations
    """

    __slots__: List[str] = ["authorizations", "users"]

    ID = 0xed56c9fc
    QUALNAME = "types.account.WebAuthorizations"

    def __init__(self, *, authorizations: List["raw.base.WebAuthorization"], users: List["raw.base.User"]) -> None:
        self.authorizations = authorizations  # Vector<WebAuthorization>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorizations":
        # No flags

        authorizations = TLObject.read(b)

        users = TLObject.read(b)

        return WebAuthorizations(authorizations=authorizations, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.authorizations))

        b.write(Vector(self.users))

        return b.getvalue()
