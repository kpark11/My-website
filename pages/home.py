#!/usr/bin/env python
# coding: utf-8


import dash
from dash import html


dash.register_page(__name__, path='/',order=0)


image_path = 'https://github.com/kpark11/Our-website/blob/main/assets/Kiman.jpeg?raw=true'

layout = html.Div([
        html.H2("Who I am:", className = 'ta archive-header'),
    html.P("""Highly analytical data scientist with a strong foundation in physics, 
           statistics, machine learning, and software development. 
           Proven track record in leveraging advanced computational methods to solve complex problems 
           and deliver impactful solutions. Experienced in collaborating with cross-functional teams to develop 
           innovative data-driven applications. Committed to continuous learning and staying updated with 
           the latest advancements in data science and technology.""", 
           className='ta'),
    html.Img(src=image_path,#app.get_asset_url('Kiman-Abby.jpeg'),
        className='image'),
], className = 'ta-left')

