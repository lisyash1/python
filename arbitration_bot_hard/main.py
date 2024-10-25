from CoinParser import CoinParse
from Exchange import Exchange
import asyncio
from File_analysis import file_analysis

async def main():

    exchanges={
        'OKX': Exchange('OKX'),
        'Bybit': Exchange('Bybit'),
        'Binance': Exchange('Binance'),
        'Kukoin': Exchange('Kukoin')
    }

    coins=['HMSTR','NOT','CATI','TON','SOL','BTC','BNB'] #список монет который необходим для анализа

    parsers = {name: CoinParse(exchange) for name, exchange in exchanges.items()}

    tasks = [parser.parse_coins(coins)
             for name, parser in parsers.items()]

    await asyncio.gather(*tasks)
    for name, parser in parsers.items():
        parser.save_to_json(f'{name}.json')

    print('Данные о монетах успешно сохранены в json')

    file_analysis(0.01) #передаем файлы для анализа и передаем нужный спред в него


asyncio.run(main())