import dash
from dash import Dash
import dash_bootstrap_components as dbc

from src.components.layout import title

# Dash setting
app = Dash(
    __name__,
    use_pages=True,
    pages_folder="src/pages",
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
