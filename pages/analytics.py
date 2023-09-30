#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc


dash.register_page(__name__,order=1,location = "sidebar")


layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Div([
        html.P(
             dcc.Link("Automobile", href="/projects/",style={'textAlign':'center'})
             )
]),
])