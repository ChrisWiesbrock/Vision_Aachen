# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:15:04 2016

@author: Chris
"""

import cv2
import numpy as np
import matplotlib.pylab as plt
import glob

#change path to your image directory
PATH='C:\Users\Chris\Desktop\Teststimuli\low'

filelist = glob.glob(PATH+'/*.tif')

for i in range(len(filelist)):
    
    grey=np.zeros((1,128))

    img = cv2.imread(filelist[i])
    print(filelist[i])
    img = img.astype(float)

    for i in range(len(img)):
        grey[:,i] = np.sum(img[:,i])

    plt.figure()
    plt.imshow(img,'gray')
    plt.figure()
    grey = grey/np.max(grey)
    grey = np.reshape(grey,(128,1))
    grey = grey
    a = np.linspace(0, 127, num=128)
    b = np.linspace(0.5, 0.5, num=128)
    plt.plot(a, grey,'r-')
    plt.plot(a, b, 'k--')
    plt.ylim(0, 1)
    plt.ylabel('luminescence')
    plt.figure()
    hist, edges = np.histogram(grey)
    plt.plot(edges[:-1], hist)
    plt.ylabel('Amount')
    plt.xlabel('luminescence')
    
    print(np.mean(grey))

