import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from bitmex import TradingChart


class TabContent:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = self.get_name()

    def get_name(self):
        if self.symbol == "XBTUSD":
            self.name = "Bitcoin"
        elif self.symbol == "ADAM20":
            self.name = "Cardano"
        elif self.symbol == "BCHUSD":
            self.name = "Bitcoin-Cash"
        elif self.symbol == "EOSM20":
            self.name = "EOS-Token"
        elif self.symbol == "ETHUSD":
            self.name = "Ethereum"
        elif self.symbol == "LTCM20":
            self.name = "Litecoin"
        elif self.symbol == "TRXM2":
            self.name = "Tron"
        elif self.symbol == "XRPM20":
            self.name = "Ripple"
        elif self.symbol == "XRPM20":
            self.name = "Ripple"

    def content(self):
        return dbc.Card(
            dbc.CardBody(
                [
                    html.Div([
                        dbc.Button("Default chart", color="primary", active=True, outline=True, style={"float": "right"}),
                        dbc.Button("Full-featured chart", color="primary", outline=True, style={"float": "right"})
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dcc.Graph(
                            id=f"{self.name}-price-fig",
                            figure=TradingChart(symbol="XBTUSD").get_figure(),
                            ),
                        html.P(self.name, className="card-text"),
                    ])
                ],
                className="mt-3"
            )
        )