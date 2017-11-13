# __init__.py

class Handler:
  set_handler_callback = None

  def switch_handler(self, event, handler):
    handler.set_handler_callback = self.set_handler_callback
    self.set_handler_callback(event, handler)

  def handle_text(self, event, bot_api):
    pass
  def handle_location(self, event, bot_api):
    pass
  def handle_postback(self, event, bot_api):
    pass
  def handle_image(self, event, bot_api):
    pass
  def handle_video(self, event, bot_api):
    pass

__all__ = ['default']
