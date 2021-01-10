
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import player
from helpers import State
from config import SUDO_FILTER, LOG_GROUP
from strings import get_string as _


def stream(client, message):
    None

    if player.STATE in (State.Playing, State.Paused):
        message.reply_text(
            _("stream_3")
        )
    else:
        args = message.text.split()

        if len(args) == 1:
            message.reply_text(
                _("stream_1")
            )
        elif len(args) != 2:
            message.reply_text(
                _("stream_2")
            )
        else:
            player.stream(
                args[1],
                [
                    client.send_message,
                    [
                        LOG_GROUP,
                        _("group_2").format(
                            args[1]
                        )
                    ]
                ] if LOG_GROUP else None
            )

            message.reply_text(
                _("stream_4")
            )


__handlers__ = [
    [
        MessageHandler(
            stream,
            filters.command("stream", "/")
            & SUDO_FILTER
        )
    ]
]
__help__ = {
    "stream": [_("help_stream"), True]
}
