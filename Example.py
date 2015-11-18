#!/usr/bin/env python
# encoding: utf-8
"""agregando a la raiz el path"""
import os, sys
import numpy as np
import scipy,scipy.signal
from math import pi, log
import matplotlib.pyplot as plt

sys.path.append("..")
from Functions import edfread_y as edfr
from Functions import peakdetect_y as pd
from Functions import marker as mk
from Functions import Erp_extraction as erp


"""Adqusition EDF file"""
fname='trial_4img.edf'
hdr,record=edfr.edfread_y(fname)
DC3=scipy.signal.resample(record[19],(len(record[19])/hdr['samples'][19])*hdr['samples'][0])

"""No FILTERING"""
Ce = record[0:19]

"""marker extraction"""
pos_Estim, Etq = mk.marker(DC3)

"""Event Related Potential Extraction"""
Erp_Channels,t_wind = erp.Erp_extraction(hdr,Ce,pos_Estim,Etq)


t = np.linspace(0, t_wind, int(t_wind*hdr['samples'][0]))

for canal in range(19):
    plt.figure(canal+1)
    plt.plot(t, Erp_Channels[canal][0], color='r', label='Estim 1')
    plt.plot(t, Erp_Channels[canal][1], color='g', label='Estim 2') 
    plt.plot(t, Erp_Channels[canal][2], color='b', label='Estim 3')
    plt.plot(t, Erp_Channels[canal][3], color='m', label='Estim 4')
    plt.plot(t, Erp_Channels[canal][4], color='k', label='Estim 5')
    plt.legend()
plt.show()
raw_input()
