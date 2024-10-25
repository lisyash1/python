import json
import asyncio

class CoinParse:
    def __init__(self,exchange):
        self.exchange=exchange
        self.coins={}

    async def parse_coins(self,coins):
        coin_json = await self.exchange.request_coins()
        if self.exchange.get_name()=='okx':
            for ticker in coin_json['data']:
                for item in coins:
                    if ticker['instId']==f'{item}-USDT':
                        symbol = ticker['instId']
                        last_price = ticker['last']
                        self.coins[symbol.replace('-USDT','')] = last_price
        elif self.exchange.get_name()=='kukoin':
            for token in coin_json["data"]["ticker"]:
                for item in coins:
                    if token["symbol"] == f'{item}-USDT':
                        symbol = token["symbol"]
                        last_price = token["last"]
                        self.coins[symbol.replace('-USDT','')] = last_price
        elif self.exchange.get_name()=='binance':
            coin_json = await self.exchange.request_coins()
            for ticker in coin_json:
                for item in coins:
                    if ticker['symbol'] == f'{item}USDT':
                        symbol = ticker['symbol']
                        last_price = ticker["price"]
                        self.coins[symbol.replace('USDT','')] = last_price
        elif self.exchange.get_name()=='bybit':
            for ticker in coin_json['result']['list']:
                for item in coins:
                    if ticker['symbol'] == f'{item}USDT':
                        symbol = ticker['symbol']
                        last_price = ticker['lastPrice']
                        self.coins[symbol.replace('USDT','')] = last_price


    def save_to_json(self,filename):
        with open(filename,'w') as file:
            json.dump(self.coins,file,indent=4)
