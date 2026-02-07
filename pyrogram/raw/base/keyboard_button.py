# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

KeyboardButton = Union["raw.types.InputKeyboardButtonRequestPeer", "raw.types.InputKeyboardButtonUrlAuth", "raw.types.InputKeyboardButtonUserProfile", "raw.types.KeyboardButton", "raw.types.KeyboardButtonBuy", "raw.types.KeyboardButtonCallback", "raw.types.KeyboardButtonCopy", "raw.types.KeyboardButtonGame", "raw.types.KeyboardButtonRequestGeoLocation", "raw.types.KeyboardButtonRequestPeer", "raw.types.KeyboardButtonRequestPhone", "raw.types.KeyboardButtonRequestPoll", "raw.types.KeyboardButtonSimpleWebView", "raw.types.KeyboardButtonSwitchInline", "raw.types.KeyboardButtonUrl", "raw.types.KeyboardButtonUrlAuth", "raw.types.KeyboardButtonUserProfile", "raw.types.KeyboardButtonWebView"]


class KeyboardButton:  # type: ignore
    """Bot or inline keyboard buttons

    Constructors:
        This base type has 18 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputKeyboardButtonRequestPeer
            InputKeyboardButtonUrlAuth
            InputKeyboardButtonUserProfile
            KeyboardButton
            KeyboardButtonBuy
            KeyboardButtonCallback
            KeyboardButtonCopy
            KeyboardButtonGame
            KeyboardButtonRequestGeoLocation
            KeyboardButtonRequestPeer
            KeyboardButtonRequestPhone
            KeyboardButtonRequestPoll
            KeyboardButtonSimpleWebView
            KeyboardButtonSwitchInline
            KeyboardButtonUrl
            KeyboardButtonUrlAuth
            KeyboardButtonUserProfile
            KeyboardButtonWebView
    """

    QUALNAME = "pyrogram.raw.base.KeyboardButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
