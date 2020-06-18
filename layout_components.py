"""
Includes layout components that are used by multiple pages.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


SIGMA_DASH_LOGO = 'https://user-images.githubusercontent.com/53675680/84823182-eefdb080-afeb-11ea-828f-ce1856c444c5.png'


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(id='search-input', type='search', placeholder='Search')),
        dbc.Col(
            dbc.Button('Search', color='primary', className='ml-2'),
            width='auto',
        ),
    ],
    no_gutters=True,
    className='ml-auto flex-nowrap mt-3 mt-md-0',
    align='center',
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=SIGMA_DASH_LOGO, height='30px')),
                    dbc.Col(dbc.NavbarBrand('SigmaDash', className='ml-2')),
                ],
                align='center',
                no_gutters=True,
            ),
            href='https://parkershamblin.com/',
        ),
        dbc.NavbarToggler(id='navbar-toggler'),
        dbc.Collapse(search_bar, id='navbar-collapse', navbar=True),
    ],
    color='dark',
    dark=True,
)