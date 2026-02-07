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


class UpdatesCombined(TLObject):  # type: ignore
    """Constructor for a group of updates.

    Constructor of :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``224``
        - ID: ``725B04C3``

    Parameters:
        updates (List of :obj:`Update <pyrogram.raw.base.Update>`):
            List of updates

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users mentioned in updates

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            List of chats mentioned in updates

        date (``int`` ``32-bit``):
            Current date

        seq_start (``int`` ``32-bit``):
            Value seq for the earliest update in a group

        seq (``int`` ``32-bit``):
            Value seq for the latest update in a group

    Functions:
        This object can be returned by 130 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetNotifyExceptions
            account.UpdateConnectedBot
            account.GetBotBusinessConnection
            users.SuggestBirthday
            contacts.DeleteContacts
            contacts.AddContact
            contacts.AcceptContact
            contacts.GetLocated
            contacts.BlockFromReplies
            messages.SendMessage
            messages.SendMedia
            messages.ForwardMessages
            messages.EditChatTitle
            messages.EditChatPhoto
            messages.DeleteChatUser
            messages.ImportChatInvite
            messages.StartBot
            messages.MigrateChat
            messages.SendInlineBotResult
            messages.EditMessage
            messages.GetAllDrafts
            messages.SetGameScore
            messages.SendScreenshotNotification
            messages.SendMultiMedia
            messages.UpdatePinnedMessage
            messages.SendVote
            messages.GetPollResults
            messages.EditChatDefaultBannedRights
            messages.SendScheduledMessages
            messages.DeleteScheduledMessages
            messages.SetHistoryTTL
            messages.SetChatTheme
            messages.HideChatJoinRequest
            messages.HideAllChatJoinRequests
            messages.ToggleNoForwards
            messages.SendReaction
            messages.GetMessagesReactions
            messages.SetChatAvailableReactions
            messages.SendWebViewData
            messages.GetExtendedMedia
            messages.SendBotRequestedPeer
            messages.SetChatWallPaper
            messages.SendQuickReplyMessages
            messages.DeleteQuickReplyMessages
            messages.EditFactCheck
            messages.DeleteFactCheck
            messages.SendPaidReaction
            messages.GetPaidReactionPrivacy
            messages.ToggleTodoCompleted
            messages.AppendTodoList
            messages.ToggleSuggestedPostApproval
            messages.EditForumTopic
            messages.UpdatePinnedForumTopic
            messages.ReorderPinnedForumTopics
            messages.CreateForumTopic
            messages.ForwardMessage
            messages.CraftStarGift
            channels.CreateChannel
            channels.EditAdmin
            channels.EditTitle
            channels.EditPhoto
            channels.JoinChannel
            channels.LeaveChannel
            channels.DeleteChannel
            channels.ToggleSignatures
            channels.EditBanned
            channels.DeleteHistory
            channels.TogglePreHistoryHidden
            channels.EditCreator
            channels.ToggleSlowMode
            channels.ConvertToGigagroup
            channels.ToggleJoinToSend
            channels.ToggleJoinRequest
            channels.ToggleForum
            channels.ToggleAntiSpam
            channels.ToggleParticipantsHidden
            channels.UpdateColor
            channels.ToggleViewForumAsMessages
            channels.UpdateEmojiStatus
            channels.SetBoostsToUnblockRestrictions
            channels.RestrictSponsoredMessages
            channels.UpdatePaidMessagesPrice
            channels.ToggleAutotranslation
            bots.AllowSendMessage
            payments.AssignAppStoreTransaction
            payments.AssignPlayMarketTransaction
            payments.ApplyGiftCode
            payments.LaunchPrepaidGiveaway
            payments.RefundStarsCharge
            payments.UpgradeStarGift
            payments.TransferStarGift
            payments.UpdateStarGiftPrice
            payments.ResolveStarGiftOffer
            payments.SendStarGiftOffer
            payments.RequestRecurringPayment
            phone.DiscardCall
            phone.SetCallRating
            phone.CreateGroupCall
            phone.JoinGroupCall
            phone.LeaveGroupCall
            phone.InviteToGroupCall
            phone.DiscardGroupCall
            phone.ToggleGroupCallSettings
            phone.ToggleGroupCallRecord
            phone.EditGroupCallParticipant
            phone.EditGroupCallTitle
            phone.ToggleGroupCallStartSubscription
            phone.StartScheduledGroupCall
            phone.JoinGroupCallPresentation
            phone.LeaveGroupCallPresentation
            phone.CreateConferenceCall
            phone.DeleteConferenceCallParticipants
            phone.SendConferenceCallBroadcast
            phone.InviteConferenceCallParticipant
            phone.DeclineConferenceCallInvite
            phone.GetGroupCallChainBlocks
            phone.SendGroupCallMessage
            phone.DeleteGroupCallMessages
            phone.DeleteGroupCallParticipantMessages
            folders.EditPeerFolders
            folders.DeleteFolder
            chatlists.JoinChatlistInvite
            chatlists.JoinChatlistUpdates
            chatlists.LeaveChatlist
            stories.SendStory
            stories.EditStory
            stories.ActivateStealthMode
            stories.SendReaction
            stories.GetAllReadPeerStories
            stories.StartLive
    """

    __slots__: List[str] = ["updates", "users", "chats", "date", "seq_start", "seq"]

    ID = 0x725b04c3
    QUALNAME = "types.UpdatesCombined"

    def __init__(self, *, updates: List["raw.base.Update"], users: List["raw.base.User"], chats: List["raw.base.Chat"], date: int, seq_start: int, seq: int) -> None:
        self.updates = updates  # Vector<Update>
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>
        self.date = date  # int
        self.seq_start = seq_start  # int
        self.seq = seq  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatesCombined":
        # No flags

        updates = TLObject.read(b)

        users = TLObject.read(b)

        chats = TLObject.read(b)

        date = Int.read(b)

        seq_start = Int.read(b)

        seq = Int.read(b)

        return UpdatesCombined(updates=updates, users=users, chats=chats, date=date, seq_start=seq_start, seq=seq)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.updates))

        b.write(Vector(self.users))

        b.write(Vector(self.chats))

        b.write(Int(self.date))

        b.write(Int(self.seq_start))

        b.write(Int(self.seq))

        return b.getvalue()
