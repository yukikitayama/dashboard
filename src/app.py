import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.FLATLY
    ]
)

app.layout = dbc.Container(
    [
        html.H1("Yuki's Dashboard"),
        html.Div([
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}",
                    href=page["relative_path"]
                )
            ) for page in dash.page_registry.values()
        ]),
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
