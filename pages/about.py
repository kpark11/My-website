# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:41:44 2023

@author: brian
"""

import dash
from dash import dcc,State,html


dash.register_page(__name__,order=1)

layout = html.Div([
        html.H2("About me:", className = ''),       
        html.Div([
            html.Div(children=[
                html.Div(children=[
                    dcc.Markdown('**Current Relevant Experience:**', className = 'bf underline'),
                    
                    html.P('Springboard - Data Scientist Fellow'),
                    
                    dcc.Markdown('**Previous Relevant Experience:**', className = 'bf underline'),
                
                    html.P('Oak Ridge National Laboratory - Postdoctoral Research Associate'),
                    
                    html.P('University of Tennessee - Graduate Research Assistant'), 
                
                    html.P('University of Tennessee - Undergraduate Research Assistant'), 
                ], className='card'),

                html.Div(children=[
                    
                    dcc.Markdown('**Education:**', className = 'bf underline'),
                    
                    dcc.Markdown(['''
                                <b>A Doctor of Philosophy (Ph.D.)</b> in Physical Chemistry, 
                                University of Tennessee, May 2018 – May 2023
                                '''],
                                dangerously_allow_html=True,), 
                    
                    dcc.Markdown(['''
                                <b>A Bachelor of Science (B.S.)</b> in Chemistry, 
                                University of Tennessee, Aug 2014 – May 2018
                                '''],
                                dangerously_allow_html=True,),
                ], className='card w1'),
                
                html.H2("Contact me on:", className = ''),
                html.Div(children=[
                    dcc.Link(href='kimanpark33@gmail.com',target='_blank'),
                    dcc.Link('LinkedIn',target='_blank',
                                    href='https://www.linkedin.com/in/kiman-park/'),
                ], className='card w2'),
            ], className = ''),
            ]),
])
