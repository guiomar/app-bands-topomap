# PSD Bands topo-map

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Plots scalp topographies of power spectral density in canonical frequency bands (delta to gamma) from MEG epochs with MNE-Python plot_psd_topomap, for gradiometers and magnetometers.**

Visualisation utility: computes PSD band topomaps from an MNE epochs file with fixed bands (delta 0-4, theta 4-8, alpha 8-12 Hz and higher bands) and saves one PNG for gradiometers and one for magnetometers. Use it for a quick look at the spatial distribution of band power in MEG epochs.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/epochs` |
| 📤 **Outputs** | `generic/image/png` |
| 🐳 **Container** | `brainlife/mne:0.24dev` |
| ⚙️ **Resources** | 8 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.586](https://doi.org/10.25663/brainlife.app.586) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `epochs01` | `neuro/meeg/mne/epochs` (epochs) | yes | MNE epochs file (-epo.fif) of MEG data. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_figs` | `generic/image/png` | PNG topomaps of band power for gradiometers and magnetometers. |

📚 **References used by this App:**
- Hayashi S, Caron BA, et al., Pestilli F. brainlife.io: A decentralized and open source cloud platform to support neuroscience research. arXiv (2023).
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.586-blue.svg)](https://doi.org/10.25663/brainlife.app.586)

## Documentation
This Brainlife App plots scalp topography of PSD for chosen frequency bands using MNE-Python `epochs.plot_psd_topomap` function.

## Authors
- [Guiomar Niso](guiomar.niso@ctb.upm.es), Instituto Cajal, CSIC, Spain

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this app. 

1. **brainlife. io: A decentralized and open source cloud platform to support neuroscience research**. Hayashi, S., Caron, B. A., et al. & Pestilli, F. (2023). ArXiv. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10274934/

2. **MEG and EEG data analysis with MNE-Python**. Gramfort A, et al. & Hämäläinen MS. (2013). Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University
