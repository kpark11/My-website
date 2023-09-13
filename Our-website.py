#!/usr/bin/env python
# coding: utf-8

# In[23]:


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
import datetime


app = dash.Dash(external_stylesheets=[dbc.themes.LUX],pages_folder="/opt/render/project/src/pages")

server = app.server

app.title = "Kiman and Abby Park"
app.style = {'textAlign':'center','color':'#503D36','font-size':24}
#---------------------------------------------------------------------------------

app.layout = html.Div([
    html.H1("Kiman and Abby Park", style={'textAlign': 'center', 'color': '#3E57B0','font-size':50}), 
    html.Div([
        html.Div(
             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
                ) for page in dash.page_registry.values()
            ]),
            dash.page_container
    ])

    
    
if __name__ == '__main__':
    app.run_server(debug=True)

