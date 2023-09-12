#!/usr/bin/env python
# coding: utf-8

# In[13]:


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

cwd = os.getcwd()
print(cwd)
file_path = cwd+'\download'
try:
    os.mkdir(file_path)
except:
    print('already exists')


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

    
])


    
    
if __name__ == '__main__':
    app.run_server(debug=True)


