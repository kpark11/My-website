# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:20:08 2023

@author: brian
"""
import xport.v56

with open('C:\Downloads\P_UHG.xpt', 'rb') as f:
    library = xport.v56.load(f)
    
    