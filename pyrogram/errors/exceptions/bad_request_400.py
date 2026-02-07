from ..rpc_error import RPCError


class BadRequest(RPCError):
    """Bad Request"""
    CODE = 400
    """``int``: RPC Error Code"""
    NAME = __doc__


class AboutTooLong(BadRequest):
    """The provided about/bio text is too long"""
    ID = "ABOUT_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AccessTokenExpired(BadRequest):
    """The bot token has expired"""
    ID = "ACCESS_TOKEN_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AccessTokenInvalid(BadRequest):
    """The bot access token is invalid"""
    ID = "ACCESS_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AddressInvalid(BadRequest):
    """The specified geopoint address is invalid."""
    ID = "ADDRESS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AdminsTooMuch(BadRequest):
    """The chat has too many administrators"""
    ID = "ADMINS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AdminIdInvalid(BadRequest):
    """The specified admin ID is invalid"""
    ID = "ADMIN_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AdminRankEmojiNotAllowed(BadRequest):
    """Emoji are not allowed in custom administrator titles"""
    ID = "ADMIN_RANK_EMOJI_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AdminRankInvalid(BadRequest):
    """The custom administrator title is invalid or too long"""
    ID = "ADMIN_RANK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AdminRightsEmpty(BadRequest):
    """The chatAdminRights constructor passed in keyboardButtonRequestPeer.peer_type.user_admin_rights has no rights set (i.e. flags is 0)."""
    ID = "ADMIN_RIGHTS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AdExpired(BadRequest):
    """The ad has expired (too old or not found)."""
    ID = "AD_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AlbumPhotosTooMany(BadRequest):
    """Too many photos were included in the album"""
    ID = "ALBUM_PHOTOS_TOO_MANY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ApiIdInvalid(BadRequest):
    """The api_id/api_hash combination is invalid"""
    ID = "API_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ApiIdPublishedFlood(BadRequest):
    """You are using an API key that is limited on the server side because it was published somewhere"""
    ID = "API_ID_PUBLISHED_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ArticleTitleEmpty(BadRequest):
    """The article title is empty"""
    ID = "ARTICLE_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AudioContentUrlEmpty(BadRequest):
    """The remote URL specified in the content field is empty"""
    ID = "AUDIO_CONTENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AudioTitleEmpty(BadRequest):
    """The title attribute of the audio is empty"""
    ID = "AUDIO_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthBytesInvalid(BadRequest):
    """The authorization bytes are invalid"""
    ID = "AUTH_BYTES_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthTokenAlreadyAccepted(BadRequest):
    """The authorization token was already used"""
    ID = "AUTH_TOKEN_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthTokenException(BadRequest):
    """An error occurred while importing the auth token"""
    ID = "AUTH_TOKEN_EXCEPTION"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthTokenExpired(BadRequest):
    """The provided authorization token has expired and the updated QR-code must be re-scanned"""
    ID = "AUTH_TOKEN_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthTokenInvalid(BadRequest):
    """An invalid authorization token was provided"""
    ID = "AUTH_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthTokenInvalid2(BadRequest):
    """An invalid authorization token was provided"""
    ID = "AUTH_TOKEN_INVALID2"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AuthTokenInvalidx(BadRequest):
    """The specified auth token is invalid"""
    ID = "AUTH_TOKEN_INVALIDX"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class AutoarchiveNotAvailable(BadRequest):
    """This feature is not yet enabled for your account due to it not receiving too many private messages from strangers"""
    ID = "AUTOARCHIVE_NOT_AVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BalanceTooLow(BadRequest):
    """The transaction cannot be completed because the current [Telegram Stars balance](https://core.telegram.org/api/stars) is too low."""
    ID = "BALANCE_TOO_LOW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BankCardNumberInvalid(BadRequest):
    """The credit card number is invalid"""
    ID = "BANK_CARD_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BannedRightsInvalid(BadRequest):
    """You provided a set of restrictions that is invalid"""
    ID = "BANNED_RIGHTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BasePortLocInvalid(BadRequest):
    """The base port location is invalid"""
    ID = "BASE_PORT_LOC_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BirthdayInvalid(BadRequest):
    """An invalid age was specified, must be between 0 and 150 years."""
    ID = "BIRTHDAY_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BoostsEmpty(BadRequest):
    """Boosts empty"""
    ID = "BOOSTS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BoostsRequired(BadRequest):
    """Channel required more boost to upload a story"""
    ID = "BOOSTS_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BoostNotModified(BadRequest):
    """You're already [boosting](https://core.telegram.org/api/boost) the specified channel."""
    ID = "BOOST_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BoostPeerInvalid(BadRequest):
    """The specified `boost_peer` is invalid."""
    ID = "BOOST_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotsTooMuch(BadRequest):
    """The chat has too many bots"""
    ID = "BOTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotAlreadyDisabled(BadRequest):
    """The connected business bot was already disabled for the specified peer."""
    ID = "BOT_ALREADY_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotAppBotInvalid(BadRequest):
    """The bot_id passed in the inputBotAppShortName constructor is invalid."""
    ID = "BOT_APP_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotAppInvalid(BadRequest):
    """The specified bot app is invalid."""
    ID = "BOT_APP_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotAppShortnameInvalid(BadRequest):
    """The specified bot app short name is invalid."""
    ID = "BOT_APP_SHORTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotBusinessMissing(BadRequest):
    """The specified bot is not a business bot (the [user](https://core.telegram.org/constructor/user).`bot_business` flag is not set)."""
    ID = "BOT_BUSINESS_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotChannelsNa(BadRequest):
    """Bots can't edit admin privileges"""
    ID = "BOT_CHANNELS_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotCommandDescriptionInvalid(BadRequest):
    """The command description was empty, too long or had invalid characters"""
    ID = "BOT_COMMAND_DESCRIPTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotCommandInvalid(BadRequest):
    """The specified command is invalid"""
    ID = "BOT_COMMAND_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotDomainInvalid(BadRequest):
    """The domain used for the auth button does not match the one configured in @BotFather"""
    ID = "BOT_DOMAIN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotFallbackUnsupported(BadRequest):
    """The fallback flag can't be set for bots."""
    ID = "BOT_FALLBACK_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotGamesDisabled(BadRequest):
    """Bot games cannot be used in this type of chat"""
    ID = "BOT_GAMES_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotGroupsBlocked(BadRequest):
    """This bot can't be added to groups"""
    ID = "BOT_GROUPS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotInlineDisabled(BadRequest):
    """The inline feature of the bot is disabled"""
    ID = "BOT_INLINE_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotInvalid(BadRequest):
    """This is not a valid bot"""
    ID = "BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotInvoiceInvalid(BadRequest):
    """The specified invoice is invalid."""
    ID = "BOT_INVOICE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotMethodInvalid(BadRequest):
    """The method can't be used by bots"""
    ID = "BOT_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotMissing(BadRequest):
    """This method can only be run by a bot"""
    ID = "BOT_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotNotConnectedYet(BadRequest):
    """No [business bot](https://core.telegram.org/api/business#connected-bots) is connected to the currently logged in user."""
    ID = "BOT_NOT_CONNECTED_YET"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotOnesideNotAvail(BadRequest):
    """Bots can't pin messages for one side only in private chats"""
    ID = "BOT_ONESIDE_NOT_AVAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotPaymentsDisabled(BadRequest):
    """This method can only be run by a bot"""
    ID = "BOT_PAYMENTS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotPollsDisabled(BadRequest):
    """Sending polls by bots has been disabled"""
    ID = "BOT_POLLS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotResponseTimeout(BadRequest):
    """The bot did not answer to the callback query in time"""
    ID = "BOT_RESPONSE_TIMEOUT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotScoreNotModified(BadRequest):
    """The bot score was not modified"""
    ID = "BOT_SCORE_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BotWebviewDisabled(BadRequest):
    """A webview cannot be opened in the specified conditions: emitted for example if `from_bot_menu` or `url` are set and `peer` is not the chat with the bot."""
    ID = "BOT_WEBVIEW_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BroadcastCallsDisabled(BadRequest):
    """Broadcast calls disabled"""
    ID = "BROADCAST_CALLS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BroadcastIdInvalid(BadRequest):
    """The channel is invalid"""
    ID = "BROADCAST_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BroadcastPublicVotersForbidden(BadRequest):
    """Polls with public voters cannot be sent in channels"""
    ID = "BROADCAST_PUBLIC_VOTERS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BroadcastRequired(BadRequest):
    """The request can only be used with a channel"""
    ID = "BROADCAST_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessConnectionInvalid(BadRequest):
    """The `connection_id` passed to the wrapping [invokeWithBusinessConnection](https://core.telegram.org/api/business) call is invalid."""
    ID = "BUSINESS_CONNECTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessConnectionNotAllowed(BadRequest):
    """This method was invoked over a business connection using [invokeWithBusinessConnection](https://core.telegram.org/api/business#connected-bots), but either (1) we're a user, and users cannot invoke methods over a business connection; (2) we're a bot, but business mode was disabled in @botfather or (3); we're a bot, but this method cannot be invoked over a business connection."""
    ID = "BUSINESS_CONNECTION_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessPeerInvalid(BadRequest):
    """Messages can't be set to the specified peer through the current [business connection](https://core.telegram.org/api/business#connected-bots)."""
    ID = "BUSINESS_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessPeerUsageMissing(BadRequest):
    """You cannot send a message to a user through a [business connection](https://core.telegram.org/api/business#connected-bots) if the user hasn't recently contacted us."""
    ID = "BUSINESS_PEER_USAGE_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessRecipientsEmpty(BadRequest):
    """You didn't set any flag in inputBusinessBotRecipients, thus the bot cannot work with *any* peer."""
    ID = "BUSINESS_RECIPIENTS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessWorkHoursEmpty(BadRequest):
    """No work hours were specified."""
    ID = "BUSINESS_WORK_HOURS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class BusinessWorkHoursPeriodInvalid(BadRequest):
    """The specified work hours are invalid, see [here »](https://core.telegram.org/api/business#opening-hours) for the exact requirements."""
    ID = "BUSINESS_WORK_HOURS_PERIOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonCopyTextInvalid(BadRequest):
    """The specified [keyboardButtonCopy](https://core.telegram.org/constructor/keyboardButtonCopy).`copy_text` is invalid."""
    ID = "BUTTON_COPY_TEXT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonDataInvalid(BadRequest):
    """The button callback data is invalid or too large"""
    ID = "BUTTON_DATA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonIdInvalid(BadRequest):
    """The specified button ID is invalid."""
    ID = "BUTTON_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonInvalid(BadRequest):
    """The specified button is invalid."""
    ID = "BUTTON_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonPosInvalid(BadRequest):
    """The position of one of the keyboard buttons is invalid (i.e. a Game or Pay button not in the first position, and so on...)."""
    ID = "BUTTON_POS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonTextInvalid(BadRequest):
    """The specified button text is invalid"""
    ID = "BUTTON_TEXT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonTypeInvalid(BadRequest):
    """The type of one of the buttons you provided is invalid"""
    ID = "BUTTON_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonUrlInvalid(BadRequest):
    """The button url is invalid"""
    ID = "BUTTON_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonUserInvalid(BadRequest):
    """The `user_id` passed to inputKeyboardButtonUserProfile is invalid!"""
    ID = "BUTTON_USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ButtonUserPrivacyRestricted(BadRequest):
    """The privacy settings of the user specified in a keyboard button do not allow creating such button"""
    ID = "BUTTON_USER_PRIVACY_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallAlreadyAccepted(BadRequest):
    """The call is already accepted"""
    ID = "CALL_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallAlreadyDeclined(BadRequest):
    """The call is already declined"""
    ID = "CALL_ALREADY_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallOccupyFailed(BadRequest):
    """The call failed because the user is already making another call."""
    ID = "CALL_OCCUPY_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallPeerInvalid(BadRequest):
    """The provided call peer object is invalid"""
    ID = "CALL_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallProtocolFlagsInvalid(BadRequest):
    """Call protocol flags invalid"""
    ID = "CALL_PROTOCOL_FLAGS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CallProtocolLayerInvalid(BadRequest):
    """The specified protocol layer version range is invalid."""
    ID = "CALL_PROTOCOL_LAYER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CdnMethodInvalid(BadRequest):
    """The method can't be used on CDN DCs"""
    ID = "CDN_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelsAdminLocatedTooMuch(BadRequest):
    """The user has reached the limit of public geogroups"""
    ID = "CHANNELS_ADMIN_LOCATED_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelsAdminPublicTooMuch(BadRequest):
    """You are an administrator of too many public channels"""
    ID = "CHANNELS_ADMIN_PUBLIC_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelsTooMuch(BadRequest):
    """You have joined too many channels or supergroups, leave some and try again"""
    ID = "CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelAddInvalid(BadRequest):
    """Internal error."""
    ID = "CHANNEL_ADD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelBanned(BadRequest):
    """The channel is banned"""
    ID = "CHANNEL_BANNED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelForumMissing(BadRequest):
    """The channel forum is missing"""
    ID = "CHANNEL_FORUM_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelIdInvalid(BadRequest):
    """The specified supergroup ID is invalid."""
    ID = "CHANNEL_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelInvalid(BadRequest):
    """The channel parameter is invalid"""
    ID = "CHANNEL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelMonoforumUnsupported(BadRequest):
    """[Monoforums](https://core.telegram.org/api/channel#monoforums) do not support this feature."""
    ID = "CHANNEL_MONOFORUM_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelParicipantMissing(BadRequest):
    """The current user is not in the channel"""
    ID = "CHANNEL_PARICIPANT_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelPrivate(BadRequest):
    """The channel/supergroup is not accessible"""
    ID = "CHANNEL_PRIVATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelTooBig(BadRequest):
    """The channel too big"""
    ID = "CHANNEL_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChannelTooLarge(BadRequest):
    """The channel is too large"""
    ID = "CHANNEL_TOO_LARGE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChargeAlreadyRefunded(BadRequest):
    """The charge id was already used for a refund."""
    ID = "CHARGE_ALREADY_REFUNDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChargeIdEmpty(BadRequest):
    """The specified charge_id is empty."""
    ID = "CHARGE_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChargeIdInvalid(BadRequest):
    """The specified charge_id is invalid."""
    ID = "CHARGE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChargeNotFound(BadRequest):
    """The charge id was not found."""
    ID = "CHARGE_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatlinksTooMuch(BadRequest):
    """Too many [business chat links](https://core.telegram.org/api/business#business-chat-links) were created, please delete some older links."""
    ID = "CHATLINKS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatlinkSlugEmpty(BadRequest):
    """The specified slug is empty."""
    ID = "CHATLINK_SLUG_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatlinkSlugExpired(BadRequest):
    """The specified [business chat link](https://core.telegram.org/api/business#business-chat-links) has expired."""
    ID = "CHATLINK_SLUG_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatlistsTooMuch(BadRequest):
    """You have created too many folder links, hitting the `chatlist_invites_limit_default`/`chatlist_invites_limit_premium` [limits »](https://core.telegram.org/api/config#chatlist-invites-limit-default)."""
    ID = "CHATLISTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatlistExcludeInvalid(BadRequest):
    """The specified `exclude_peers` are invalid."""
    ID = "CHATLIST_EXCLUDE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatAboutNotModified(BadRequest):
    """The chat about text was not modified because you tried to edit it using the same content"""
    ID = "CHAT_ABOUT_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatAboutTooLong(BadRequest):
    """The chat about text is too long"""
    ID = "CHAT_ABOUT_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatAdminRequired(BadRequest):
    """The method requires chat admin privileges"""
    ID = "CHAT_ADMIN_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatDiscussionUnallowed(BadRequest):
    """The chat discussion is not allowed"""
    ID = "CHAT_DISCUSSION_UNALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatForwardsRestricted(BadRequest):
    """The chat restricts forwarding content"""
    ID = "CHAT_FORWARDS_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatIdEmpty(BadRequest):
    """The provided chat id is empty"""
    ID = "CHAT_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatIdInvalid(BadRequest):
    """The chat id being used is invalid or not known yet. Make sure you see the chat before interacting with it"""
    ID = "CHAT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatInvalid(BadRequest):
    """The chat is invalid"""
    ID = "CHAT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatInvitePermanent(BadRequest):
    """The chat invite link is primary"""
    ID = "CHAT_INVITE_PERMANENT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatLinkExists(BadRequest):
    """The action failed because the supergroup is linked to a channel"""
    ID = "CHAT_LINK_EXISTS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatMemberAddFailed(BadRequest):
    """Could not add participants."""
    ID = "CHAT_MEMBER_ADD_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatNotModified(BadRequest):
    """The chat settings (title, permissions, photo, etc..) were not modified because you tried to edit them using the same content"""
    ID = "CHAT_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatPublicRequired(BadRequest):
    """You can only enable join requests in public groups."""
    ID = "CHAT_PUBLIC_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatRestricted(BadRequest):
    """The chat is restricted and cannot be used"""
    ID = "CHAT_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatRevokeDateUnsupported(BadRequest):
    """`min_date` and `max_date` are not available for using with non-user peers"""
    ID = "CHAT_REVOKE_DATE_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatSendInlineForbidden(BadRequest):
    """You cannot use inline bots to send messages in this chat"""
    ID = "CHAT_SEND_INLINE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatTitleEmpty(BadRequest):
    """The chat title is empty"""
    ID = "CHAT_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ChatTooBig(BadRequest):
    """The chat is too big for this action"""
    ID = "CHAT_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CodeEmpty(BadRequest):
    """The provided code is empty"""
    ID = "CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CodeHashInvalid(BadRequest):
    """The provided code hash invalid"""
    ID = "CODE_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CodeInvalid(BadRequest):
    """The provided code is invalid (i.e. from email)"""
    ID = "CODE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CollectibleInvalid(BadRequest):
    """The specified collectible is invalid."""
    ID = "COLLECTIBLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CollectibleNotFound(BadRequest):
    """The specified collectible could not be found."""
    ID = "COLLECTIBLE_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ColorInvalid(BadRequest):
    """The provided color is invalid"""
    ID = "COLOR_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionApiIdInvalid(BadRequest):
    """The provided API id is invalid"""
    ID = "CONNECTION_API_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionAppVersionEmpty(BadRequest):
    """App version is empty"""
    ID = "CONNECTION_APP_VERSION_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionDeviceModelEmpty(BadRequest):
    """The device model is empty"""
    ID = "CONNECTION_DEVICE_MODEL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionIdInvalid(BadRequest):
    """The specified connection ID is invalid."""
    ID = "CONNECTION_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionLangPackInvalid(BadRequest):
    """The specified language pack is not valid"""
    ID = "CONNECTION_LANG_PACK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionLayerInvalid(BadRequest):
    """The connection layer is invalid. Missing InvokeWithLayer-InitConnection call"""
    ID = "CONNECTION_LAYER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionNotInited(BadRequest):
    """The connection was not initialized"""
    ID = "CONNECTION_NOT_INITED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionSystemEmpty(BadRequest):
    """The connection to the system is empty"""
    ID = "CONNECTION_SYSTEM_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ConnectionSystemLangCodeEmpty(BadRequest):
    """The system language code is empty"""
    ID = "CONNECTION_SYSTEM_LANG_CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ContactAddMissing(BadRequest):
    """Contact to add is missing"""
    ID = "CONTACT_ADD_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ContactIdInvalid(BadRequest):
    """The provided contact id is invalid"""
    ID = "CONTACT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ContactMissing(BadRequest):
    """The specified user is not a contact."""
    ID = "CONTACT_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ContactNameEmpty(BadRequest):
    """The provided contact name is empty"""
    ID = "CONTACT_NAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ContactReqMissing(BadRequest):
    """Missing contact request"""
    ID = "CONTACT_REQ_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CreateCallFailed(BadRequest):
    """An error occurred while creating the call"""
    ID = "CREATE_CALL_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CurrencyTotalAmountInvalid(BadRequest):
    """The total amount of all prices is invalid"""
    ID = "CURRENCY_TOTAL_AMOUNT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class CustomReactionsTooMany(BadRequest):
    """Too many custom reactions were specified."""
    ID = "CUSTOM_REACTIONS_TOO_MANY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DataHashSizeInvalid(BadRequest):
    """The size of the specified secureValueErrorData.data_hash is invalid."""
    ID = "DATA_HASH_SIZE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DataInvalid(BadRequest):
    """The encrypted data is invalid"""
    ID = "DATA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DataJsonInvalid(BadRequest):
    """The provided JSON data is invalid"""
    ID = "DATA_JSON_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DataTooLong(BadRequest):
    """Data too long"""
    ID = "DATA_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DateEmpty(BadRequest):
    """The date argument is empty"""
    ID = "DATE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DcIdInvalid(BadRequest):
    """The dc_id parameter is invalid"""
    ID = "DC_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DhGAInvalid(BadRequest):
    """The g_a parameter invalid"""
    ID = "DH_G_A_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class DocumentInvalid(BadRequest):
    """The document is invalid"""
    ID = "DOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EffectIdInvalid(BadRequest):
    """The specified effect ID is invalid."""
    ID = "EFFECT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailHashExpired(BadRequest):
    """The email hash expired and cannot be used to verify it"""
    ID = "EMAIL_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailInvalid(BadRequest):
    """The email provided is invalid"""
    ID = "EMAIL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailNotAllowed(BadRequest):
    """This email is not allowed"""
    ID = "EMAIL_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailNotSetup(BadRequest):
    """In order to change the login email with emailVerifyPurposeLoginChange, an existing login email must already be set using emailVerifyPurposeLoginSetup."""
    ID = "EMAIL_NOT_SETUP"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailUnconfirmed(BadRequest):
    """Email unconfirmed"""
    ID = "EMAIL_UNCONFIRMED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailUnconfirmed(BadRequest):
    """The provided email isn't confirmed, {value} is the length of the verification code that was just sent to the email"""
    ID = "EMAIL_UNCONFIRMED_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmailVerifyExpired(BadRequest):
    """The verification email has expired"""
    ID = "EMAIL_VERIFY_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmojiInvalid(BadRequest):
    """The specified theme emoji is valid"""
    ID = "EMOJI_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmojiMarkupInvalid(BadRequest):
    """The specified `video_emoji_markup` was invalid."""
    ID = "EMOJI_MARKUP_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmojiNotModified(BadRequest):
    """The theme wasn't changed"""
    ID = "EMOJI_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmoticonEmpty(BadRequest):
    """The emoticon parameter is empty"""
    ID = "EMOTICON_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmoticonInvalid(BadRequest):
    """The emoticon parameter is invalid"""
    ID = "EMOTICON_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EmoticonStickerpackMissing(BadRequest):
    """The emoticon sticker pack you are trying to obtain is missing"""
    ID = "EMOTICON_STICKERPACK_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EncryptedMessageInvalid(BadRequest):
    """The special binding message (bind_auth_key_inner) contains invalid data"""
    ID = "ENCRYPTED_MESSAGE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EncryptionAlreadyAccepted(BadRequest):
    """The secret chat is already accepted"""
    ID = "ENCRYPTION_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EncryptionAlreadyDeclined(BadRequest):
    """The secret chat is already declined"""
    ID = "ENCRYPTION_ALREADY_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EncryptionDeclined(BadRequest):
    """The secret chat was declined"""
    ID = "ENCRYPTION_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EncryptionIdInvalid(BadRequest):
    """The provided secret chat id is invalid"""
    ID = "ENCRYPTION_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EntitiesTooLong(BadRequest):
    """The entity provided contains data that is too long, or you passed too many entities to this message"""
    ID = "ENTITIES_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EntityBoundsInvalid(BadRequest):
    """The message entity bounds are invalid"""
    ID = "ENTITY_BOUNDS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class EntityMentionUserInvalid(BadRequest):
    """The mentioned entity is not an user"""
    ID = "ENTITY_MENTION_USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ErrorTextEmpty(BadRequest):
    """The provided error message is empty"""
    ID = "ERROR_TEXT_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExpiresAtInvalid(BadRequest):
    """The specified `expires_at` timestamp is invalid."""
    ID = "EXPIRES_AT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExpireDateInvalid(BadRequest):
    """The expiration date is invalid"""
    ID = "EXPIRE_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExpireForbidden(BadRequest):
    """Expire forbidden"""
    ID = "EXPIRE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExportCardInvalid(BadRequest):
    """The provided card is invalid"""
    ID = "EXPORT_CARD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExtendedMediaAmountInvalid(BadRequest):
    """The specified `stars_amount` of the passed [inputMediaPaidMedia](https://core.telegram.org/constructor/inputMediaPaidMedia) is invalid."""
    ID = "EXTENDED_MEDIA_AMOUNT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExtendedMediaInvalid(BadRequest):
    """The specified paid media is invalid."""
    ID = "EXTENDED_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ExternalUrlInvalid(BadRequest):
    """The external media URL is invalid"""
    ID = "EXTERNAL_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FieldNameEmpty(BadRequest):
    """The field with the name FIELD_NAME is missing"""
    ID = "FIELD_NAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FieldNameInvalid(BadRequest):
    """The field with the name FIELD_NAME is invalid"""
    ID = "FIELD_NAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileContentTypeInvalid(BadRequest):
    """File content-type is invalid"""
    ID = "FILE_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileEmtpy(BadRequest):
    """An empty file was provided"""
    ID = "FILE_EMTPY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileIdInvalid(BadRequest):
    """The file id is invalid"""
    ID = "FILE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileMigrate(BadRequest):
    """The file is in Data Center No. {value}"""
    ID = "FILE_MIGRATE_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartsInvalid(BadRequest):
    """Invalid number of parts."""
    ID = "FILE_PARTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePart0Missing(BadRequest):
    """File part 0 missing"""
    ID = "FILE_PART_0_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartEmpty(BadRequest):
    """The file part sent is empty"""
    ID = "FILE_PART_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartInvalid(BadRequest):
    """The file part number is invalid."""
    ID = "FILE_PART_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartLengthInvalid(BadRequest):
    """The length of a file part is invalid"""
    ID = "FILE_PART_LENGTH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartSizeChanged(BadRequest):
    """The part size is different from the size of one of the previous parts in the same file"""
    ID = "FILE_PART_SIZE_CHANGED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartSizeInvalid(BadRequest):
    """The file part size is invalid"""
    ID = "FILE_PART_SIZE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartTooBig(BadRequest):
    """The size limit for the content of the file part has been exceeded"""
    ID = "FILE_PART_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartTooSmall(BadRequest):
    """The size of the uploaded file part is too small, please see the documentation for the allowed sizes."""
    ID = "FILE_PART_TOO_SMALL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilePartMissing(BadRequest):
    """Part {value} of the file is missing from storage"""
    ID = "FILE_PART_X_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileReferenceEmpty(BadRequest):
    """The file id contains an empty file reference, you must obtain a valid one by fetching the message from the origin context"""
    ID = "FILE_REFERENCE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileReferenceExpired(BadRequest):
    """The file id contains an expired file reference, you must obtain a valid one by fetching the message from the origin context"""
    ID = "FILE_REFERENCE_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileReferenceInvalid(BadRequest):
    """The file id contains an invalid file reference, you must obtain a valid one by fetching the message from the origin context"""
    ID = "FILE_REFERENCE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileReferenceExpired(BadRequest):
    """The file reference of the media file at index {value} in the passed media array expired, it [must be refreshed](https://core.telegram.org/api/file_reference)."""
    ID = "FILE_REFERENCE_X_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileReferenceInvalid(BadRequest):
    """The file reference of the media file at index {value} in the passed media array is invalid."""
    ID = "FILE_REFERENCE_X_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileTitleEmpty(BadRequest):
    """An empty file title was specified"""
    ID = "FILE_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FileTokenInvalid(BadRequest):
    """The master DC did not accept the `file_token` (e.g., the token has expired). Continue downloading the file from the master DC using upload.getFile."""
    ID = "FILE_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilterIdInvalid(BadRequest):
    """The specified filter ID is invalid"""
    ID = "FILTER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilterIncludeEmpty(BadRequest):
    """The filter include is empty"""
    ID = "FILTER_INCLUDE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilterNotSupported(BadRequest):
    """The specified filter cannot be used in this context"""
    ID = "FILTER_NOT_SUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FilterTitleEmpty(BadRequest):
    """The title field of the filter is empty"""
    ID = "FILTER_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FirstnameInvalid(BadRequest):
    """The first name is invalid"""
    ID = "FIRSTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FolderIdEmpty(BadRequest):
    """The folder you tried to delete was already empty"""
    ID = "FOLDER_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FolderIdInvalid(BadRequest):
    """The folder id is invalid"""
    ID = "FOLDER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FormExpired(BadRequest):
    """The form was generated more than 10 minutes ago and has expired, please re-generate it using [payments.getPaymentForm](https://core.telegram.org/method/payments.getPaymentForm) and pass the new `form_id`."""
    ID = "FORM_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FormIdEmpty(BadRequest):
    """The specified form ID is empty."""
    ID = "FORM_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FormIdExpired(BadRequest):
    """The specified id has expired."""
    ID = "FORM_ID_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FormSubmitDuplicate(BadRequest):
    """The same payment form was already submitted.  ."""
    ID = "FORM_SUBMIT_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FormUnsupported(BadRequest):
    """Please update your client."""
    ID = "FORM_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ForumEnabled(BadRequest):
    """You can't execute the specified action because the group is a [forum](https://core.telegram.org/api/forum), disable forum functionality to continue."""
    ID = "FORUM_ENABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FreshChangeAdminsForbidden(BadRequest):
    """You can't change administrator settings in this chat because your session was logged-in recently"""
    ID = "FRESH_CHANGE_ADMINS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FromMessageBotDisabled(BadRequest):
    """Bots can't use fromMessage min constructors"""
    ID = "FROM_MESSAGE_BOT_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FromPeerInvalid(BadRequest):
    """The from peer value is invalid"""
    ID = "FROM_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class FrozenParticipantMissing(BadRequest):
    """The current account is [frozen](https://core.telegram.org/api/auth#frozen-accounts), and cannot access the specified peer."""
    ID = "FROZEN_PARTICIPANT_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GameBotInvalid(BadRequest):
    """You cannot send that game with the current bot"""
    ID = "GAME_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GeneralModifyIconForbidden(BadRequest):
    """You can't modify the icon of the "General" topic."""
    ID = "GENERAL_MODIFY_ICON_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GeoPointInvalid(BadRequest):
    """Invalid geo point provided"""
    ID = "GEO_POINT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GiftMonthsInvalid(BadRequest):
    """The value passed in invoice.inputInvoicePremiumGiftStars.months is invalid."""
    ID = "GIFT_MONTHS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GiftSlugExpired(BadRequest):
    """The gift slug is expired"""
    ID = "GIFT_SLUG_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GiftSlugInvalid(BadRequest):
    """The specified slug is invalid."""
    ID = "GIFT_SLUG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GiftStarsInvalid(BadRequest):
    """The specified amount of stars is invalid."""
    ID = "GIFT_STARS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GifContentTypeInvalid(BadRequest):
    """GIF content-type invalid"""
    ID = "GIF_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GifIdInvalid(BadRequest):
    """The provided gif/animation id is invalid"""
    ID = "GIF_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GraphExpiredReload(BadRequest):
    """This graph has expired, please obtain a new graph token"""
    ID = "GRAPH_EXPIRED_RELOAD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GraphInvalidReload(BadRequest):
    """Invalid graph token provided, please reload the stats and provide the updated token"""
    ID = "GRAPH_INVALID_RELOAD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GraphOutdatedReload(BadRequest):
    """The graph data is outdated"""
    ID = "GRAPH_OUTDATED_RELOAD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupcallAlreadyDiscarded(BadRequest):
    """The group call was already discarded"""
    ID = "GROUPCALL_ALREADY_DISCARDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupcallForbidden(BadRequest):
    """The group call has already ended."""
    ID = "GROUPCALL_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupcallInvalid(BadRequest):
    """The specified group call is invalid"""
    ID = "GROUPCALL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupcallJoinMissing(BadRequest):
    """You haven't joined this group call"""
    ID = "GROUPCALL_JOIN_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupcallNotModified(BadRequest):
    """Group call settings weren't modified"""
    ID = "GROUPCALL_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupcallSsrcDuplicateMuch(BadRequest):
    """Too many group call synchronization source duplicates"""
    ID = "GROUPCALL_SSRC_DUPLICATE_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupedMediaInvalid(BadRequest):
    """The album contains invalid media"""
    ID = "GROUPED_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class GroupCallInvalid(BadRequest):
    """The group call is invalid"""
    ID = "GROUP_CALL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class HashtagInvalid(BadRequest):
    """The specified hashtag is invalid."""
    ID = "HASHTAG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class HashInvalid(BadRequest):
    """The provided hash is invalid"""
    ID = "HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class HashSizeInvalid(BadRequest):
    """The size of the specified secureValueError.hash is invalid."""
    ID = "HASH_SIZE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class HideRequesterMissing(BadRequest):
    """The join request was missing or was already handled"""
    ID = "HIDE_REQUESTER_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class IdExpired(BadRequest):
    """The passed prepared inline message ID has expired."""
    ID = "ID_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class IdInvalid(BadRequest):
    """The passed ID is invalid."""
    ID = "ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ImageProcessFailed(BadRequest):
    """The server failed to process your image"""
    ID = "IMAGE_PROCESS_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ImportFileInvalid(BadRequest):
    """The imported file is invalid"""
    ID = "IMPORT_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ImportFormatDateInvalid(BadRequest):
    """The date specified in the import file is invalid."""
    ID = "IMPORT_FORMAT_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ImportFormatUnrecognized(BadRequest):
    """The imported format is unrecognized"""
    ID = "IMPORT_FORMAT_UNRECOGNIZED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ImportIdInvalid(BadRequest):
    """The import id is invalid"""
    ID = "IMPORT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ImportTokenInvalid(BadRequest):
    """The specified token is invalid."""
    ID = "IMPORT_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InlineResultExpired(BadRequest):
    """The inline bot query expired"""
    ID = "INLINE_RESULT_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputChatlistInvalid(BadRequest):
    """The specified folder is invalid."""
    ID = "INPUT_CHATLIST_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputConstructorInvalid(BadRequest):
    """The provided constructor is invalid"""
    ID = "INPUT_CONSTRUCTOR_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputFetchError(BadRequest):
    """An error occurred while deserializing TL parameters"""
    ID = "INPUT_FETCH_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputFetchFail(BadRequest):
    """Failed deserializing TL payload"""
    ID = "INPUT_FETCH_FAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputFileInvalid(BadRequest):
    """The specified [InputFile](https://core.telegram.org/type/InputFile) is invalid."""
    ID = "INPUT_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputFilterInvalid(BadRequest):
    """The filter is invalid for this query"""
    ID = "INPUT_FILTER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputLayerInvalid(BadRequest):
    """The provided layer is invalid"""
    ID = "INPUT_LAYER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputMethodInvalid(BadRequest):
    """The method invoked is invalid in the current schema"""
    ID = "INPUT_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputPeersEmpty(BadRequest):
    """The specified peer array is empty."""
    ID = "INPUT_PEERS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputPurposeInvalid(BadRequest):
    """The specified payment purpose is invalid."""
    ID = "INPUT_PURPOSE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputRequestTooLong(BadRequest):
    """The input request is too long"""
    ID = "INPUT_REQUEST_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputTextEmpty(BadRequest):
    """The specified text is empty"""
    ID = "INPUT_TEXT_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputTextTooLong(BadRequest):
    """The specified text is too long."""
    ID = "INPUT_TEXT_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InputUserDeactivated(BadRequest):
    """The target user has been deleted/deactivated"""
    ID = "INPUT_USER_DEACTIVATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InvitesTooMuch(BadRequest):
    """The maximum number of per-folder invites specified by the `chatlist_invites_limit_default`/`chatlist_invites_limit_premium` [client configuration parameters »](https://core.telegram.org/api/config#chatlist-invites-limit-default) was reached."""
    ID = "INVITES_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteForbiddenWithJoinas(BadRequest):
    """If the user has anonymously joined a group call as a channel, they can't invite other users to the group call because that would cause deanonymization, because the invite would be sent using the original user ID, not the anonymized channel ID"""
    ID = "INVITE_FORBIDDEN_WITH_JOINAS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteHashEmpty(BadRequest):
    """The invite hash is empty"""
    ID = "INVITE_HASH_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteHashExpired(BadRequest):
    """The chat invite link is no longer valid"""
    ID = "INVITE_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteHashInvalid(BadRequest):
    """The invite link hash is invalid"""
    ID = "INVITE_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteRequestSent(BadRequest):
    """The request to join this chat or channel has been successfully sent"""
    ID = "INVITE_REQUEST_SENT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteRevokedMissing(BadRequest):
    """The action required a chat invite link to be revoked first"""
    ID = "INVITE_REVOKED_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteSlugEmpty(BadRequest):
    """The invite slug is empty"""
    ID = "INVITE_SLUG_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteSlugExpired(BadRequest):
    """The invite slug is expired"""
    ID = "INVITE_SLUG_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InviteSlugInvalid(BadRequest):
    """The specified invitation slug is invalid."""
    ID = "INVITE_SLUG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InvoiceInvalid(BadRequest):
    """The specified invoice is invalid."""
    ID = "INVOICE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class InvoicePayloadInvalid(BadRequest):
    """The specified invoice payload is invalid"""
    ID = "INVOICE_PAYLOAD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class JoinAsPeerInvalid(BadRequest):
    """The specified peer cannot be used to join a group call"""
    ID = "JOIN_AS_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LanguageInvalid(BadRequest):
    """The specified lang_code is invalid."""
    ID = "LANGUAGE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LangCodeInvalid(BadRequest):
    """The specified language code is invalid"""
    ID = "LANG_CODE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LangCodeNotSupported(BadRequest):
    """The specified language code is not supported"""
    ID = "LANG_CODE_NOT_SUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LangPackInvalid(BadRequest):
    """The provided language pack is invalid"""
    ID = "LANG_PACK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LastnameInvalid(BadRequest):
    """The last name is invalid"""
    ID = "LASTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LimitInvalid(BadRequest):
    """The limit parameter is invalid"""
    ID = "LIMIT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LinkNotModified(BadRequest):
    """The chat link was not modified because you tried to link to the same target"""
    ID = "LINK_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class LocationInvalid(BadRequest):
    """The file location is invalid"""
    ID = "LOCATION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MaxDateInvalid(BadRequest):
    """The specified maximum date is invalid"""
    ID = "MAX_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MaxIdInvalid(BadRequest):
    """The max_id parameter is invalid"""
    ID = "MAX_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MaxQtsInvalid(BadRequest):
    """The provided QTS is invalid"""
    ID = "MAX_QTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class Md5ChecksumInvalid(BadRequest):
    """The file's checksum did not match the md5_checksum parameter"""
    ID = "MD5_CHECKSUM_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaAlreadyPaid(BadRequest):
    """You already paid for the specified media."""
    ID = "MEDIA_ALREADY_PAID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaCaptionTooLong(BadRequest):
    """The media caption is too long"""
    ID = "MEDIA_CAPTION_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaEmpty(BadRequest):
    """The media you tried to send is invalid"""
    ID = "MEDIA_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaFileInvalid(BadRequest):
    """The provided media file is invalid"""
    ID = "MEDIA_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaGroupedInvalid(BadRequest):
    """You tried to send media of different types in an album"""
    ID = "MEDIA_GROUPED_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaInvalid(BadRequest):
    """The media is invalid"""
    ID = "MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaNewInvalid(BadRequest):
    """The new media to edit the message with is invalid"""
    ID = "MEDIA_NEW_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaPrevInvalid(BadRequest):
    """The previous media cannot be edited with anything else"""
    ID = "MEDIA_PREV_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaTtlInvalid(BadRequest):
    """The media ttl is invalid"""
    ID = "MEDIA_TTL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaTypeInvalid(BadRequest):
    """The specified media type cannot be used in stories."""
    ID = "MEDIA_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MediaVideoStoryMissing(BadRequest):
    """The media does not have a photo or a video"""
    ID = "MEDIA_VIDEO_STORY_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MegagroupGeoRequired(BadRequest):
    """This method can only be invoked on a geogroup."""
    ID = "MEGAGROUP_GEO_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MegagroupIdInvalid(BadRequest):
    """The supergroup is invalid"""
    ID = "MEGAGROUP_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MegagroupPrehistoryHidden(BadRequest):
    """The action failed because the supergroup has the pre-history hidden"""
    ID = "MEGAGROUP_PREHISTORY_HIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MegagroupRequired(BadRequest):
    """The request can only be used with a supergroup"""
    ID = "MEGAGROUP_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageEditTimeExpired(BadRequest):
    """You can no longer edit this message because too much time has passed"""
    ID = "MESSAGE_EDIT_TIME_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageEmpty(BadRequest):
    """The message sent is empty or contains invalid characters"""
    ID = "MESSAGE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageIdsEmpty(BadRequest):
    """The requested message doesn't exist or you provided no message id"""
    ID = "MESSAGE_IDS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageIdInvalid(BadRequest):
    """The message id is invalid"""
    ID = "MESSAGE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageNotModified(BadRequest):
    """The message was not modified because you tried to edit it using the same content"""
    ID = "MESSAGE_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageNotReadYet(BadRequest):
    """The specified message wasn't read yet."""
    ID = "MESSAGE_NOT_READ_YET"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessagePollClosed(BadRequest):
    """You can't interact with a closed poll"""
    ID = "MESSAGE_POLL_CLOSED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageTooLong(BadRequest):
    """The message text is too long"""
    ID = "MESSAGE_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MessageTooOld(BadRequest):
    """The message is too old, the requested information is not available."""
    ID = "MESSAGE_TOO_OLD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MethodInvalid(BadRequest):
    """The API method is invalid and cannot be used"""
    ID = "METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MinDateInvalid(BadRequest):
    """The specified minimum date is invalid"""
    ID = "MIN_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MonthInvalid(BadRequest):
    """The number of months specified in inputInvoicePremiumGiftStars.months is invalid."""
    ID = "MONTH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MsgIdInvalid(BadRequest):
    """The message ID used in the peer was invalid"""
    ID = "MSG_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MsgTooOld(BadRequest):
    """chat_read_mark_expire_period have passed since the message was sent, read receipts were deleted"""
    ID = "MSG_TOO_OLD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MsgVoiceMissing(BadRequest):
    """The message does not contain a voice message"""
    ID = "MSG_VOICE_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MsgWaitFailed(BadRequest):
    """A waiting call returned an error"""
    ID = "MSG_WAIT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class MultiMediaTooLong(BadRequest):
    """The album/media group contains too many items"""
    ID = "MULTI_MEDIA_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NewSaltInvalid(BadRequest):
    """The new salt is invalid"""
    ID = "NEW_SALT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NewSettingsEmpty(BadRequest):
    """No password is set on the current account, and no new password was specified in `new_settings`"""
    ID = "NEW_SETTINGS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NewSettingsInvalid(BadRequest):
    """The new settings are invalid"""
    ID = "NEW_SETTINGS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NextOffsetInvalid(BadRequest):
    """The next offset value is invalid"""
    ID = "NEXT_OFFSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NogeneralHideForbidden(BadRequest):
    """Only the "General" topic with `id=1` can be hidden."""
    ID = "NOGENERAL_HIDE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NotEligible(BadRequest):
    """The current user is not eligible to join the Peer-to-Peer Login Program."""
    ID = "NOT_ELIGIBLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NotJoined(BadRequest):
    """The current user hasn't joined the Peer-to-Peer Login Program."""
    ID = "NOT_JOINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class NoPaymentNeeded(BadRequest):
    """The upgrade/transfer of the specified gift was already paid for or is free."""
    ID = "NO_PAYMENT_NEEDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class OffsetInvalid(BadRequest):
    """The offset parameter is invalid"""
    ID = "OFFSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class OffsetPeerIdInvalid(BadRequest):
    """The provided offset peer is invalid"""
    ID = "OFFSET_PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class OptionsTooMuch(BadRequest):
    """The poll options are too many"""
    ID = "OPTIONS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class OptionInvalid(BadRequest):
    """The option specified is invalid and does not exist in the target poll"""
    ID = "OPTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class OrderInvalid(BadRequest):
    """The specified username order is invalid."""
    ID = "ORDER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PackShortNameInvalid(BadRequest):
    """Invalid sticker pack name. It must begin with a letter, can't contain consecutive underscores and must end in '_by_<bot username>'."""
    ID = "PACK_SHORT_NAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PackShortNameOccupied(BadRequest):
    """A sticker pack with this name already exists"""
    ID = "PACK_SHORT_NAME_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PackTitleInvalid(BadRequest):
    """The sticker pack title is invalid"""
    ID = "PACK_TITLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PackTypeInvalid(BadRequest):
    """The masks and emojis flags are mutually exclusive."""
    ID = "PACK_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ParentPeerInvalid(BadRequest):
    """The specified `parent_peer` is invalid."""
    ID = "PARENT_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ParticipantsTooFew(BadRequest):
    """The chat doesn't have enough participants"""
    ID = "PARTICIPANTS_TOO_FEW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ParticipantIdInvalid(BadRequest):
    """The specified participant ID is invalid"""
    ID = "PARTICIPANT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ParticipantJoinMissing(BadRequest):
    """Trying to enable a presentation, when the user hasn't joined the Video Chat with phone.joinGroupCall"""
    ID = "PARTICIPANT_JOIN_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ParticipantVersionOutdated(BadRequest):
    """The other participant is using an outdated Telegram app version"""
    ID = "PARTICIPANT_VERSION_OUTDATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordEmpty(BadRequest):
    """The password provided is empty"""
    ID = "PASSWORD_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordHashInvalid(BadRequest):
    """The two-step verification password is invalid"""
    ID = "PASSWORD_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordMissing(BadRequest):
    """The account is missing the two-step verification password"""
    ID = "PASSWORD_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordRecoveryExpired(BadRequest):
    """The recovery code has expired."""
    ID = "PASSWORD_RECOVERY_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordRecoveryNa(BadRequest):
    """The password recovery e-mail is not available"""
    ID = "PASSWORD_RECOVERY_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordRequired(BadRequest):
    """The two-step verification password is required for this method"""
    ID = "PASSWORD_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PasswordTooFresh(BadRequest):
    """The two-step verification password was added recently and you are required to wait {value} seconds"""
    ID = "PASSWORD_TOO_FRESH_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PaymentCredentialsInvalid(BadRequest):
    """The specified payment credentials are invalid."""
    ID = "PAYMENT_CREDENTIALS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PaymentProviderInvalid(BadRequest):
    """The payment provider was not recognised or its token was invalid"""
    ID = "PAYMENT_PROVIDER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PaymentRequired(BadRequest):
    """Payment is required for this action, see [here »](https://core.telegram.org/api/gifts) for more info."""
    ID = "PAYMENT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeersListEmpty(BadRequest):
    """The specified list of peers is empty."""
    ID = "PEERS_LIST_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeerFlood(BadRequest):
    """The method can't be used because your account is currently limited"""
    ID = "PEER_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeerHistoryEmpty(BadRequest):
    """Peer history empty"""
    ID = "PEER_HISTORY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeerIdInvalid(BadRequest):
    """The peer id being used is invalid or not known yet. Make sure you meet the peer before interacting with it"""
    ID = "PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeerIdNotSupported(BadRequest):
    """The provided peer id is not supported"""
    ID = "PEER_ID_NOT_SUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PeerTypesInvalid(BadRequest):
    """The passed [keyboardButtonSwitchInline](https://core.telegram.org/constructor/keyboardButtonSwitchInline).`peer_types` field is invalid."""
    ID = "PEER_TYPES_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PersistentTimestampEmpty(BadRequest):
    """The pts argument is empty"""
    ID = "PERSISTENT_TIMESTAMP_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PersistentTimestampInvalid(BadRequest):
    """The persistent timestamp is invalid"""
    ID = "PERSISTENT_TIMESTAMP_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneCodeEmpty(BadRequest):
    """The phone code is missing"""
    ID = "PHONE_CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneCodeExpired(BadRequest):
    """The confirmation code has expired"""
    ID = "PHONE_CODE_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneCodeHashEmpty(BadRequest):
    """The phone code hash is missing"""
    ID = "PHONE_CODE_HASH_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneCodeInvalid(BadRequest):
    """The confirmation code is invalid"""
    ID = "PHONE_CODE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneHashExpired(BadRequest):
    """An invalid or expired phone_code_hash was provided"""
    ID = "PHONE_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNotOccupied(BadRequest):
    """No user is associated to the specified phone number"""
    ID = "PHONE_NOT_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberAppSignupForbidden(BadRequest):
    """You can't sign up using this app"""
    ID = "PHONE_NUMBER_APP_SIGNUP_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberBanned(BadRequest):
    """The phone number is banned from Telegram and cannot be used"""
    ID = "PHONE_NUMBER_BANNED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberFlood(BadRequest):
    """This number has tried to login too many times"""
    ID = "PHONE_NUMBER_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberInvalid(BadRequest):
    """The phone number is invalid"""
    ID = "PHONE_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberOccupied(BadRequest):
    """The phone number is already in use"""
    ID = "PHONE_NUMBER_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhoneNumberUnoccupied(BadRequest):
    """The phone number is not yet being used"""
    ID = "PHONE_NUMBER_UNOCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhonePasswordProtected(BadRequest):
    """The phone is password protected"""
    ID = "PHONE_PASSWORD_PROTECTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoContentTypeInvalid(BadRequest):
    """The photo content type is invalid"""
    ID = "PHOTO_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoContentUrlEmpty(BadRequest):
    """The photo content URL is empty"""
    ID = "PHOTO_CONTENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoCropFileMissing(BadRequest):
    """Photo crop file missing"""
    ID = "PHOTO_CROP_FILE_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoCropSizeSmall(BadRequest):
    """The photo is too small"""
    ID = "PHOTO_CROP_SIZE_SMALL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoExtInvalid(BadRequest):
    """The photo extension is invalid"""
    ID = "PHOTO_EXT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoFileMissing(BadRequest):
    """Profile photo file missing"""
    ID = "PHOTO_FILE_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoIdInvalid(BadRequest):
    """The photo id is invalid"""
    ID = "PHOTO_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoInvalid(BadRequest):
    """The photo is invalid"""
    ID = "PHOTO_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoInvalidDimensions(BadRequest):
    """The photo dimensions are invalid"""
    ID = "PHOTO_INVALID_DIMENSIONS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoSaveFileInvalid(BadRequest):
    """The photo you tried to send cannot be saved by Telegram"""
    ID = "PHOTO_SAVE_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoThumbUrlEmpty(BadRequest):
    """The photo thumb URL is empty"""
    ID = "PHOTO_THUMB_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PhotoThumbUrlInvalid(BadRequest):
    """The photo thumb URL is invalid"""
    ID = "PHOTO_THUMB_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PinnedDialogsTooMuch(BadRequest):
    """Too many pinned dialogs"""
    ID = "PINNED_DIALOGS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PinnedTooMuch(BadRequest):
    """There are too many pinned topics, unpin some first."""
    ID = "PINNED_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PinRestricted(BadRequest):
    """You can't pin messages in private chats with other people"""
    ID = "PIN_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollAnswersInvalid(BadRequest):
    """The poll answers are invalid"""
    ID = "POLL_ANSWERS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollAnswerInvalid(BadRequest):
    """One of the poll answers is not acceptable"""
    ID = "POLL_ANSWER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollOptionDuplicate(BadRequest):
    """A duplicate option was sent in the same poll"""
    ID = "POLL_OPTION_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollOptionInvalid(BadRequest):
    """A poll option used invalid data (the data may be too long)"""
    ID = "POLL_OPTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollQuestionInvalid(BadRequest):
    """The poll question is invalid"""
    ID = "POLL_QUESTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollUnsupported(BadRequest):
    """This layer does not support polls in the invoked method"""
    ID = "POLL_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PollVoteRequired(BadRequest):
    """Cast a vote in the poll before calling this method"""
    ID = "POLL_VOTE_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PremiumAccountRequired(BadRequest):
    """The method requires a premium user account"""
    ID = "PREMIUM_ACCOUNT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PricingChatInvalid(BadRequest):
    """The pricing for the [subscription](https://core.telegram.org/api/subscriptions) is invalid, the maximum price is specified in the [`stars_subscription_amount_max` config key »](https://core.telegram.org/api/config#stars-subscription-amount-max)."""
    ID = "PRICING_CHAT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PrivacyKeyInvalid(BadRequest):
    """The privacy key is invalid"""
    ID = "PRIVACY_KEY_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PrivacyTooLong(BadRequest):
    """Your privacy exception list has exceeded the maximum capacity"""
    ID = "PRIVACY_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PrivacyValueInvalid(BadRequest):
    """The privacy value is invalid"""
    ID = "PRIVACY_VALUE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PublicKeyRequired(BadRequest):
    """A public key is required"""
    ID = "PUBLIC_KEY_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class PurposeInvalid(BadRequest):
    """The specified payment purpose is invalid."""
    ID = "PURPOSE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QueryIdEmpty(BadRequest):
    """The query ID is empty"""
    ID = "QUERY_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QueryIdInvalid(BadRequest):
    """The callback query id is invalid"""
    ID = "QUERY_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QueryTooShort(BadRequest):
    """The query is too short"""
    ID = "QUERY_TOO_SHORT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuickRepliesBotNotAllowed(BadRequest):
    """[Quick replies](https://core.telegram.org/api/business#quick-reply-shortcuts) cannot be used by bots."""
    ID = "QUICK_REPLIES_BOT_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuickRepliesTooMuch(BadRequest):
    """A maximum of [appConfig.`quick_replies_limit`](https://core.telegram.org/api/config#quick-replies-limit) shortcuts may be created, the limit was reached."""
    ID = "QUICK_REPLIES_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuizAnswerMissing(BadRequest):
    """You can forward a quiz while hiding the original author only after choosing an option in the quiz"""
    ID = "QUIZ_ANSWER_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuizCorrectAnswersEmpty(BadRequest):
    """The correct answers of the quiz are empty"""
    ID = "QUIZ_CORRECT_ANSWERS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuizCorrectAnswersTooMuch(BadRequest):
    """The quiz contains too many correct answers"""
    ID = "QUIZ_CORRECT_ANSWERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuizCorrectAnswerInvalid(BadRequest):
    """The correct answers of the quiz are invalid"""
    ID = "QUIZ_CORRECT_ANSWER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuizMultipleInvalid(BadRequest):
    """A quiz can't have multiple answers"""
    ID = "QUIZ_MULTIPLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class QuoteTextInvalid(BadRequest):
    """The specified `reply_to`.`quote_text` field is invalid."""
    ID = "QUOTE_TEXT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RaiseHandForbidden(BadRequest):
    """You cannot raise your hand."""
    ID = "RAISE_HAND_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RandomIdEmpty(BadRequest):
    """The random ID is empty"""
    ID = "RANDOM_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RandomIdExpired(BadRequest):
    """The specified `random_id` was expired (most likely it didn't follow the required `uint64_t random_id = (time() << 32) | ((uint64_t)random_uint32_t())` format, or the specified time is too far in the past)."""
    ID = "RANDOM_ID_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RandomIdInvalid(BadRequest):
    """The provided random ID is invalid"""
    ID = "RANDOM_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RandomLengthInvalid(BadRequest):
    """The random length is invalid"""
    ID = "RANDOM_LENGTH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RangesInvalid(BadRequest):
    """Invalid range provided"""
    ID = "RANGES_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReactionsCountInvalid(BadRequest):
    """The specified number of reactions is invalid."""
    ID = "REACTIONS_COUNT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReactionsTooMany(BadRequest):
    """Currently, non-premium users, can set up to one reaction per message"""
    ID = "REACTIONS_TOO_MANY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReactionEmpty(BadRequest):
    """The reaction provided is empty"""
    ID = "REACTION_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReactionInvalid(BadRequest):
    """Invalid reaction provided (only valid emoji are allowed)"""
    ID = "REACTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReceiptEmpty(BadRequest):
    """The specified receipt is empty."""
    ID = "RECEIPT_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReflectorNotAvailable(BadRequest):
    """The call reflector is not available"""
    ID = "REFLECTOR_NOT_AVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyMarkupBuyEmpty(BadRequest):
    """Reply markup for buy button empty"""
    ID = "REPLY_MARKUP_BUY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyMarkupGameEmpty(BadRequest):
    """The provided reply markup for the game is empty"""
    ID = "REPLY_MARKUP_GAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyMarkupInvalid(BadRequest):
    """The provided reply markup is invalid"""
    ID = "REPLY_MARKUP_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyMarkupTooLong(BadRequest):
    """The reply markup is too long"""
    ID = "REPLY_MARKUP_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyMessagesTooMuch(BadRequest):
    """Each shortcut can contain a maximum of [appConfig.`quick_reply_messages_limit`](https://core.telegram.org/api/config#quick-reply-messages-limit) messages, the limit was reached."""
    ID = "REPLY_MESSAGES_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyMessageIdInvalid(BadRequest):
    """The reply message id is invalid"""
    ID = "REPLY_MESSAGE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyToInvalid(BadRequest):
    """The specified `reply_to` field is invalid."""
    ID = "REPLY_TO_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyToMonoforumPeerInvalid(BadRequest):
    """The specified inputReplyToMonoForum.monoforum_peer_id is invalid."""
    ID = "REPLY_TO_MONOFORUM_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ReplyToUserInvalid(BadRequest):
    """The replied-to user is invalid."""
    ID = "REPLY_TO_USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RequestTokenInvalid(BadRequest):
    """The master DC did not accept the `request_token` from the CDN DC. Continue downloading the file from the master DC using upload.getFile."""
    ID = "REQUEST_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ResetRequestMissing(BadRequest):
    """No password reset is in progress"""
    ID = "RESET_REQUEST_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ResultsTooMuch(BadRequest):
    """The result contains too many items"""
    ID = "RESULTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ResultIdDuplicate(BadRequest):
    """The result contains items with duplicated identifiers"""
    ID = "RESULT_ID_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ResultIdEmpty(BadRequest):
    """Result ID empty"""
    ID = "RESULT_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ResultIdInvalid(BadRequest):
    """The given result cannot be used to send the selection to the bot"""
    ID = "RESULT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ResultTypeInvalid(BadRequest):
    """The result type is invalid"""
    ID = "RESULT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RevoteNotAllowed(BadRequest):
    """You cannot change your vote"""
    ID = "REVOTE_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RightsNotModified(BadRequest):
    """The new admin rights are equal to the old rights, no change was made"""
    ID = "RIGHTS_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RingtoneInvalid(BadRequest):
    """The specified ringtone is invalid."""
    ID = "RINGTONE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RingtoneMimeInvalid(BadRequest):
    """The MIME type for the ringtone is invalid."""
    ID = "RINGTONE_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class RsaDecryptFailed(BadRequest):
    """Internal RSA decryption failed"""
    ID = "RSA_DECRYPT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SavedIdEmpty(BadRequest):
    """The passed inputSavedStarGiftChat.saved_id is empty."""
    ID = "SAVED_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ScheduleBotNotAllowed(BadRequest):
    """Bots are not allowed to schedule messages"""
    ID = "SCHEDULE_BOT_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ScheduleDateInvalid(BadRequest):
    """Invalid schedule date provided"""
    ID = "SCHEDULE_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ScheduleDateTooLate(BadRequest):
    """The date you tried to schedule is too far in the future (more than one year)"""
    ID = "SCHEDULE_DATE_TOO_LATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ScheduleStatusPrivate(BadRequest):
    """You cannot schedule a message until the person comes online if their privacy does not show this information"""
    ID = "SCHEDULE_STATUS_PRIVATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ScheduleTooMuch(BadRequest):
    """You tried to schedule too many messages in this chat"""
    ID = "SCHEDULE_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ScoreInvalid(BadRequest):
    """The specified game score is invalid"""
    ID = "SCORE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SearchQueryEmpty(BadRequest):
    """The search query is empty"""
    ID = "SEARCH_QUERY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SearchWithLinkNotSupported(BadRequest):
    """You cannot provide a search query and an invite link at the same time"""
    ID = "SEARCH_WITH_LINK_NOT_SUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SecondsInvalid(BadRequest):
    """The seconds interval is invalid"""
    ID = "SECONDS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SecureSecretRequired(BadRequest):
    """A secure secret is required."""
    ID = "SECURE_SECRET_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SelfDeleteRestricted(BadRequest):
    """Business bots can't delete messages just for the user, `revoke` **must** be set."""
    ID = "SELF_DELETE_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SendAsPeerInvalid(BadRequest):
    """You can't send messages as the specified peer"""
    ID = "SEND_AS_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SendMessageGameInvalid(BadRequest):
    """An inputBotInlineMessageGame can only be contained in an inputBotInlineResultGame, not in an inputBotInlineResult/inputBotInlineResultPhoto/etc."""
    ID = "SEND_MESSAGE_GAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SendMessageMediaInvalid(BadRequest):
    """The message media is invalid"""
    ID = "SEND_MESSAGE_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SendMessageTypeInvalid(BadRequest):
    """The message type is invalid"""
    ID = "SEND_MESSAGE_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SessionTooFresh(BadRequest):
    """You can't do this action because the current session was logged-in recently"""
    ID = "SESSION_TOO_FRESH_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SettingsInvalid(BadRequest):
    """Invalid settings were provided"""
    ID = "SETTINGS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class Sha256HashInvalid(BadRequest):
    """The provided SHA256 hash is invalid"""
    ID = "SHA256_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ShortcutInvalid(BadRequest):
    """The specified shortcut is invalid."""
    ID = "SHORTCUT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ShortnameOccupyFailed(BadRequest):
    """An error occurred when trying to register the short-name used for the sticker pack. Try a different name"""
    ID = "SHORTNAME_OCCUPY_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ShortNameInvalid(BadRequest):
    """The specified short name is invalid"""
    ID = "SHORT_NAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ShortNameOccupied(BadRequest):
    """The specified short name is already in use"""
    ID = "SHORT_NAME_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SlotsEmpty(BadRequest):
    """The specified slot list is empty."""
    ID = "SLOTS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SlowmodeMultiMsgsDisabled(BadRequest):
    """Slowmode is enabled, you cannot forward multiple messages to this group"""
    ID = "SLOWMODE_MULTI_MSGS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SlugInvalid(BadRequest):
    """The specified invoice slug is invalid."""
    ID = "SLUG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SmsjobIdInvalid(BadRequest):
    """The specified job ID is invalid."""
    ID = "SMSJOB_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SmsCodeCreateFailed(BadRequest):
    """An error occurred while creating the SMS code"""
    ID = "SMS_CODE_CREATE_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SrpAInvalid(BadRequest):
    """The specified inputCheckPasswordSRP.A value is invalid."""
    ID = "SRP_A_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SrpIdInvalid(BadRequest):
    """Invalid SRP ID provided"""
    ID = "SRP_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SrpPasswordChanged(BadRequest):
    """The password has changed"""
    ID = "SRP_PASSWORD_CHANGED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftAlreadyConverted(BadRequest):
    """The specified star gift was already converted to Stars."""
    ID = "STARGIFT_ALREADY_CONVERTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftAlreadyRefunded(BadRequest):
    """The specified star gift was already refunded."""
    ID = "STARGIFT_ALREADY_REFUNDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftAlreadyUpgraded(BadRequest):
    """The specified gift was already upgraded to a collectible gift."""
    ID = "STARGIFT_ALREADY_UPGRADED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftInvalid(BadRequest):
    """The passed [inputInvoiceStarGift](https://core.telegram.org/constructor/inputInvoiceStarGift) is invalid."""
    ID = "STARGIFT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftNotFound(BadRequest):
    """The specified gift was not found."""
    ID = "STARGIFT_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftOwnerInvalid(BadRequest):
    """You cannot transfer or sell a gift owned by another user."""
    ID = "STARGIFT_OWNER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftPeerInvalid(BadRequest):
    """The specified inputSavedStarGiftChat.peer is invalid."""
    ID = "STARGIFT_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftResellCurrencyNotAllowed(BadRequest):
    """You can't buy the gift using the specified currency (i.e. trying to pay in Stars for TON gifts)."""
    ID = "STARGIFT_RESELL_CURRENCY_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftSlugInvalid(BadRequest):
    """The specified gift slug is invalid."""
    ID = "STARGIFT_SLUG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftTransferTooEarly(BadRequest):
    """You cannot transfer this gift yet, wait {value} seconds."""
    ID = "STARGIFT_TRANSFER_TOO_EARLY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftUpgradeUnavailable(BadRequest):
    """A received gift can only be upgraded to a collectible gift if the [messageActionStarGift](https://core.telegram.org/constructor/messageActionStarGift)/[savedStarGift](https://core.telegram.org/constructor/savedStarGift).`can_upgrade` flag is set."""
    ID = "STARGIFT_UPGRADE_UNAVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftUsageLimited(BadRequest):
    """The gift is sold out."""
    ID = "STARGIFT_USAGE_LIMITED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StargiftUserUsageLimited(BadRequest):
    """You've reached the starGift.limited_per_user limit, you can't buy any more gifts of this type."""
    ID = "STARGIFT_USER_USAGE_LIMITED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarrefAwaitingEnd(BadRequest):
    """The previous referral program was terminated less than 24 hours ago: further changes can be made after the date specified in userFull.starref_program.end_date."""
    ID = "STARREF_AWAITING_END"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarrefExpired(BadRequest):
    """The specified referral link is invalid."""
    ID = "STARREF_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarrefHashRevoked(BadRequest):
    """The specified affiliate link was already revoked."""
    ID = "STARREF_HASH_REVOKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarrefPermilleInvalid(BadRequest):
    """The specified commission_permille is invalid: the minimum and maximum values for this parameter are contained in the [starref_min_commission_permille](https://core.telegram.org/api/config#starref-min-commission-permille) and [starref_max_commission_permille](https://core.telegram.org/api/config#starref-max-commission-permille) client configuration parameters."""
    ID = "STARREF_PERMILLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarrefPermilleTooLow(BadRequest):
    """The specified commission_permille is too low: the minimum and maximum values for this parameter are contained in the [starref_min_commission_permille](https://core.telegram.org/api/config#starref-min-commission-permille) and [starref_max_commission_permille](https://core.telegram.org/api/config#starref-max-commission-permille) client configuration parameters."""
    ID = "STARREF_PERMILLE_TOO_LOW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarsAmountInvalid(BadRequest):
    """The specified amount in stars is invalid."""
    ID = "STARS_AMOUNT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarsInvoiceInvalid(BadRequest):
    """The specified Telegram Star invoice is invalid."""
    ID = "STARS_INVOICE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StarsPaymentRequired(BadRequest):
    """To import this chat invite link, you must first [pay for the associated Telegram Star subscription »](https://core.telegram.org/api/subscriptions#channel-subscriptions)."""
    ID = "STARS_PAYMENT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StartParamEmpty(BadRequest):
    """The start parameter is empty"""
    ID = "START_PARAM_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StartParamInvalid(BadRequest):
    """The start parameter is invalid"""
    ID = "START_PARAM_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StartParamTooLong(BadRequest):
    """The start parameter is too long"""
    ID = "START_PARAM_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerpackStickersTooMuch(BadRequest):
    """There are too many stickers in this stickerpack, you can't add any more"""
    ID = "STICKERPACK_STICKERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickersetInvalid(BadRequest):
    """The requested sticker set is invalid"""
    ID = "STICKERSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickersetNotModified(BadRequest):
    """The sticker set is not modified"""
    ID = "STICKERSET_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickersEmpty(BadRequest):
    """The sticker provided is empty"""
    ID = "STICKERS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickersTooMuch(BadRequest):
    """Too many stickers in the set"""
    ID = "STICKERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerDocumentInvalid(BadRequest):
    """The sticker document is invalid"""
    ID = "STICKER_DOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerEmojiInvalid(BadRequest):
    """The sticker emoji is invalid"""
    ID = "STICKER_EMOJI_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerFileInvalid(BadRequest):
    """The sticker file is invalid"""
    ID = "STICKER_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerGifDimensions(BadRequest):
    """The specified video sticker has invalid dimensions"""
    ID = "STICKER_GIF_DIMENSIONS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerIdInvalid(BadRequest):
    """The provided sticker id is invalid"""
    ID = "STICKER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerInvalid(BadRequest):
    """The provided sticker is invalid"""
    ID = "STICKER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerMimeInvalid(BadRequest):
    """Make sure to pass a valid image file for the right InputFile parameter"""
    ID = "STICKER_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerPngDimensions(BadRequest):
    """The sticker png dimensions are invalid"""
    ID = "STICKER_PNG_DIMENSIONS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerPngNopng(BadRequest):
    """Stickers must be png files but the provided image was not a png"""
    ID = "STICKER_PNG_NOPNG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerTgsNodoc(BadRequest):
    """You must send the animated sticker as a document"""
    ID = "STICKER_TGS_NODOC"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerTgsNotgs(BadRequest):
    """A tgs sticker file was expected, but something else was provided"""
    ID = "STICKER_TGS_NOTGS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerThumbPngNopng(BadRequest):
    """A png sticker thumbnail file was expected, but something else was provided"""
    ID = "STICKER_THUMB_PNG_NOPNG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerThumbTgsNotgs(BadRequest):
    """Incorrect stickerset TGS thumb file provided."""
    ID = "STICKER_THUMB_TGS_NOTGS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerVideoBig(BadRequest):
    """The specified video sticker is too big"""
    ID = "STICKER_VIDEO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerVideoNodoc(BadRequest):
    """You must send the video sticker as a document"""
    ID = "STICKER_VIDEO_NODOC"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StickerVideoNowebm(BadRequest):
    """A webm video file was expected, but something else was provided"""
    ID = "STICKER_VIDEO_NOWEBM"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StoriesNeverCreated(BadRequest):
    """You have never created any stories"""
    ID = "STORIES_NEVER_CREATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StoriesTooMuch(BadRequest):
    """Too many stories in the current account"""
    ID = "STORIES_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StoryIdEmpty(BadRequest):
    """You specified no story IDs."""
    ID = "STORY_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StoryIdInvalid(BadRequest):
    """The specified story ID is invalid."""
    ID = "STORY_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StoryNotModified(BadRequest):
    """The new story information you passed is equal to the previous story information, thus it wasn't modified."""
    ID = "STORY_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StoryPeriodInvalid(BadRequest):
    """The story period is invalid"""
    ID = "STORY_PERIOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StorySendFloodMonthly(BadRequest):
    """You've hit the monthly story limit as specified by the [`stories_sent_monthly_limit_*` client configuration parameters](https://core.telegram.org/api/config#stories-sent-monthly-limit-default): wait for the specified number of seconds before posting a new story."""
    ID = "STORY_SEND_FLOOD_MONTHLY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class StorySendFloodWeekly(BadRequest):
    """You've hit the weekly story limit as specified by the [`stories_sent_weekly_limit_*` client configuration parameters](https://core.telegram.org/api/config#stories-sent-weekly-limit-default): wait for the specified number of seconds before posting a new story."""
    ID = "STORY_SEND_FLOOD_WEEKLY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SubscriptionExportMissing(BadRequest):
    """You cannot send a [bot subscription invoice](https://core.telegram.org/api/subscriptions#bot-subscriptions) directly, you may only create invoice links using [payments.exportInvoice](https://core.telegram.org/method/payments.exportInvoice)."""
    ID = "SUBSCRIPTION_EXPORT_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SubscriptionIdInvalid(BadRequest):
    """The specified subscription_id is invalid."""
    ID = "SUBSCRIPTION_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SubscriptionPeriodInvalid(BadRequest):
    """The specified subscription_pricing.period is invalid."""
    ID = "SUBSCRIPTION_PERIOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SuggestedPostAmountInvalid(BadRequest):
    """The specified price for the suggested post is invalid."""
    ID = "SUGGESTED_POST_AMOUNT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SuggestedPostPeerInvalid(BadRequest):
    """You cannot send suggested posts to non-[monoforum](https://core.telegram.org/api/monoforum) peers."""
    ID = "SUGGESTED_POST_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SwitchPmTextEmpty(BadRequest):
    """The switch_pm.text field was empty"""
    ID = "SWITCH_PM_TEXT_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class SwitchWebviewUrlInvalid(BadRequest):
    """The URL specified in switch_webview.url is invalid!"""
    ID = "SWITCH_WEBVIEW_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TakeoutInvalid(BadRequest):
    """The takeout id is invalid"""
    ID = "TAKEOUT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TakeoutRequired(BadRequest):
    """The method must be invoked inside a takeout session"""
    ID = "TAKEOUT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TaskAlreadyExists(BadRequest):
    """An email reset was already requested."""
    ID = "TASK_ALREADY_EXISTS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TempAuthKeyAlreadyBound(BadRequest):
    """The passed temporary key is already bound to another perm_auth_key_id"""
    ID = "TEMP_AUTH_KEY_ALREADY_BOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TempAuthKeyEmpty(BadRequest):
    """The temporary auth key provided is empty"""
    ID = "TEMP_AUTH_KEY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TermsUrlInvalid(BadRequest):
    """The specified [invoice](https://core.telegram.org/constructor/invoice).`terms_url` is invalid."""
    ID = "TERMS_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeFileInvalid(BadRequest):
    """Invalid theme file provided"""
    ID = "THEME_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeFormatInvalid(BadRequest):
    """Invalid theme format provided"""
    ID = "THEME_FORMAT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeInvalid(BadRequest):
    """Invalid theme provided"""
    ID = "THEME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeMimeInvalid(BadRequest):
    """You cannot create this theme because the mime-type is invalid"""
    ID = "THEME_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeParamsInvalid(BadRequest):
    """The specified `theme_params` field is invalid."""
    ID = "THEME_PARAMS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeSlugInvalid(BadRequest):
    """The specified theme slug is invalid."""
    ID = "THEME_SLUG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ThemeTitleInvalid(BadRequest):
    """The specified theme title is invalid"""
    ID = "THEME_TITLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TimezoneInvalid(BadRequest):
    """The specified timezone does not exist."""
    ID = "TIMEZONE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TitleInvalid(BadRequest):
    """The specified stickerpack title is invalid"""
    ID = "TITLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TmpPasswordDisabled(BadRequest):
    """The temporary password is disabled"""
    ID = "TMP_PASSWORD_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TmpPasswordInvalid(BadRequest):
    """The temporary password is invalid"""
    ID = "TMP_PASSWORD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TodoItemsEmpty(BadRequest):
    """A checklist was specified, but no [checklist items](https://core.telegram.org/api/todo) were passed."""
    ID = "TODO_ITEMS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TodoItemDuplicate(BadRequest):
    """Duplicate [checklist items](https://core.telegram.org/api/todo) detected."""
    ID = "TODO_ITEM_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TodoNotModified(BadRequest):
    """No todo items were specified, so no changes were made to the todo list."""
    ID = "TODO_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TokenEmpty(BadRequest):
    """The specified token is empty."""
    ID = "TOKEN_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TokenInvalid(BadRequest):
    """The provided token is invalid"""
    ID = "TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TokenTypeInvalid(BadRequest):
    """The specified token type is invalid."""
    ID = "TOKEN_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicsEmpty(BadRequest):
    """You specified no topic IDs."""
    ID = "TOPICS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicClosed(BadRequest):
    """The topic was closed"""
    ID = "TOPIC_CLOSED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicCloseSeparately(BadRequest):
    """The `close` flag cannot be provided together with any of the other flags."""
    ID = "TOPIC_CLOSE_SEPARATELY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicDeleted(BadRequest):
    """The topic was deleted"""
    ID = "TOPIC_DELETED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicHideSeparately(BadRequest):
    """The `hide` flag cannot be provided together with any of the other flags."""
    ID = "TOPIC_HIDE_SEPARATELY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicIdInvalid(BadRequest):
    """The provided topic ID is invalid"""
    ID = "TOPIC_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicNotModified(BadRequest):
    """The topic was not modified"""
    ID = "TOPIC_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TopicTitleEmpty(BadRequest):
    """The specified topic title is empty."""
    ID = "TOPIC_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ToIdInvalid(BadRequest):
    """The specified `to_id` of the passed inputInvoiceStarGiftResale or inputInvoiceStarGiftTransfer is invalid."""
    ID = "TO_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class ToLangInvalid(BadRequest):
    """The specified destination language is invalid"""
    ID = "TO_LANG_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TransactionIdInvalid(BadRequest):
    """The specified transaction ID is invalid."""
    ID = "TRANSACTION_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TranscriptionFailed(BadRequest):
    """Telegram is having internal problems. Please try again later to transcribe the audio."""
    ID = "TRANSCRIPTION_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TranslateReqQuotaExceeded(BadRequest):
    """Translation is currently unavailable due to a temporary server-side lack of resources."""
    ID = "TRANSLATE_REQ_QUOTA_EXCEEDED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TtlDaysInvalid(BadRequest):
    """The provided TTL days is invalid"""
    ID = "TTL_DAYS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TtlMediaInvalid(BadRequest):
    """The media does not support self-destruction"""
    ID = "TTL_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TtlPeriodInvalid(BadRequest):
    """The provided TTL period is invalid"""
    ID = "TTL_PERIOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TypesEmpty(BadRequest):
    """The types parameter is empty"""
    ID = "TYPES_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class TypeConstructorInvalid(BadRequest):
    """The type constructor is invalid"""
    ID = "TYPE_CONSTRUCTOR_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UnknownError(BadRequest):
    """Unknown error"""
    ID = "UNKNOWN_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class Unsupported(BadRequest):
    """`require_payment` cannot be *set* by users, only by monoforums: users must instead use the [inputPrivacyKeyNoPaidMessages](https://core.telegram.org/constructor/inputPrivacyKeyNoPaidMessages) privacy setting to remove a previously added exemption."""
    ID = "UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UntilDateInvalid(BadRequest):
    """That date parameter is invalid"""
    ID = "UNTIL_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UrlInvalid(BadRequest):
    """The URL provided is invalid"""
    ID = "URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsageLimitInvalid(BadRequest):
    """The usage limit is invalid"""
    ID = "USAGE_LIMIT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsernamesActiveTooMuch(BadRequest):
    """The maximum number of active usernames was reached."""
    ID = "USERNAMES_ACTIVE_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsernameInvalid(BadRequest):
    """The username is invalid"""
    ID = "USERNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsernameNotModified(BadRequest):
    """The username was not modified because you tried to edit it using the same one"""
    ID = "USERNAME_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsernameNotOccupied(BadRequest):
    """The username is not occupied by anyone"""
    ID = "USERNAME_NOT_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsernameOccupied(BadRequest):
    """The username is already in use by someone else"""
    ID = "USERNAME_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsernamePurchaseAvailable(BadRequest):
    """The username is available for purchase on fragment.com"""
    ID = "USERNAME_PURCHASE_AVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserpicUploadRequired(BadRequest):
    """You are required to upload a profile picture for this action"""
    ID = "USERPIC_UPLOAD_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsersTooFew(BadRequest):
    """Not enough users (to create a chat, for example)"""
    ID = "USERS_TOO_FEW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UsersTooMuch(BadRequest):
    """The maximum number of users has been exceeded (to create a chat, for example)"""
    ID = "USERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserAdminInvalid(BadRequest):
    """The action requires admin privileges. Probably you tried to edit admin privileges on someone you don't have rights to"""
    ID = "USER_ADMIN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserAlreadyInvited(BadRequest):
    """You have already invited this user"""
    ID = "USER_ALREADY_INVITED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserAlreadyParticipant(BadRequest):
    """The user is already a participant of this chat"""
    ID = "USER_ALREADY_PARTICIPANT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserBannedInChannel(BadRequest):
    """You are limited from sending messages in supergroups/channels, check @SpamBot for details"""
    ID = "USER_BANNED_IN_CHANNEL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserBlocked(BadRequest):
    """The user is blocked"""
    ID = "USER_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserBot(BadRequest):
    """Bots in channels can only be administrators, not members."""
    ID = "USER_BOT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserBotInvalid(BadRequest):
    """This method can only be used by a bot"""
    ID = "USER_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserBotRequired(BadRequest):
    """The method can be used by bots only"""
    ID = "USER_BOT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserChannelsTooMuch(BadRequest):
    """The user is already in too many channels or supergroups"""
    ID = "USER_CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserCreator(BadRequest):
    """You can't leave this channel because you're its creator"""
    ID = "USER_CREATOR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserGiftUnavailable(BadRequest):
    """Gifts are not available in the current region ([stars_gifts_enabled](https://core.telegram.org/api/config#stars-gifts-enabled) is equal to false)."""
    ID = "USER_GIFT_UNAVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserIdInvalid(BadRequest):
    """The user id being used is invalid or not known yet. Make sure you meet the user before interacting with it"""
    ID = "USER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserInvalid(BadRequest):
    """The provided user is invalid"""
    ID = "USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserIsBlocked(BadRequest):
    """The user blocked you"""
    ID = "USER_IS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserIsBot(BadRequest):
    """A bot cannot send messages to other bots or to itself"""
    ID = "USER_IS_BOT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserKicked(BadRequest):
    """This user was kicked from this chat"""
    ID = "USER_KICKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserNotMutualContact(BadRequest):
    """The user is not a mutual contact"""
    ID = "USER_NOT_MUTUAL_CONTACT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserNotParticipant(BadRequest):
    """The user is not a member of this chat"""
    ID = "USER_NOT_PARTICIPANT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserPublicMissing(BadRequest):
    """The accounts username is missing"""
    ID = "USER_PUBLIC_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class UserVolumeInvalid(BadRequest):
    """The specified user volume is invalid"""
    ID = "USER_VOLUME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VenueIdInvalid(BadRequest):
    """The specified venue ID is invalid."""
    ID = "VENUE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VideoContentTypeInvalid(BadRequest):
    """The video content type is invalid (i.e.: not streamable)"""
    ID = "VIDEO_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VideoFileInvalid(BadRequest):
    """The video file is invalid"""
    ID = "VIDEO_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VideoPauseForbidden(BadRequest):
    """You cannot pause the video stream."""
    ID = "VIDEO_PAUSE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VideoStopForbidden(BadRequest):
    """You cannot stop the video stream."""
    ID = "VIDEO_STOP_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VideoTitleEmpty(BadRequest):
    """The specified video title is empty"""
    ID = "VIDEO_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VoiceMessagesForbidden(BadRequest):
    """Voice messages are restricted"""
    ID = "VOICE_MESSAGES_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class VolumeLocNotFound(BadRequest):
    """The volume location can't be found"""
    ID = "VOLUME_LOC_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WallpaperFileInvalid(BadRequest):
    """The provided file cannot be used as a wallpaper"""
    ID = "WALLPAPER_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WallpaperInvalid(BadRequest):
    """The input wallpaper was not valid"""
    ID = "WALLPAPER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WallpaperMimeInvalid(BadRequest):
    """The wallpaper mime type is invalid"""
    ID = "WALLPAPER_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WallpaperNotFound(BadRequest):
    """The specified wallpaper could not be found."""
    ID = "WALLPAPER_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WcConvertUrlInvalid(BadRequest):
    """WC convert URL invalid"""
    ID = "WC_CONVERT_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebdocumentInvalid(BadRequest):
    """The web document is invalid"""
    ID = "WEBDOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebdocumentMimeInvalid(BadRequest):
    """The web document mime type is invalid"""
    ID = "WEBDOCUMENT_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebdocumentSizeTooBig(BadRequest):
    """The web document is too big"""
    ID = "WEBDOCUMENT_SIZE_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebdocumentUrlEmpty(BadRequest):
    """The web document URL is empty"""
    ID = "WEBDOCUMENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebdocumentUrlInvalid(BadRequest):
    """The web document URL is invalid"""
    ID = "WEBDOCUMENT_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpageCurlFailed(BadRequest):
    """Telegram server could not fetch the provided URL"""
    ID = "WEBPAGE_CURL_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpageMediaEmpty(BadRequest):
    """The URL doesn't contain any valid media"""
    ID = "WEBPAGE_MEDIA_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpageNotFound(BadRequest):
    """Webpage not found"""
    ID = "WEBPAGE_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpageUrlInvalid(BadRequest):
    """Webpage url invalid"""
    ID = "WEBPAGE_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpushAuthInvalid(BadRequest):
    """The specified web push authentication secret is invalid"""
    ID = "WEBPUSH_AUTH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpushKeyInvalid(BadRequest):
    """The specified web push elliptic curve Diffie-Hellman public key is invalid"""
    ID = "WEBPUSH_KEY_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class WebpushTokenInvalid(BadRequest):
    """The specified web push token is invalid"""
    ID = "WEBPUSH_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
class YouBlockedUser(BadRequest):
    """You blocked this user"""
    ID = "YOU_BLOCKED_USER"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__
