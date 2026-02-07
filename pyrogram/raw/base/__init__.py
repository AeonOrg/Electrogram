# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from .res_pq import ResPQ
from .pq_inner_data import PQInnerData
from .bind_auth_key_inner import BindAuthKeyInner
from .server_dh_params import ServerDHParams
from .server_dh_inner_data import ServerDHInnerData
from .client_dh_inner_data import ClientDHInnerData
from .set_client_dh_params_answer import SetClientDHParamsAnswer
from .destroy_auth_key_res import DestroyAuthKeyRes
from .msgs_ack import MsgsAck
from .bad_msg_notification import BadMsgNotification
from .msgs_state_req import MsgsStateReq
from .msgs_state_info import MsgsStateInfo
from .msgs_all_info import MsgsAllInfo
from .msg_detailed_info import MsgDetailedInfo
from .msg_resend_req import MsgResendReq
from .rpc_result import RpcResult
from .rpc_error import RpcError
from .rpc_drop_answer import RpcDropAnswer
from .pong import Pong
from .destroy_session_res import DestroySessionRes
from .new_session import NewSession
from .http_wait import HttpWait
from .ip_port import IpPort
from .access_point_rule import AccessPointRule
from .input_peer import InputPeer
from .input_user import InputUser
from .input_contact import InputContact
from .input_file import InputFile
from .input_media import InputMedia
from .input_chat_photo import InputChatPhoto
from .input_geo_point import InputGeoPoint
from .input_photo import InputPhoto
from .input_file_location import InputFileLocation
from .peer import Peer
from .user import User
from .user_profile_photo import UserProfilePhoto
from .user_status import UserStatus
from .chat import Chat
from .chat_full import ChatFull
from .chat_participant import ChatParticipant
from .chat_participants import ChatParticipants
from .chat_photo import ChatPhoto
from .message import Message
from .message_media import MessageMedia
from .message_action import MessageAction
from .dialog import Dialog
from .photo import Photo
from .photo_size import PhotoSize
from .geo_point import GeoPoint
from .input_notify_peer import InputNotifyPeer
from .input_peer_notify_settings import InputPeerNotifySettings
from .peer_notify_settings import PeerNotifySettings
from .peer_settings import PeerSettings
from .wall_paper import WallPaper
from .report_reason import ReportReason
from .user_full import UserFull
from .contact import Contact
from .imported_contact import ImportedContact
from .contact_status import ContactStatus
from .messages_filter import MessagesFilter
from .update import Update
from .updates_t import Updates
from .dc_option import DcOption
from .config import Config
from .nearest_dc import NearestDc
from .encrypted_chat import EncryptedChat
from .input_encrypted_chat import InputEncryptedChat
from .encrypted_file import EncryptedFile
from .input_encrypted_file import InputEncryptedFile
from .encrypted_message import EncryptedMessage
from .input_document import InputDocument
from .document import Document
from .notify_peer import NotifyPeer
from .send_message_action import SendMessageAction
from .input_privacy_key import InputPrivacyKey
from .privacy_key import PrivacyKey
from .input_privacy_rule import InputPrivacyRule
from .privacy_rule import PrivacyRule
from .account_days_ttl import AccountDaysTTL
from .document_attribute import DocumentAttribute
from .sticker_pack import StickerPack
from .web_page import WebPage
from .authorization import Authorization
from .received_notify_message import ReceivedNotifyMessage
from .exported_chat_invite import ExportedChatInvite
from .chat_invite import ChatInvite
from .input_sticker_set import InputStickerSet
from .sticker_set import StickerSet
from .bot_command import BotCommand
from .bot_info import BotInfo
from .keyboard_button import KeyboardButton
from .keyboard_button_row import KeyboardButtonRow
from .reply_markup import ReplyMarkup
from .message_entity import MessageEntity
from .input_channel import InputChannel
from .message_range import MessageRange
from .channel_messages_filter import ChannelMessagesFilter
from .channel_participant import ChannelParticipant
from .channel_participants_filter import ChannelParticipantsFilter
from .input_bot_inline_message import InputBotInlineMessage
from .input_bot_inline_result import InputBotInlineResult
from .bot_inline_message import BotInlineMessage
from .bot_inline_result import BotInlineResult
from .exported_message_link import ExportedMessageLink
from .message_fwd_header import MessageFwdHeader
from .input_bot_inline_message_id import InputBotInlineMessageID
from .inline_bot_switch_pm import InlineBotSwitchPM
from .top_peer import TopPeer
from .top_peer_category import TopPeerCategory
from .top_peer_category_peers import TopPeerCategoryPeers
from .draft_message import DraftMessage
from .sticker_set_covered import StickerSetCovered
from .mask_coords import MaskCoords
from .input_stickered_media import InputStickeredMedia
from .game import Game
from .input_game import InputGame
from .high_score import HighScore
from .rich_text import RichText
from .page_block import PageBlock
from .phone_call_discard_reason import PhoneCallDiscardReason
from .data_json import DataJSON
from .labeled_price import LabeledPrice
from .invoice import Invoice
from .payment_charge import PaymentCharge
from .post_address import PostAddress
from .payment_requested_info import PaymentRequestedInfo
from .payment_saved_credentials import PaymentSavedCredentials
from .web_document import WebDocument
from .input_web_document import InputWebDocument
from .input_web_file_location import InputWebFileLocation
from .input_payment_credentials import InputPaymentCredentials
from .shipping_option import ShippingOption
from .input_sticker_set_item import InputStickerSetItem
from .input_phone_call import InputPhoneCall
from .phone_call import PhoneCall
from .phone_connection import PhoneConnection
from .phone_call_protocol import PhoneCallProtocol
from .cdn_public_key import CdnPublicKey
from .cdn_config import CdnConfig
from .lang_pack_string import LangPackString
from .lang_pack_difference import LangPackDifference
from .lang_pack_language import LangPackLanguage
from .channel_admin_log_event_action import ChannelAdminLogEventAction
from .channel_admin_log_event import ChannelAdminLogEvent
from .channel_admin_log_events_filter import ChannelAdminLogEventsFilter
from .popular_contact import PopularContact
from .recent_me_url import RecentMeUrl
from .input_single_media import InputSingleMedia
from .web_authorization import WebAuthorization
from .input_message import InputMessage
from .input_dialog_peer import InputDialogPeer
from .dialog_peer import DialogPeer
from .file_hash import FileHash
from .input_client_proxy import InputClientProxy
from .input_secure_file import InputSecureFile
from .secure_file import SecureFile
from .secure_data import SecureData
from .secure_plain_data import SecurePlainData
from .secure_value_type import SecureValueType
from .secure_value import SecureValue
from .input_secure_value import InputSecureValue
from .secure_value_hash import SecureValueHash
from .secure_value_error import SecureValueError
from .secure_credentials_encrypted import SecureCredentialsEncrypted
from .saved_contact import SavedContact
from .password_kdf_algo import PasswordKdfAlgo
from .secure_password_kdf_algo import SecurePasswordKdfAlgo
from .secure_secret_settings import SecureSecretSettings
from .input_check_password_srp import InputCheckPasswordSRP
from .secure_required_type import SecureRequiredType
from .input_app_event import InputAppEvent
from .json_object_value import JSONObjectValue
from .json_value import JSONValue
from .page_table_cell import PageTableCell
from .page_table_row import PageTableRow
from .page_caption import PageCaption
from .page_list_item import PageListItem
from .page_list_ordered_item import PageListOrderedItem
from .page_related_article import PageRelatedArticle
from .page import Page
from .poll_answer import PollAnswer
from .poll import Poll
from .poll_answer_voters import PollAnswerVoters
from .poll_results import PollResults
from .chat_onlines import ChatOnlines
from .stats_url import StatsURL
from .chat_admin_rights import ChatAdminRights
from .chat_banned_rights import ChatBannedRights
from .input_wall_paper import InputWallPaper
from .code_settings import CodeSettings
from .wall_paper_settings import WallPaperSettings
from .auto_download_settings import AutoDownloadSettings
from .emoji_keyword import EmojiKeyword
from .emoji_keywords_difference import EmojiKeywordsDifference
from .emoji_url import EmojiURL
from .emoji_language import EmojiLanguage
from .folder import Folder
from .input_folder_peer import InputFolderPeer
from .folder_peer import FolderPeer
from .url_auth_result import UrlAuthResult
from .channel_location import ChannelLocation
from .peer_located import PeerLocated
from .restriction_reason import RestrictionReason
from .input_theme import InputTheme
from .theme import Theme
from .base_theme import BaseTheme
from .input_theme_settings import InputThemeSettings
from .theme_settings import ThemeSettings
from .web_page_attribute import WebPageAttribute
from .bank_card_open_url import BankCardOpenUrl
from .dialog_filter import DialogFilter
from .dialog_filter_suggested import DialogFilterSuggested
from .stats_date_range_days import StatsDateRangeDays
from .stats_abs_value_and_prev import StatsAbsValueAndPrev
from .stats_percent_value import StatsPercentValue
from .stats_graph import StatsGraph
from .video_size import VideoSize
from .stats_group_top_poster import StatsGroupTopPoster
from .stats_group_top_admin import StatsGroupTopAdmin
from .stats_group_top_inviter import StatsGroupTopInviter
from .global_privacy_settings import GlobalPrivacySettings
from .message_views import MessageViews
from .message_reply_header import MessageReplyHeader
from .message_replies import MessageReplies
from .peer_blocked import PeerBlocked
from .group_call import GroupCall
from .input_group_call import InputGroupCall
from .group_call_participant import GroupCallParticipant
from .inline_query_peer_type import InlineQueryPeerType
from .chat_invite_importer import ChatInviteImporter
from .chat_admin_with_invites import ChatAdminWithInvites
from .group_call_participant_video_source_group import GroupCallParticipantVideoSourceGroup
from .group_call_participant_video import GroupCallParticipantVideo
from .bot_command_scope import BotCommandScope
from .chat_theme import ChatTheme
from .sponsored_message import SponsoredMessage
from .search_results_calendar_period import SearchResultsCalendarPeriod
from .search_results_position import SearchResultsPosition
from .reaction_count import ReactionCount
from .message_reactions import MessageReactions
from .available_reaction import AvailableReaction
from .message_peer_reaction import MessagePeerReaction
from .group_call_stream_channel import GroupCallStreamChannel
from .attach_menu_bot_icon_color import AttachMenuBotIconColor
from .attach_menu_bot_icon import AttachMenuBotIcon
from .attach_menu_bot import AttachMenuBot
from .attach_menu_bots import AttachMenuBots
from .attach_menu_bots_bot import AttachMenuBotsBot
from .web_view_result import WebViewResult
from .web_view_message_sent import WebViewMessageSent
from .bot_menu_button import BotMenuButton
from .notification_sound import NotificationSound
from .attach_menu_peer_type import AttachMenuPeerType
from .input_invoice import InputInvoice
from .input_store_payment_purpose import InputStorePaymentPurpose
from .payment_form_method import PaymentFormMethod
from .emoji_status import EmojiStatus
from .reaction import Reaction
from .chat_reactions import ChatReactions
from .email_verify_purpose import EmailVerifyPurpose
from .email_verification import EmailVerification
from .premium_subscription_option import PremiumSubscriptionOption
from .send_as_peer import SendAsPeer
from .message_extended_media import MessageExtendedMedia
from .sticker_keyword import StickerKeyword
from .username import Username
from .forum_topic import ForumTopic
from .default_history_ttl import DefaultHistoryTTL
from .exported_contact_token import ExportedContactToken
from .request_peer_type import RequestPeerType
from .emoji_list import EmojiList
from .emoji_group import EmojiGroup
from .text_with_entities import TextWithEntities
from .auto_save_settings import AutoSaveSettings
from .auto_save_exception import AutoSaveException
from .input_bot_app import InputBotApp
from .bot_app import BotApp
from .inline_bot_web_view import InlineBotWebView
from .read_participant_date import ReadParticipantDate
from .input_chatlist import InputChatlist
from .exported_chatlist_invite import ExportedChatlistInvite
from .message_peer_vote import MessagePeerVote
from .story_views import StoryViews
from .story_item import StoryItem
from .story_view import StoryView
from .input_reply_to import InputReplyTo
from .exported_story_link import ExportedStoryLink
from .stories_stealth_mode import StoriesStealthMode
from .media_area_coordinates import MediaAreaCoordinates
from .media_area import MediaArea
from .peer_stories import PeerStories
from .premium_gift_code_option import PremiumGiftCodeOption
from .prepaid_giveaway import PrepaidGiveaway
from .boost import Boost
from .my_boost import MyBoost
from .story_fwd_header import StoryFwdHeader
from .post_interaction_counters import PostInteractionCounters
from .public_forward import PublicForward
from .peer_color import PeerColor
from .story_reaction import StoryReaction
from .saved_dialog import SavedDialog
from .saved_reaction_tag import SavedReactionTag
from .outbox_read_date import OutboxReadDate
from .sms_job import SmsJob
from .business_weekly_open import BusinessWeeklyOpen
from .business_work_hours import BusinessWorkHours
from .business_location import BusinessLocation
from .input_business_recipients import InputBusinessRecipients
from .business_recipients import BusinessRecipients
from .business_away_message_schedule import BusinessAwayMessageSchedule
from .input_business_greeting_message import InputBusinessGreetingMessage
from .business_greeting_message import BusinessGreetingMessage
from .input_business_away_message import InputBusinessAwayMessage
from .business_away_message import BusinessAwayMessage
from .timezone import Timezone
from .quick_reply import QuickReply
from .input_quick_reply_shortcut import InputQuickReplyShortcut
from .connected_bot import ConnectedBot
from .birthday import Birthday
from .bot_business_connection import BotBusinessConnection
from .input_business_intro import InputBusinessIntro
from .business_intro import BusinessIntro
from .input_collectible import InputCollectible
from .input_business_bot_recipients import InputBusinessBotRecipients
from .business_bot_recipients import BusinessBotRecipients
from .contact_birthday import ContactBirthday
from .missing_invitee import MissingInvitee
from .input_business_chat_link import InputBusinessChatLink
from .business_chat_link import BusinessChatLink
from .requested_peer import RequestedPeer
from .sponsored_message_report_option import SponsoredMessageReportOption
from .reaction_notifications_from import ReactionNotificationsFrom
from .reactions_notify_settings import ReactionsNotifySettings
from .available_effect import AvailableEffect
from .fact_check import FactCheck
from .stars_transaction_peer import StarsTransactionPeer
from .stars_topup_option import StarsTopupOption
from .stars_transaction import StarsTransaction
from .found_story import FoundStory
from .geo_point_address import GeoPointAddress
from .stars_revenue_status import StarsRevenueStatus
from .input_stars_transaction import InputStarsTransaction
from .stars_gift_option import StarsGiftOption
from .bot_preview_media import BotPreviewMedia
from .stars_subscription_pricing import StarsSubscriptionPricing
from .stars_subscription import StarsSubscription
from .message_reactor import MessageReactor
from .stars_giveaway_option import StarsGiveawayOption
from .stars_giveaway_winners_option import StarsGiveawayWinnersOption
from .star_gift import StarGift
from .message_report_option import MessageReportOption
from .report_result import ReportResult
from .bot_app_settings import BotAppSettings
from .star_ref_program import StarRefProgram
from .connected_bot_star_ref import ConnectedBotStarRef
from .stars_amount import StarsAmount
from .bot_verifier_settings import BotVerifierSettings
from .bot_verification import BotVerification
from .star_gift_attribute import StarGiftAttribute
from .saved_star_gift import SavedStarGift
from .input_saved_star_gift import InputSavedStarGift
from .paid_reaction_privacy import PaidReactionPrivacy
from .requirement_to_contact import RequirementToContact
from .business_bot_rights import BusinessBotRights
from .disallowed_gifts_settings import DisallowedGiftsSettings
from .sponsored_peer import SponsoredPeer
from .star_gift_attribute_id import StarGiftAttributeId
from .star_gift_attribute_counter import StarGiftAttributeCounter
from .pending_suggestion import PendingSuggestion
from .todo_item import TodoItem
from .todo_list import TodoList
from .todo_completion import TodoCompletion
from .suggested_post import SuggestedPost
from .stars_rating import StarsRating
from .star_gift_collection import StarGiftCollection
from .story_album import StoryAlbum
from .search_posts_flood import SearchPostsFlood
from .profile_tab import ProfileTab
from .input_chat_theme import InputChatTheme
from .star_gift_upgrade_price import StarGiftUpgradePrice
from .group_call_message import GroupCallMessage
from .group_call_donor import GroupCallDonor
from .recent_story import RecentStory
from .auction_bid_level import AuctionBidLevel
from .star_gift_auction_state import StarGiftAuctionState
from .star_gift_auction_user_state import StarGiftAuctionUserState
from .star_gift_auction_acquired_gift import StarGiftAuctionAcquiredGift
from .star_gift_active_auction_state import StarGiftActiveAuctionState
from .input_star_gift_auction import InputStarGiftAuction
from .passkey import Passkey
from .input_passkey_response import InputPasskeyResponse
from .input_passkey_credential import InputPasskeyCredential
from .star_gift_background import StarGiftBackground
from .star_gift_auction_round import StarGiftAuctionRound
from .star_gift_attribute_rarity import StarGiftAttributeRarity
from .keyboard_button_style import KeyboardButtonStyle
from .premium_gift_option import PremiumGiftOption
from . import help, storage, auth, contacts, messages, updates, photos, upload, account, channels, payments, phone, stats, stickers, users, chatlists, bots, stories, premium, smsjobs, fragment

__all__ = [
    "ResPQ",
    "PQInnerData",
    "BindAuthKeyInner",
    "ServerDHParams",
    "ServerDHInnerData",
    "ClientDHInnerData",
    "SetClientDHParamsAnswer",
    "DestroyAuthKeyRes",
    "MsgsAck",
    "BadMsgNotification",
    "MsgsStateReq",
    "MsgsStateInfo",
    "MsgsAllInfo",
    "MsgDetailedInfo",
    "MsgResendReq",
    "RpcResult",
    "RpcError",
    "RpcDropAnswer",
    "Pong",
    "DestroySessionRes",
    "NewSession",
    "HttpWait",
    "IpPort",
    "AccessPointRule",
    "InputPeer",
    "InputUser",
    "InputContact",
    "InputFile",
    "InputMedia",
    "InputChatPhoto",
    "InputGeoPoint",
    "InputPhoto",
    "InputFileLocation",
    "Peer",
    "User",
    "UserProfilePhoto",
    "UserStatus",
    "Chat",
    "ChatFull",
    "ChatParticipant",
    "ChatParticipants",
    "ChatPhoto",
    "Message",
    "MessageMedia",
    "MessageAction",
    "Dialog",
    "Photo",
    "PhotoSize",
    "GeoPoint",
    "InputNotifyPeer",
    "InputPeerNotifySettings",
    "PeerNotifySettings",
    "PeerSettings",
    "WallPaper",
    "ReportReason",
    "UserFull",
    "Contact",
    "ImportedContact",
    "ContactStatus",
    "MessagesFilter",
    "Update",
    "Updates",
    "DcOption",
    "Config",
    "NearestDc",
    "EncryptedChat",
    "InputEncryptedChat",
    "EncryptedFile",
    "InputEncryptedFile",
    "EncryptedMessage",
    "InputDocument",
    "Document",
    "NotifyPeer",
    "SendMessageAction",
    "InputPrivacyKey",
    "PrivacyKey",
    "InputPrivacyRule",
    "PrivacyRule",
    "AccountDaysTTL",
    "DocumentAttribute",
    "StickerPack",
    "WebPage",
    "Authorization",
    "ReceivedNotifyMessage",
    "ExportedChatInvite",
    "ChatInvite",
    "InputStickerSet",
    "StickerSet",
    "BotCommand",
    "BotInfo",
    "KeyboardButton",
    "KeyboardButtonRow",
    "ReplyMarkup",
    "MessageEntity",
    "InputChannel",
    "MessageRange",
    "ChannelMessagesFilter",
    "ChannelParticipant",
    "ChannelParticipantsFilter",
    "InputBotInlineMessage",
    "InputBotInlineResult",
    "BotInlineMessage",
    "BotInlineResult",
    "ExportedMessageLink",
    "MessageFwdHeader",
    "InputBotInlineMessageID",
    "InlineBotSwitchPM",
    "TopPeer",
    "TopPeerCategory",
    "TopPeerCategoryPeers",
    "DraftMessage",
    "StickerSetCovered",
    "MaskCoords",
    "InputStickeredMedia",
    "Game",
    "InputGame",
    "HighScore",
    "RichText",
    "PageBlock",
    "PhoneCallDiscardReason",
    "DataJSON",
    "LabeledPrice",
    "Invoice",
    "PaymentCharge",
    "PostAddress",
    "PaymentRequestedInfo",
    "PaymentSavedCredentials",
    "WebDocument",
    "InputWebDocument",
    "InputWebFileLocation",
    "InputPaymentCredentials",
    "ShippingOption",
    "InputStickerSetItem",
    "InputPhoneCall",
    "PhoneCall",
    "PhoneConnection",
    "PhoneCallProtocol",
    "CdnPublicKey",
    "CdnConfig",
    "LangPackString",
    "LangPackDifference",
    "LangPackLanguage",
    "ChannelAdminLogEventAction",
    "ChannelAdminLogEvent",
    "ChannelAdminLogEventsFilter",
    "PopularContact",
    "RecentMeUrl",
    "InputSingleMedia",
    "WebAuthorization",
    "InputMessage",
    "InputDialogPeer",
    "DialogPeer",
    "FileHash",
    "InputClientProxy",
    "InputSecureFile",
    "SecureFile",
    "SecureData",
    "SecurePlainData",
    "SecureValueType",
    "SecureValue",
    "InputSecureValue",
    "SecureValueHash",
    "SecureValueError",
    "SecureCredentialsEncrypted",
    "SavedContact",
    "PasswordKdfAlgo",
    "SecurePasswordKdfAlgo",
    "SecureSecretSettings",
    "InputCheckPasswordSRP",
    "SecureRequiredType",
    "InputAppEvent",
    "JSONObjectValue",
    "JSONValue",
    "PageTableCell",
    "PageTableRow",
    "PageCaption",
    "PageListItem",
    "PageListOrderedItem",
    "PageRelatedArticle",
    "Page",
    "PollAnswer",
    "Poll",
    "PollAnswerVoters",
    "PollResults",
    "ChatOnlines",
    "StatsURL",
    "ChatAdminRights",
    "ChatBannedRights",
    "InputWallPaper",
    "CodeSettings",
    "WallPaperSettings",
    "AutoDownloadSettings",
    "EmojiKeyword",
    "EmojiKeywordsDifference",
    "EmojiURL",
    "EmojiLanguage",
    "Folder",
    "InputFolderPeer",
    "FolderPeer",
    "UrlAuthResult",
    "ChannelLocation",
    "PeerLocated",
    "RestrictionReason",
    "InputTheme",
    "Theme",
    "BaseTheme",
    "InputThemeSettings",
    "ThemeSettings",
    "WebPageAttribute",
    "BankCardOpenUrl",
    "DialogFilter",
    "DialogFilterSuggested",
    "StatsDateRangeDays",
    "StatsAbsValueAndPrev",
    "StatsPercentValue",
    "StatsGraph",
    "VideoSize",
    "StatsGroupTopPoster",
    "StatsGroupTopAdmin",
    "StatsGroupTopInviter",
    "GlobalPrivacySettings",
    "MessageViews",
    "MessageReplyHeader",
    "MessageReplies",
    "PeerBlocked",
    "GroupCall",
    "InputGroupCall",
    "GroupCallParticipant",
    "InlineQueryPeerType",
    "ChatInviteImporter",
    "ChatAdminWithInvites",
    "GroupCallParticipantVideoSourceGroup",
    "GroupCallParticipantVideo",
    "BotCommandScope",
    "ChatTheme",
    "SponsoredMessage",
    "SearchResultsCalendarPeriod",
    "SearchResultsPosition",
    "ReactionCount",
    "MessageReactions",
    "AvailableReaction",
    "MessagePeerReaction",
    "GroupCallStreamChannel",
    "AttachMenuBotIconColor",
    "AttachMenuBotIcon",
    "AttachMenuBot",
    "AttachMenuBots",
    "AttachMenuBotsBot",
    "WebViewResult",
    "WebViewMessageSent",
    "BotMenuButton",
    "NotificationSound",
    "AttachMenuPeerType",
    "InputInvoice",
    "InputStorePaymentPurpose",
    "PaymentFormMethod",
    "EmojiStatus",
    "Reaction",
    "ChatReactions",
    "EmailVerifyPurpose",
    "EmailVerification",
    "PremiumSubscriptionOption",
    "SendAsPeer",
    "MessageExtendedMedia",
    "StickerKeyword",
    "Username",
    "ForumTopic",
    "DefaultHistoryTTL",
    "ExportedContactToken",
    "RequestPeerType",
    "EmojiList",
    "EmojiGroup",
    "TextWithEntities",
    "AutoSaveSettings",
    "AutoSaveException",
    "InputBotApp",
    "BotApp",
    "InlineBotWebView",
    "ReadParticipantDate",
    "InputChatlist",
    "ExportedChatlistInvite",
    "MessagePeerVote",
    "StoryViews",
    "StoryItem",
    "StoryView",
    "InputReplyTo",
    "ExportedStoryLink",
    "StoriesStealthMode",
    "MediaAreaCoordinates",
    "MediaArea",
    "PeerStories",
    "PremiumGiftCodeOption",
    "PrepaidGiveaway",
    "Boost",
    "MyBoost",
    "StoryFwdHeader",
    "PostInteractionCounters",
    "PublicForward",
    "PeerColor",
    "StoryReaction",
    "SavedDialog",
    "SavedReactionTag",
    "OutboxReadDate",
    "SmsJob",
    "BusinessWeeklyOpen",
    "BusinessWorkHours",
    "BusinessLocation",
    "InputBusinessRecipients",
    "BusinessRecipients",
    "BusinessAwayMessageSchedule",
    "InputBusinessGreetingMessage",
    "BusinessGreetingMessage",
    "InputBusinessAwayMessage",
    "BusinessAwayMessage",
    "Timezone",
    "QuickReply",
    "InputQuickReplyShortcut",
    "ConnectedBot",
    "Birthday",
    "BotBusinessConnection",
    "InputBusinessIntro",
    "BusinessIntro",
    "InputCollectible",
    "InputBusinessBotRecipients",
    "BusinessBotRecipients",
    "ContactBirthday",
    "MissingInvitee",
    "InputBusinessChatLink",
    "BusinessChatLink",
    "RequestedPeer",
    "SponsoredMessageReportOption",
    "ReactionNotificationsFrom",
    "ReactionsNotifySettings",
    "AvailableEffect",
    "FactCheck",
    "StarsTransactionPeer",
    "StarsTopupOption",
    "StarsTransaction",
    "FoundStory",
    "GeoPointAddress",
    "StarsRevenueStatus",
    "InputStarsTransaction",
    "StarsGiftOption",
    "BotPreviewMedia",
    "StarsSubscriptionPricing",
    "StarsSubscription",
    "MessageReactor",
    "StarsGiveawayOption",
    "StarsGiveawayWinnersOption",
    "StarGift",
    "MessageReportOption",
    "ReportResult",
    "BotAppSettings",
    "StarRefProgram",
    "ConnectedBotStarRef",
    "StarsAmount",
    "BotVerifierSettings",
    "BotVerification",
    "StarGiftAttribute",
    "SavedStarGift",
    "InputSavedStarGift",
    "PaidReactionPrivacy",
    "RequirementToContact",
    "BusinessBotRights",
    "DisallowedGiftsSettings",
    "SponsoredPeer",
    "StarGiftAttributeId",
    "StarGiftAttributeCounter",
    "PendingSuggestion",
    "TodoItem",
    "TodoList",
    "TodoCompletion",
    "SuggestedPost",
    "StarsRating",
    "StarGiftCollection",
    "StoryAlbum",
    "SearchPostsFlood",
    "ProfileTab",
    "InputChatTheme",
    "StarGiftUpgradePrice",
    "GroupCallMessage",
    "GroupCallDonor",
    "RecentStory",
    "AuctionBidLevel",
    "StarGiftAuctionState",
    "StarGiftAuctionUserState",
    "StarGiftAuctionAcquiredGift",
    "StarGiftActiveAuctionState",
    "InputStarGiftAuction",
    "Passkey",
    "InputPasskeyResponse",
    "InputPasskeyCredential",
    "StarGiftBackground",
    "StarGiftAuctionRound",
    "StarGiftAttributeRarity",
    "KeyboardButtonStyle",
    "PremiumGiftOption",
    "help",
    "storage",
    "auth",
    "contacts",
    "messages",
    "updates",
    "photos",
    "upload",
    "account",
    "channels",
    "payments",
    "phone",
    "stats",
    "stickers",
    "users",
    "chatlists",
    "bots",
    "stories",
    "premium",
    "smsjobs",
    "fragment",
]
