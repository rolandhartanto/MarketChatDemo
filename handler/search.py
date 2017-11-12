# default.py

from . import Handler

from linebot.models import *

class GroceryHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[
      CarouselColumn(text='Rp 25.000,00', title='Arabian egg', actions=[
        PostbackTemplateAction(label='view detail', data='arabian-egg')
      ]),
      CarouselColumn(text='Rp 25.000,00', title='Australian egg', actions=[
        PostbackTemplateAction(label='view detail', data='arabian-egg')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

class SearchHandler(Handler):
  def __init__(self, reply_token, bot_api):
    buttons_template = ButtonsTemplate(
      title='In what category?', text='Choose category:', actions=[
        PostbackTemplateAction(label='Grocery', data='grocery'),
        PostbackTemplateAction(label='Fashion', data='fashion')
      ])
    template_message = TemplateSendMessage(
      alt_text='Buttons alt text', template=buttons_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'grocery':
      switch_handler(GroceryHandler(event.reply_token, bot_api))
    elif data == 'fashion':
      pass
