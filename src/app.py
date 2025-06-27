import plotly.graph_objs as go

from utils import fx

candles = fx.get_candles()
df = fx.convert_candle_to_df(candles)

print(df.shape)
print(df.head())
print(df.tail())

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df["time"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"]
        )
    ]
)

fig.show()