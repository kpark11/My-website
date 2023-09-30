#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc



dash.register_page(__name__,order=1)


layout = html.Div([
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Div([
           html.Div(children=[
               html.P(dcc.Link('Polarization matrix',href='https://reflection-list.onrender.com/')),
               html.P(dcc.Link('Automobile', href=dash.get_relative_path('/projects-automobile'))),
               ],
               style={'textAlign':'center'}            
                ) #for page in dash.page_registry.values() if page["path"].startswith("/projects/")
        
        
         #   html.Div(
         #       dcc.Link(f"{page['name']}", href=dash.get_relative_path('/projects/autombile'))
         #       ) #for page in dash.page_registry.values() if page["path"].startswith("/projects/")
        ]),
    #dash.page_container
])