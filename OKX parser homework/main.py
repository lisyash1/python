from CoinParser import CoinParse
from Exchange import Exchange
import asyncio

async def main():
    newcoins=Exchange('OKX')
    parse=CoinParse(newcoins)
    await parse.parse_coins()
    parse.save_to_json('OKX.json')
    print('Данные о монетах сохранены в OKX.json')


asyncio.run(main())