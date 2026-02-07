# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Update = Union["raw.types.UpdateAttachMenuBots", "raw.types.UpdateAutoSaveSettings", "raw.types.UpdateBotBusinessConnect", "raw.types.UpdateBotCallbackQuery", "raw.types.UpdateBotChatBoost", "raw.types.UpdateBotChatInviteRequester", "raw.types.UpdateBotCommands", "raw.types.UpdateBotDeleteBusinessMessage", "raw.types.UpdateBotEditBusinessMessage", "raw.types.UpdateBotInlineQuery", "raw.types.UpdateBotInlineSend", "raw.types.UpdateBotMenuButton", "raw.types.UpdateBotMessageReaction", "raw.types.UpdateBotMessageReactions", "raw.types.UpdateBotNewBusinessMessage", "raw.types.UpdateBotPrecheckoutQuery", "raw.types.UpdateBotPurchasedPaidMedia", "raw.types.UpdateBotShippingQuery", "raw.types.UpdateBotStopped", "raw.types.UpdateBotSubscriptionExpire", "raw.types.UpdateBotWebhookJSON", "raw.types.UpdateBotWebhookJSONQuery", "raw.types.UpdateBusinessBotCallbackQuery", "raw.types.UpdateChannel", "raw.types.UpdateChannelAvailableMessages", "raw.types.UpdateChannelMessageForwards", "raw.types.UpdateChannelMessageViews", "raw.types.UpdateChannelParticipant", "raw.types.UpdateChannelReadMessagesContents", "raw.types.UpdateChannelTooLong", "raw.types.UpdateChannelUserTyping", "raw.types.UpdateChannelViewForumAsMessages", "raw.types.UpdateChannelWebPage", "raw.types.UpdateChat", "raw.types.UpdateChatDefaultBannedRights", "raw.types.UpdateChatParticipant", "raw.types.UpdateChatParticipantAdd", "raw.types.UpdateChatParticipantAdmin", "raw.types.UpdateChatParticipantDelete", "raw.types.UpdateChatParticipants", "raw.types.UpdateChatUserTyping", "raw.types.UpdateConfig", "raw.types.UpdateContactsReset", "raw.types.UpdateDcOptions", "raw.types.UpdateDeleteChannelMessages", "raw.types.UpdateDeleteGroupCallMessages", "raw.types.UpdateDeleteMessages", "raw.types.UpdateDeleteQuickReply", "raw.types.UpdateDeleteQuickReplyMessages", "raw.types.UpdateDeleteScheduledMessages", "raw.types.UpdateDialogFilter", "raw.types.UpdateDialogFilterOrder", "raw.types.UpdateDialogFilters", "raw.types.UpdateDialogPinned", "raw.types.UpdateDialogUnreadMark", "raw.types.UpdateDraftMessage", "raw.types.UpdateEditChannelMessage", "raw.types.UpdateEditMessage", "raw.types.UpdateEmojiGameInfo", "raw.types.UpdateEncryptedChatTyping", "raw.types.UpdateEncryptedMessagesRead", "raw.types.UpdateEncryption", "raw.types.UpdateFavedStickers", "raw.types.UpdateFolderPeers", "raw.types.UpdateGeoLiveViewed", "raw.types.UpdateGroupCall", "raw.types.UpdateGroupCallChainBlocks", "raw.types.UpdateGroupCallConnection", "raw.types.UpdateGroupCallEncryptedMessage", "raw.types.UpdateGroupCallMessage", "raw.types.UpdateGroupCallParticipants", "raw.types.UpdateInlineBotCallbackQuery", "raw.types.UpdateLangPack", "raw.types.UpdateLangPackTooLong", "raw.types.UpdateLoginToken", "raw.types.UpdateMessageExtendedMedia", "raw.types.UpdateMessageID", "raw.types.UpdateMessagePoll", "raw.types.UpdateMessagePollVote", "raw.types.UpdateMessageReactions", "raw.types.UpdateMonoForumNoPaidException", "raw.types.UpdateMoveStickerSetToTop", "raw.types.UpdateNewAuthorization", "raw.types.UpdateNewChannelMessage", "raw.types.UpdateNewEncryptedMessage", "raw.types.UpdateNewMessage", "raw.types.UpdateNewQuickReply", "raw.types.UpdateNewScheduledMessage", "raw.types.UpdateNewStickerSet", "raw.types.UpdateNewStoryReaction", "raw.types.UpdateNotifySettings", "raw.types.UpdatePaidReactionPrivacy", "raw.types.UpdatePeerBlocked", "raw.types.UpdatePeerHistoryTTL", "raw.types.UpdatePeerLocated", "raw.types.UpdatePeerSettings", "raw.types.UpdatePeerWallpaper", "raw.types.UpdatePendingJoinRequests", "raw.types.UpdatePhoneCall", "raw.types.UpdatePhoneCallSignalingData", "raw.types.UpdatePinnedChannelMessages", "raw.types.UpdatePinnedDialogs", "raw.types.UpdatePinnedForumTopic", "raw.types.UpdatePinnedForumTopics", "raw.types.UpdatePinnedMessages", "raw.types.UpdatePinnedSavedDialogs", "raw.types.UpdatePrivacy", "raw.types.UpdatePtsChanged", "raw.types.UpdateQuickReplies", "raw.types.UpdateQuickReplyMessage", "raw.types.UpdateReadChannelDiscussionInbox", "raw.types.UpdateReadChannelDiscussionOutbox", "raw.types.UpdateReadChannelInbox", "raw.types.UpdateReadChannelOutbox", "raw.types.UpdateReadFeaturedEmojiStickers", "raw.types.UpdateReadFeaturedStickers", "raw.types.UpdateReadHistoryInbox", "raw.types.UpdateReadHistoryOutbox", "raw.types.UpdateReadMessagesContents", "raw.types.UpdateReadMonoForumInbox", "raw.types.UpdateReadMonoForumOutbox", "raw.types.UpdateReadStories", "raw.types.UpdateRecentEmojiStatuses", "raw.types.UpdateRecentReactions", "raw.types.UpdateRecentStickers", "raw.types.UpdateSavedDialogPinned", "raw.types.UpdateSavedGifs", "raw.types.UpdateSavedReactionTags", "raw.types.UpdateSavedRingtones", "raw.types.UpdateSentPhoneCode", "raw.types.UpdateSentStoryReaction", "raw.types.UpdateServiceNotification", "raw.types.UpdateSmsJob", "raw.types.UpdateStarGiftAuctionState", "raw.types.UpdateStarGiftAuctionUserState", "raw.types.UpdateStarGiftCraftFail", "raw.types.UpdateStarsBalance", "raw.types.UpdateStarsRevenueStatus", "raw.types.UpdateStickerSets", "raw.types.UpdateStickerSetsOrder", "raw.types.UpdateStoriesStealthMode", "raw.types.UpdateStory", "raw.types.UpdateStoryID", "raw.types.UpdateTheme", "raw.types.UpdateTranscribeAudio", "raw.types.UpdateTranscribedAudio", "raw.types.UpdateUser", "raw.types.UpdateUserEmojiStatus", "raw.types.UpdateUserName", "raw.types.UpdateUserPhone", "raw.types.UpdateUserStatus", "raw.types.UpdateUserTyping", "raw.types.UpdateWebPage", "raw.types.UpdateWebViewResultSent"]


class Update:  # type: ignore
    """Object contains info on events occurred.

    Constructors:
        This base type has 154 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UpdateAttachMenuBots
            UpdateAutoSaveSettings
            UpdateBotBusinessConnect
            UpdateBotCallbackQuery
            UpdateBotChatBoost
            UpdateBotChatInviteRequester
            UpdateBotCommands
            UpdateBotDeleteBusinessMessage
            UpdateBotEditBusinessMessage
            UpdateBotInlineQuery
            UpdateBotInlineSend
            UpdateBotMenuButton
            UpdateBotMessageReaction
            UpdateBotMessageReactions
            UpdateBotNewBusinessMessage
            UpdateBotPrecheckoutQuery
            UpdateBotPurchasedPaidMedia
            UpdateBotShippingQuery
            UpdateBotStopped
            UpdateBotSubscriptionExpire
            UpdateBotWebhookJSON
            UpdateBotWebhookJSONQuery
            UpdateBusinessBotCallbackQuery
            UpdateChannel
            UpdateChannelAvailableMessages
            UpdateChannelMessageForwards
            UpdateChannelMessageViews
            UpdateChannelParticipant
            UpdateChannelReadMessagesContents
            UpdateChannelTooLong
            UpdateChannelUserTyping
            UpdateChannelViewForumAsMessages
            UpdateChannelWebPage
            UpdateChat
            UpdateChatDefaultBannedRights
            UpdateChatParticipant
            UpdateChatParticipantAdd
            UpdateChatParticipantAdmin
            UpdateChatParticipantDelete
            UpdateChatParticipants
            UpdateChatUserTyping
            UpdateConfig
            UpdateContactsReset
            UpdateDcOptions
            UpdateDeleteChannelMessages
            UpdateDeleteGroupCallMessages
            UpdateDeleteMessages
            UpdateDeleteQuickReply
            UpdateDeleteQuickReplyMessages
            UpdateDeleteScheduledMessages
            UpdateDialogFilter
            UpdateDialogFilterOrder
            UpdateDialogFilters
            UpdateDialogPinned
            UpdateDialogUnreadMark
            UpdateDraftMessage
            UpdateEditChannelMessage
            UpdateEditMessage
            UpdateEmojiGameInfo
            UpdateEncryptedChatTyping
            UpdateEncryptedMessagesRead
            UpdateEncryption
            UpdateFavedStickers
            UpdateFolderPeers
            UpdateGeoLiveViewed
            UpdateGroupCall
            UpdateGroupCallChainBlocks
            UpdateGroupCallConnection
            UpdateGroupCallEncryptedMessage
            UpdateGroupCallMessage
            UpdateGroupCallParticipants
            UpdateInlineBotCallbackQuery
            UpdateLangPack
            UpdateLangPackTooLong
            UpdateLoginToken
            UpdateMessageExtendedMedia
            UpdateMessageID
            UpdateMessagePoll
            UpdateMessagePollVote
            UpdateMessageReactions
            UpdateMonoForumNoPaidException
            UpdateMoveStickerSetToTop
            UpdateNewAuthorization
            UpdateNewChannelMessage
            UpdateNewEncryptedMessage
            UpdateNewMessage
            UpdateNewQuickReply
            UpdateNewScheduledMessage
            UpdateNewStickerSet
            UpdateNewStoryReaction
            UpdateNotifySettings
            UpdatePaidReactionPrivacy
            UpdatePeerBlocked
            UpdatePeerHistoryTTL
            UpdatePeerLocated
            UpdatePeerSettings
            UpdatePeerWallpaper
            UpdatePendingJoinRequests
            UpdatePhoneCall
            UpdatePhoneCallSignalingData
            UpdatePinnedChannelMessages
            UpdatePinnedDialogs
            UpdatePinnedForumTopic
            UpdatePinnedForumTopics
            UpdatePinnedMessages
            UpdatePinnedSavedDialogs
            UpdatePrivacy
            UpdatePtsChanged
            UpdateQuickReplies
            UpdateQuickReplyMessage
            UpdateReadChannelDiscussionInbox
            UpdateReadChannelDiscussionOutbox
            UpdateReadChannelInbox
            UpdateReadChannelOutbox
            UpdateReadFeaturedEmojiStickers
            UpdateReadFeaturedStickers
            UpdateReadHistoryInbox
            UpdateReadHistoryOutbox
            UpdateReadMessagesContents
            UpdateReadMonoForumInbox
            UpdateReadMonoForumOutbox
            UpdateReadStories
            UpdateRecentEmojiStatuses
            UpdateRecentReactions
            UpdateRecentStickers
            UpdateSavedDialogPinned
            UpdateSavedGifs
            UpdateSavedReactionTags
            UpdateSavedRingtones
            UpdateSentPhoneCode
            UpdateSentStoryReaction
            UpdateServiceNotification
            UpdateSmsJob
            UpdateStarGiftAuctionState
            UpdateStarGiftAuctionUserState
            UpdateStarGiftCraftFail
            UpdateStarsBalance
            UpdateStarsRevenueStatus
            UpdateStickerSets
            UpdateStickerSetsOrder
            UpdateStoriesStealthMode
            UpdateStory
            UpdateStoryID
            UpdateTheme
            UpdateTranscribeAudio
            UpdateTranscribedAudio
            UpdateUser
            UpdateUserEmojiStatus
            UpdateUserName
            UpdateUserPhone
            UpdateUserStatus
            UpdateUserTyping
            UpdateWebPage
            UpdateWebViewResultSent
    """

    QUALNAME = "pyrogram.raw.base.Update"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
