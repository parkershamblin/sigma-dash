# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    price_performance,
)

app = dash.Dash(
    __name__, meta_tags = [{'name': 'viewport', 'content': 'width=device-width'}]
)
server = app.server

app.layout = html.Div(
    [dcc.Location(id='url', refresh=False), html.Div(id='page-content')]
)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    return price_performance.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)