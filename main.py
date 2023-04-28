from __future__ import annotations

import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import filters

from oobabooga import oobabooga

load_dotenv()

_TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
_CHATS = [int(c) for c in os.getenv('CHATS').split(',')]


async def query_llm(
        update: Update,
        _context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message.text in ('/ask', '/ask@llm_bot'):
        await update.message.reply_text('What is your question?')

    if any(q in update.message.text for q in ['/ask ', '/ask@llm_bot ']):
        _, question = update.message.text.split(' ', 1)
        if not question:
            return
        answer = await oobabooga(question)
        await update.message.reply_text(answer)


def main() -> None:
    application = Application.builder().token(_TELEGRAM_TOKEN).build()
    application.add_handler(
        CommandHandler(
            'ask',
            query_llm,
            filters.Chat(_CHATS),
        ),
    )
    application.run_polling()


if __name__ == '__main__':
    main()
