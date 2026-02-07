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


class UrlAuthResultRequest(TLObject):  # type: ignore
    """Details about the authorization request, for more info click here »

    Constructor of :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``224``
        - ID: ``32FABF1A``

    Parameters:
        bot (:obj:`User <pyrogram.raw.base.User>`):
            Username of a bot, which will be used for user authorization. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.

        domain (``str``):
            The domain name of the website on which the user will log in.

        request_write_access (``bool``, *optional*):
            Whether the bot would like to send messages to the user

        request_phone_number (``bool``, *optional*):
            N/A

        browser (``str``, *optional*):
            N/A

        platform (``str``, *optional*):
            N/A

        ip (``str``, *optional*):
            N/A

        region (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = ["bot", "domain", "request_write_access", "request_phone_number", "browser", "platform", "ip", "region"]

    ID = 0x32fabf1a
    QUALNAME = "types.UrlAuthResultRequest"

    def __init__(self, *, bot: "raw.base.User", domain: str, request_write_access: Optional[bool] = None, request_phone_number: Optional[bool] = None, browser: Optional[str] = None, platform: Optional[str] = None, ip: Optional[str] = None, region: Optional[str] = None) -> None:
        self.bot = bot  # User
        self.domain = domain  # string
        self.request_write_access = request_write_access  # flags.0?true
        self.request_phone_number = request_phone_number  # flags.1?true
        self.browser = browser  # flags.2?string
        self.platform = platform  # flags.2?string
        self.ip = ip  # flags.2?string
        self.region = region  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultRequest":

        flags = Int.read(b)

        request_write_access = True if flags & (1 << 0) else False
        request_phone_number = True if flags & (1 << 1) else False
        bot = TLObject.read(b)

        domain = String.read(b)

        browser = String.read(b) if flags & (1 << 2) else None
        platform = String.read(b) if flags & (1 << 2) else None
        ip = String.read(b) if flags & (1 << 2) else None
        region = String.read(b) if flags & (1 << 2) else None
        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access, request_phone_number=request_phone_number, browser=browser, platform=platform, ip=ip, region=region)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.request_phone_number else 0
        flags |= (1 << 2) if self.browser is not None else 0
        flags |= (1 << 2) if self.platform is not None else 0
        flags |= (1 << 2) if self.ip is not None else 0
        flags |= (1 << 2) if self.region is not None else 0
        b.write(Int(flags))

        b.write(self.bot.write())

        b.write(String(self.domain))

        if self.browser is not None:
            b.write(String(self.browser))

        if self.platform is not None:
            b.write(String(self.platform))

        if self.ip is not None:
            b.write(String(self.ip))

        if self.region is not None:
            b.write(String(self.region))

        return b.getvalue()
