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


class GetCollectibleInfo(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``BE1E85BA``

    Parameters:
        collectible (:obj:`InputCollectible <pyrogram.raw.base.InputCollectible>`):


    Returns:
        :obj:`fragment.CollectibleInfo <pyrogram.raw.base.fragment.CollectibleInfo>`
    """

    __slots__: List[str] = ["collectible"]

    ID = 0xbe1e85ba
    QUALNAME = "functions.fragment.GetCollectibleInfo"

    def __init__(self, *, collectible: "raw.base.InputCollectible") -> None:
        self.collectible = collectible  # InputCollectible

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCollectibleInfo":
        # No flags

        collectible = TLObject.read(b)

        return GetCollectibleInfo(collectible=collectible)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.collectible.write())

        return b.getvalue()
