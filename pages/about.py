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
                
                dcc.Markdown('''
                             <b>A Doctor of Philosophy (Ph.D.)</b> in Physical Chemistry, 
                             University of Tennessee, May 2018 – May 2023
                             ''',
                             dangerously_allow_html=True,), 
                
                dcc.Markdown('''
                             <b>A Bachelor of Science (B.S.)</b> in Chemistry, 
                             University of Tennessee, Aug 2014 – May 2018
                             ''',
                             dangerously_allow_html=True,),                 
                
                html.Br(),
                
                html.H2("Contact me on:", className = 'ta archive-header'),
                
                html.P(dcc.Link(href='kimanpark33@gmail.com')),
                html.P(dcc.Link('LinkedIn',href='https://www.linkedin.com/in/kiman-park/')),
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
