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
      alt_text='Payment Method', template=buttons_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'transfer':
      text1 = TextMessage(text='Wait a moment while we validate your transactions\'s seller status.')
      text2 = TextMessage(text='We already validate your transaction\'s seller status.')
      text3 = TextMessage(text='Your seller status verdict are safe.')
      text4 = TextMessage(text='The seller account\'s name are: Toko Yoyo')
      text5 = TextMessage(text='The seller account\'s number are: 900-00-123-123.')
      text6 = TextMessage(text='The seller account\'s bank name are: Mandiri')
      text7 = TextMessage(text='We guarantee that transfer payment with the seller is safe.')
      text8 = TextMessage(text='If you have any dificulty in the payment please contact our administrator: +6282821821821.')
      bot_api.reply_message(
        event.reply_token,
        text1)
    elif data == 'cod':
      buttons_template = ButtonsTemplate(
        title='When?', text='Choose Schedule:', actions=[
          PostbackTemplateAction(label='Time - Place: 30 Nov 08.00 - Marina', data='choose1'),
          PostbackTemplateAction(label='Time - Place: 20 Dec 19.00 - Sydney', data='choose2')
        ])
      template_message = TemplateSendMessage(
        alt_text='Cash On Delivery Payment', template=buttons_template)
      bot_api.reply_message(event.reply_token, [TextSendMessage(text='Your transaction\'s seller name is Toko Yoyo.\nSeller Contact: +6281-222-333-444'), template_message])
    elif data == 'choose1' or data == 'choose2':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Your seller has been contacted by our system. Please meet your seller at the meeting point on time.\nSeller name: Toko Yoyo. Seller contact: +6281-222-333-444'))
      state.switch_handler(DefaultHandler())
    
  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'validate':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Please upload your evidence of transfer.'))
    elif text == 'cancel':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Activity cancelled.\n\nType "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    else:
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Are you lost?\nPlease type "validate" to validate your transfer evidence, type "cancel" to cancel your order or push the button at the image before'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.'))
