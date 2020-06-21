import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from app import app

from layout_components import navbar

from pages.chart import update_price_fig
from settings import PRICE_FIG_LAYOUT

from bitmex import TradingChart
#################################################################################################################
################################################################################################################

#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas_datareader.data as web
from datetime import datetime
import numpy as np
import pandas as pd
from plotly.offline import plot


# In[ ]:





# In[33]:


import requests
import pandas as pd
import numpy as np
from datetime import datetime
from time import time
import plotly.graph_objects as go


# TODO Can I create these tab contents using list comprehension?
bitcoin_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='bitcoin-price-fig', figure=TradingChart(symbol='XBTUSD').get_figure()),
            html.P('Bitcoin', className='card-text'),
            dbc.Button('Click here', color='danger'),
        ],
        className='mt-3',
    )
)

cardano_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='cardano-price-fig', figure=TradingChart(symbol='ADAM20').get_figure()),
            html.P('Cardano', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)

bitcoin_cash_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='bitcoin-cash-price-fig', figure=TradingChart(symbol='BCHUSD').get_figure()),
            html.P('Bitcoin Cash', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)

EOS_token_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='EOS-token-price-fig', figure=TradingChart(symbol='EOSM20').get_figure()),
            html.P('EOS Token', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)

ethereum_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='ethereum-price-fig', figure=TradingChart(symbol='ETHUSD').get_figure()),
            html.P('Ethereum', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)

litecoin_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='litecoin-price-fig', figure=TradingChart(symbol='LTCM20').get_figure()),
            html.P('Litecoin', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)

tron_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='tron-price-fig', figure=TradingChart(symbol='TRXM20').get_figure()),
            html.P('Tron', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)

ripple_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id='ripple-price-fig', figure=TradingChart(symbol='XRPM20').get_figure()),
            html.P('Ripple', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)


tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label='Bitcoin', tab_id='Bitcoin'),
                dbc.Tab(label='Cardano', tab_id='Cardano'),
                dbc.Tab(label='Bitcoin Cash', tab_id='Bitcoin-Cash'),
                dbc.Tab(label='EOS Token', tab_id='EOS-Token'),
                dbc.Tab(label='Ethereum', tab_id='Ethereum'),
                dbc.Tab(label='Litecoin', tab_id='Litecoin'),
                dbc.Tab(label='Tron', tab_id='Tron'),
                dbc.Tab(label='Ripple', tab_id='Ripple'),
            ],
            id='tabs',
            active_tab='Bitcoin',
        ),
        html.Div(id='content'),
    ]
)

layout = html.Div(
    [
        navbar,
        html.P(id='search-output'),
        tabs,
    ]
)

# TODO This callback may need to placed on each page with navbar
# or in another file
# callback for toggling the collapse on small screens
@app.callback(
    Output('navbar-collapse', 'is_open'),
    [Input('navbar-toggler', 'n_clicks')],
    [State('navbar-collapse', 'is_open')],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('search-output', 'children'), [Input('search-input', 'value')])
def output_text(value):
    return value

@app.callback(Output('content', 'children'), [Input('tabs', 'active_tab')])
def switch_tab(selected_tab):
    if selected_tab == 'Bitcoin':
        return bitcoin_content
    elif selected_tab == 'Cardano':
        return cardano_content
    elif selected_tab == 'Bitcoin-Cash':
        return bitcoin_cash_content
    elif selected_tab == 'EOS-Token':
        return EOS_token_content
    elif selected_tab == 'Ethereum':
        return ethereum_content
    elif selected_tab == 'Litecoin':
        return litecoin_content
    elif selected_tab == 'Tron':
        return tron_content
    elif selected_tab == 'Ripple':
        return ripple_content