import requests
import pandas as pd
import json
import time
from datetime import datetime

access_key = "Minha api do site marketstack"
base_url = "http://api.marketstack.com/v1/eod"

stock_tickers = {
    "Saudi Aramco": "2222.SR",
    "Exxon Mobil": "XOM",
    "Chevron Corp": "CVX",
    "Shell PLC": "SHEL",
    "TotalEnergies": "TTE",
    "BP PLC": "BP",
    "Equinor": "EQNR"
}

all_stocks_data = {}
start_date = "2025-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")
request_interval_seconds = 5

for company_name, ticker in stock_tickers.items():
    params = {
        "access_key": access_key,
        "symbols": ticker,
        "date_from": start_date,
        "date_to": end_date,
        "limit": 1000,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data and 'data' in data and data['data']:
            df = pd.DataFrame(data['data'])
            df['date'] = pd.to_datetime(df['date'])
            df = df.rename(columns={'date': 'datetime'})

            numeric_cols = ['open', 'high', 'low', 'close', 'volume','dividend']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            df['symbol'] = ticker
            all_stocks_data[ticker] = df

        elif 'error' in data:
            pass
        else:
            pass

    except requests.exceptions.RequestException:
        pass
    except ValueError:
        pass
    except Exception:
        pass

    if ticker != list(stock_tickers.values())[-1]:
        time.sleep(request_interval_seconds)

if all_stocks_data:
    valid_dataframes = [df for df in all_stocks_data.values() if not df.empty]

    if valid_dataframes:
        combined_df = pd.concat(valid_dataframes).sort_values(by=['symbol', 'datetime']).reset_index(drop=True)
    else:
        combined_df = pd.DataFrame()
else:
    combined_df = pd.DataFrame()


df = combined_df.drop(columns=['dividend','split_factor'])
simbolo_empresa = {
    "XOM": "Exxon Mobil",
    "CVX": "Chevron Corp",
    "SHEL": "Shell PLC",
    "TTE": "TotalEnergies",
    "BP": "BP PLC",
    "EQNR": "Equinor",
    "2222.SR": "Saudi Aramco"
}

simbolo_para_empresa = {}
simbolo_para_empresa.update(simbolo_empresa)

df['nome_empresa'] = df['symbol'].map(simbolo_para_empresa)

mask = df['symbol'] == '2222.SR'
columns_to_divide = ['open', 'high', 'low', 'close', 'adj_low', 'adj_high', 'adj_close', 'adj_open']

df.loc[mask, columns_to_divide] = df.loc[mask, columns_to_divide] / 3.75

df.to_csv('AnalisePetro.xlsx')
