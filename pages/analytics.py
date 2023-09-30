#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc


dash.register_page(__name__)


layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div(
             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
                ) for page in dash.page_registry.values() 
        if page["path"].startswith("/projects")
    ]),
    dash.page_container
])