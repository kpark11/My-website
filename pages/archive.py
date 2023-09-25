#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html,dcc

dash.register_page(__name__)

layout = html.Div([
    html.H2('This is our Archive page',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Div('This is our Archive page content.',style={'textAlign':'center'}),
    html.Div('Go to the github page:'),
    html.Div(html.P(dcc.Link(href='https://github.com/kpark11'),
                       style={'textAlign': 'center'}),)
])

