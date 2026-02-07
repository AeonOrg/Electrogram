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


class UpdateShort(TLObject):  # type: ignore
    """Shortened constructor containing info on one update not requiring auxiliary data

    Constructor of :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``224``
        - ID: ``78D4DEC1``

    Parameters:
        update (:obj:`Update <pyrogram.raw.base.Update>`):
            Update

        date (``int`` ``32-bit``):
            Date of event

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

    __slots__: List[str] = ["update", "date"]

    ID = 0x78d4dec1
    QUALNAME = "types.UpdateShort"

    def __init__(self, *, update: "raw.base.Update", date: int) -> None:
        self.update = update  # Update
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShort":
        # No flags

        update = TLObject.read(b)

        date = Int.read(b)

        return UpdateShort(update=update, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.update.write())

        b.write(Int(self.date))

        return b.getvalue()
