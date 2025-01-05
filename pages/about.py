# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:41:44 2023

@author: brian
"""

import dash
from dash import dcc,State,html


dash.register_page(__name__,order=2)

layout = html.Div([
        html.H2("About me:",
                style={'textAlign': 'center', 'color': '#FF8903'}),
        html.Br(),
        
        
         html.Div([
            html.Div(children=[
               
               html.P('Kiman Park, Ph.D.:',
                       style={'textAlign': 'center','font-weight': 'bold'}),
                html.P('Oak Ridge National Laboratory - Postdoctoral Research Associate',
                       style={'textAlign': 'center'}),
                html.P(dcc.Link(href='kimanpark33@gmail.com'),
                       style={'textAlign': 'center'}),
                    ],
                        #style={
                        #'backgroundColor':'darkslategray',
                        #'color':'lightsteelblue',
                        #'height':'100px',
                        #'margin-left':'10px',
                        #'width':'49%',
                        #'text-align':'center',
                        #'display':'inline-block'}
                        ),
            ]),
         
         
        
        
        
])
