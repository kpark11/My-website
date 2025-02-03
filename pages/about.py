# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:41:44 2023

@author: brian
"""

import dash
from dash import dcc,State,html


dash.register_page(__name__,order=2)

layout = html.Div([
        html.H2("About me:", className = 'ta archive-header'),
        html.Br(),
        
        
         html.Div([
            html.Div(children=[
               
                dcc.Markdown('**Current Working History:**', className = 'bf underline'),
                
                html.P('Springboard - Data Scientist Fellow'),
                
                dcc.Markdown('**Previous Working History:**', className = 'bf underline'),
               
                html.P('Oak Ridge National Laboratory - Postdoctoral Research Associate'),
                
                html.P('University of Tennessee - Graduate Research Assistant'), 
              
                html.P('University of Tennessee - Undergraduate Research Assistant'), 
                
                html.Br(),
                
                dcc.Markdown('**Education:**', className = 'bf underline'),
                
                dcc.Markdown('**A Doctor of Philosophy (Ph.D.)** in Physical Chemistry | University of Tennessee | MAY 2018 – MAY 2023'), 
                
                dcc.Markdown('**A Bachelor of Science (B.S.)** in Chemistry | University of Tennessee | AUG 2014 – MAY 2018'),                 
                
                html.Br(),
                
                html.H2("Contact me on:", className = 'ta archive-header'),
                
                html.P(dcc.Link(href='kimanpark33@gmail.com')),
            ], className = 'ta'
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
