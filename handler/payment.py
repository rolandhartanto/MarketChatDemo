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
          PostbackTemplateAction(label='30 Nov 2017 08.00 - Marina Bay', data='choose_sched'),
          PostbackTemplateAction(label='1 Dec 2017 19.00 - Sydney Opera House', data='choose_sched')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, template_message)
    elif data == 'choose_sched':
      line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Your seller has been contacted by our system. Please meet your seller at the meeting point on time.'))
