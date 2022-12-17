# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:08:41 2022

@author: wmy
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits.mplot3d
import matplotlib.lines as mlines
import os
from PIL import Image
from cube import Cube
from sphere import Sphere

def draw2d(cube, sphere=None, savepath=None):
    x = cube.p2d_array[:, 0]
    y = cube.p2d_array[:, 1]
    p1, p2, p3, p4, p5, p6, p7, p8 = zip(x, y)
    args = cube.p_array[:, 0].argsort()
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
    if sphere != None:
        circle = plt.Circle(sphere.pcenter2d, sphere.r2d, color='gray', fill=False)
        ax.add_artist(circle)
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

def generate_cubes_spheres_49(cubelength=1, cubewidth=1, cubeheight=1, cubecenter=(5, 0, 0), \
                              spherer=0.5, spherecenter=(5, 0, 0), \
                              savedir="./outputs", imgsize=(576, 576), interval=(100, 100)):
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
    sphere = Sphere(spherer, spherecenter)
    i = 0
    j = 0
    for drotatez in drotatez_list:
        for drotatey in drotatey_list:
            cube = Cube(cubelength, cubewidth, cubeheight, cubecenter, \
                        drotatex=0, drotatey=drotatey, drotatez=drotatez)
            savepath = savedir + "/" + "o_" + str(drotatez) + "_c_" + str(drotatey) + ".png"
            draw2d(cube, sphere, savepath=savepath)
            img = Image.open(savepath)
            combined_image.paste(img, (i*img_w+(i+1)*itv_w, j*img_h+(j+1)*itv_h, (i+1)*img_w+(i+1)*itv_w, (j+1)*img_h+(j+1)*itv_h))
            j += 1
            pass
        j = 0
        i += 1
        pass
    combined_image.save(savedir + "/" + "cs47_{}_{}_{}.png".format(cubelength, cubewidth, cubeheight), quality=95)
    pass

generate_cubes_spheres_49(cubelength=1, cubewidth=1, cubeheight=1, cubecenter=(5, 0, 0), \
                          spherer=0.5, spherecenter=(5, 0, 0))
