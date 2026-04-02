import logging

class RiskManager:
      def __init__(self, config_manager):
                self.config = config_manager
                self.account_id = self.config.get("account_id")
                self.sl_ticks = self.config.get("sl_ticks", 10)
                self.tp_ticks = self.config.get("tp_ticks", 10)
                self.active_position = None
                self.entry_price = 0.0

      async def manage_tick(self, price):
                if not self.active_position:
                              return
                          pass

    def on_order_filled(self, price, side):
              self.active_position = side
              self.entry_price = price
              logging.info(f"Position opened: {side} at {price}")
      
