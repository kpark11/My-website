#!/usr/bin/env python
# coding: utf-8

# In[21]:


### This program for Kiman and Abby to utilize the internet space for jobs, projects, and data visualizations. ###


import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import os

image_path = 'https://github.com/kpark11/Our-website/blob/main/assets/statistics.webp?raw=true'

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])#,pages_folder="/opt/render/project/src/pages")

#server = app.server

app.title = "Kiman and Abby Park"
app.style = {'textAlign':'center','color':'#503D36','font-size':24}
#---------------------------------------------------------------------------------

app.layout = html.Div([
    
    html.Div([html.Img(src=image_path,
    style={
          'verticalAlign':'middle',
          'textAlign': 'center',
          #'background-image':image,
          'position':'fixed',
          'width':'100%',
          'height':'100%',
          'top':'0px',
          'left':'0px',
          'z-index':'1000',
          'opacity': '0.2'
            })
    ]),
    
    html.H1("Kiman and Abby Park", style={'textAlign': 'center', 'color': '#3E57B0','font-size':50}), 
    html.P(print(cwd)),
    html.P(print(directors)),
        html.Div([
            html.Div(
                dcc.Link(f"{page['name']}", href=page["path"])
                ) for page in dash.page_registry.values() if not page["path"].startswith("/projects")
                ]),
            dash.page_container
    ])
    
    
if __name__ == '__main__':
    app.run_server(debug=True)

