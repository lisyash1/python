import pandas as pd
import os
import json

def file_analysis(spread):
    list_of_file=[]
    for file_name in os.listdir():
        if file_name.endswith('.json'):
            list_of_file.append(file_name)
    df_final=pd.DataFrame(columns=['coin','price','exchange'])
    for item in list_of_file:
        with open(item,'r') as file:
             data=json.load(file)
             df= pd.DataFrame(list(data.items()), columns=['coin', 'price'])
             df['exchange'] = item.replace('.json','')
             df_final=pd.concat([df_final,df],ignore_index=True)
    price=df_final.groupby('coin')['price'].agg(['max','min'])
    price=price.reset_index()
    for index, row in price.iterrows():
        if ((float(row['max']) - float(row['min']))/float(row['max']))*100>=spread:
            print(f'Нашел спред на монете {row['coin']} c {df_final['exchange'][(df_final['coin']==row['coin'])&(df_final['price']==row['max'])].item()} '
                  f'на {df_final['exchange'][(df_final['coin'] == row['coin']) & (df_final['price'] == row['min'])].item()}')
            print(f'Покупка {row['max']}$')
            print(f'Продажа {row['min']}$')
            print(f'Профит: {(float(row['max']) - float(row['min']))}')
