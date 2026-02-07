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


class CdnConfig(TLObject):  # type: ignore
    """Configuration for CDN file downloads.

    Constructor of :obj:`~pyrogram.raw.base.CdnConfig`.

    Details:
        - Layer: ``224``
        - ID: ``5725E40A``

    Parameters:
        public_keys (List of :obj:`CdnPublicKey <pyrogram.raw.base.CdnPublicKey>`):
            Vector of public keys to use only during handshakes to CDN DCs.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCdnConfig
    """

    __slots__: List[str] = ["public_keys"]

    ID = 0x5725e40a
    QUALNAME = "types.CdnConfig"

    def __init__(self, *, public_keys: List["raw.base.CdnPublicKey"]) -> None:
        self.public_keys = public_keys  # Vector<CdnPublicKey>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CdnConfig":
        # No flags

        public_keys = TLObject.read(b)

        return CdnConfig(public_keys=public_keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.public_keys))

        return b.getvalue()
