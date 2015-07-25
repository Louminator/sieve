# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 17:36:38 2014

@author: rossi

A sieve simulation program.
"""

from scipy import *
from scipy.special import lambertw
from numpy.random import uniform

class sieve_experiment():
    
    def __init__(self,m,n,iterations):
        self.n = n
        self.m = m
        self.iterations=iterations
        phi0 = 1.*m/n
        smallPores = [m]
        for i in range(1,iterations):
            if (uniform(0,smallPores[-1] + n) < n):
                smallPores.append(smallPores[-1])
            else:
                smallPores.append(smallPores[-1]-1)
        self.smallPores = array(smallPores)
        self.simphi = double(smallPores)/n

        
        T = 1.0*iterations/n
        simphi = double(smallPores)/n
        self.simp = simphi/(1.+simphi)
        self.sims = r_[0:T:iterations*1.j]
        self.s = r_[0:T:1000j]

        c = log(phi0*exp(phi0))
        self.phi = lambertw(exp(-self.s+c)).real
        self.p = self.phi/(1.+self.phi)
