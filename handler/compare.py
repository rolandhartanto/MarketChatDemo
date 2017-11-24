# default.py

from . import Handler

from linebot.models import *

class CompareHandler(Handler):

  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[
      CarouselColumn(text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Choose', data='compare_ok')
      ]),
      CarouselColumn(text='Rp 25.000,-', title='Australian Egg', actions=[
        PostbackTemplateAction(label='Choose', data='compare_ok')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'cancel':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Activity cancelled.\n\nType "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    elif text == 'change':
  	  carousel_template = CarouselTemplate(columns=[
        CarouselColumn(text='1', title='Arabian Egg', actions=[
          PostbackTemplateAction(label='Choose', data='compare_chg')
        ]),
        CarouselColumn(text='2', title='Australian Egg', actions=[
          PostbackTemplateAction(label='Choose', data='compare_chg')
        ])
      ])
      template_message = TemplateSendMessage(
        alt_text='Carousel alt text', template=carousel_template)
      bot_api.reply_message(reply_token, [TextSendMessage(text='Choose which item to replace in the comparison:'),template_message])
  
	  else:
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Are you lost?\nYou can push the button at the image before or type "cancel" to cancel your order'))

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'compare_ok':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Arabian egg(1) vs Australian egg(2)\n\nPrice:\n(1)Rp 25.000,-\n(2)Rp 25.000,-\n\nShape:\nRound shape vs Oval shape\n\nSize:10inch vs 18inch\n\nColor:\nRed vs Cream.\n\nExp. date:\n(1)17-11-2017\n(2)18-11-2017\n\nCondition:\n(1)Good\n(2)Good'))
    elif data == 'compare_chg':
      carousel_template = CarouselTemplate(columns=[
        CarouselColumn(text='Rp 25.000,-', title='Arabian Egg', actions=[
          PostbackTemplateAction(label='Choose', data='compare_ok')
        ]),
        CarouselColumn(text='Rp 25.000,-', title='Australian Egg', actions=[
          PostbackTemplateAction(label='Choose', data='compare_ok')
        ])
      ])
      template_message = TemplateSendMessage(
        alt_text='Carousel alt text', template=carousel_template)
      bot_api.reply_message(event.reply_token, [TextSendMessage(text='Choose which item to replace the previous item:'),template_message])

      