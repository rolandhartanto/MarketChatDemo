# default.py

from . import Handler

from linebot.models import *

class GroceryHandler(Handler):
  def __init__(self, reply_token, bot_api):
    image_carousel_template = ImageCarouselTemplate(columns=[
      ImageCarouselColumn(
        image_url='https://via.placeholder.com/1024x1024',
        action=PostbackTemplateAction(label='Arabian egg\nRp 25.000,00', data='arabian-egg')),
      ImageCarouselColumn(
        image_url='https://via.placeholder.com/1024x1024',
        action=PostbackTemplateAction(label='Australian egg\nRp 25.000,00', data='australian-egg'))
    ])
    template_message = TemplateSendMessage(
      alt_text='ImageCarousel alt text', template=image_carousel_template)
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
