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


class UpdateShortChatMessage(TLObject):  # type: ignore
    """Shortened constructor containing info on one new incoming text message from a chat

    Constructor of :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``224``
        - ID: ``4D6DEEA5``

    Parameters:
        id (``int`` ``32-bit``):
            ID of the message

        from_id (``int`` ``64-bit``):
            ID of the sender of the message

        chat_id (``int`` ``64-bit``):
            ID of the chat where the message was sent

        message (``str``):
            Message

        pts (``int`` ``32-bit``):
            PTS

        pts_count (``int`` ``32-bit``):
            PTS count

        date (``int`` ``32-bit``):
            date

        out (``bool``, *optional*):
            Whether the message is outgoing

        mentioned (``bool``, *optional*):
            Whether we were mentioned in this message

        media_unread (``bool``, *optional*):
            Whether the message contains some unread mentions

        silent (``bool``, *optional*):
            If true, the message is a silent message, no notifications should be triggered

        fwd_from (:obj:`MessageFwdHeader <pyrogram.raw.base.MessageFwdHeader>`, *optional*):
            Info about a forwarded message

        via_bot_id (``int`` ``64-bit``, *optional*):
            Info about the inline bot used to generate this message

        reply_to (:obj:`MessageReplyHeader <pyrogram.raw.base.MessageReplyHeader>`, *optional*):
            Reply (thread) information

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Entities for styled text

        ttl_period (``int`` ``32-bit``, *optional*):
            Time To Live of the message, once updateShortChatMessage.date+updateShortChatMessage.ttl_period === time(), the message will be deleted on the server, and must be deleted locally as well.

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

    __slots__: List[str] = ["id", "from_id", "chat_id", "message", "pts", "pts_count", "date", "out", "mentioned", "media_unread", "silent", "fwd_from", "via_bot_id", "reply_to", "entities", "ttl_period"]

    ID = 0x4d6deea5
    QUALNAME = "types.UpdateShortChatMessage"

    def __init__(self, *, id: int, from_id: int, chat_id: int, message: str, pts: int, pts_count: int, date: int, out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, fwd_from: "raw.base.MessageFwdHeader" = None, via_bot_id: Optional[int] = None, reply_to: "raw.base.MessageReplyHeader" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, ttl_period: Optional[int] = None) -> None:
        self.id = id  # int
        self.from_id = from_id  # long
        self.chat_id = chat_id  # long
        self.message = message  # string
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # int
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.fwd_from = fwd_from  # flags.2?MessageFwdHeader
        self.via_bot_id = via_bot_id  # flags.11?long
        self.reply_to = reply_to  # flags.3?MessageReplyHeader
        self.entities = entities  # flags.7?Vector<MessageEntity>
        self.ttl_period = ttl_period  # flags.25?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShortChatMessage":

        flags = Int.read(b)

        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        id = Int.read(b)

        from_id = Long.read(b)

        chat_id = Long.read(b)

        message = String.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        date = Int.read(b)

        fwd_from = TLObject.read(b) if flags & (1 << 2) else None

        via_bot_id = Long.read(b) if flags & (1 << 11) else None
        reply_to = TLObject.read(b) if flags & (1 << 3) else None

        entities = TLObject.read(b) if flags & (1 << 7) else []

        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return UpdateShortChatMessage(id=id, from_id=from_id, chat_id=chat_id, message=message, pts=pts, pts_count=pts_count, date=date, out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, fwd_from=fwd_from, via_bot_id=via_bot_id, reply_to=reply_to, entities=entities, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 4) if self.mentioned else 0
        flags |= (1 << 5) if self.media_unread else 0
        flags |= (1 << 13) if self.silent else 0
        flags |= (1 << 2) if self.fwd_from is not None else 0
        flags |= (1 << 11) if self.via_bot_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 7) if self.entities else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(Long(self.from_id))

        b.write(Long(self.chat_id))

        b.write(String(self.message))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        b.write(Int(self.date))

        if self.fwd_from is not None:
            b.write(self.fwd_from.write())

        if self.via_bot_id is not None:
            b.write(Long(self.via_bot_id))

        if self.reply_to is not None:
            b.write(self.reply_to.write())

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))

        return b.getvalue()
