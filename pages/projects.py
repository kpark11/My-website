#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc



dash.register_page(__name__,order=1)


layout = html.Div([
    html.H2('This is my projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Div([
            html.P(dcc.Link('Polarization Matrix',href='https://reflection-list.onrender.com/')),
            html.P(dcc.Link('Automobile Sales Statistics', href=dash.get_relative_path('/projects-automobile'))),
            html.P(dcc.Link('Origin of Names using recurrent Neural Network', href=dash.get_relative_path('/projects-name-origins'))),
            html.Br(),
            html.Br(),
            html.A('More in Github',href='https://github.com/kpark11',target='_blank'),
        
         #   html.Div(
         #       dcc.Link(f"{page['name']}", href=dash.get_relative_path('/projects/autombile'))
         #       ) #for page in dash.page_registry.values() if page["path"].startswith("/projects/")
        ], className = 'ta'),
    #dash.page_container
],  className = 'ta')