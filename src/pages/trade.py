import dash
from dash import html
import dash_bootstrap_components as dbc

from src.components.chart import main_chart

dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row(main_chart)
    ]
)