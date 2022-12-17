# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:15:00 2021

@author: wmy
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits.mplot3d
import matplotlib.lines as mlines
import os
from PIL import Image

class Cube(object):
    
    def __init__(self, length, width, height, center=(0, 0, 0), drotatex=0, drotatey=0, drotatez=0):
        self.length = length
        self.width = width
        self.height = height
        self.center = center
        self.drotatex = drotatex
        self.drotatey = drotatey
        self.drotatez = drotatez
        self.rotatex = self.drotatex / 180 * 3.1415926
        self.rotatey = self.drotatey / 180 * 3.1415926
        self.rotatez = self.drotatez / 180 * 3.1415926
        self.calpoint()
        self.cast2d()
        pass
    
    def atan(self, y, x):
        angle = math.atan(y/x)
        if y < 0  and x < 0:
            angle += 3.1415926
            pass
        elif y > 0  and x < 0:
            angle += 3.1415926
            pass
        return angle
    
    def calpoint(self):
        # raw point
        self.p1 = [0+self.width/2, 0+self.length/2, 0+self.height/2]
        self.p2 = [0-self.width/2, 0+self.length/2, 0+self.height/2]
        self.p3 = [0-self.width/2, 0-self.length/2, 0+self.height/2]
        self.p4 = [0+self.width/2, 0-self.length/2, 0+self.height/2]
        self.p5 = [0+self.width/2, 0+self.length/2, 0-self.height/2]
        self.p6 = [0-self.width/2, 0+self.length/2, 0-self.height/2]
        self.p7 = [0-self.width/2, 0-self.length/2, 0-self.height/2]
        self.p8 = [0+self.width/2, 0-self.length/2, 0-self.height/2]
        
        # rotate z object angle
        angle = self.atan(self.p1[1], self.p1[0]) + self.rotatez
        distance = (self.p1[0]**2 + self.p1[1]**2) ** 0.5
        self.p1 = [distance*math.cos(angle), distance*math.sin(angle), self.p1[2]]
        
        angle = self.atan(self.p2[1], self.p2[0]) + self.rotatez
        distance = (self.p2[0]**2 + self.p2[1]**2) ** 0.5
        self.p2 = [distance*math.cos(angle), distance*math.sin(angle), self.p2[2]]
        
        angle = self.atan(self.p3[1], self.p3[0]) + self.rotatez
        distance = (self.p3[0]**2 + self.p3[1]**2) ** 0.5
        self.p3 = [distance*math.cos(angle), distance*math.sin(angle), self.p3[2]]
        
        angle = self.atan(self.p4[1], self.p4[0]) + self.rotatez
        distance = (self.p4[0]**2 + self.p4[1]**2) ** 0.5
        self.p4 = [distance*math.cos(angle), distance*math.sin(angle), self.p4[2]]
        
        angle = self.atan(self.p5[1], self.p5[0]) + self.rotatez
        distance = (self.p5[0]**2 + self.p5[1]**2) ** 0.5
        self.p5 = [distance*math.cos(angle), distance*math.sin(angle), self.p5[2]]
        
        angle = self.atan(self.p6[1], self.p6[0]) + self.rotatez
        distance = (self.p6[0]**2 + self.p6[1]**2) ** 0.5
        self.p6 = [distance*math.cos(angle), distance*math.sin(angle), self.p6[2]]
        
        angle = self.atan(self.p7[1], self.p7[0]) + self.rotatez
        distance = (self.p7[0]**2 + self.p7[1]**2) ** 0.5
        self.p7 = [distance*math.cos(angle), distance*math.sin(angle), self.p7[2]]
        
        angle = self.atan(self.p8[1], self.p8[0]) + self.rotatez
        distance = (self.p8[0]**2 + self.p8[1]**2) ** 0.5
        self.p8 = [distance*math.cos(angle), distance*math.sin(angle), self.p8[2]]
        
        # rotate y camera angle
        angle = self.atan(self.p1[2], self.p1[0]) + self.rotatey
        distance = (self.p1[0]**2 + self.p1[2]**2) ** 0.5
        self.p1 = [distance*math.cos(angle), self.p1[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p2[2], self.p2[0]) + self.rotatey
        distance = (self.p2[0]**2 + self.p2[2]**2) ** 0.5
        self.p2 = [distance*math.cos(angle), self.p2[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p3[2], self.p3[0]) + self.rotatey
        distance = (self.p3[0]**2 + self.p3[2]**2) ** 0.5
        self.p3 = [distance*math.cos(angle), self.p3[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p4[2], self.p4[0]) + self.rotatey
        distance = (self.p4[0]**2 + self.p4[2]**2) ** 0.5
        self.p4 = [distance*math.cos(angle), self.p4[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p5[2], self.p5[0]) + self.rotatey
        distance = (self.p5[0]**2 + self.p5[2]**2) ** 0.5
        self.p5 = [distance*math.cos(angle), self.p5[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p6[2], self.p6[0]) + self.rotatey
        distance = (self.p6[0]**2 + self.p6[2]**2) ** 0.5
        self.p6 = [distance*math.cos(angle), self.p6[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p7[2], self.p7[0]) + self.rotatey
        distance = (self.p7[0]**2 + self.p7[2]**2) ** 0.5
        self.p7 = [distance*math.cos(angle), self.p7[1], distance*math.sin(angle)]
        
        angle = self.atan(self.p8[2], self.p8[0]) + self.rotatey
        distance = (self.p8[0]**2 + self.p8[2]**2) ** 0.5
        self.p8 = [distance*math.cos(angle), self.p8[1], distance*math.sin(angle)]
        
        # rotate x
        angle = self.atan(self.p1[2], self.p1[1]) + self.rotatex
        distance = (self.p1[1]**2 + self.p1[2]**2) ** 0.5
        self.p1 = [self.p1[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p2[2], self.p2[1]) + self.rotatex
        distance = (self.p2[1]**2 + self.p2[2]**2) ** 0.5
        self.p2 = [self.p2[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p3[2], self.p3[1]) + self.rotatex
        distance = (self.p3[1]**2 + self.p3[2]**2) ** 0.5
        self.p3 = [self.p3[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p4[2], self.p4[1]) + self.rotatex
        distance = (self.p4[1]**2 + self.p4[2]**2) ** 0.5
        self.p4 = [self.p4[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p5[2], self.p5[1]) + self.rotatex
        distance = (self.p5[1]**2 + self.p5[2]**2) ** 0.5
        self.p5 = [self.p5[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p6[2], self.p6[1]) + self.rotatex
        distance = (self.p6[1]**2 + self.p6[2]**2) ** 0.5
        self.p6 = [self.p6[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p7[2], self.p7[1]) + self.rotatex
        distance = (self.p7[1]**2 + self.p7[2]**2) ** 0.5
        self.p7 = [self.p7[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        angle = self.atan(self.p8[2], self.p8[1]) + self.rotatex
        distance = (self.p8[1]**2 + self.p8[2]**2) ** 0.5
        self.p8 = [self.p8[0], distance*math.cos(angle), distance*math.sin(angle)]
        
        # move to the center
        self.p1 = [self.center[0]+self.p1[0], self.center[1]+self.p1[1], self.center[2]+self.p1[2]]
        self.p2 = [self.center[0]+self.p2[0], self.center[1]+self.p2[1], self.center[2]+self.p2[2]]
        self.p3 = [self.center[0]+self.p3[0], self.center[1]+self.p3[1], self.center[2]+self.p3[2]]
        self.p4 = [self.center[0]+self.p4[0], self.center[1]+self.p4[1], self.center[2]+self.p4[2]]
        self.p5 = [self.center[0]+self.p5[0], self.center[1]+self.p5[1], self.center[2]+self.p5[2]]
        self.p6 = [self.center[0]+self.p6[0], self.center[1]+self.p6[1], self.center[2]+self.p6[2]]
        self.p7 = [self.center[0]+self.p7[0], self.center[1]+self.p7[1], self.center[2]+self.p7[2]]
        self.p8 = [self.center[0]+self.p8[0], self.center[1]+self.p8[1], self.center[2]+self.p8[2]]
        
        # array
        self.p_array = np.array([self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8])
        pass
    
    def draw3d(self, savepath=None):
        x = self.p_array[:, 0]
        y = self.p_array[:, 1]
        z = self.p_array[:, 2]
        p1, p2, p3, p4, p5, p6, p7, p8 = zip(x, y, z)
        args = self.p_array[:, 0].argsort()
        pcs = []
        for i in range(4):
            pc = [p1, p2, p3, p4, p5, p6, p7, p8][args[i]]
            pcs.append(pc)
            pass
        lines = [(p1, p2), (p2, p3), (p3, p4), \
                 (p4, p1), (p1, p5), (p5, p6), \
                 (p6, p7), (p7, p8), (p8, p5), \
                 (p6, p2), (p4, p8), (p3, p7)]
        fig = plt.figure(figsize=(8, 8))
        ax = fig.gca(projection='3d')
        for line in lines:
            if line[0] in pcs and line[1] in pcs:
                l = zip(line[0], line[1])
                ax.plot(*l, c='k', marker='o', mfc='r', mec='g', ms=10)
                pass
            else:
                l = zip(line[0], line[1])
                ax.plot(*l, ls=':', c='gray', marker='o', mfc='r', mec='g', ms=10)
                pass
            pass
        size = max(self.width, self.length, self.height)
        ax.set(xlabel='X', ylabel='Y', zlabel='Z', \
               xlim=(self.center[0]-size, self.center[0]+size),
               ylim=(self.center[1]-size, self.center[1]+size),
               zlim=(self.center[2]-size, self.center[2]+size))
        ax.view_init(elev=20, azim=180)
        if savepath != None:
            plt.savefig(savepath)
            pass
        plt.show()
        pass
    
    def cast2d(self, c=1):
        self.p12d = [-1*c*self.p1[1]/self.p1[0], c*self.p1[2]/self.p1[0]]
        self.p22d = [-1*c*self.p2[1]/self.p2[0], c*self.p2[2]/self.p2[0]]
        self.p32d = [-1*c*self.p3[1]/self.p3[0], c*self.p3[2]/self.p3[0]]
        self.p42d = [-1*c*self.p4[1]/self.p4[0], c*self.p4[2]/self.p4[0]]
        self.p52d = [-1*c*self.p5[1]/self.p5[0], c*self.p5[2]/self.p5[0]]
        self.p62d = [-1*c*self.p6[1]/self.p6[0], c*self.p6[2]/self.p6[0]]
        self.p72d = [-1*c*self.p7[1]/self.p7[0], c*self.p7[2]/self.p7[0]]
        self.p82d = [-1*c*self.p8[1]/self.p8[0], c*self.p8[2]/self.p8[0]]
        self.p2d_array = np.array([self.p12d, self.p22d, self.p32d, self.p42d, self.p52d, self.p62d, self.p72d, self.p82d])
        pass
    
    def draw2d(self, savepath=None):
        x = self.p2d_array[:, 0]
        y = self.p2d_array[:, 1]
        p1, p2, p3, p4, p5, p6, p7, p8 = zip(x, y)
        args = self.p_array[:, 0].argsort()
        pcs = []
        for i in range(4):
            pc = [p1, p2, p3, p4, p5, p6, p7, p8][args[i]]
            pcs.append(pc)
            pass
        lines = [(p1, p2), (p2, p3), (p3, p4), \
                 (p4, p1), (p1, p5), (p5, p6), \
                 (p6, p7), (p7, p8), (p8, p5), \
                 (p6, p2), (p4, p8), (p3, p7)]
        fig = plt.figure(figsize=(8, 8))
        ax = fig.gca()
        for line in lines:
            if line[0] in pcs and line[1] in pcs:
                l = zip(line[0], line[1])
                ax.plot(*l, c='k', marker='o', mfc='r', mec='g', ms=10)
                pass
            else:
                l = zip(line[0], line[1])
                ax.plot(*l, ls=':', c='gray', marker='o', mfc='r', mec='g', ms=10)
                pass
            pass
        xlim_max = np.squeeze(np.max(x))
        xlim_min = np.squeeze(np.min(x))
        ylim_max = np.squeeze(np.max(y))
        ylim_min = np.squeeze(np.min(y))
        lim_min = min(xlim_min, ylim_min)
        lim_max = max(xlim_max, ylim_max)
        ax.set(xlabel='X', ylabel='Y', \
               xlim=(lim_min, lim_max),
               ylim=(lim_min, lim_max))
        if savepath != None:
            plt.savefig(savepath)
            pass
        plt.show()
    
    pass


def generate_cubes_49(length=1, width=1, height=1, distance=5, savedir="./outputs", imgsize=(576, 576), interval=(100, 100)):
    img_w = imgsize[0]
    img_h = imgsize[1]
    itv_w = interval[0]
    itv_h = interval[1]
    if not os.path.exists(savedir): 
        os.makedirs(savedir)
        pass
    drotatez_list = [-67.5, -45, -22.5, 0, 22.5, 45, 67.5]
    drotatey_list = [-67.5, -45, -22.5, 0, 22.5, 45, 67.5]
    combined_image = Image.new('RGB', (itv_w*8+img_w*7, itv_h*8+img_h*7), "#FFFFFF")
    i = 0
    j = 0
    for drotatez in drotatez_list:
        for drotatey in drotatey_list:
            c = Cube(length, width, height, center=(distance, 0, 0), \
                     drotatex=0, drotatey=drotatey, drotatez=drotatez)
            savepath = savedir + "/" + "o_" + str(drotatez) + "_c_" + str(drotatey) + ".png"
            c.draw2d(savepath=savepath)
            img = Image.open(savepath)
            combined_image.paste(img, (i*img_w+(i+1)*itv_w, j*img_h+(j+1)*itv_h, (i+1)*img_w+(i+1)*itv_w, (j+1)*img_h+(j+1)*itv_h))
            j += 1
            pass
        j = 0
        i += 1
        pass
    combined_image.save(savedir + "/" + "c47_{}_{}_{}_d_{}.png".format(length, width, height, distance), quality=95)
    pass

generate_cubes_49(2, 1, 1, 8)

