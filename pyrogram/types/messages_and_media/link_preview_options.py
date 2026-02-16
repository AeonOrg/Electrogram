from __future__ import annotations

from typing import TYPE_CHECKING

from pyrogram.types.object import Object

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import raw


class LinkPreviewOptions(Object):
    """Link preview options.

    Parameters:
        is_disabled (``bool``, *optional*):
            True, if the link preview is disabled.

        url (``str``, *optional*):
            URL to use for the link preview.

        prefer_small_media (``bool``, *optional*):
            True, if the small media is preferred.

        prefer_large_media (``bool``, *optional*):
            True, if the large media is preferred.

        show_above_text (``bool``, *optional*):
            True, if the link preview should be shown above the message text.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client | None = None,
        is_disabled: bool | None = None,
        url: str | None = None,
        prefer_small_media: bool | None = None,
        prefer_large_media: bool | None = None,
        show_above_text: bool | None = None,
    ) -> None:
        super().__init__(client)

        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text

    @staticmethod
    def _parse(
        client: pyrogram.Client,
        media: raw.base.MessageMedia | raw.base.InputMedia | None = None,
        url: str | None = None,
        show_above_text: bool | None = None,
    ) -> LinkPreviewOptions:
        return LinkPreviewOptions(
            client=client,
            is_disabled=media is None and url is None,
            url=url,
            prefer_small_media=getattr(media, "force_small_media", None),
            prefer_large_media=getattr(media, "force_large_media", None),
            show_above_text=show_above_text,
        )
