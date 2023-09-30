#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__,order=1)


layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Div([
        html.Div(
            dcc.Link('Automobile statistics', href=dash.page_registry['pages.automobile']['path'],style={'textAlign':'center'})
             )
]),
])