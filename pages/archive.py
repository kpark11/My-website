#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html,dcc

dash.register_page(__name__,order=3)

layout = html.Div([
    html.H2('This is our Archive page',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Div('Our archive is in Github.',style={'textAlign':'center'}),
    html.Br(),
    html.Div('Go to our Github:',style={'textAlign':'center'}),
    html.Div(html.P(dcc.Link(href='https://github.com/kpark11'),
                       style={'textAlign': 'center'}),)
])

