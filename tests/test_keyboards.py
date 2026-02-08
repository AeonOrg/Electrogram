from __future__ import annotations

import pytest

from pyrogram import raw, types


def test_keyboard_button_style():
    style = types.KeyboardButtonStyle(
        bg_primary=True, bg_danger=False, bg_success=True, icon=123
    )
    assert style.bg_primary is True
    assert style.bg_danger is False
    assert style.bg_success is True
    assert style.icon == 123

    raw_style = style.write()
    assert isinstance(raw_style, raw.types.KeyboardButtonStyle)
    assert raw_style.bg_primary is True
    assert raw_style.bg_danger is False
    assert raw_style.bg_success is True
    assert raw_style.icon == 123

    style2 = types.KeyboardButtonStyle.read(raw_style)
    assert style2.bg_primary is True
    assert style2.bg_danger is False
    assert style2.bg_success is True
    assert style2.icon == 123


def test_inline_keyboard_button_with_style():
    style = types.KeyboardButtonStyle(bg_primary=True)
    button = types.InlineKeyboardButton(
        "Test", url="https://example.com", style=style
    )
    assert button.style == style

    raw_button = raw.types.KeyboardButtonUrl(
        text="Test", url="https://example.com", style=style.write()
    )
    button2 = types.InlineKeyboardButton.read(raw_button)
    assert button2.text == "Test"
    assert button2.url == "https://example.com"
    assert button2.style.bg_primary is True


def test_keyboard_button_with_style():
    style = types.KeyboardButtonStyle(bg_success=True)
    button = types.KeyboardButton("Test", style=style)
    assert button.style == style

    raw_button = raw.types.KeyboardButton(text="Test", style=style.write())
    button2 = types.KeyboardButton.read(raw_button)
    assert isinstance(button2, types.KeyboardButton)
    assert button2.text == "Test"
    assert button2.style.bg_success is True


def test_keyboard_button_backward_compatibility():
    raw_button = raw.types.KeyboardButton(text="Test")
    button = types.KeyboardButton.read(raw_button)
    assert button == "Test"
    assert isinstance(button, str)


@pytest.mark.asyncio
async def test_inline_keyboard_button_write():
    # Mock client for resolve_peer
    class MockClient:
        async def resolve_peer(self, peer_id):
            return raw.types.InputPeerSelf()

    client = MockClient()
    style = types.KeyboardButtonStyle(bg_danger=True)
    button = types.InlineKeyboardButton("Test", callback_data="data", style=style)

    raw_button = await button.write(client)
    assert isinstance(raw_button, raw.types.KeyboardButtonCallback)
    assert raw_button.style.bg_danger is True
    assert raw_button.data == b"data"


@pytest.mark.asyncio
async def test_login_url_write_with_style():
    class MockClient:
        async def resolve_peer(self, peer_id):
            return raw.types.InputUserSelf()

    client = MockClient()
    style = types.KeyboardButtonStyle(bg_primary=True)
    login_url = types.LoginUrl(url="https://example.com")
    button = types.InlineKeyboardButton("Login", login_url=login_url, style=style)

    raw_button = await button.write(client)
    assert isinstance(raw_button, raw.types.InputKeyboardButtonUrlAuth)
    assert raw_button.style.bg_primary is True
    assert raw_button.url == "https://example.com"
