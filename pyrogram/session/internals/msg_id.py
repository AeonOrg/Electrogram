from __future__ import annotations

import logging
import time

log = logging.getLogger(__name__)

_last_time = 0
_offset = 0


def MsgId() -> int:
    global _last_time, _offset

    now = int(time.time())
    _offset = (_offset + 4) if now == _last_time else 0
    msg_id = (now * 2**32) + _offset
    _last_time = now

    return msg_id
