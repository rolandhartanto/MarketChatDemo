# __init__.py

class Handler:
  set_handler_callback = None

  def switch_handler(handler):
    handler.set_handler_callback = set_handler_callback
    self.set_handler_callback(handler)

  def handle_text(event, bot_api):
    pass
  def handle_location(event, bot_api):
    pass
  def handle_postback(event, bot_api):
    pass

__all__ = ['default']
