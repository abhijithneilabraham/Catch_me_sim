#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 01:04:48 2020

@author: abhijithneilabraham
"""

import numpy as np
a=np.zeros(
            3, dtype=[('l', np.float32), ('r', np.float32)])
a['r']=100
print(a['r'])
ac=np.clip(a['r'],[1,0])