from ..rpc_error import RPCError


class NotAcceptable(RPCError):
    """Not Acceptable"""
    CODE = 406
    """``int``: RPC Error Code"""
    NAME = __doc__


class AllowPaymentRequired(NotAcceptable):
    """This peer only accepts [paid messages »](https://core.telegram.org/api/paid-messages): this error is only emitted for older layers without paid messages support, so the client must be updated in order to use paid messages.  ."""
    ID = "ALLOW_PAYMENT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ApiGiftRestrictedUpdateApp(NotAcceptable):
    """Please update the app to access the gift API."""
    ID = "API_GIFT_RESTRICTED_UPDATE_APP"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthKeyDuplicated(NotAcceptable):
    """The same authorization key (session file) was used in more than one place simultaneously. You must delete your session file and log in again with your phone number or bot token"""
    ID = "AUTH_KEY_DUPLICATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BannedRightsInvalid(NotAcceptable):
    """You provided some invalid flags in the banned rights."""
    ID = "BANNED_RIGHTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessAddressActive(NotAcceptable):
    """The user is currently advertising a [Business Location](https://core.telegram.org/api/business#location), the location may only be changed (or removed) using [account.updateBusinessLocation »](https://core.telegram.org/method/account.updateBusinessLocation).  ."""
    ID = "BUSINESS_ADDRESS_ACTIVE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallProtocolCompatLayerInvalid(NotAcceptable):
    """The other side of the call does not support any of the VoIP protocols supported by the local client, as specified by the `protocol.layer` and `protocol.library_versions` fields."""
    ID = "CALL_PROTOCOL_COMPAT_LAYER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelPrivate(NotAcceptable):
    """The channel/supergroup is not accessible"""
    ID = "CHANNEL_PRIVATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelTooLarge(NotAcceptable):
    """Сhannel is too large to be deleted. Contact support for removal"""
    ID = "CHANNEL_TOO_LARGE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatForwardsRestricted(NotAcceptable):
    """You can't forward messages from a protected chat"""
    ID = "CHAT_FORWARDS_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilerefUpgradeNeeded(NotAcceptable):
    """The file reference has expired and you must use a refreshed one by obtaining the original media message"""
    ID = "FILEREF_UPGRADE_NEEDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FreshChangeAdminsForbidden(NotAcceptable):
    """You were just elected admin, you can't add or modify other admins yet"""
    ID = "FRESH_CHANGE_ADMINS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FreshChangePhoneForbidden(NotAcceptable):
    """You can't change your phone number because your session was logged-in recently"""
    ID = "FRESH_CHANGE_PHONE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FreshResetAuthorisationForbidden(NotAcceptable):
    """You can't terminate other authorized sessions because the current was logged-in recently"""
    ID = "FRESH_RESET_AUTHORISATION_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GiftcodeNotAllowed(NotAcceptable):
    """Giftcode not allowed"""
    ID = "GIFTCODE_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteHashExpired(NotAcceptable):
    """The chat the user tried to join has expired and is not valid anymore"""
    ID = "INVITE_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PaymentUnsupported(NotAcceptable):
    """A detailed description of the error will be received separately as described [here »](https://core.telegram.org/api/errors#406-not-acceptable)."""
    ID = "PAYMENT_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeerIdInvalid(NotAcceptable):
    """The provided peer id is invalid."""
    ID = "PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberInvalid(NotAcceptable):
    """The phone number is invalid"""
    ID = "PHONE_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhonePasswordFlood(NotAcceptable):
    """You have tried to log-in too many times"""
    ID = "PHONE_PASSWORD_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PrecheckoutFailed(NotAcceptable):
    """Precheckout failed, a detailed and localized description for the error will be emitted via an [updateServiceNotification as specified here »](https://core.telegram.org/api/errors#406-not-acceptable)."""
    ID = "PRECHECKOUT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PremiumCurrentlyUnavailable(NotAcceptable):
    """Premium currently unavailable"""
    ID = "PREMIUM_CURRENTLY_UNAVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PreviousChatImportActiveWaitMin(NotAcceptable):
    """Similar to a flood wait, must wait {value} minutes"""
    ID = "PREVIOUS_CHAT_IMPORT_ACTIVE_WAIT_XMIN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PrivacyPremiumRequired(NotAcceptable):
    """You need a [Telegram Premium subscription](https://core.telegram.org/api/premium) to send a message to this user."""
    ID = "PRIVACY_PREMIUM_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SendCodeUnavailable(NotAcceptable):
    """Returned when all available options for this type of number were already used (e.g. flash-call, then SMS, then this error might be returned to trigger a second resend)"""
    ID = "SEND_CODE_UNAVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftExportInProgress(NotAcceptable):
    """A gift export is in progress, a detailed and localized description for the error will be emitted via an [updateServiceNotification as specified here »](https://core.telegram.org/api/errors#406-not-acceptable)."""
    ID = "STARGIFT_EXPORT_IN_PROGRESS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarsFormAmountMismatch(NotAcceptable):
    """The form amount has changed, please fetch the new form using [payments.getPaymentForm](https://core.telegram.org/method/payments.getPaymentForm) and restart the process."""
    ID = "STARS_FORM_AMOUNT_MISMATCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickersetInvalid(NotAcceptable):
    """The sticker set is invalid"""
    ID = "STICKERSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickersetOwnerAnonymous(NotAcceptable):
    """This sticker set can't be used as the group's sticker set because it was created by one of its anonymous admins"""
    ID = "STICKERSET_OWNER_ANONYMOUS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicClosed(NotAcceptable):
    """This topic was closed, you can't send messages to it anymore."""
    ID = "TOPIC_CLOSED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicDeleted(NotAcceptable):
    """The specified topic was deleted."""
    ID = "TOPIC_DELETED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TranslationsDisabled(NotAcceptable):
    """Translations are unavailable, a detailed and localized description for the error will be emitted via an [updateServiceNotification as specified here »](https://core.telegram.org/api/errors#406-not-acceptable)."""
    ID = "TRANSLATIONS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UpdateAppToLogin(NotAcceptable):
    """Update app to login"""
    ID = "UPDATE_APP_TO_LOGIN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserpicPrivacyRequired(NotAcceptable):
    """You need to disable privacy settings for your profile picture in order to make your geolocation public"""
    ID = "USERPIC_PRIVACY_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserpicUploadRequired(NotAcceptable):
    """You must have a profile picture to publish your geolocation"""
    ID = "USERPIC_UPLOAD_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserRestricted(NotAcceptable):
    """You are limited/restricted. You can't perform this action"""
    ID = "USER_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
