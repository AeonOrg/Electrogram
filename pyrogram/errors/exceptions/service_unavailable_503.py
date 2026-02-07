from ..rpc_error import RPCError


class ServiceUnavailable(RPCError):
    """Service Unavailable"""
    CODE = 503
    """``int``: RPC Error Code"""
    NAME = __doc__


class ApiCallError(ServiceUnavailable):
    """Telegram is having internal problems. Please try again later."""
    ID = "ApiCallError"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class Timedout(ServiceUnavailable):
    """Telegram is having internal problems. Please try again later."""
    ID = "Timedout"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class Timeout(ServiceUnavailable):
    """Telegram is having internal problems. Please try again later."""
    ID = "Timeout"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
