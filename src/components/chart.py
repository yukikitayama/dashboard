import pandas as pd
import plotly.graph_objs as go
from dash import dcc

from src.utils import fx
from src.utils.constants import SMA_WINDOWS

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("expand_frame_repr", False)


candles = fx.get_candles()
df = fx.convert_candle_to_df(candles)
df = fx.get_indicators(df)

print(df.shape)
print(df.head())
print(df.tail())

data = []

candle_stick = go.Candlestick(
    x=df.index,
    open=df["open"],
    high=df["high"],
    low=df["low"],
    close=df["close"],
    name="Candlestick"
)
data.append(candle_stick)

for window in SMA_WINDOWS:
    scatter = go.Scatter(
        x=df.index,
        y=df[f"sma_{window}"],
        mode="lines",
        name=f"SMA({window})"
    )
    data.append(scatter)


fig = go.Figure(
    data=data
)

chart = dcc.Graph(
    id="chart",
    figure=fig
)
