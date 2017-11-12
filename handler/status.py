# default.py

from . import Handler

from linebot.models import *

class StatusHandler(Handler):

  def __init__(self, reply_token, bot_api):
    buttons_template = ButtonsTemplate(
      title='Transactions?', text='Choose transaction:', actions=[
        PostbackTemplateAction(label='Transaction 1', data='t1'),
        PostbackTemplateAction(label='Transaction 2', data='t2')
      ])
    template_message = TemplateSendMessage(
      alt_text='Buttons alt text', template=buttons_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 't1':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text="Transaction ID 1.\nArabian Egg.\n\nStatus: Delivering"))
    elif data == 't2':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text="Transaction ID 2.\nAustralian Egg.\n\nStatus: Packing"))

