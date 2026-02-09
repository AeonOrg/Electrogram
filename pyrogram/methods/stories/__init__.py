from __future__ import annotations

from .delete_stories import DeleteStories
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .forward_story import ForwardStory
from .get_all_stories import GetAllStories
from .get_peer_stories import GetPeerStories
from .get_stories import GetStories
from .get_stories_history import GetUserStoriesHistory
from .send_story import SendStory


class Stories(
    DeleteStories,
    EditStory,
    ExportStoryLink,
    ForwardStory,
    GetAllStories,
    GetPeerStories,
    GetStories,
    GetUserStoriesHistory,
    SendStory,
):
    pass
