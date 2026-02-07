# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StickerSetInstallResult = Union["raw.types.messages.StickerSetInstallResultArchive", "raw.types.messages.StickerSetInstallResultSuccess"]


class StickerSetInstallResult:  # type: ignore
    """Result of stickerset installation process

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.StickerSetInstallResultArchive
            messages.StickerSetInstallResultSuccess

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InstallStickerSet
    """

    QUALNAME = "pyrogram.raw.base.messages.StickerSetInstallResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
