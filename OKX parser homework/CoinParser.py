import json
import asyncio

class CoinParse:
    def __init__(self,exchange):
        self.exchange=exchange
        self.instType='SPOT'
        self.coins={}

    async def parse_coins(self):
        coin_json=await self.exchange.request_coins(self.instType)
        for ticker in coin_json['data']:
            symbol = ticker['instId']
            last_price = ticker['last']
            self.coins[symbol] = last_price

    def save_to_json(self,filename):
        with open(filename,'w') as file:
            json.dump(self.coins,file)
