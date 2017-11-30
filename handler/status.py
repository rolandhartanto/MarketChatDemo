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
        TextMessage(text="Transaction ID 2.\nSkinny Patched Up Jeans A|X\n\nStatus: Packing"))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'validate':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Please upload your evidence of transfer.'))
    elif text == 'done':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Type "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    elif text == 'cancel':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Activity cancelled.\n\nType "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    else:
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Are you lost?\nYou can validate your transfer here by typing "validate" or push the button at the image before or type "cancel" to cancel your order'))
 
  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))
