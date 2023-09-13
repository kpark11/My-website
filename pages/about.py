# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:41:44 2023

@author: brian
"""

import dash
from dash import dcc,State,html


dash.register_page(__name__)

layout = html.Div([
        html.H2("About us:",
                style={'textAlign': 'center', 'color': '#FF8903'}),
        html.Br(),
        html.P('Kiman Park, Ph.D.:',
               style={'textAlign': 'center'}),
        html.P('Oak Ridge National Laboratory - Postdoctoral Research Associate',
               style={'textAlign': 'center'}),
        html.P(dcc.Link(href='kimanpark33@gmail.com'),
                     style={'textAlign': 'center'}),
        html.Br(),
        html.P('Abby Carpenter, MPH:',
               style={'textAlign': 'center'}),
        html.P('Tennessee Department of Health - Epidemiologist',
               style={'textAlign': 'center'}),
        html.P(dcc.Link(href='carpenter.abby25@gmail.com'),
                     style={'textAlign': 'center'})
        
])
