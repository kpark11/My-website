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
    html.H2('This is our Projects: ',style={'textAlign': 'center', 'color': '#FF8903'}),
    ]),
    html.Div([
        html.Div(
             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
                ) for page in dash.page_registry.values() if page["name"].startswith("pages"),style={'textAlign':'center'}
        ])
    dash.page_container,
    
])