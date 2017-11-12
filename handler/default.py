# default.py

from . import Handler

from linebot.models import *

class DefaultHandler(Handler):

  def handle_set_handler(self, cb):
    self.set_handler_callback = cb

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'hi':
      buttons_template = ButtonsTemplate(
        title='My buttons sample', text='Hello, my buttons', actions=[
          URITemplateAction(
            label='Go to line.me', uri='https://line.me'),
          PostbackTemplateAction(label='ping', data='ping'),
          PostbackTemplateAction(
            label='ping with text', data='ping',
            text='ping'),
          MessageTemplateAction(label='Translate Rice', text='米')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data
