# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from .dialogs import Dialogs
from .dialogs_slice import DialogsSlice
from .dialogs_not_modified import DialogsNotModified
from .messages import Messages
from .messages_slice import MessagesSlice
from .channel_messages import ChannelMessages
from .messages_not_modified import MessagesNotModified
from .chats import Chats
from .chats_slice import ChatsSlice
from .chat_full import ChatFull
from .affected_history import AffectedHistory
from .dh_config_not_modified import DhConfigNotModified
from .dh_config import DhConfig
from .sent_encrypted_message import SentEncryptedMessage
from .sent_encrypted_file import SentEncryptedFile
from .stickers_not_modified import StickersNotModified
from .stickers import Stickers
from .all_stickers_not_modified import AllStickersNotModified
from .all_stickers import AllStickers
from .affected_messages import AffectedMessages
from .sticker_set import StickerSet
from .sticker_set_not_modified import StickerSetNotModified
from .saved_gifs_not_modified import SavedGifsNotModified
from .saved_gifs import SavedGifs
from .bot_results import BotResults
from .bot_callback_answer import BotCallbackAnswer
from .message_edit_data import MessageEditData
from .peer_dialogs import PeerDialogs
from .featured_stickers_not_modified import FeaturedStickersNotModified
from .featured_stickers import FeaturedStickers
from .recent_stickers_not_modified import RecentStickersNotModified
from .recent_stickers import RecentStickers
from .archived_stickers import ArchivedStickers
from .sticker_set_install_result_success import StickerSetInstallResultSuccess
from .sticker_set_install_result_archive import StickerSetInstallResultArchive
from .high_scores import HighScores
from .faved_stickers_not_modified import FavedStickersNotModified
from .faved_stickers import FavedStickers
from .found_sticker_sets_not_modified import FoundStickerSetsNotModified
from .found_sticker_sets import FoundStickerSets
from .search_counter import SearchCounter
from .inactive_chats import InactiveChats
from .votes_list import VotesList
from .message_views import MessageViews
from .discussion_message import DiscussionMessage
from .history_import import HistoryImport
from .history_import_parsed import HistoryImportParsed
from .affected_found_messages import AffectedFoundMessages
from .exported_chat_invites import ExportedChatInvites
from .exported_chat_invite import ExportedChatInvite
from .exported_chat_invite_replaced import ExportedChatInviteReplaced
from .chat_invite_importers import ChatInviteImporters
from .chat_admins_with_invites import ChatAdminsWithInvites
from .checked_history_import_peer import CheckedHistoryImportPeer
from .sponsored_messages import SponsoredMessages
from .sponsored_messages_empty import SponsoredMessagesEmpty
from .search_results_calendar import SearchResultsCalendar
from .search_results_positions import SearchResultsPositions
from .peer_settings import PeerSettings
from .message_reactions_list import MessageReactionsList
from .available_reactions_not_modified import AvailableReactionsNotModified
from .available_reactions import AvailableReactions
from .transcribed_audio import TranscribedAudio
from .reactions_not_modified import ReactionsNotModified
from .reactions import Reactions
from .forum_topics import ForumTopics
from .emoji_groups_not_modified import EmojiGroupsNotModified
from .emoji_groups import EmojiGroups
from .translate_result import TranslateResult
from .bot_app import BotApp
from .web_page import WebPage
from .saved_dialogs import SavedDialogs
from .saved_dialogs_slice import SavedDialogsSlice
from .saved_dialogs_not_modified import SavedDialogsNotModified
from .saved_reaction_tags_not_modified import SavedReactionTagsNotModified
from .saved_reaction_tags import SavedReactionTags
from .quick_replies import QuickReplies
from .quick_replies_not_modified import QuickRepliesNotModified
from .dialog_filters import DialogFilters
from .my_stickers import MyStickers
from .invited_users import InvitedUsers
from .available_effects_not_modified import AvailableEffectsNotModified
from .available_effects import AvailableEffects
from .bot_prepared_inline_message import BotPreparedInlineMessage
from .prepared_inline_message import PreparedInlineMessage
from .found_stickers_not_modified import FoundStickersNotModified
from .found_stickers import FoundStickers
from .web_page_preview import WebPagePreview
from .emoji_game_outcome import EmojiGameOutcome
from .emoji_game_unavailable import EmojiGameUnavailable
from .emoji_game_dice_info import EmojiGameDiceInfo
from .message_empty import MessageEmpty
from .web_view_result import WebViewResult


__all__ = [
    "Dialogs",
    "DialogsSlice",
    "DialogsNotModified",
    "Messages",
    "MessagesSlice",
    "ChannelMessages",
    "MessagesNotModified",
    "Chats",
    "ChatsSlice",
    "ChatFull",
    "AffectedHistory",
    "DhConfigNotModified",
    "DhConfig",
    "SentEncryptedMessage",
    "SentEncryptedFile",
    "StickersNotModified",
    "Stickers",
    "AllStickersNotModified",
    "AllStickers",
    "AffectedMessages",
    "StickerSet",
    "StickerSetNotModified",
    "SavedGifsNotModified",
    "SavedGifs",
    "BotResults",
    "BotCallbackAnswer",
    "MessageEditData",
    "PeerDialogs",
    "FeaturedStickersNotModified",
    "FeaturedStickers",
    "RecentStickersNotModified",
    "RecentStickers",
    "ArchivedStickers",
    "StickerSetInstallResultSuccess",
    "StickerSetInstallResultArchive",
    "HighScores",
    "FavedStickersNotModified",
    "FavedStickers",
    "FoundStickerSetsNotModified",
    "FoundStickerSets",
    "SearchCounter",
    "InactiveChats",
    "VotesList",
    "MessageViews",
    "DiscussionMessage",
    "HistoryImport",
    "HistoryImportParsed",
    "AffectedFoundMessages",
    "ExportedChatInvites",
    "ExportedChatInvite",
    "ExportedChatInviteReplaced",
    "ChatInviteImporters",
    "ChatAdminsWithInvites",
    "CheckedHistoryImportPeer",
    "SponsoredMessages",
    "SponsoredMessagesEmpty",
    "SearchResultsCalendar",
    "SearchResultsPositions",
    "PeerSettings",
    "MessageReactionsList",
    "AvailableReactionsNotModified",
    "AvailableReactions",
    "TranscribedAudio",
    "ReactionsNotModified",
    "Reactions",
    "ForumTopics",
    "EmojiGroupsNotModified",
    "EmojiGroups",
    "TranslateResult",
    "BotApp",
    "WebPage",
    "SavedDialogs",
    "SavedDialogsSlice",
    "SavedDialogsNotModified",
    "SavedReactionTagsNotModified",
    "SavedReactionTags",
    "QuickReplies",
    "QuickRepliesNotModified",
    "DialogFilters",
    "MyStickers",
    "InvitedUsers",
    "AvailableEffectsNotModified",
    "AvailableEffects",
    "BotPreparedInlineMessage",
    "PreparedInlineMessage",
    "FoundStickersNotModified",
    "FoundStickers",
    "WebPagePreview",
    "EmojiGameOutcome",
    "EmojiGameUnavailable",
    "EmojiGameDiceInfo",
    "MessageEmpty",
    "WebViewResult",
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
