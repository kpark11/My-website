#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html


dash.register_page(__name__, path='/',order=0)


image_path = 'https://github.com/kpark11/Our-website/blob/main/assets/Kiman-Abby.JPG?raw=true'

layout = html.Div([
        html.H2("Our Story:", style={'textAlign': 'center', 'color': '#FF8903'}),
    html.P("This is our story! We have so much to show and tell!", 
           style={'textAlign':'center'}),
    html.Img(src=image_path,#app.get_asset_url('Kiman-Abby.jpeg'),
        style={'width': 550, #'98%''
                'height': 650, #'60px'
                'borderRadius': "5px",
                'textAlign': "center",
                'margin': "0 auto",
               'display': 'block',
              'margin-left': 'auto',
              'margin-right': 'auto'}),
])

