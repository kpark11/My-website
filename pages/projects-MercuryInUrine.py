# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:20:08 2023

@author: brian
"""
import xport.v56
import pandas as pd

with open(r'C:\Users\brian\Downloads\P_UHG.xpt', 'rb') as f:
    library = xport.v56.load(f)


df = pd.read_html(r'C:\Users\brian\Downloads\P_UHG.xpt',flavor='html5lib')