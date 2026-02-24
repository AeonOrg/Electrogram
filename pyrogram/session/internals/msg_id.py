from __future__ import annotations

import logging
import time

log = logging.getLogger(__name__)


class _MsgIdGenerator:
    def __init__(self) -> None:
        self.last_time = 0
        self.offset = 0

    def __call__(self) -> int:
        now = int(time.time())
        self.offset = (self.offset + 4) if now == self.last_time else 0
        msg_id = (now * 2**32) + self.offset
        self.last_time = now
        return msg_id


MsgId = _MsgIdGenerator()
