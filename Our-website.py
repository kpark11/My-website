#!/usr/bin/env python
# coding: utf-8

# In[22]:


### This program for Kiman and Abby to utilize the internet space for jobs, projects, and data visualizations. ###


import dash
from dash import dcc
from dash import State
from dash import html
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


image_path = 'https://github.com/kpark11/Our-website/tree/main/assets/Kiman-Abby.jpeg'

cwd = os.getcwd()
lists = os.listdir(cwd)
lists1 = os.listdir('/opt/render/project')
lists2 = os.listdir('/opt/render')
lists3 = os.listdir('/opt')

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

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
    html.P(lists),
    html.P(lists1),
    html.P(lists2),
    html.P(lists3)
])


    
    
if __name__ == '__main__':
    app.run_server(debug=True)


