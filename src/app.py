from dash import Dash, html

from components.chart import chart

app = Dash()

app.layout = html.Div(
    [
        html.H1("Yuki Kitayama"),
        chart
    ]
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
