# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import errno
import os
import sys

from flask import Flask, request, abort

from linebot import (
  LineBotApi, WebhookHandler
)
from linebot.exceptions import (
  InvalidSignatureError
)
from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage,
  SourceUser, SourceGroup, SourceRoom,
  TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
  ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
  PostbackTemplateAction, DatetimePickerTemplateAction,
  CarouselTemplate, CarouselColumn, PostbackEvent,
  StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
  ImageMessage, VideoMessage, AudioMessage, FileMessage,
  UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

from handler.default import DefaultHandler

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
  print('Specify LINE_CHANNEL_SECRET as environment variable.')
  sys.exit(1)
if channel_access_token is None:
  print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
  sys.exit(1)

bot_api = LineBotApi(channel_access_token)
webhook = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']

  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  # handle webhook body
  try:
    webhook.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'


handle = DefaultHandler()

@handle.handle_set_handler
def set_handler(handler):
  print("SET CURRENT HANDLE: " + handle)
  handle = handler

@webhook.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
  text = event.message.text.lower()
  print("SERVER: " + handle)

  if text == 'cancel':
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text="Switch to main menu."))
    handle.switch_handler(DefaultHandler())

  handle.handle_text(event, bot_api)

@webhook.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
  handle.handle_location(event, bot_api)

@webhook.add(PostbackEvent)
def handle_postback(event):
  handle.handle_postback(event, bot_api)


# Run application.

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
