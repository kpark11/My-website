#!/usr/bin/env python
# coding: utf-8

# In[11]:


### This program for Kiman and Abby to utilize the internet space for jobs, projects, and data visualizations. ###


import dash
from dash import dcc,State,html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import os
import re
import sys
import fnmatch
import matplotlib.pyplot as plt
import base64
import dash_bootstrap_components as dbc



image_path = 'https://github.com/kpark11/Our-website/blob/main/assets/Kiman-Abby.jpeg?raw=true'

page = 'https://github.com/kpark11/Our-website/tree/main/pages'

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])



os.chdir('/opt/render/project/src/')
cwd = os.listdir('/opt/render/project/src/')
print(cwd)
cwd1 = os.listdir('/opt/render/project/')
print(cwd1)
cwd2 = os.listdir('/opt/render/')
print(cwd2)



server = app.server

app.title = "Kiman and Abby Park"
app.style = {'textAlign':'center','color':'#503D36','font-size':24}
#---------------------------------------------------------------------------------

app.layout = html.Div([
    html.H1("Kiman and Abby Park", style={'textAlign': 'center', 'color': '#3E57B0','font-size':50}),
    html.H2("Our Story:", style={'textAlign': 'center', 'color': '#FF8903'}),
    html.P("This is our story! We have so much to show and tell!", 
           style={'textAlign':'center'}),
    html.Img(src=image_path,#app.get_asset_url('Kiman-Abby.jpeg'),
        style={'width': 500, #'98%''
                'height': 400, #'60px'
                'borderRadius': "5px",
                'textAlign': "center",
                'margin': "0 auto",
               'display': 'block',
              'margin-left': 'auto',
              'margin-right': 'auto'}),
    
    html.P(cwd),
    html.P(cwd1),
    html.P(cwd2),
    
    html.Div([
        html.Div(
            dcc.Link(page)
                ) for page in dash.page_registry.values()
            ]),
            dash.page_container
    ])

    
    
if __name__ == '__main__':
    app.run_server(debug=True)

