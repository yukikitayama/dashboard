import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from components.layout import title

# Dash setting
app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.FLATLY
    ]
)

# Dash layout
app.layout = dbc.Container(
    [
        dbc.Row(title),
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
