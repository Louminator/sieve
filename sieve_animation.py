# -*- coding: utf-8 -*-
"""
Created on July 2015

@author: rossi

A sieve simulation program.
"""

from scipy import *
from numpy.random import uniform,permutation

import matplotlib.backends.backend_agg as agg
import pygame
import matplotlib.pyplot as plt

from sieve_experiment import *

class sieve_animate(sieve_experiment):
    def __init__(self,m=110,n=10,iterations=300,size = (600,500)):
        
        sieve_experiment.__init__(self,m,n,iterations)
        
        self.size = size

        pygame.init()
        self.disp = pygame.display.set_mode(self.size)
        self.disp.fill((0,0,0))
        
        self.DrawSieve()
        
    def play(self):
        for its in range(1,self.iterations):
            fig,raw_data,canvas = self.CreatePlot(its)
            
            if (its == 1):
                self.size2 = canvas.get_width_height()
                
            surf = pygame.image.fromstring(raw_data, self.size2, "ARGB")
            if (self.smallPores[its-1] == self.smallPores[its]):
                # Fall into the next large pore.
                q = int(uniform(0,self.m+self.n))
                while (self.arrangement[q] >= self.n):
                    q = int(uniform(0,self.m+self.n))
                self.ParticleFall(q,surf)
            else:
                # Fall into the next small pore.
                idx = argwhere(self.arrangement == self.n+self.smallPores[its])
                idx = idx[0][0]
                self.ParticleStuck(idx,surf)
            plt.close(fig)
        
    def DrawSieve(self):
        self.pos = map(int,self.size[0]/(self.m+self.n+1.)*r_[0:self.m+self.n]+2.5)
        self.arrangement = permutation(self.n+self.m)
        
        pygame.draw.rect(self.disp,(0,255,0),(0,self.size[1]-20,self.size[0],20))
        for k in arange(len(self.pos)):
            if (self.arrangement[k] >= self.n):
                pygame.draw.rect(self.disp,(0,0,0),(self.pos[k],self.size[1]-20,1,20))
            else:
                pygame.draw.rect(self.disp,(0,0,0),(self.pos[k]-1,self.size[1]-20,3,20))
        pygame.display.flip()

    def CreatePlot(self,ind):
        fig = plt.figure(figsize=[self.size[0]/100, (self.size[1]-40)/100], dpi=100)
        ax = fig.gca()
        ax.plot(self.s,self.p,'c')
        ax.plot(self.sims[:ind],self.simp[:ind],'xb')
        plt.xlabel('time (t)',fontsize=12)
        plt.title('Probability',fontsize=12)
        ax.legend(('Theory','Experiment'),numpoints=1)
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_argb()
        return(fig,raw_data,canvas)
    
    def ParticleFall(self,ind,surf):
        for j in range(0,self.size[1],2):
            self.disp.blit(surf, ((self.size[0]-self.size2[0])/2,0))
            x = int((self.pos[ind]+self.size[0]/2.)/2. + (self.size[0]/2.-self.pos[ind])*(cos(pi*j/self.size[1]))/2.)
            pygame.draw.rect(self.disp,(200,0,200),(x,j,3,3))
            pygame.display.flip()
            pygame.draw.rect(self.disp,(0,0,0),(x,j,3,3))
            
    def ParticleStuck(self,ind,surf):
        for j in range(0,self.size[1]-21,2):
            self.disp.blit(surf, ((self.size[0]-self.size2[0])/2,0))
            x = int((self.pos[ind]+self.size[0]/2.)/2. + (self.size[0]/2.-self.pos[ind])*(cos(pi*j/(self.size[1]-21)))/2.)
            pygame.draw.rect(self.disp,(200,0,200),(x,j,3,3))
            pygame.display.flip()
            pygame.draw.rect(self.disp,(0,0,0),(x,j,3,3))
        pygame.draw.rect(self.disp,(255,0,0),(self.pos[ind],self.size[1]-23,2,2))
        pygame.display.flip()
        
