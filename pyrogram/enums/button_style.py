from __future__ import annotations

from enum import auto

from .auto_name import AutoName


class ButtonStyle(AutoName):
    """Button style enumeration."""

    PRIMARY = auto()
    """Primary button style."""

    DANGER = auto()
    """Danger button style."""

    SUCCESS = auto()
    """Success button style."""
