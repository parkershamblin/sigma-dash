import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

DBC_DOCS = "https://dash-bootstrap-components.opensource.faculty.ai/"
DBC_GITHUB = "https://github.com/facultyai/dash-bootstrap-components"
SIGMA_DASH_LOGO = "https://user-images.githubusercontent.com/53675680/84823182-eefdb080-afeb-11ea-828f-ce1856c444c5.png"


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
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
                    dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)

tv_ticker_header = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "70px", "border-style": "solid"},
                    ),
                    md=2,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "70px", "border-style": "solid"},
                    ),
                    md=2,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 3",
                        style={"height": "70px", "border-style": "solid"},
                    ),
                    md=2,
                ),
                            dbc.Col(
                    html.Div(
                        "This is column 1",
                        style={"height": "70px", "border-style": "solid"},
                    ),
                    md=2,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "70px", "border-style": "solid"},
                    ),
                    md=2,
                ),
                dbc.Col(
                    html.Div(
                        "This is column 2",
                        style={"height": "70px", "border-style": "solid"},
                    ),
                    md=2,
                ),
            ],
            no_gutters=True,
        ),
    ]
)