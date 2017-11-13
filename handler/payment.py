# default.py

from . import Handler

from linebot.models import *

class PaymentHandler(Handler):

  def __init__(self, reply_token, bot_api):
    buttons_template = ButtonsTemplate(
      title='Payment method?', text='Choose method:', actions=[
        PostbackTemplateAction(label='Payment by Transfer', data='transfer'),
        PostbackTemplateAction(label='Payment by COD', data='cod')
      ])
    template_message = TemplateSendMessage(
      alt_text='Buttons alt text', template=buttons_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'transfer':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Here\'s your seller account number: 900-00-123-123\n\nYour seller are certified seller'))
    elif data == 'cod':
      buttons_template = ButtonsTemplate(
        title='When?', text='Choose schedule:', actions=[
          PostbackTemplateAction(label='30 Nov 08.00: Marina', data='choose1'),
          PostbackTemplateAction(label='20 Dec 19.00: Sydney', data='choose2')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, template_message)
    elif data == 'choose1' or data == 'choose2':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Your seller has been contacted by our system. Please meet your seller at the meeting point on time.'))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'validate transfer':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Please upload your evidence of transfer.'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.'))
