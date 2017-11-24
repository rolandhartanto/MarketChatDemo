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
          PostbackTemplateAction(label='Others', data='others')
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, [TextSendMessage(text='Welcome to MarketChat!\n\nYou can choose what you want to do on the menu below.\nHappy shopping! :D\n\n To view list of instructions, type "help"'),template_message])
    elif text == 'help':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='List of instructions (type the instruction to use it)\n- menu: if you want to view main menu\n- back: if you want to go back to previous activity\n- cancel: if you want to cancel current activity and go back to start\n- help: if you want to see the list of instructions\n- recommended: if you want to see recommended items based on your transaction history\n- popular: if you want to see popular items recently\n- validate transfer: if you want to validate your transfer evidence\n\nMenus (press the menu option button to choose)\n- Search Items: if you want to search a item that you want to buy\n- Search Store: if you want to search your preferrence store\n- View Transactions: if you want to find your transaction status with this feature'))
    elif text == 'validate transfer':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Please upload your evidence of transfer.'))
    elif text == 'done':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Type "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    elif text == 'cancel':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Activity cancelled.\n\nType "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    else:
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Are you lost?\nPlease type "help" to see the list of instructions'))
      state.switch_handler(DefaultHandler())

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'search':
      self.switch_handler(SearchHandler(event.reply_token, bot_api))
    elif data == 'searchstore':
      self.switch_handler(SearchStoreHandler(event.reply_token, bot_api))
    elif data == 'status':
      self.switch_handler(StatusHandler(event.reply_token, bot_api))
    elif data == 'others':
      buttons_template = ButtonsTemplate(
        title='What do you want to do?', text='Choose action:', actions=[
          PostbackTemplateAction(label='Promo Items', data='promo'),
		      PostbackTemplateAction(label='Recommended Items', data='recommended'),
          PostbackTemplateAction(label='Popular Items', data='popular'),
        ])
      template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
      bot_api.reply_message(event.reply_token, [template_message,TextSendMessage(text='Type "cancel" to cancel this activity.')])
    elif data == 'promo':
      self.switch_handler(RecommendByPromoHandler(event.reply_token, bot_api))
    elif data == 'recommended':
      self.switch_handler(RecommendByHistoryHandler(event.reply_token, bot_api))
    elif data == 'popular':
      self.switch_handler(RecommendByPopularityHandler(event.reply_token, bot_api))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))
