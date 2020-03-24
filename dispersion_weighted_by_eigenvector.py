#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:44:22 2020

@author: shanyang
"""

import yaml
import numpy as np
import matplotlib.pyplot as plt

Thz_meV = 4.136
atom =[0,1]

with open('/Users/shanyang/Desktop/VO2_temperature/VO2_R/425K/MD-4/band.yaml') as file:
    try:
        data=yaml.safe_load(file)
    except yaml.error as error:
        print(error)

phonon = data['phonon']
position=[item['q-position'] for item in phonon]
distance=[item['distance'] for item in phonon]
band =[item['band'] for item in phonon]
band_at_position=[item for item in band]

fig, axis = plt.subplots()
for  point,band_at_position  in  zip(range(len(distance)),band):
    for freq in band_at_position:
#        axis.errorbar(point,freq['frequency'][0:2],freq['eigenvector'][0:2])
#        print(freq['frequency'])
#        print(freq['eigenvector'][0])
        for index in atom:
            eigenvector = [freq['eigenvector'][index][0][0],freq['eigenvector'][index][1][0],freq['eigenvector'][index][2][0]]
            eigenvector_norm = np.linalg.norm(eigenvector)
            axis.errorbar(point,freq['frequency']*Thz_meV, eigenvector_norm, ecolor ='black')

plt.xticks([0,len(distance)],[r'$\Gamma$', 'X']);
plt.ylabel('Energy (meV)')
plt.xlim([0,len(distance)])
plt.ylim([0,30])
plt.savefig('Eigenvector_weighted_V')

fig, axis = plt.subplots()
for  point,band_at_position  in  zip(range(len(distance)),band):
    for freq in band_at_position:
#        axis.errorbar(point,freq['frequency'][0:2],freq['eigenvector'][0:2])
#        print(freq['frequency'])
#        print(freq['eigenvector'][0])
        for index in atom:
            eigenvector = [freq['eigenvector'][index][0][0]]
            eigenvector_norm = np.linalg.norm(eigenvector)
            axis.errorbar(point,freq['frequency']*Thz_meV, eigenvector_norm, ecolor ='black')

plt.xticks([0,len(distance)],[r'$\Gamma$', 'X']);
plt.ylabel('Energy (meV)')
plt.xlim([0,len(distance)])
plt.ylim([0,30])
plt.savefig('Eigenvector_weighted_V_X')

fig, axis = plt.subplots()
for  point,band_at_position  in  zip(range(len(distance)),band):
    for freq in band_at_position:
#        axis.errorbar(point,freq['frequency'][0:2],freq['eigenvector'][0:2])
#        print(freq['frequency'])
#        print(freq['eigenvector'][0])
        for index in atom:
            eigenvector = [freq['eigenvector'][index][1][0]]
            eigenvector_norm = np.linalg.norm(eigenvector)
            axis.errorbar(point,freq['frequency']*Thz_meV, eigenvector_norm, ecolor ='black')

plt.xticks([0,len(distance)],[r'$\Gamma$', 'X']);
plt.ylabel('Energy (meV)')
plt.xlim([0,len(distance)])
plt.ylim([0,30])
plt.savefig('Eigenvector_weighted_V_Y')

fig, axis = plt.subplots()
for  point,band_at_position  in  zip(range(len(distance)),band):
    for freq in band_at_position:
#        axis.errorbar(point,freq['frequency'][0:2],freq['eigenvector'][0:2])
#        print(freq['frequency'])
#        print(freq['eigenvector'][0])
        for index in atom:
            eigenvector = [freq['eigenvector'][index][2][0]]
            eigenvector_norm = np.linalg.norm(eigenvector)
            axis.errorbar(point,freq['frequency']*Thz_meV, eigenvector_norm, ecolor ='black')

plt.xticks([0,len(distance)],[r'$\Gamma$', 'X']);
plt.ylabel('Energy (meV)')
plt.xlim([0,len(distance)])
plt.ylim([0,30])
plt.savefig('Eigenvector_weighted_V_Z')





