from ..rpc_error import RPCError


class Unauthorized(RPCError):
    """Unauthorized"""
    CODE = 401
    """``int``: RPC Error Code"""
    NAME = __doc__


class ActiveUserRequired(Unauthorized):
    """The method is only available to already activated users"""
    ID = "ACTIVE_USER_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthKeyInvalid(Unauthorized):
    """The key is invalid"""
    ID = "AUTH_KEY_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthKeyPermEmpty(Unauthorized):
    """The method is unavailable for temporary authorization key, not bound to permanent"""
    ID = "AUTH_KEY_PERM_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthKeyUnregistered(Unauthorized):
    """The key is not registered in the system. Delete your session file and login again"""
    ID = "AUTH_KEY_UNREGISTERED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SessionExpired(Unauthorized):
    """The authorization has expired"""
    ID = "SESSION_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SessionPasswordNeeded(Unauthorized):
    """The two-step verification is enabled and a password is required"""
    ID = "SESSION_PASSWORD_NEEDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SessionRevoked(Unauthorized):
    """The authorization has been invalidated, because of the user terminating all sessions"""
    ID = "SESSION_REVOKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserDeactivated(Unauthorized):
    """The user has been deleted/deactivated"""
    ID = "USER_DEACTIVATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserDeactivatedBan(Unauthorized):
    """The user has been deleted/deactivated"""
    ID = "USER_DEACTIVATED_BAN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
