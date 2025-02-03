#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html, dcc

dash.register_page(__name__,order=1)


layout = html.Div([
    html.H2('Recent projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Div([
        html.P(dcc.Link('Pancreatic Cancer Detection',target='_blank',
                        href='https://github.com/kpark11/Springboard/blob/master/Capstone-Project/SERS_Raman_Pancreatic_Cancer/Capstone_Presentation.pdf')),
        html.P(dcc.Link("Driver's Fatigue Detection",target='_blank',
                        href='https://github.com/kpark11/RTI-simulator/blob/master/The%20Detection%20of%20Driver%E2%80%99s%20Fatigue%20Level.pdf')),
        html.P(dcc.Link('Pneumonia Detection',target='_blank',
                        href='https://github.com/kpark11/Pneumonia_Detection/blob/master/Pneumonia_Detection.ipynb')),
        html.P(dcc.Link('Point-Charge Model', href=dash.get_relative_path('/projects-pointcharge'))),
        html.P(dcc.Link('Polarization Matrix',target='_blank'
                        ,href='https://reflection-list.onrender.com/')),
        html.P(dcc.Link('Automobile Sales Statistics',target='_blank', 
                        href=dash.get_relative_path('/projects-automobile'))),
        html.P(dcc.Link('Origin of Names using recurrent Neural Network',target='_blank', 
                        href=dash.get_relative_path('/projects-name-origins'))),
        html.Br(),
        html.Br(),
        html.A('More in Github',href='https://github.com/kpark11',target='_blank'),
        
         #   html.Div(
         #       dcc.Link(f"{page['name']}", href=dash.get_relative_path('/projects/autombile'))
         #       ) #for page in dash.page_registry.values() if page["path"].startswith("/projects/")
        ], className = 'ta'),
    #dash.page_container
],  className = 'ta')