# default.py

from . import Handler

class DefaultHandler(Handler):

  def handle_set_handler(self, cb):
    self.set_handler_callback = cb

  def handle_text(self, event, bot_api):
    text = event.message.text

    if text == 'hi':
      buttons = ButtonsTemplate(
        title='What do you want to do?', actions=[
          PostbackTemplateAction(label='Search Items', data='search'),
          PostbackTemplateAction(label='View transactions', data='transact')
        ])
      message = TemplateSendMessage(template=buttons)
      bot_api.reply_message(event.reply_token, message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data
