# default.py

from . import Handler
from handler.compare import CompareHandler

from linebot.models import *

# class CompareHandler(Handler):

#   def __init__(self, reply_token, bot_api):
#     carousel_template = CarouselTemplate(columns=[
#       CarouselColumn(text='Rp 25.000,-', title='Arabian Egg', actions=[
#         PostbackTemplateAction(label='Choose', data='compare_ok')
#       ]),
#       CarouselColumn(text='Rp 25.000,-', title='Australian Egg', actions=[
#         PostbackTemplateAction(label='Buy', data='buy_b'),
#         PostbackTemplateAction(label='Details', data='details_b'),
#         PostbackTemplateAction(label='Choose', data='compare_ok')
#       ])
#     ])
#     template_message = TemplateSendMessage(
#       alt_text='Carousel alt text', template=carousel_template)
#     bot_api.reply_message(reply_token, template_message)

#   def handle_postback(self, event, bot_api):
#     data = event.postback.data

#     if data == 'compare_ok':
#       bot_api.reply_message(
#         event.reply_token,
#         TextMessage(text="Arabian egg vs Mysterious egg\n\nShell:\nSpike shell vs Smooth shell\n\nShape:\nRound shape vs Oval shape\n\nSize:10inch vs 18inch\n\nColor:\nRed vs Cream.\n\nMysterious egg's exclusive properties:\nDoes not break when thrown with a force.\nIs not known if it's an actual egg.\n\nAustralian egg's exclusive properties:\n-"))

class RecommendHandler(Handler):

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
      event.reply_token, TextSendMessage(text="'Arabian egg\n\nOriginal Price: Rp. 25,000.00\nPrice after promo : Rp 20.000,-(Off 20%)\nStore location: Yogya Karapitan (Bandung)\nCondition: Good"))
  elif data == 'details_b':
    bot_api.reply_message(
      event.reply_token, TextSendMessage(text="'Australian egg\n\nPrice: Rp. 20,000.00\n\nPrice after promo : Rp 15.000,-(Off 25%)\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good"))
  elif data == 'compare':
    self.switch_handler(CompareHandler(event.reply_token, bot_api))