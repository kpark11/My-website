#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__,order=1)


test = dash.page_registry['path']

layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.P(test),
    html.Div([
            html.Div(
                dcc.Link(f"{page['name']}", href=page["path"])
                ) for page in dash.page_registry.values() if page["path"].startswith("/projects/")
        ]),
])