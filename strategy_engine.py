import pandas as pd
import pandas_ta as ta

class StrategyEngine:
      def __init__(self, config_manager):
                self.config = config_manager
                self.indicators = {}

      def calculate_indicators(self, data: pd.DataFrame):
                data["EMA"] = ta.ema(data["close"], length=20)
                data["VWAP"] = ta.vwap(data["high"], data["low"], data["close"], data["volume"])
                return data

      def generate_signal(self, data: pd.DataFrame):
                if data["close"].iloc[-1] > data["EMA"].iloc[-1]:
                              return "BUY"
elif data["close"].iloc[-1] < data["EMA"].iloc[-1]:
            return "SELL"
        return "NONE"
