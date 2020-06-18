import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app

from layout_components import navbar

tab1_content = dbc.Card(
    [
        html.P('This is tab 1!', className='card-text'),
        dbc.Button('Click here', color='success'),
    ],
    className='mt-3',
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P('This is tab 2!', className='card-text'),
            dbc.Button("Don't click here", color='danger'),
        ]
    ),
    className='mt-3',
)


tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label='Tab 1', tab_id='tab-1'),
                dbc.Tab(label='Tab 2', tab_id='tab-2'),
            ],
            id='tabs',
            active_tab='tab-1',
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
    if selected_tab == 'tab-1':
        return tab1_content
    elif selected_tab == 'tab-2':
        return tab2_content