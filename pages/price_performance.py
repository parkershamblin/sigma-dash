import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
from datetime import datetime

from settings import COLORS, PRICE_FIG_LAYOUT, VOLUME_FIG_LAYOUT

from bitmex import request_history

def create_layout(app):
    # inital figures to load when user visits site
    df = request_history(symbol='XBTUSD')
    price_fig = go.Figure(data=[
        go.Candlestick(
            x=df['date'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'])],
        layout=PRICE_FIG_LAYOUT)
    price_fig.update_layout(title='XBTUSD')

    volume_fig = go.Figure(data=[go.Bar(x=df['date'], y=df['volume'], marker_color=df['color'])], layout=VOLUME_FIG_LAYOUT)
    volume_fig.update_layout(title='XBTUSD Volume')

    return html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id='ticker-symbol', options=pd.read_csv(r"C:\Users\Parke\Documents\GitHub\sigma-dash\data\bitmex_tickers.csv").to_dict(orient='records'), multi=False, value='XBTUSD')),
                dbc.Col(html.Div("One of three columns")),
            ],
            align="start",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='price-fig', figure=price_fig)),
                dbc.Col(dcc.Graph(id='volume-fig', figure=volume_fig)),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ],
            align="end",
        ),
    ]
)