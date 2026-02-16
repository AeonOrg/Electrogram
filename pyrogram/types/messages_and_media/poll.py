from __future__ import annotations

from typing import TYPE_CHECKING, List, cast

import pyrogram
from pyrogram import enums, raw, types, utils
from pyrogram.types.object import Object
from pyrogram.types.update import Update

if TYPE_CHECKING:
    from datetime import datetime


class Poll(Object, Update):
    """A Poll.

    Parameters:
        id (``str``):
            Unique poll identifier.

        question (``str``):
            Poll question, 1-255 characters.

        options (List of :obj:`~pyrogram.types.PollOption`):
            List of poll options.

        question_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities like usernames, URLs, bot commands, etc. that appear in the poll question.

        total_voter_count (``int``):
            Total number of users that voted in the poll.

        is_closed (``bool``):
            True, if the poll is closed.

        is_anonymous (``bool``, *optional*):
            True, if the poll is anonymous

        type (:obj:`~pyrogram.enums.PollType`, *optional*):
            Poll type.

        allows_multiple_answers (``bool``, *optional*):
            True, if the poll allows multiple answers.

        chosen_option_id (``int``, *optional*):
            0-based index of the chosen option), None in case of no vote yet.

        correct_option_id (``int``, *optional*):
            0-based identifier of the correct answer option.
            Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to
            the private chat with the bot.

        explanation (``str``, *optional*):
            Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,
            0-200 characters.

        explanation_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities like usernames, URLs, bot commands, etc. that appear in the explanation.

        open_period (``int``, *optional*):
            Amount of time in seconds the poll will be active after creation.

        close_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the poll will be automatically closed.

        recent_voters (List of :obj:`~pyrogram.types.User`, *optional*):
            List of user whos recently vote.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client | None = None,
        id: str,
        question: str,
        options: list[types.PollOption],
        question_entities: list[types.MessageEntity] | None = None,
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool | None = None,
        type: enums.PollType | None = None,
        allows_multiple_answers: bool | None = None,
        chosen_option_id: int | None = None,
        correct_option_id: int | None = None,
        explanation: str | None = None,
        explanation_entities: list[types.MessageEntity] | None = None,
        open_period: int | None = None,
        close_date: datetime | None = None,
        recent_voters: list[types.User] | None = None,
    ) -> None:
        super().__init__(client)

        self.id = id
        self.question = question
        self.options = options
        self.question_entities = question_entities
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.chosen_option_id = chosen_option_id
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
        self.recent_voters = recent_voters

        self.chat: types.Chat | None = None
        self.message_id: int | None = None
        self.business_connection_id: str | None = None

    @staticmethod
    async def _parse(
        client,
        media_poll: raw.types.MessageMediaPoll | raw.types.UpdateMessagePoll,
        users: dict,
    ) -> Poll:
        poll = cast(raw.types.Poll, media_poll.poll)
        poll_results = cast(raw.types.PollResults, media_poll.results)
        results = cast(List[raw.types.PollAnswerVoters], poll_results.results)

        chosen_option_id = None
        correct_option_id = None
        options = []

        for i, answer in enumerate(poll.answers):
            voter_count = 0

            if results:
                result = results[i]
                voter_count = result.voters

                if result.chosen:
                    chosen_option_id = i

                if result.correct:
                    correct_option_id = i

            answer_text = cast(raw.types.TextWithEntities, answer.text)
            o_entities = (
                [
                    types.MessageEntity._parse(client, entity, {})
                    for entity in answer_text.entities
                ]
                if answer_text.entities
                else []
            )
            option_entities = cast(
                list[types.MessageEntity],
                types.List([i for i in o_entities if i is not None]),
            )

            options.append(
                types.PollOption(
                    text=answer_text.text,
                    voter_count=voter_count,
                    data=answer.option,
                    entities=option_entities,
                    client=client,
                ),
            )

        poll_question = cast(raw.types.TextWithEntities, poll.question)
        q_entities = (
            [
                types.MessageEntity._parse(client, entity, {})
                for entity in poll_question.entities
            ]
            if poll_question.entities
            else []
        )
        question_entities = cast(
            list[types.MessageEntity],
            types.List([i for i in q_entities if i is not None]),
        )

        return Poll(
            id=str(poll.id),
            question=poll_question.text,
            options=options,
            question_entities=question_entities,
            total_voter_count=poll_results.total_voters or 0,
            is_closed=bool(poll.closed),
            is_anonymous=not poll.public_voters,
            type=enums.PollType.QUIZ if poll.quiz else enums.PollType.REGULAR,
            allows_multiple_answers=bool(poll.multiple_choice),
            chosen_option_id=chosen_option_id,
            correct_option_id=correct_option_id,
            explanation=poll_results.solution,
            explanation_entities=cast(
                list[types.MessageEntity],
                [
                    types.MessageEntity._parse(client, i, {})
                    for i in poll_results.solution_entities
                ],
            )
            if poll_results.solution_entities
            else None,
            open_period=poll.close_period,
            close_date=utils.timestamp_to_datetime(poll.close_date),
            recent_voters=[
                await client.get_users(utils.get_raw_peer_id(user))
                for user in poll_results.recent_voters
            ]
            if poll_results.recent_voters
            else None,
            client=client,
        )

    @staticmethod
    async def _parse_update(
        client,
        update: raw.types.UpdateMessagePoll,
        users: list[raw.base.User] | dict,
    ) -> Poll:
        if update.poll is not None:
            return await Poll._parse(client, update, cast(dict, users))

        poll_results = cast(raw.types.PollResults, update.results)
        results = cast(List[raw.types.PollAnswerVoters], poll_results.results)
        chosen_option_id = None
        correct_option_id = None
        options = []

        for i, result in enumerate(results):
            if result.chosen:
                chosen_option_id = i

            if result.correct:
                correct_option_id = i

            options.append(
                types.PollOption(
                    text="",
                    voter_count=result.voters,
                    data=result.option,
                    client=client,
                ),
            )

        users_dict = users if isinstance(users, dict) else {cast(raw.types.User, i).id: i for i in users}

        parsed_poll = Poll(
            id=str(update.poll_id),
            question="",
            options=options,
            total_voter_count=poll_results.total_voters or 0,
            is_closed=False,
            chosen_option_id=chosen_option_id,
            correct_option_id=correct_option_id,
            recent_voters=cast(
                list[types.User],
                [
                    types.User._parse(
                        client,
                        users_dict.get(utils.get_raw_peer_id(user) or 0),
                    )
                    for user in poll_results.recent_voters
                ],
            )
            if poll_results.recent_voters
            else None,
            client=client,
        )

        parsed_poll.chat = types.Chat._parse(client, cast(Any, update), {}, {}, is_chat=True)
        return parsed_poll

    async def stop(
        self,
        reply_markup: types.InlineKeyboardMarkup | None = None,
        business_connection_id: str | None = None,
    ) -> types.Poll:
        """Bound method *stop* of :obj:`~pyrogram.types.Poll`.

        Use as a shortcut for:

        .. code-block:: python

            client.stop_poll(
                chat_id=message.chat.id,
                message_id=message.id,
            )

        Parameters:
            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

            business_connection_id (``str``, *optional*):
                Unique identifier of the business connection.

        Example:
            .. code-block:: python

                message.poll.stop()

        Returns:
            :obj:`~pyrogram.types.Poll`: On success, the stopped poll with the final results is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.stop_poll(
            chat_id=cast(types.Chat, self.chat).id,
            message_id=cast(int, self.message_id),
            reply_markup=reply_markup,
            business_connection_id=self.business_connection_id
            if business_connection_id is None
            else business_connection_id,
        )
