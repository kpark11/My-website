#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html,dcc

dash.register_page(__name__,order=4)

layout = html.Div([
    html.H2('This is archive page', className = ''),
    html.Div(children=[
        html.Div('My archive is in Github.', className = ''),
        html.Br(),
        html.Div('Go to my Github:', className = ''),
        html.Div(html.P(dcc.Link(href='https://github.com/kpark11',target='_blank'),
                        className = ''),)
    ], className='card')
], className = '')

