import dash_bootstrap_components as dbc
import dash_html_components as html
import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ],
            align="start",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ],
            align="end",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns"), align="start"),
                dbc.Col(html.Div("One of three columns"), align="center"),
                dbc.Col(html.Div("One of three columns"), align="end"),
            ]
        ),
    ]
)

app.run_server(debug=True)