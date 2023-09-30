#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc


dash.register_page(__name__)


layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Div([
        html.Div(
             dcc.Link(page['name'], href=page["relative_path"],style={'textAlign':'center'})
                ) for page in dash.page_registry.values() 
        if page["path"].startswith("/projects")
    ]),
])