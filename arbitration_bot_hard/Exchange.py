import aiohttp
import asyncio
from aiohttp import ClientSession


class Exchange:
    def __init__(self,name):
        self.name=name.lower()
        self.base_url=self.get_url()

    def get_name(self):
        return self.name

    def get_url(self):
        urls={'okx':'https://www.okx.com/api/v5/market/tickers?instType=SPOT',
              'kukoin':'https://api.kucoin.com/api/v1/market/allTickers',
              'binance':'https://api.binance.com/api/v3/ticker/price',
              'bybit':'https://api.bybit.com/v5/market/tickers?category=spot'}
        return urls[self.name]

    async def request_coins(self):
        async with ClientSession() as session:
            async with session.get(url=self.base_url) as response:
                return await response.json()

