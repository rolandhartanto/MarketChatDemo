# default.py

from . import Handler

from linebot.models import *

class GroceryHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[
      CarouselColumn(text='hoge1', title='fuga1', actions=[
        PostbackTemplateAction(label='ping', data='ping'),
        PostbackTemplateAction(label='ping', data='ping')
      ]),
      CarouselColumn(text='hoge1', title='fuga1', actions=[
        PostbackTemplateAction(label='ping', data='ping'),
        PostbackTemplateAction(label='ping', data='ping')
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
      self.switch_handler(GroceryHandler(event.reply_token, bot_api))
    elif data == 'fashion':
      pass
