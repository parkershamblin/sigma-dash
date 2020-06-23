import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from layout_components import navbar, TabContent, NewsCard


# TODO rename to bitcoin_chart_tab
bitcoin_content = TabContent(symbol="XBTUSD").content()
cardano_content = TabContent(symbol="ADAM20").content()
bitcoin_cash_content = TabContent(symbol="BCHUSD").content()
EOS_token_content = TabContent(symbol="EOSM20").content()
ethereum_content = TabContent(symbol="ETHUSD").content()
litecoin_content = TabContent(symbol="LTCM20").content()
tron_content = TabContent(symbol="TRXM20").content()
ripple_content = TabContent(symbol="XRPM20").content()

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Bitcoin", tab_id="Bitcoin"),
                dbc.Tab(label="Cardano", tab_id="Cardano"),
                dbc.Tab(label="Bitcoin Cash", tab_id="Bitcoin-Cash"),
                dbc.Tab(label="EOS Token", tab_id="EOS-Token"),
                dbc.Tab(label="Ethereum", tab_id="Ethereum"),
                dbc.Tab(label="Litecoin", tab_id="Litecoin"),
                dbc.Tab(label="Tron", tab_id="Tron"),
                dbc.Tab(label="Ripple", tab_id="Ripple"),
            ],
            id="tabs",
            active_tab="Bitcoin",
        ),
        html.Div(id="content"),
    ]
)

bitcoin_news = NewsCard(symbol="XBTUSD").card_content()


layout = html.Div([
    navbar,
    html.P(id="search-output"),
    tabs,
    bitcoin_news,
])


# TODO This callback may need to placed on each page with navbar
# or in another file
# callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("search-output", "children"), [Input("search-input", "value")]
)
def output_text(value):
    return value


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(selected_tab):
    if selected_tab == "Bitcoin":
        return bitcoin_content
    elif selected_tab == "Cardano":
        return cardano_content
    elif selected_tab == "Bitcoin-Cash":
        return bitcoin_cash_content
    elif selected_tab == "EOS-Token":
        return EOS_token_content
    elif selected_tab == "Ethereum":
        return ethereum_content
    elif selected_tab == "Litecoin":
        return litecoin_content
    elif selected_tab == "Tron":
        return tron_content
    elif selected_tab == "Ripple":
        return ripple_content
