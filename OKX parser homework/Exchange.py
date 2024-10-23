import aiohttp
import asyncio
from aiohttp import ClientSession


class Exchange:
    def __init__(self,name):
        self.name=name
        self.base_url=self.get_url()

    def get_name(self):
        return self.name

    def get_url(self):
        urls={'OKX':'https://www.okx.com/api/v5/market/tickers'}
        return urls[self.name]

    async def request_coins(self,instType):
        async with ClientSession() as session:
            params={"instType": instType}
            async with session.get(url=self.base_url,params=params) as response:
                return await response.json()

