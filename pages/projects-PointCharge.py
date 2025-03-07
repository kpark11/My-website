# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:04:46 2025

@author: brian
"""

import dash
from dash import dcc,State,html
import os
import dash_bootstrap_components as dbc


image_path = 'https://github.com/kpark11/Our-website/blob/main/assets/PC'

dash.register_page(__name__)

layout = html.Div([
        html.H2("Point-Charge Model", className = 'ta archive-header'),
        html.Br(),
        

        html.Div(children=[
            html.Div(dcc.Markdown('**Using the software:**',  className = 'bf underline'),
                     className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                These software and package allow researchers to calculate the optical properties
                using Point-Charge modeling.
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                I will demonstrate the workflow and the usage here.
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'1.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                As you can see, this is the initialized GUI. First, you need to choose the metal ion
                that you want to calculate.
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Then, you have to input the correct L and S for that metal ion. 
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Next, Z value is needed. For example, oxygen ligand has 2-, so the Z value
                is 2 here. If it is chloride, the value would be 1.
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Lastly, you can specify the number of ligands around the metal ion. By clicking
                "insert", it will populate the input form to write the metal ion and ligand positions, 
                which you can easily find in .cif files.
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                You can change the name of ion names, 
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                You are ready to click the "initialize" button. It will calculate the 
                B<sup>l</sup><sub>m</sub> parameters and plot the energies. Also, the result
                section will populate with the parameters you have written and show the 
                B<sup>l</sup><sub>m</sub> parameters it calculated. 
                '''],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'2.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'3.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'4.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Furthermore, you can just plug in the B<sup>l</sup><sub>m</sub> parameters
                on the right to plot and calculate the energies. 
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                As you can see, you can save your workspace, so you do not have to input all of the 
                parameters again. You can also see the r<sub>l</sub> and theta parameters that I am 
                using. 
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Furthermore, you can look at the log that it creates to see previous values and energies
                that you calculated. You can clear the log as well. Help and operational manual is under
                construction as of now.
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Lastly, it will also calculate Sping-Orbit coupling strength, Spin-Spin coupling strength, and 
                Moleculate Field strength as you can see below. 
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'5.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                You can click on the "get energies" button to see the calculated energies with 
                B<sup>l</sup><sub>m</sub> parameters and show them in the results. It will also give
                eigenvectors as well. See below.
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'6.PNG?raw=true'),style={'width':'100%',
                                                                                   'margin':'0px'}),className = 'cardShowAni'),
            
            html.Br(),
            html.Div(dcc.Markdown('**Using the Python package:**', className = 'bf underline'), 
                     className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                You can use Python to calculate optical properties using this package! You can do so much more!
                Similarly, you have to input metal ion, L, S, and ligand positions to calculate 
                B<sup>l</sup><sub>m</sub> parameters.
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'7.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Here is the result in the terminal.
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'8.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Or you can input your own B<sup>l</sup><sub>m</sub> parameters.
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'9.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Now, you can diagonalize it and calculate energies and eigenvectors. 
                It will show the energies and plot them
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'10.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'11.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                Once you have all of parameters and energies, you can simulate various properties.
                The below is the magnetic moment of each axis and electronic states. 
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'12.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'13.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(dcc.Markdown([
                '''
                You can also calculate and simulate specific heat, magnetic entropy, 
                Zeeman effect, and magnetic susceptibility
                '''
                ],
                dangerously_allow_html=True,),
                className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'14.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'15.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'16.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'17.PNG?raw=true'),),className = 'cardShowAni'),
            html.Div(html.Img(src=os.path.join(image_path,'18.PNG?raw=true'),),className = 'cardShowAni'),
        ]),
])
