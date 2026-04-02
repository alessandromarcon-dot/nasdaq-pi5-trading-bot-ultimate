import asyncio
import logging
from config_manager import ConfigManager
from main_dashboard import MainDashboard

async def main():
      logging.basicConfig(level=logging.INFO)
      config = ConfigManager()
      dashboard = MainDashboard(config)
      dashboard.mainloop()

if __name__ == "__main__":
      asyncio.run(main())
