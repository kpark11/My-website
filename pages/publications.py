# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:11:20 2025

@author: brian
"""

import dash
from dash import html,dcc

dash.register_page(__name__,order=3)

layout = html.Div([
    html.H2('Publications:', className = 'ta archive-header'),
    html.Br(),
    
    dcc.Link('Magnetically-driven quantum phase transitions in a low-dimensional pyrazine-bridged Cu<sup>2+</sup> chain magnet',
             href='https://pubs.acs.org/journal/inocaj', className = 'ta'),
    html.Div('Inorganic Chemistry, (Submitted) January 1, 2025'),
    dcc.Link('Spin-phonon interactions and magnetoelectric coupling in Co<sub>4</sub>B<sub>2</sub>O<sub>9</sub> (B = Nb, Ta)',
             href='https://pubs.aip.org/aip/apl/article-abstract/122/18/182902/2887973/Spin-phonon-interactions-and-magnetoelectric?redirectedFrom=PDF', 
             className = 'ta'),
    html.Div('Applied Physics Letters, May 2, 2023', className = 'ta'),
    html.Link('Nonreciprocal directional dichroism at telecom wavelengths',
              href='https://www.nature.com/articles/s41535-022-00438-6', className = 'ta'),
    html.Div('npj Quantum Materials, April 4, 2022'),
    html.Link('Vibrational fingerprints of ferroelectric HfO<sub>2</sub>',
              href='https://www.nature.com/articles/s41535-022-00436-8', className = 'ta'),
    html.Div('npj Quantum Materials, March 18, 2022', className = 'ta'),
    html.Link('Band-Mott mixing hybridizes the gap in Fe<sub>2</sub>Mo<sub>3</sub>O<sub>8</sub>', 
              href='https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.195143', className = 'ta'),
    html.Div('Physical Review B, November 22, 2021', className = 'ta'),
    html.Link('Jolly green MOF: confinement and photoactivation of photosystem I in the metal-organic framework ZIF-8',
              href='https://pubs.rsc.org/en/content/articlelanding/2019/na/c8na00093j', className = 'ta'),
    html.Div('Nanoscale Advances, October 11, 2018', className = 'ta'),
    html.Link('A facile and surfactant-free route for nanomanufacturing of tailored ternary nanoalloys as superior oxygen reduction reaction electrocatalysts',
              href='https://pubs.rsc.org/en/content/articlelanding/2017/cy/c7cy00073a', className = 'ta'),
    html.Div('Catalysis Science & Technology, April 6, 2017', className = 'ta'),
])
