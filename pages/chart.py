import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

from settings import COLORS, PRICE_FIG_LAYOUT, VOLUME_FIG_LAYOUT

from bitmex import request_history

from app import app

from layout_components import navbar


def load_inital_figures():
    # inital figures to load when user visits site
    df = request_history(symbol="XBTUSD")
    price_fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["date"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
            )
        ],
        layout=PRICE_FIG_LAYOUT,
    )
    price_fig.update_layout(title="XBTUSD")

    volume_fig = go.Figure(
        data=[go.Bar(x=df["date"], y=df["volume"], marker_color=df["color"])],
        layout=VOLUME_FIG_LAYOUT,
    )
    volume_fig.update_layout(title="XBTUSD Volume")

    return html.Div(
        [
            navbar,
            html.Br(),
            html.P(id="search-output"),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Dropdown(
                            id="ticker-symbol",
                            options=pd.read_csv(
                                "data/bitmex_tickers.csv"
                            ).to_dict(orient="records"),
                            multi=False,
                            value="XBTUSD",
                        )
                    ),
                ],
                align="start",
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="price-fig", figure=price_fig)),
                    dbc.Col(dcc.Graph(id="volume-fig", figure=volume_fig)),
                ],
                align="center",
            ),
        ]
    )


@app.callback(Output("price-fig", "figure"), [Input("ticker-symbol", "value")])
def update_price_fig(symbol):
    df = request_history(symbol)
    price_fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["date"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
            )
        ],
        layout=PRICE_FIG_LAYOUT,
    )
    price_fig.update_layout(title=f"{symbol} Price")
    return price_fig


@app.callback(
    Output("volume-fig", "figure"), [Input("ticker-symbol", "value")]
)
def update_volume_fig(symbol):
    df = request_history(symbol)
    volume_fig = go.Figure(
        data=[go.Bar(x=df["date"], y=df["volume"], marker_color=df["color"])],
        layout=VOLUME_FIG_LAYOUT,
    )
    volume_fig.update_layout(title=f"{symbol} Volume")
    return volume_fig
