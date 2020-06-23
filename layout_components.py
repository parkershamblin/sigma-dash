# This file contains layout components that are used by multiple pages.

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from bitmex import TradingChart
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SIGMA_DASH_LOGO = "https://user-images.githubusercontent.com/53675680/84823182-eefdb080-afeb-11ea-828f-ce1856c444c5.png"

search_bar = dbc.Row(
    [
        dbc.Col(
            dbc.Input(id="search-input", type="search", placeholder="Search")
        ),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=SIGMA_DASH_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("SigmaDash", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://parkershamblin.com/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)


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
                    dbc.ButtonGroup(
                        [
                            dbc.Button("Default chart", color="primary", active=True, outline=True),
                            dbc.Button("Full-featured chart", color="primary", outline=True)
                        ],
                        style={"float": "right"},
                    ),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        dcc.Graph(
                            id=f"{self.name}-price-fig",
                            figure=TradingChart(symbol=self.symbol).get_figure(),
                            ),
                        html.P(self.name, className="card-text"),
                    ])
                ],
                className="mt-3"
            )
        )


class NewsCard:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_news(self):
        baseurl = "https://www.tradingview.com/symbols"
        symbol = self.symbol
        exchange = "BITMEX"
        url = f"{baseurl}/{symbol}/?exchange={exchange}"


        # run headless
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.

        res = []

        driver = webdriver.Chrome("misc/chromedriver.exe", options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        news_div = soup.find("div", {"class": "js-news-body-container"})
        for child in news_div.find_all('a'):
            res.append(child['href'])
            # counter = 0
            # for child2 in child.find_all('span'):
            #     counter += 1
            #     res.append(child)
        return res

    def card_content(self):
        return html.Div(
                [
                    html.H2("News"),
                    dbc.CardDeck(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader("Header"),
                                    dbc.CardBody(
                                        [
                                            html.H5(
                                                "This card has a title",
                                                className="card-title",
                                            ),
                                            html.P("test", className="card-text"),
                                        ]
                                    ),
                                ]
                            ),
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5(
                                                "This card has a title",
                                                className="card-title",
                                            ),
                                            html.P(
                                                "and some text, but no header",
                                                className="card-text",
                                            ),
                                        ]
                                    )
                                ],
                                outline=True,
                                color="primary",
                            ),
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5(
                                                "This card has a title",
                                                className="card-title",
                                            ),
                                            html.P(
                                                str(self.get_news()),
                                                className="card-text",
                                            ),
                                        ]
                                    ),
                                    dbc.CardFooter("Footer"),
                                ],
                                outline=True,
                                color="dark",
                            ),
                        ]
                    ),
                ]
            )
