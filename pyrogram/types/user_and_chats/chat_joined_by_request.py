from pyrogram.types.object import Object


class ChatJoinedByRequest(Object):
    """A service message about a user join request approved in the chat.

    Currently holds no information.
    """

    def __init__(self):
        super().__init__()
