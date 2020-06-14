import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
from datetime import datetime

from vnpy.gateway.bitmex import BitmexGateway
from vnpy.trader.object import ContractData, HistoryRequest, Exchange, Interval, Product
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine

def create_layout(app):

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(BitmexGateway)
    contract = ContractData(gateway_name='BITMEX', symbol='XBTUSD', exchange=Exchange.BITMEX, name='XBTUSD', product=Product.FUTURES, size=1, pricetick=0.5, min_volume=1, stop_supported=True, net_position=True, history_data=True, option_strike=0, option_underlying='', option_type=None, option_expiry=None)
    req = HistoryRequest(symbol='XBTUSD', exchange=Exchange.BITMEX, interval=Interval.HOUR, end=datetime.today(), start=datetime(2020,6,1))
    gateway = main_engine.get_gateway('BITMEX')
    gateway.query_history(req)
    data = main_engine.query_history(req, contract.gateway_name)

    data_list = []
    for i in data:
        data_list.append({'date': i.datetime, 'close_price': i.close_price, 'high_price': i.high_price, 'low_price': i.low_price, 'open_price': i.open_price, 'volume': i.volume})
    df = pd.DataFrame(data_list)
    df['bar_color'] = np.where(df['close_price'] > df['open_price'], 'green', 'red')

    price_fig = go.Figure(data=[go.Candlestick(x=df['date'], 
                                        open=df['open_price'],
                                        high=df['high_price'],
                                        low=df['low_price'],
                                        close=df['close_price'])])
    price_fig.update_layout(xaxis_rangeslider_visible=False)
    volume_fig = go.Figure(data=[go.Bar(x=df['date'], y=df['volume'], marker_color=df['bar_color'])])
    
    return html.Div([dcc.Graph(figure=price_fig), dcc.Graph(figure=volume_fig)])