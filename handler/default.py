# default.py

from handler import Handler
from handler.search import SearchHandler, SearchStoreHandler, FashionHandler, YogyaKHandler, AllHandler
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
          PostbackTemplateAction(label='View Promos', data='promo')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, [TextSendMessage(text='Welcome to MarketChat!\n\nYou can choose what you want to do on the menu below.\nHappy shopping! :D\n\n To view list of instructions, type "help"'),template_message])
    elif text == 'help':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='List of instructions\n- menu: if you want to view main menu\n- back: if you want to go back to previous activity\n- cancel: if you want to cancel current activity and go back to start\n- help: if you want to see the list of instructions\n- recommended: if you want to see recommended items based on your transaction history\n- popular: if you want to see popular items recently\n\nMenus\n- Search: if you want to search a item that you want to buy\n- Search Store: if you want to search your preferrence store\n- Status: if you want to find your transaction status with this feature\n- View Promos: if you want to find the item that recommended by our system\n'))
    elif text == 'recommended':
      self.switch_handler(RecommendByHistoryHandler(event.reply_token, bot_api))
    elif text == 'popular':
      self.switch_handler(RecommendByPopularityHandler(event.reply_token, bot_api))

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
    