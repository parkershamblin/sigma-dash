import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from pages import (
    price_performance,
)
from bitmex import request_history
from settings import PRICE_FIG_LAYOUT, VOLUME_FIG_LAYOUT, COLORS

app = dash.Dash(
    __name__, meta_tags = [{'name': 'viewport', 'content': 'width=device-width'}], external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

app.layout = html.Div(children=[dcc.Location(id='url', refresh=False), html.Div(id='page-content')])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    return price_performance.create_layout(app)

@app.callback(Output('price-fig', 'figure'), [Input('ticker-symbol', 'value')])
def update_price_fig(symbol):
    df = request_history(symbol)
    price_fig = go.Figure(data=[go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])], layout=PRICE_FIG_LAYOUT)
    price_fig.update_layout(title=f'{symbol} Price')
    return price_fig

@app.callback(Output('volume-fig', 'figure'), [Input('ticker-symbol', 'value')])
def update_volume_fig(symbol):
    df = request_history(symbol)
    volume_fig = go.Figure(data=[go.Bar(x=df['date'], y=df['volume'], marker_color=df['color'])], layout=VOLUME_FIG_LAYOUT)
    volume_fig.update_layout(title=f'{symbol} Volume')
    return volume_fig

if __name__ == "__main__":
    app.config['suppress_callback_exceptions'] = True
    app.run_server(debug=True)