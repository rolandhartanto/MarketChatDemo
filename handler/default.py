# default.py

from handler import Handler
from handler.search import SearchHandler, SearchStoreHandler, FashionHandler, YogyaKHandler
from handler.status import StatusHandler
from handler.recommend import RecommendByPopularityHandler, RecommendByHistoryHandler, RecommendByPromoHandler

from linebot.models import *

class DefaultHandler(Handler):

  def handle_set_handler(self, cb):
    self.set_handler_callback = cb

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'menu':
      buttons_template = ButtonsTemplate(
        title='What do you want to do?', text='Choose action:', actions=[
          PostbackTemplateAction(label='Search Items', data='search'),
		      PostbackTemplateAction(label='Search Store', data='searchstore'),
          PostbackTemplateAction(label='View Transactions', data='status'),
          PostbackTemplateAction(label='View Promos', data='promo'),
          PostbackTemplateAction(label='Recommended Items', data='history')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, template_message)
    elif text == 'help':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='List of instructions\n- menu: to view main menu\n- cancel: to cancel current activity and go back to start\n- help: to view list of instructions\n'))
    elif text == 'ehehe':
      bot_api.reply_message(
        event.reply_token, [
          TextMessage(text='Text 1'),
          TextMessage(text='Text 2'),
          TextMessage(text='Text 3')
        ])

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'search':
      self.switch_handler(SearchHandler(event.reply_token, bot_api))
    elif data == 'searchstore':
      self.switch_handler(SearchStoreHandler(event.reply_token, bot_api))
    elif data == 'status':
      self.switch_handler(StatusHandler(event.reply_token, bot_api))
    elif data == 'promo':
      self.switch_handler(RecommendByPromoHandler(event.reply_token, bot_api))
    elif data == 'history':
      self.switch_handler(RecommendByHistoryHandler(event.reply_token, bot_api))
    elif data == 'popularity':
      self.switch_handler(RecommendByPopularityHandler(event.reply_token, bot_api))