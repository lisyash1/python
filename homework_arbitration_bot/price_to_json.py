import json
import requests

def price_to_json(coins):
    if len(coins)==0:
        print('Нужны монеты для поиска цены')
    else:
        url_kukoin = f"https://api.kucoin.com/api/v1/market/allTickers"
        url_binance = f"https://api.binance.com/api/v3/ticker/price"
        response_kukoin=requests.get(url_kukoin)
        if response_kukoin.status_code==200:
            data_kukoin=response_kukoin.json()
        else:
            print('При запросе в Kukoin возникли проблемы')
        response_binance=requests.get(url_binance)
        if response_binance.status_code==200:
            data_binance=response_binance.json()
        else:
            print('При запросе в Binance возникли проблемы')
        json_kukoin={}
        json_binance={}
        for coin in coins:
            for item in data_binance:
                if item['symbol']==f'{coin}USDT':
                    json_binance[f'{coin}']=item["price"]

            for token in data_kukoin["data"]["ticker"]:
                symbol = token["symbol"]
                price = token["last"]
                if symbol == f'{coin}-USDT':
                    json_kukoin[f'{coin}']=price

        with open('result_binance.json','w') as json_file:
            json.dump(json_binance, json_file)

        with open('result_kukoin.json','w') as json_file:
            json.dump(json_kukoin, json_file)

        print('Данные в json загружены успешно')

