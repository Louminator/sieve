# -*- coding: utf-8 -*-
"""
Created on July 2015

@author: rossi

A sieve simulation program.
"""

from scipy import *

import matplotlib.pyplot as plt

#from sieve_experiment import *

from sieve_plots import *
from sieve_animation import *

p = sieve_plots()
p.PlotSieve()
plt.show()

experiment = sieve_animate()
experiment.play()
