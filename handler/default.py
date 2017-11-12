# default.py

from handler import Handler
from handler.search import SearchHandler

from linebot.models import *

class DefaultHandler(Handler):

  def handle_set_handler(self, cb):
    self.set_handler_callback = cb

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'hi':
      buttons_template = ButtonsTemplate(
        title='What do you want to do?', text='Choose action:', actions=[
          PostbackTemplateAction(label='Search Items', data='search'),
          PostbackTemplateAction(label='View Transactions', data='status')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'search':
      self.switch_handler(SearchHandler(event.reply_token, bot_api))
