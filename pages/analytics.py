#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc


dash.register_page(__name__,order=1,location = "sidebar")


layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Div([
        html.P(
             dcc.Link(f"{page['name']}", href=page["relative_path"],style={'textAlign':'center'})
                ) for page in dash.page_registry.values() if page["location"] != "sidebar"
        if page["path"].startswith("/projects")
    ])
])