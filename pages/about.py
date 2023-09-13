# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:41:44 2023

@author: brian
"""

import dash
from dash import dcc,State,html


dash.register_page(__name__)

layout = html.Div([
        html.H2("About us:"),
        html.P('Kiman Park: Oak Ridge National Laboratory - Postdoctoral Research Associate'),
        dcc.Link('kimanpark33@gmail.com'),
        html.br(),
        html.P('Abby Carpenter: Tennessee Department of Health - Epidemiologist'),
        dcc.Link('carpenter.abby25@gmail.com')
        
])
