import asyncio
import aiohttp
import websockets
import json
import logging
from config_manager import ConfigManager

class TopstepClient:
      def __init__(self, config_manager: ConfigManager):
                self.config = config_manager
                self.api_key = self.config.get("api_key")
                self.username = self.config.get("username")
                self.token = None
                self.base_url = "https://api.topstepx.com/api"
                self.ws_base_url = "wss://rtc.topstepx.com/hubs/market"

      async def _get_token(self):
                if self.token:
                              return self.token
                          url = f"{self.base_url}/Auth/loginKey"
                payload = {"username": self.username, "api_key": self.api_key}
                async with aiohttp.ClientSession() as session:
                              async with session.post(url, json=payload) as resp:
                                                if resp.status == 200:
                                                                      data = await resp.json()
                                                                      self.token = data.get("token")
                                                                      return self.token
else:
                    logging.error(f"Login failed: {resp.status}")
                      return None

    async def place_order(self, account_id, symbol, side, qty, order_type='Market'):
              token = await self._get_token()
        if not token:
                      return None
                  url = f"{self.base_url}/Order/place"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {
                      "accountId": account_id,
                      "symbol": symbol,
                      "side": side,
                      "quantity": qty,
                      "orderType": order_type
        }
        async with aiohttp.ClientSession() as session:
                      async with session.post(url, json=payload, headers=headers) as resp:
                                        data = await resp.json()
                                        return data

              async def stream_prices(self, symbol, callback):
                        token = await self._get_token()
                        if not token:
                                      return
                                  pass
