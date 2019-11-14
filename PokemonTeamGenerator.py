# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pokebase as pb

liepard = pb.pokemon("liepard")

total_stats = 0
for i in liepard.stats:
    total_stats = i.base_stat

print(total_stats)