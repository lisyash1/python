import json

def json_to_spread(spread):
    with open('result_binance.json', 'r') as json_file:
        binance=json.load(json_file)

    with open('result_kukoin.json', 'r') as json_file:
        kukoin=json.load(json_file)

    for key in binance.keys():
        if key in kukoin:
            if (abs(float(binance[key])-float(kukoin[key]))/max(float(binance[key]),float(kukoin[key])))*100>=spread:
                if binance[key]>kukoin[key]:
                    print(f'Нашел спред на монете {key} c Kukoin на Binance')
                    print(f'Покупка:{kukoin[key]}$')
                    print(f'Продажа:{binance[key]}$')
                    print(f'Профит:{float(binance[key])-float(kukoin[key])}$')
                else:
                    print(f'Нашел спред на монете {key} c Binance на Kukoin')
                    print(f'Покупка:{binance[key]}$')
                    print(f'Продажа:{kukoin[key]}$')
                    print(f'Профит:{float(kukoin[key])-float(binance[key])}$')
            else:
                print(f'По {key} спред не выгодный')
