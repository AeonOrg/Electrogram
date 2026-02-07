from ..rpc_error import RPCError


class Flood(RPCError):
    """Flood"""
    CODE = 420
    """``int``: RPC Error Code"""
    NAME = __doc__


class TwoFaConfirmWait(Flood):
    """A wait of {value} seconds is required because this account is active and protected by a 2FA password"""
    ID = "2FA_CONFIRM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AddressInvalid(Flood):
    """The specified geopoint address is invalid."""
    ID = "ADDRESS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FloodPremiumWait(Flood):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_PREMIUM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FloodTestPhoneWait(Flood):
    """A wait of {value} seconds is required in the test servers"""
    ID = "FLOOD_TEST_PHONE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FloodWait(Flood):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FrozenMethodInvalid(Flood):
    """The current account is [frozen](https://core.telegram.org/api/auth#frozen-accounts), and thus cannot execute the specified action."""
    ID = "FROZEN_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PremiumSubActiveUntil(Flood):
    """A wait of {value} seconds is required"""
    ID = "PREMIUM_SUB_ACTIVE_UNTIL_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SlowmodeWait(Flood):
    """A wait of {value} seconds is required to send messages in this chat"""
    ID = "SLOWMODE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StorySendFlood(Flood):
    """A wait of {value} seconds is required to continue posting stories"""
    ID = "STORY_SEND_FLOOD_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TakeoutInitDelay(Flood):
    """You have to confirm the data export request using one of your mobile devices or wait {value} seconds"""
    ID = "TAKEOUT_INIT_DELAY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
