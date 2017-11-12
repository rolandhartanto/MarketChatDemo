# default.py

from . import Handler
from handler.compare import CompareHandler

from linebot.models import *

class RecommendByPromoHandler(Handler):

  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(text='Rp 20.000,-', title='Chinese Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_a'),
        PostbackTemplateAction(label='Details', data='details_a')
      ]),
      CarouselColumn(text='Rp 15.000,-', title='Indonesian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_b'),
        PostbackTemplateAction(label='Details', data='details_b')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
  data = event.postback.data

  elif data == 'details_a':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Chinese egg\n\nOriginal Price: Rp. 25,000.00\nPrice after promo : Rp 20.000,-(Off 20%)\nStore location: Yogya Karapitan (Bandung)\nCondition: Good"))
  elif data == 'details_b':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Indonesian egg\n\nOriginal Price: Rp. 20,000.00\n\nPrice after promo : Rp 15.000,-(Off 25%)\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good"))
  elif data == 'compare':
    self.switch_handler(event, CompareHandler(event.reply_token, bot_api))

class RecommendByHistoryHandler(Handler):

  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(text='Rp 19.500,-', title='Indonesian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_a'),
        PostbackTemplateAction(label='Details', data='details_a')
      ]),
      CarouselColumn(text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_b'),
        PostbackTemplateAction(label='Details', data='details_b')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
  data = event.postback.data

  elif data == 'details_a':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Indonesian egg\n\nPrice: Rp. 25,000.00\nYou've purchased this product 3 days ago\nStore location: Yogya Karapitan (Bandung)\nCondition: Good"))
  elif data == 'details_b':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Arabian egg\n\nPrice: Rp. 25,000.00\n\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good"))
  elif data == 'compare':
    self.switch_handler(event, CompareHandler(event.reply_token, bot_api))

class PopularProductHandler(Handler):

  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(text='Rp 25.000,-', title='Indonesian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_a'),
        PostbackTemplateAction(label='Details', data='details_a')
      ]),
      CarouselColumn(text='Rp 22.500,-', title='Japanese Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy_b'),
        PostbackTemplateAction(label='Details', data='details_b')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
  data = event.postback.data

  elif data == 'details_a':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Indonesian egg\n\nPrice: Rp. 25,000.00\nOrdered 5,454 times today\nStore location: Yogya Karapitan (Bandung)\nCondition: Good"))
  elif data == 'details_b':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Japanese egg\n\nPrice: Rp. 22,500.00\nOrdered 4,759 times today\nStore location: Yogya Sunda (Bandung)\nCondition: Good"))
  elif data == 'compare':
    self.switch_handler(event, CompareHandler(event.reply_token, bot_api))