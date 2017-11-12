# default.py

from . import Handler

from linebot.models import *

class SearchHandler(Handler):

  def __init__(self, reply_token, bot_api):
    bot_api.reply_message(
      reply_token,
      TextMessage(text="TEST"))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'hi':
      bot_api.reply_message(
        reply_token,
        TextMessage(text="Test LAGI"))

  def handle_postback(self, event, bot_api):
    data = event.postback.data
