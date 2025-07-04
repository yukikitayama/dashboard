import dash
from dash import html, dcc

title = html.H1("Yuki's Dashboard", style={"textAlign": "center"})

navigation = html.Div([
    html.Div(
        dcc.Link(
            f"{page['name']} - {page['path']}",
            href=page["relative_path"]
        )
    ) for page in dash.page_registry.values()
])