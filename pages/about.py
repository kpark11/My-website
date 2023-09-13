# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:41:44 2023

@author: brian
"""

import dash
from dash import dcc,State,html


dash.register_page(__name__)

layout = html.Div([
        html.H2("About us:",style={'textAlign': 'center', 'color': '#FF8903'}),
        html.P('Kiman Park:',style={'textAlign': 'center', 'color': '#FF8903'}),
        html.P('Oak Ridge National Laboratory - Postdoctoral Research Associate',style={'textAlign': 'center', 'color': '#FF8903'}),
        dcc.Link('kimanpark33@gmail.com',style={'textAlign': 'center', 'color': '#FF8903'}),
        html.br(),
        html.P('Abby Carpenter:',style={'textAlign': 'center', 'color': '#FF8903'}),
        html.P('Tennessee Department of Health - Epidemiologist',style={'textAlign': 'center', 'color': '#FF8903'}),
        dcc.Link('carpenter.abby25@gmail.com',style={'textAlign': 'center', 'color': '#FF8903'})
        
])
