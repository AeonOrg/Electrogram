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


class WallPaperSettings(TLObject):  # type: ignore
    """Wallpaper rendering information.

    Constructor of :obj:`~pyrogram.raw.base.WallPaperSettings`.

    Details:
        - Layer: ``224``
        - ID: ``372EFCD0``

    Parameters:
        blur (``bool``, *optional*):
            For image wallpapers »: if set, the JPEG must be downscaled to fit in 450x450 square and then box-blurred with radius 12.

        motion (``bool``, *optional*):
            If set, the background needs to be slightly moved when the device is rotated.

        background_color (``int`` ``32-bit``, *optional*):
            Used for solid », gradient » and freeform gradient » fills.

        second_background_color (``int`` ``32-bit``, *optional*):
            Used for gradient » and freeform gradient » fills.

        third_background_color (``int`` ``32-bit``, *optional*):
            Used for freeform gradient » fills.

        fourth_background_color (``int`` ``32-bit``, *optional*):
            Used for freeform gradient » fills.

        intensity (``int`` ``32-bit``, *optional*):
            Used for pattern wallpapers ».

        rotation (``int`` ``32-bit``, *optional*):
            Clockwise rotation angle of the gradient, in degrees; 0-359. Should be always divisible by 45.

        emoticon (``str``, *optional*):
            If set, this wallpaper can be used as a channel wallpaper and is represented by the specified UTF-8 emoji.

    """

    __slots__: List[str] = ["blur", "motion", "background_color", "second_background_color", "third_background_color", "fourth_background_color", "intensity", "rotation", "emoticon"]

    ID = 0x372efcd0
    QUALNAME = "types.WallPaperSettings"

    def __init__(self, *, blur: Optional[bool] = None, motion: Optional[bool] = None, background_color: Optional[int] = None, second_background_color: Optional[int] = None, third_background_color: Optional[int] = None, fourth_background_color: Optional[int] = None, intensity: Optional[int] = None, rotation: Optional[int] = None, emoticon: Optional[str] = None) -> None:
        self.blur = blur  # flags.1?true
        self.motion = motion  # flags.2?true
        self.background_color = background_color  # flags.0?int
        self.second_background_color = second_background_color  # flags.4?int
        self.third_background_color = third_background_color  # flags.5?int
        self.fourth_background_color = fourth_background_color  # flags.6?int
        self.intensity = intensity  # flags.3?int
        self.rotation = rotation  # flags.4?int
        self.emoticon = emoticon  # flags.7?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPaperSettings":

        flags = Int.read(b)

        blur = True if flags & (1 << 1) else False
        motion = True if flags & (1 << 2) else False
        background_color = Int.read(b) if flags & (1 << 0) else None
        second_background_color = Int.read(b) if flags & (1 << 4) else None
        third_background_color = Int.read(b) if flags & (1 << 5) else None
        fourth_background_color = Int.read(b) if flags & (1 << 6) else None
        intensity = Int.read(b) if flags & (1 << 3) else None
        rotation = Int.read(b) if flags & (1 << 4) else None
        emoticon = String.read(b) if flags & (1 << 7) else None
        return WallPaperSettings(blur=blur, motion=motion, background_color=background_color, second_background_color=second_background_color, third_background_color=third_background_color, fourth_background_color=fourth_background_color, intensity=intensity, rotation=rotation, emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.blur else 0
        flags |= (1 << 2) if self.motion else 0
        flags |= (1 << 0) if self.background_color is not None else 0
        flags |= (1 << 4) if self.second_background_color is not None else 0
        flags |= (1 << 5) if self.third_background_color is not None else 0
        flags |= (1 << 6) if self.fourth_background_color is not None else 0
        flags |= (1 << 3) if self.intensity is not None else 0
        flags |= (1 << 4) if self.rotation is not None else 0
        flags |= (1 << 7) if self.emoticon is not None else 0
        b.write(Int(flags))

        if self.background_color is not None:
            b.write(Int(self.background_color))

        if self.second_background_color is not None:
            b.write(Int(self.second_background_color))

        if self.third_background_color is not None:
            b.write(Int(self.third_background_color))

        if self.fourth_background_color is not None:
            b.write(Int(self.fourth_background_color))

        if self.intensity is not None:
            b.write(Int(self.intensity))

        if self.rotation is not None:
            b.write(Int(self.rotation))

        if self.emoticon is not None:
            b.write(String(self.emoticon))

        return b.getvalue()
