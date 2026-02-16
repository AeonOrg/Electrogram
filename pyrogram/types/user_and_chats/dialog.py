from __future__ import annotations

import pyrogram
from pyrogram import raw, types, utils
from pyrogram.types.object import Object


class Dialog(Object):
    """A user's dialog.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Conversation the dialog belongs to.

        top_message (:obj:`~pyrogram.types.Message`):
            The last message sent in the dialog at this time.

        unread_messages_count (``int``):
            Amount of unread messages in this dialog.

        unread_mentions_count (``int``):
            Amount of unread messages containing a mention in this dialog.

        unread_reactions_count (``int``):
            Amount of unread messages containing a reaction in this dialog.

        unread_mark (``bool``):
            True, if the dialog has the unread mark set.

        is_pinned (``bool``):
            True, if the dialog is pinned.

        chat_list (``int``):
            Chat list in which the dialog is present; Only Main (0) and Archive (1) chat lists are supported.

        message_auto_delete_time (``int``)
            Current message auto-delete or self-destruct timer setting for the chat, in seconds; 0 if disabled.
            Self-destruct timer in secret chats starts after the message or its content is viewed.
            Auto-delete timer in other chats starts from the send date.

        view_as_topics (``bool``):
            True, if the chat is a forum supergroup that must be shown in the "View as topics" mode, or Saved Messages chat that must be shown in the "View as chats".

        draft (:obj:`~pyrogram.types.DraftMessage`, *optional*):
            Contains information about a message draft.

    """

    def __init__(
        self,
        *,
        client: pyrogram.Client | None = None,
        chat: types.Chat | None = None,
        top_message: types.Message | None = None,
        unread_messages_count: int | None = None,
        unread_mentions_count: int | None = None,
        unread_reactions_count: int | None = None,
        unread_mark: bool | None = None,
        is_pinned: bool | None = None,
        chat_list: int | None = None,
        message_auto_delete_time: int | None = None,
        view_as_topics: bool | None = None,
        draft: types.DraftMessage | None = None,
        _raw: raw.types.Dialog | None = None,
    ) -> None:
        super().__init__(client)

        self.chat = chat
        self.top_message = top_message
        self.unread_messages_count = unread_messages_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_mark = unread_mark
        self.is_pinned = is_pinned
        self.chat_list = chat_list
        self.message_auto_delete_time = message_auto_delete_time
        self.view_as_topics = view_as_topics
        self.draft = draft
        self._raw = _raw

    @staticmethod
    def _parse(client, dialog: raw.types.Dialog, messages, users, chats) -> Dialog:
        return Dialog(
            chat=types.Chat._parse_dialog(client, dialog.peer, users, chats),
            top_message=messages.get(utils.get_peer_id(dialog.peer)),
            unread_messages_count=getattr(dialog, "unread_count", None),
            unread_mentions_count=getattr(dialog, "unread_mentions_count", None),
            unread_reactions_count=getattr(dialog, "unread_reactions_count", None),
            unread_mark=getattr(dialog, "unread_mark", None),
            is_pinned=getattr(dialog, "pinned", None),
            chat_list=getattr(dialog, "folder_id", None),
            message_auto_delete_time=getattr(dialog, "ttl_period", 0),
            view_as_topics=not getattr(dialog, "view_forum_as_messages", True),
            client=client,
            draft=types.DraftMessage._parse(client, dialog.draft, users)
            if isinstance(
                dialog.draft, (raw.types.DraftMessage, raw.types.DraftMessageEmpty)
            )
            else None,
            _raw=dialog,
        )
