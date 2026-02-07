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


class UpdateShortSentMessage(TLObject):  # type: ignore
    """Shortened constructor containing info on one outgoing message to a contact (the destination chat has to be extracted from the method call that returned this object).

    Constructor of :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``224``
        - ID: ``9015E101``

    Parameters:
        id (``int`` ``32-bit``):
            ID of the sent message

        pts (``int`` ``32-bit``):
            PTS

        pts_count (``int`` ``32-bit``):
            PTS count

        date (``int`` ``32-bit``):
            date

        out (``bool``, *optional*):
            Whether the message is outgoing

        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            Attached media

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Entities for styled text

        ttl_period (``int`` ``32-bit``, *optional*):
            Time To Live of the message, once message.date+message.ttl_period === time(), the message will be deleted on the server, and must be deleted locally as well.

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

    __slots__: List[str] = ["id", "pts", "pts_count", "date", "out", "media", "entities", "ttl_period"]

    ID = 0x9015e101
    QUALNAME = "types.UpdateShortSentMessage"

    def __init__(self, *, id: int, pts: int, pts_count: int, date: int, out: Optional[bool] = None, media: "raw.base.MessageMedia" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, ttl_period: Optional[int] = None) -> None:
        self.id = id  # int
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # int
        self.out = out  # flags.1?true
        self.media = media  # flags.9?MessageMedia
        self.entities = entities  # flags.7?Vector<MessageEntity>
        self.ttl_period = ttl_period  # flags.25?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShortSentMessage":

        flags = Int.read(b)

        out = True if flags & (1 << 1) else False
        id = Int.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        date = Int.read(b)

        media = TLObject.read(b) if flags & (1 << 9) else None

        entities = TLObject.read(b) if flags & (1 << 7) else []

        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return UpdateShortSentMessage(id=id, pts=pts, pts_count=pts_count, date=date, out=out, media=media, entities=entities, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 9) if self.media is not None else 0
        flags |= (1 << 7) if self.entities else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        b.write(Int(self.date))

        if self.media is not None:
            b.write(self.media.write())

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))

        return b.getvalue()
