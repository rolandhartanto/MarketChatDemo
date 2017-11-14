# default.py

from . import Handler
from handler.compare import CompareHandler
from handler.payment import PaymentHandler

from linebot.models import *

class RecommendByPromoHandler(Handler):

  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46532237xt_14_f.jpg',text='Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)', title='Camo Jacquard Straight Fit Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'buy':
        self.switch_handler(PaymentHandler(event.reply_token, bot_api))
    elif data == 'details_a':
      bot_api.reply_message(
          event.reply_token, TextSendMessage(text='Camo Jacquard Straight Fit Jeans\nArmani Exchange\n\nPrice: Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good'))

class RecommendByHistoryHandler(Handler):

 def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46539875vo_14_f.jpg',text='Rp 1.400.000,-', title='Skinny Patched Up Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a')
      ]),
      CarouselColumn(thumbnail_image_url='https://matriposterous.files.wordpress.com/2010/11/image_298.jpg',text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_b')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'buy':
        self.switch_handler(PaymentHandler(event.reply_token, bot_api))
    elif data == 'details_a':
      bot_api.reply_message(
          event.reply_token, TextSendMessage(text='Skinny Patched Up Jeans\nArmani Exchange\n\nPrice: Rp 1.400.000,00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
    elif data == 'details_b':
      bot_api.reply_message(
          event.reply_token, TextSendMessage(text='Arabian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))

class RecommendHandler(Handler):

  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46539875vo_14_f.jpg',text='Rp 1.400.000,-', title='Skinny Patched Up Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a')
      ]),
      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46532237xt_14_f.jpg',text='Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)', title='Camo Jacquard Straight Fit Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_b')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
  data = event.postback.data

  if data == 'buy':
      self.switch_handler(PaymentHandler(event.reply_token, bot_api))
  elif data == 'details_a':
    bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Skinny Patched Up Jeans\nArmani Exchange\n\nPrice: Rp 1.400.000,00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
  elif data == 'details_b':
    bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Camo Jacquard Straight Fit Jeans\nArmani Exchange\n\nPrice: Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good'))