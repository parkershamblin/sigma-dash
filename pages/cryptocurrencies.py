import dash_core_components as dcc
import dash_html_components as html
import dash_table

from app import app

from layout_components import navbar
from coinmarketcap import crypto_market


crypto_market_df = crypto_market()


layout = html.Div([
    navbar,
    dash_table.DataTable(
            id='top-crypto-table',
            columns=[{"name": i, "id": i} for i in crypto_market_df.columns],
            data=crypto_market_df.to_dict('records'),
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{{col}}} < 0'.format(col=col),
                        'column_id': col
                    },
                    'color': 'red',
                } for col in crypto_market_df.columns
            ] +
            [
                {
                    'if': {
                        'filter_query': '{{{col}}} > 0'.format(col=col),
                        'column_id': col
                    },
                    'color': 'green',
                } for col in crypto_market_df.columns
            ],
            css=[{
                'selector': '.dash-spreadsheet-container .dash-spreadsheet-inner *, .dash-spreadsheet-container .dash-spreadsheet-inner *:after, .dash-spreadsheet-container .dash-spreadsheet-inner *:before',
                'rule': 'box-sizing: inherit; width: 50%;'
            }]
        )
    ])

