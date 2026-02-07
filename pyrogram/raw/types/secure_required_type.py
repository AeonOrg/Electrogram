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


class SecureRequiredType(TLObject):  # type: ignore
    """Required type

    Constructor of :obj:`~pyrogram.raw.base.SecureRequiredType`.

    Details:
        - Layer: ``224``
        - ID: ``829D99DA``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            Secure value type

        native_names (``bool``, *optional*):
            Native names

        selfie_required (``bool``, *optional*):
            Is a selfie required

        translation_required (``bool``, *optional*):
            Is a translation required

    """

    __slots__: List[str] = ["type", "native_names", "selfie_required", "translation_required"]

    ID = 0x829d99da
    QUALNAME = "types.SecureRequiredType"

    def __init__(self, *, type: "raw.base.SecureValueType", native_names: Optional[bool] = None, selfie_required: Optional[bool] = None, translation_required: Optional[bool] = None) -> None:
        self.type = type  # SecureValueType
        self.native_names = native_names  # flags.0?true
        self.selfie_required = selfie_required  # flags.1?true
        self.translation_required = translation_required  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureRequiredType":

        flags = Int.read(b)

        native_names = True if flags & (1 << 0) else False
        selfie_required = True if flags & (1 << 1) else False
        translation_required = True if flags & (1 << 2) else False
        type = TLObject.read(b)

        return SecureRequiredType(type=type, native_names=native_names, selfie_required=selfie_required, translation_required=translation_required)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.native_names else 0
        flags |= (1 << 1) if self.selfie_required else 0
        flags |= (1 << 2) if self.translation_required else 0
        b.write(Int(flags))

        b.write(self.type.write())

        return b.getvalue()
