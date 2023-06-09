#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

import distinctipy
import numpy as np

## !!! Data section - Set these for your data
num_curves = 3
# !!! Legend and axis labels
filename = 'figure'
legends  = ['one', 'two', 'three']
xlabel   = 'x-axis'
ylabel   = 'y-axis'
title    = r'Title - $(\alpha, \beta, \gamma)$'

# !!! Dummy data - replace with your x and y data, paired
range_one   = range_two = range_three = np.arange(10)
curve_one   = np.linspace(0, 10, num=10)
curve_two   = np.sqrt(curve_one)
curve_three = 3 * np.log(1 + curve_one) 

## Config section
fontsize = 22
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['backend'] = 'pdf'
plt.rcParams['font.size'] = fontsize
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = plt.rcParams['axes.facecolor']
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['xtick.labelsize'] = fontsize - 1
plt.rcParams['ytick.color'] = plt.rcParams['xtick.color']
plt.rcParams['ytick.labelsize'] = fontsize - 1
plt.rcParams.update({
    'font.family': 'lmodern',
    'text.usetex': True 
    })
linewidth = 3.5
colors    = distinctipy.get_colors(num_curves, colorblind_type='Tritanopia', 
                                   rng=1)

# !!! Extend this beyond eight if needed (more than 8 curves)
# See https://matplotlib.org/stable/api/markers_api.html 
markers    = ['o', 's', '<', 'p', '>', '*', 'v', '^']
markersize = 9

## Plot section
fig = plt.figure(figsize=(11, 10))
# !!! Change linestyles of each curve manually if desired
# See https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

# First curve
plt.plot(range_one, curve_one,
         linewidth=linewidth, color=colors[0], linestyle='solid',
         marker=markers[0], label=legends[0], markersize=markersize)

# Second curve
plt.plot(range_two, curve_two,
         linewidth=linewidth, color=colors[1], linestyle='solid',
         marker=markers[1], label=legends[1], markersize=markersize)

# Third curve
plt.plot(range_three, curve_three,
         linewidth=linewidth, color=colors[2], linestyle='solid',
         marker=markers[2], label=legends[2], markersize=markersize)

# !!! Add more curves if required
# And increment color, marker and legend index accordingly

## Wrap-up plot
plt.grid(visible=True)
plt.xlabel(xlabel, fontsize=fontsize-2)
plt.ylabel(ylabel, fontsize=fontsize-2)
plt.xticks(fontsize=fontsize-1)
plt.yticks(fontsize=fontsize-1)
plt.title(title, fontsize=fontsize-1)

plt.legend(loc='best', fontsize=fontsize-2)
plt.tight_layout()
# Save both as png and pdf
plt.savefig(filename + '.png', bbox_inches='tight', pad_inches=0.01, dpi=300)
plt.savefig(filename + '.pdf', bbox_inches='tight', pad_inches=0.01)
plt.close()
