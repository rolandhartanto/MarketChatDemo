# default.py

from handler import Handler
from handler.compare import CompareHandler

from linebot.models import *

class GroceryHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[
      CarouselColumn(text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_a'),
        PostbackTemplateAction(label='Details', data='details_a')
      ]),
      CarouselColumn(text='Rp 25.000,-', title='Australian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_b'),
        PostbackTemplateAction(label='Details', data='details_b')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'buy_a':
      # TODO: Checkout
      pass
    elif data == 'buy_b':
      # TODO: Checkout
      pass
    elif data == 'details_a':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text="'Arabian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good"))
    elif data == 'details_b':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text="'Australian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good"))
    elif data == 'compare':
      self.switch_handler(CompareHandler(event.reply_token, bot_api))


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
