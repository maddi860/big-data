# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 00:38:21 2026

@author: maddi
"""

import sys
import re
for line in sys.stdin:
    line = line.lower()
    line = re.sub(r'[^a-z\s]', '', line)
    for word in line.split():
        print(f'{word}\t1')