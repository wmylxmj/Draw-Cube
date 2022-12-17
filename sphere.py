# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:19:21 2022

@author: wmy
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits.mplot3d
import matplotlib.lines as mlines
import os
from PIL import Image

class Sphere(object):
    
    def __init__(self, r, center=(0, 0, 0)):
        self.r = r
        self.center = center
        self.cast2d()
        pass
    
    def cast2d(self, c=1):
        self.r2d = c*self.r/self.center[0]
        self.pcenter2d = (-1*c*self.center[1]/self.center[0], c*self.center[2]/self.center[0])
        pass
    
    def draw2d(self, savepath=None):
        plt.Circle(self.pcenter2d, self.r2d, fill=False)
        if savepath != None:
            plt.savefig(savepath)
            pass
        plt.show()
        pass
    
    pass

