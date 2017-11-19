# default.py

from handler import Handler
from handler.compare import CompareHandler
from handler.payment import PaymentHandler

from linebot.models import *

class GroceryHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(thumbnail_image_url='https://matriposterous.files.wordpress.com/2010/11/image_298.jpg',text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a'),
        PostbackTemplateAction(label='Compare', data='compare')
      ]),
      CarouselColumn(thumbnail_image_url='https://22251-presscdn-pagely.netdna-ssl.com/wp-content/uploads/2015/09/1401323431993.jpg',text='Rp 25.000,-', title='Australian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_b'),
        PostbackTemplateAction(label='Compare', data='compare')
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
        event.reply_token, TextSendMessage(text='Arabian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
    elif data == 'details_b':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Australian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good'))
    elif data == 'compare':
      self.switch_handler(CompareHandler(event.reply_token, bot_api))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()
    if text == 'egg':
      self.switch_handler(GroceryHandler(event.reply_token, bot_api))
    elif text == 'jeans':
      self.switch_handler(FashionHandler(event.reply_token, bot_api))
    elif text == 'back':
      self.switch_handler(SearchHandler(event.reply_token, bot_api))
    elif text == 'validate transfer':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Please upload your evidence of transfer.'))
    elif text == 'cancel':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Activity cancelled.\n\nType "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    elif text == 'done':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Type "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    else:
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='There is no such item or command. There are 2 item in the list such as egg and jeans and you can validate your transfer by type "validate transfer" or cancel your order by type "cancel"'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))

class FashionHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46539875vo_14_f.jpg',text='Rp 1.400.000,-', title='Skinny Patched Up Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a'),
        PostbackTemplateAction(label='Compare', data='compare')
      ]),
      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46532237xt_14_f.jpg',text='Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)', title='Camo Jacquard Straight Fit Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_b'),
        PostbackTemplateAction(label='Compare', data='compare')
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
    elif data == 'compare':
      self.switch_handler(CompareHandler(event.reply_token, bot_api))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()
    if text == 'jeans':
      self.switch_handler(FashionHandler(event.reply_token, bot_api))
    elif text == 'egg':
      self.switch_handler(GroceryHandler(event.reply_token, bot_api))
    elif text == 'back':
      self.switch_handler(SearchHandler(event.reply_token, bot_api))
    elif text == 'validate transfer':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Please upload your evidence of transfer.'))
    elif text == 'cancel':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Activity cancelled.\n\nType "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    elif text == 'done':
      bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Type "menu" to view main menu.\nTo view other instructions, type "help".'))
      state.switch_handler(DefaultHandler())
    else:
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='There is no such item or command. There are 2 items in the list such as egg and jeans and you can validate your transfer by type "validate transfer" or cancel your order by type "cancel"'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))
          
class SearchHandler(Handler):
  def __init__(self, reply_token, bot_api):
    buttons_template = ButtonsTemplate(
      title='In what category?', text='Choose category:', actions=[
        PostbackTemplateAction(label='Grocery', data='grocery'),
        PostbackTemplateAction(label='Fashion', data='fashion'),
        PostbackTemplateAction(label='All', data='all')
      ])
    template_message = TemplateSendMessage(
      alt_text='Buttons alt text', template=buttons_template)
    bot_api.reply_message(reply_token, [TextSendMessage(text='Type item name or key word to search items.\ne.g.: egg\nYou can also choose the categories below.'),template_message,TextMessage(text='Type "cancel" to cancel this activity.')])

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'grocery':
      self.switch_handler(GroceryHandler(event.reply_token, bot_api))
    elif data == 'fashion':
      self.switch_handler(FashionHandler(event.reply_token, bot_api))
    elif data == 'all':
      self.switch_handler(AllHandler(event.reply_token, bot_api))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()
    if text == 'egg':
      self.switch_handler(GroceryHandler(event.reply_token, bot_api))
    if text == 'jeans':
      self.switch_handler(FashionHandler(event.reply_token, bot_api))
    if text == 'validate transfer':
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
        event.reply_token, TextSendMessage(text='There is no such item. There are 2 items in the list such as egg and jeans. You can validate your transfer by type "validate transfer" or cancel your order by type "cancel"'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))

class SearchStoreHandler(Handler):
  def __init__(self, reply_token, bot_api):
    buttons_template = ButtonsTemplate(
      title='Available store', text='Choose store:', actions=[
        PostbackTemplateAction(label='Yogya kepatihan', data='yogyak'),
        PostbackTemplateAction(label='Yogya riau', data='yogyar')
      ])
    template_message = TemplateSendMessage(
      alt_text='Buttons alt text', template=buttons_template)
    bot_api.reply_message(reply_token, [template_message,TextMessage(text='Type "cancel" to cancel this activity.')])

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'yogyak':
      self.switch_handler(YogyaKHandler(event.reply_token, bot_api))
    elif data == 'yogyar':
      pass

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()

    if text == 'validate transfer':
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
        TextMessage(text='Are you lost?\nYou can validate your transfer here by typing "validate transfer" or push the button at the image before or type "cancel" to cancel your order'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))

class YogyaKHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[

      CarouselColumn(thumbnail_image_url='https://matriposterous.files.wordpress.com/2010/11/image_298.jpg',text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a'),
        PostbackTemplateAction(label='Compare', data='compare')
      ]),
      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46539875vo_14_f.jpg',text='Rp 1.400.000,-', title='Skinny Patched Up Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_b'),
        PostbackTemplateAction(label='Compare', data='compare')
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
        event.reply_token, TextSendMessage(text='Arabian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
    elif data == 'details_b':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Skinny Patched Up Jeans\nArmani Exchange\n\nPrice: Rp 1.400.000,00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
    elif data == 'compare':
      self.switch_handler(CompareHandler(event.reply_token, bot_api))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()
    if text == 'jeans':
      carousel_template = CarouselTemplate(columns=[
        CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46539875vo_14_f.jpg',text='Rp 1.400.000,-', title='Skinny Patched Up Jeans A|X', actions=[
          PostbackTemplateAction(label='Buy', data='buy'),
          PostbackTemplateAction(label='Details', data='details_b'),
          PostbackTemplateAction(label='Compare', data='compare')
        ])
      ])
      template_message = TemplateSendMessage(
        alt_text='Carousel alt text', template=carousel_template)
      bot_api.reply_message(event.reply_token, template_message)
    elif text == 'egg':
      carousel_template = CarouselTemplate(columns=[
        CarouselColumn(thumbnail_image_url='https://matriposterous.files.wordpress.com/2010/11/image_298.jpg',text='Rp 25.000,-', title='Arabian Egg', actions=[
          PostbackTemplateAction(label='Buy', data='buy'),
          PostbackTemplateAction(label='Details', data='details_a'),
          PostbackTemplateAction(label='Compare', data='compare')
        ])
      ])
      template_message = TemplateSendMessage(
        alt_text='Carousel alt text', template=carousel_template)
      bot_api.reply_message(event.reply_token, template_message)
    elif text == 'back':
      self.switch_handler(SearchStoreHandler(event.reply_token, bot_api))
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
        event.reply_token, TextSendMessage(text='There is no such item or command. There are 2 items in the list such as jeans and egg. You can validate your transfer by type"validate transfer" or cancel your order by type "cancel"'))

  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))

class AllHandler(Handler):
  def __init__(self, reply_token, bot_api):
    carousel_template = CarouselTemplate(columns=[
      CarouselColumn(thumbnail_image_url='https://matriposterous.files.wordpress.com/2010/11/image_298.jpg',text='Rp 25.000,-', title='Arabian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_a'),
        PostbackTemplateAction(label='Compare', data='compare')
      ]),
      CarouselColumn(thumbnail_image_url='https://22251-presscdn-pagely.netdna-ssl.com/wp-content/uploads/2015/09/1401323431993.jpg',text='Rp 25.000,-', title='Australian Egg', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_b'),
        PostbackTemplateAction(label='Compare', data='compare')
      ]),
      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46539875vo_14_f.jpg',text='Rp 1.400.000,-', title='Skinny Patched Up Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_c'),
        PostbackTemplateAction(label='Compare', data='compare')
      ]),
      CarouselColumn(thumbnail_image_url='https://cdn.yoox.biz/46/46532237xt_14_f.jpg',text='Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)', title='Camo Jacquard Straight Fit Jeans A|X', actions=[
        PostbackTemplateAction(label='Buy', data='buy'),
        PostbackTemplateAction(label='Details', data='details_d'),
        PostbackTemplateAction(label='Compare', data='compare')
      ])
    ])
    template_message = TemplateSendMessage(
      alt_text='Carousel alt text', template=carousel_template)
    bot_api.reply_message(reply_token, template_message)

  def handle_postback(self, event, bot_api):
    data = event.postback.data

    if data == 'buy':
      self.switch_handler(PaymentHandler(event.reply_token, bot_api))
    elif data == 'details_c':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Skinny Patched Up Jeans\nArmani Exchange\n\nPrice: Rp 1.400.000,00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
    elif data == 'details_d':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Camo Jacquard Straight Fit Jeans\nArmani Exchange\n\nPrice: Rp 1.320.000,- --> Rp 660.000,- (-50\%\off)\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good'))
    elif data == 'details_a':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Arabian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Karapitan (Bandung)\nCondition: Good'))
    elif data == 'details_b':
      bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Australian egg\n\nPrice: Rp. 25,000.00\nStore location: Yogya Riau Junction (Bandung)\nCondition: Good'))
    elif data == 'compare':
      self.switch_handler(CompareHandler(event.reply_token, bot_api))

  def handle_text(self, event, bot_api):
    text = event.message.text.lower()
    if text == 'jeans':
      self.switch_handler(FashionHandler(event.reply_token, bot_api))
    elif text == 'egg':
      self.switch_handler(GroceryHandler(event.reply_token, bot_api))
    elif text == 'back':
      self.switch_handler(SearchHandler(event.reply_token, bot_api))
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
        event.reply_token, TextSendMessage(text='There is no such item or command. There are 2 items in the list such as egg and jeans. You can validate your transfer by type "valida transfer" or cancel your order by type "cancel"'))
          
  def handle_image(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are accepted by our system. Our system already contacted the seller. You can check the status of your order.\nType "done" to complete transaction.'))

  def handle_video(self, event, bot_api):
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text='The system already validate your evidence of transfer.\nYour transfer are not accepted by our system.\nPlease validate your transfer again.\nType "done" to complete transaction.'))
