# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:20:08 2023

@author: brian
"""
import pandas as pd

'''
Mercury: Inorganic - Urine

SEQN - Respondent sequence number
WTSAPRP - Subsample A Weights Pre-Pandemic
URXUHG - Urine Mercury (ug/L)
URDUHGLC - Mercury, Urine Comment Code

For more description: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_UHG.htm
'''
mercury = pd.read_sas(r'C:\Users\brian\Downloads\P_UHG.xpt', format='xport', encoding='utf-8')

'''
Iodine - Urine

SEQN - Respondent sequence number
WTSAPRP - Subsample A Weights Pre-Pandemic
URXUIO - Iodine, urine (ug/L)
URDUIOLC - Iodine, urine comment code

For more description: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_UIO.htm
'''
iodine = pd.read_sas(r'C:\Users\brian\Downloads\P_UIO.xpt', format='xport', encoding='utf-8')

'''
Metals - Urine

SEQN - Respondent sequence number
WTSAPRP - Subsample A Weights Pre-Pandemic
URXUBA - Barium, urine (ug/L)
URDUBALC - Urinary Barium Comment Code
URXUCD - Cadmium, urine (ug/L)
URDUCDLC - Urinary Cadmium Comment Code
URXUCO - Cobalt, urine (ug/L)
URDUCOLC - Urinary Cobalt Comment Code
URXUCS - Cesium, urine (ug/L)
URDUCSLC - Urinary Cesium Comment Code
URXUMO - Molybdenum, urine (ug/L)
URDUMOLC - Urinary Molybdenum Comment Code
URXUMN - Manganese, urine (ug/L)
URDUMNLC - Urinary Mn Comment Code
URXUPB - Lead, urine (ug/L)
URDUPBLC - Urinary Lead Comment Code
URXUSB - Antimony, urine (ug/L)
URDUSBLC - Urinary Antimony Comment Code
URXUSN - Tin, urine (ug/L)
URDUSNLC - USN Comment Code
URXUTL - Thallium, urine (ug/L)
URDUTLLC - Urinary Thallium Comment Code
URXUTU - Tungsten, urine (ug/L)
URDUTULC - Urinary Tungsten Comment Code

For more description: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_UM.htm
'''
metals = pd.read_sas(r'C:\Users\brian\Downloads\P_UM.xpt', format='xport', encoding='utf-8')

'''
Nickel - Urine

SEQN - Respondent sequence number
WTSAPRP - Subsample A Weights Pre-Pandemic
URXUNI - Nickel, Urine (ug/L)
URDUNILC - Nickel, Urine Comment Code

For more description: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_UNI.htm
'''
nickel = pd.read_sas(r'C:\Users\brian\Downloads\P_UNI.xpt', format='xport', encoding='utf-8')

'''
Perchlorate, Nitrate & Thiocyanate - Urine

SEQN - Respondent sequence number
WTSAPRP - Subsample A Weights Pre-Pandemic
URXUP8 - Perchlorate, urine (ng/mL)
URDUP8LC - Perchlorate, urine Comment Code
URXNO3 - Nitrate, urine (ng/mL)
URDNO3LC - Nitrate, urine Comment Code
URXSCN - Thiocyanate, urine (ng/mL)
URDSCNLC - Thiocyanate, urine Comment Code

For more description: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_PERNT.htm
'''
perchlorate = pd.read_sas(r'C:\Users\brian\Downloads\P_PERNT.xpt', format='xport', encoding='utf-8')

df = pd.concat([iodine,mercury,metals,nickel,perchlorate],axis=1)




