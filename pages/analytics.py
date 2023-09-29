#!/usr/bin/env python
# coding: utf-8




import dash
from dash import html, dcc, callback
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px


dash.register_page(__name__)


layout = html.Div([
    
    html.Div([
        html.Div(
             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"],style={'textAlign':'center'})
                ) for page in dash.page_registry.values()
            if page["name"].startswith("Pages")
        
        ]),
            dash.page_container
    
    ])