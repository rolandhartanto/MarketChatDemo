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


# Session handler.

session = {}

def handle_session(event):
  user_id = event.source.user_id

  if user_id not in session:
    handle = DefaultHandler()
    session[user_id] = handle

    @handle.handle_set_handler
    def set_handler(handler):
      session[user_id] = handler
      print("SET HANDLE: " + str(handle) + ", uid: " + str(user_id))

  return session[user_id]


# Message handler.

@webhook.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
  state = handle_session(event)
  text = event.message.text.lower()

  if text == 'cancel':
    bot_api.reply_message(
      event.reply_token,
      TextMessage(text="Switch to main menu."))
    state.switch_handler(DefaultHandler())

  state.handle_text(event, bot_api)

@webhook.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
  state = handle_session(event)
  state.handle_location(event, bot_api)

@webhook.add(MessageEvent, message=ImageMessage)
def handle_location_message(event):
  state = handle_session(event)
  state.handle_image(event, bot_api)

@webhook.add(MessageEvent, message=VideoMessage)
def handle_location_message(event):
  state = handle_session(event)
  state.handle_video(event, bot_api)

@webhook.add(PostbackEvent)
def handle_postback(event):
  state = handle_session(event)
  state.handle_postback(event, bot_api)


# Run application.

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
