# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# Required libraries
# pip install mne-bids coloredlogs tqdm pandas scikit-learn json_tricks fire

# set up environment
#import mne-study-template
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == LOAD DATA ==
fname = config['epo']
epochs = mne.read_epochs(fname)


# == GET CONFIG VALUES ==

#bands = config['bands']

bands = [(0, 4, 'Delta'), (4, 8, 'Theta'), (8, 12, 'Alpha'),
         (12, 30, 'Beta'), (30, 45, 'Gamma')]

tmin=None
tmax=None
proj=None

fig_grad = epochs.plot_psd_topomap(bands=bands, tmin=tmin, tmax=tmax, proj=proj, 
            bandwidth=None, adaptive=False, low_bias=True, normalization='length', 
            ch_type='grad', cmap=None, agg_fun=None, dB=True, n_jobs=1, 
            normalize=False, 
            cbar_fmt='auto', outlines='head', axes=None, 
            show=True, sphere=None, vlim=(None, None), verbose=None)
plt.savefig(os.path.join('out_figs','bands_topomap_grad.png'))


fig_mag = epochs.plot_psd_topomap(bands=bands, tmin=tmin, tmax=tmax, proj=proj, 
            bandwidth=None, adaptive=False, low_bias=True, normalization='length', 
            ch_type='mag', cmap=None, agg_fun=None, dB=True, n_jobs=1, 
            normalize=False, 
            cbar_fmt='auto', outlines='head', axes=None, 
            show=True, sphere=None, vlim=(None, None), verbose=None)

plt.savefig(os.path.join('out_figs','bands_topomap_mag.png'))

# --------------------------------------------------------------------------

