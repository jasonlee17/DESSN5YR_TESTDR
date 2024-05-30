#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utils.py
#
#  Copyright 2022 bruno <bruno.sanchez@duke.edu>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
from copy import copy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


oldParams = copy(plt.rcParams)
#print(oldParams)

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 20}

matplotlib.rc('font', **font)

FLTCOLORS = {}
FLTCOLORS['u'] = '#ac53b9ff'
FLTCOLORS['g'] = '#3995e4ff'
FLTCOLORS['r'] = '#51bc64ff'
FLTCOLORS['i'] = '#2a7f13ff'
FLTCOLORS['z'] = '#ffc627ff'
FLTCOLORS['y'] = '#e43939ff'

FLTLIST = ('g', 'r', 'i', 'z')



def plot_sn_light_curve(df, 
        mjd_col='MJD', flux_col='FLUXCAL', flux_err_col='FLUXCALERR', 
        band_col='BAND', ax=None, CID=None, 
        *args, **kwargs
    ):
    """
    Plots a Supernova light curve from a DataFrame with error bars.

    Parameters:
    - df: pandas DataFrame containing the photometry data
    - mjd_col: str, name of the column for Modified Julian Date (default: 'MJD')
    - flux_col: str, name of the column for Flux (default: 'FLUX')
    - flux_err_col: str, name of the column for Flux Uncertainty (default: 'FLUX_ERR')
    - band_col: str, name of the column for Band (default: 'BAND')
    - CID: int, candidate ID in DES

    Returns:
    - A plot of the light curve with error bars.
    """
    if ax is None:
        fig, ax = plt.subplots(*args, **kwargs)

    # Group the data by the BAND column
    grouped = df.groupby(band_col)

    # Loop through each group (each band) and plot the light curve with error bars
    for band, group in grouped:
        color = FLTCOLORS[band.strip()]
        ax.errorbar(
            group[mjd_col], group[flux_col], 
            yerr=group[flux_err_col], fmt='o', linestyle='', color=color,
            label=f'{band}')
    
    # Set plot labels and title
    ax.set_xlabel('MJD')
    ax.set_ylabel('Flux')
    suffix = ''
    if CID is not None: 
        suffix = "CID: %s"%CID 
    
    ax.set_title('Supernova Light Curve'+suffix)
    plt.legend()
    plt.tight_layout()
    return fig, ax

