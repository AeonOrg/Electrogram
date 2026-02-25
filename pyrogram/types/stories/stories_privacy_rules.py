from __future__ import annotations

from pyrogram import enums, raw
from pyrogram.types.object import Object


class StoriesPrivacyRules(Object):
    """A story privacy.

    Parameters:
        type (:obj:`~pyrogram.enums.StoriesPrivacyRules`):
            Story privacy type.
    """

    def __init__(self, *, type: enums.StoriesPrivacyRules) -> None:
        super().__init__()
        self.type = type

    def write(self):
        if self.type == enums.StoriesPrivacyRules.PUBLIC:
            return raw.types.InputPrivacyValueAllowAll()
        if self.type == enums.StoriesPrivacyRules.CLOSE_FRIENDS:
            return raw.types.InputPrivacyValueAllowCloseFriends()
        if self.type == enums.StoriesPrivacyRules.CONTACTS:
            return raw.types.InputPrivacyValueAllowContacts()
        if self.type == enums.StoriesPrivacyRules.NO_CONTACTS:
            return raw.types.InputPrivacyValueDisallowContacts()
        if self.type == enums.StoriesPrivacyRules.PRIVATE:
            return raw.types.InputPrivacyValueDisallowAll()
        return None
