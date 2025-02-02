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
    
    dcc.Markdown(
            [
                """
            <dccLink href="https://pubs.acs.org/journal/inocaj">
                Magnetically-driven quantum phase transitions in a low-dimensional pyrazine-bridged Cu<sup>2+</sup> chain magnet
            </dccLink>
            <div>
                Inorganic Chemistry, (Submitted) January 1, 2025
            </div>
            
            
            <dccLink href="https://pubs.aip.org/aip/apl/article-abstract/122/18/182902/2887973/Spin-phonon-interactions-and-magnetoelectric?redirectedFrom=PDF">
                Spin-phonon interactions and magnetoelectric coupling in Co<sub>4</sub>B<sub>2</sub>O<sub>9</sub> (B = Nb, Ta)
            </dccLink>
            <div>
                Applied Physics Letters, May 2, 2023
            </div>
            
            <dccLink href="https://www.nature.com/articles/s41535-022-00438-6">
                Nonreciprocal directional dichroism at telecom wavelengths
            </dccLink>
            <div>
                npj Quantum Materials, April 4, 2022
            </div>
            
            
            <dccLink href="https://www.nature.com/articles/s41535-022-00436-8">
                Vibrational fingerprints of ferroelectric HfO<sub>2</sub>
            </dccLink>
            <div>
                npj Quantum Materials, March 18, 2022
            </div>
            
            
            <dccLink href="https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.195143">
                Band-Mott mixing hybridizes the gap in Fe<sub>2</sub>Mo<sub>3</sub>O<sub>8</sub>
            </dccLink>
            <div>
                Physical Review B, November 22, 2021
            </div>
            
            
            <dccLink href="https://pubs.rsc.org/en/content/articlelanding/2019/na/c8na00093j">
                Jolly green MOF: confinement and photoactivation of photosystem I in the metal-organic framework ZIF-8
            </dccLink>
            <div>
                Nanoscale Advances, October 11, 2018
            </div>
            
            
            <dccLink href="https://pubs.rsc.org/en/content/articlelanding/2017/cy/c7cy00073a">
                A facile and surfactant-free route for nanomanufacturing of tailored ternary nanoalloys as superior oxygen reduction reaction electrocatalysts
            </dccLink>
            <div>
                Catalysis Science & Technology, April 6, 2017
            </div>
            
            
            
                """
            ],
            dangerously_allow_html=True,
        ),
    
    
    
], className = 'ta')



'''
dcc.Link(dcc.Markdown('Magnetically-driven quantum phase transitions in a low-dimensional pyrazine-bridged Cu<sup>2+</sup> chain magnet'),
         href='https://pubs.acs.org/journal/inocaj'),
html.Div('Inorganic Chemistry, (Submitted) January 1, 2025'),
dcc.Link(dcc.Markdown('Spin-phonon interactions and magnetoelectric coupling in Co<sub>4</sub>B<sub>2</sub>O<sub>9</sub> (B = Nb, Ta)'),
         href='https://pubs.aip.org/aip/apl/article-abstract/122/18/182902/2887973/Spin-phonon-interactions-and-magnetoelectric?redirectedFrom=PDF', 
         className = 'ta'),
html.Div('Applied Physics Letters, May 2, 2023'),
dcc.Link('Nonreciprocal directional dichroism at telecom wavelengths',
          href='https://www.nature.com/articles/s41535-022-00438-6'),
html.Div('npj Quantum Materials, April 4, 2022'),
dcc.Link(dcc.Markdown('Vibrational fingerprints of ferroelectric HfO<sub>2</sub>'),
          href='https://www.nature.com/articles/s41535-022-00436-8'),
html.Div('npj Quantum Materials, March 18, 2022'),
dcc.Link(dcc.Markdown('Band-Mott mixing hybridizes the gap in Fe<sub>2</sub>Mo<sub>3</sub>O<sub>8</sub>'), 
          href='https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.195143'),
html.Div('Physical Review B, November 22, 2021'),
dcc.Link('Jolly green MOF: confinement and photoactivation of photosystem I in the metal-organic framework ZIF-8',
          href='https://pubs.rsc.org/en/content/articlelanding/2019/na/c8na00093j'),
html.Div('Nanoscale Advances, October 11, 2018'),
dcc.Link('A facile and surfactant-free route for nanomanufacturing of tailored ternary nanoalloys as superior oxygen reduction reaction electrocatalysts',
          href='https://pubs.rsc.org/en/content/articlelanding/2017/cy/c7cy00073a'),
html.Div('Catalysis Science & Technology, April 6, 2017'),
'''

