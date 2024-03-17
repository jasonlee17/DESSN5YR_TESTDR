# DES-SN 5YR Data Release

## The Dark Energy Survey Supernova 5YR Cosmological analysis and Data Release

This repo contains the data, simulations, pipeline inputs and results from the Dark Energy Survey Supernova Program 5-Year results.

Please check our [ReadTheDocs](dessnvyrdr.readthedocs.org) for all details on contents and ancillary data description.


## Contents of the Data Release

 - **0_DATA**: The light-curves produced using the Scene Modelling Photometry pipeline descibre in Brout et al. 2019a and Sanchez et al. 2024 (in prep.).

 - **1_SIMULATIONS:** DES Monte Carlo simulation mocks used for testing and validation of the DES cosmological pipeline.

 - **2_LCFIT_MODEL:** The SALT3 model used for the Nominal DES-SN5YR cosmological analysis

 - **3_CLASSIFICATION:** The classification probabilities for the 1635 DES SNe.
  
 - **4_DISTANCES_COVMAT:**
   - Data vector with redshifts (zHD) and distance modulii (MU) for the 1829 SNe (194 low-z + 1635 DES).
   - STAT only covariance matrix
   - STAT+SYST covariance matrix
   - Single systematic covariance matrices 

 - **7_PIPPIN_FILES:** This folder includes the pippin input files needed to reproduce DES simulations and cosmological analysis.


## The DES-SN5YR utility package

We release basic utilities for using this data. To install this package simply clone this github repo and install locally. This is also one way to obtain the full dataset.

```console
$ git clone https://github.com/des-science/DES-SN5YR_DataRelease.git
$ cd DES-SN5YR_DataRelease
$ pip install -e .
```

### Examples of use of this Data Release

We provide some Jupyter Notebooks with examples to load and read this data, and produce some example figures. These are in the ``docs/tutorial`` directory. 

## References and citing this work

> The Dark Energy Survey: Cosmology Results With ~1500 New High-redshift Type Ia Supernovae Using The Full 5-year Dataset. JOURNAL NUMBER. [DES Collaboration (2024).](https://ui.adsabs.harvard.edu/link_gateway/2024arXiv240102929D/doi:10.48550/arXiv.2401.02929)

> The Dark Energy Survey Supernova Program: Cosmological Analysis and Systematic Uncertainties JOURNAL NUMBER. [Vincenzi et al (2024).](https://ui.adsabs.harvard.edu/link_gateway/2024arXiv240102945V/doi:10.48550/arXiv.2401.02945) 

> Light curve and ancillary data release for the full Dark Energy Survey Supernova Program. JOURNAL NUMBER. [Sánchez et al (2024)](...)

