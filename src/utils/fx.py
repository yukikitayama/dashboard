import requests
import pandas as pd

from .constants import API_URL, API_KEY, INSTRUMENT, ALIGNMENT_TIMEZONE


def make_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


def get_candles(
        instrument=INSTRUMENT,
        price="M",
        granularity="D",
        count="260",
        alignment_timezone=ALIGNMENT_TIMEZONE
):
    headers = make_headers()
    payload = {
        "price": price,
        "granularity": granularity,
        "count": count,
        "alignmentTimezone": alignment_timezone
    }
    r = requests.get(
        url=f"{API_URL}/v3/instruments/{instrument}/candles",
        headers=headers,
        params=payload
    )
    # print("get_candles()")
    # print(f"Status code: {r.status_code}")
    # pprint.pprint(r.json()["candles"])

    candles = r.json()["candles"]


    return candles


def convert_candle_to_df(candles):
    data = []
    for candle in candles:
        d = dict()
        d["time"] = candle["time"]
        d["open"] = candle["mid"]["o"]
        d["high"] = candle["mid"]["h"]
        d["low"] = candle["mid"]["l"]
        d["close"] = candle["mid"]["c"]
        data.append(d)

    # pprint.pprint(data)

    df = pd.DataFrame(data)
    df = clean_df(df)

    # print("convert_candle_to_df()")
    # print(df.shape)
    # print(df.dtypes)
    # print(df.head())
    # print(df.tail())
    # print()

    return df


def clean_df(df):
    df_c = df.copy()
    df_c["time"] = pd.to_datetime(df_c["time"])
    for c in ["open", "high", "low", "close"]:
        df_c[c] = pd.to_numeric(df_c[c])
    return df_c

