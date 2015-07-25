# -*- coding: utf-8 -*-
"""
Created on July 2015

@author: rossi

A sieve simulation program.
"""

from scipy import *

import matplotlib.pyplot as plt

from sieve_experiment import *

class sieve_plots(sieve_experiment):
    def __init__(self,m=110,n=10,iterations=300,size = (600,500)):
        
        sieve_experiment.__init__(self,m,n,iterations)
 
    def PlotSieve(self):
        plt.figure(figsize=(18,9), dpi=80)
        plt.rc('xtick', labelsize=24)
        plt.rc('ytick', labelsize=24)
    
        plt.subplot(121)
        plt.plot(self.sims,self.simphi,'o')
        plt.plot(self.s,self.phi,'k',linewidth=2)
        plt.legend(('Simulation','Analytic'),fontsize=24)
        plt.xlabel('time (t)',fontsize=24)
        plt.title(r'$\phi$',fontsize=24)
        plt.subplot(122)
        plt.plot(self.sims,self.simp,'o')
        plt.xlabel('time (t)',fontsize=24)
        plt.plot(self.s,self.p,'k',linewidth=2)
        plt.title('Probability',fontsize=24)        
        
