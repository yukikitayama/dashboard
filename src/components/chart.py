from datetime import datetime

import pandas as pd
import plotly.graph_objs as go
from dash import dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from google.cloud import bigquery
from dotenv import load_dotenv

from src.utils import fx
from src.utils.constants import SMA_WINDOWS

load_dotenv()
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("expand_frame_repr", False)


candles = fx.get_candles()
df = fx.convert_candle_to_df(candles)
df = fx.get_indicators(df)

print(df.shape)
# print(df.head())
print(df.tail(31))

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
        name=f"SMA({window})",
        connectgaps=True
    )
    data.append(scatter)


fig = go.Figure(
    data=data
)
# fig.update_xaxes(
#     rangebreaks=[
#         dict(bounds=["sat", "mon"])  # Hide weekends
#     ]
# )


@callback(
    Output("chart", "figure"),
    Input("update-button", "n_clicks"),
    State("date-picker-range", "start_date"),
    State("date-picker-range", "end_date")
)
def update_graph(n_clicks, start_date, end_date):
    s = start_date[:10]
    e = end_date[:10]

    print(f"Start: {s}, end: {e}")

    query = f"""
    SELECT
      date,
      open,
      high,
      low,
      close
    FROM
      `oanda.usdjpy_ny_day_mid_candles`
    WHERE
      date BETWEEN '{s}' AND '{e}'
    ORDER BY
      date
    """
    df = bigquery.Client().query(query).to_dataframe()
    df = fx.get_indicators(df)
    print(df.dtypes)
    print(df.head(1))
    print(df.tail(1))

    data = []
    candle_stick = go.Candlestick(
        x=df["date"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="Candlestick"
    )
    data.append(candle_stick)

    for window in SMA_WINDOWS:
        scatter = go.Scatter(
            x=df["date"],
            y=df[f"sma_{window}"],
            mode="lines",
            name=f"SMA({window})",
            connectgaps=True
        )
        data.append(scatter)

    figure = go.Figure(
        data=data
    )
    # figure.update_xaxes(
    #     rangebreaks=[
    #         dict(bounds=["sat", "mon"])  # Hide weekends
    #     ]
    # )

    return figure


main_chart = dbc.Container(
    [
        dcc.DatePickerRange(
            id="date-picker-range",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31)
        ),
        dbc.Button(
            "Update",
            id="update-button",
            n_clicks=0
        ),
        dbc.Row(
            dcc.Graph(
                id="chart",
                figure=fig,
                style={"height": "70vh"}
            )
        )
    ]
)
