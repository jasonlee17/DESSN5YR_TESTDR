########################################
Dark Energy Survey Supernova Program 5YR
########################################

Data Release Package documentation
==================================

The SN program consisted on 5 years of observations using the Dark Energy Survey instrument, finding Type Ia Supernovae up to cosmological redshifts :math:`z>1.1`.

This public data release encompases the full set of light-curve measurements obtained, as well as any ancillary data products needed to constrain the cosmological expansion rate model parameters. 

.. toctree::
   :maxdepth: 2

   desSNprogram
   releaseDetails


The 5-year Data release 
-----------------------

This is the full public data release of the Dark Energy Survey Supernova Program, DES-SN5YR, consisting of data products used to compute the cosmological result from the full 5 years of photometrically classified supernovae (SNe) combined with a sample of low-redshift SNe. 

We provide both real and simulated data used in the cosmological analysis, the Machine Learning classification probabilities, the distances obtained for each SN event with the covariance matrix, the CosmoSIS input and obtained chains.
Additionally, we provide the analysis tools used to orchestrate this large analysis stage, this is the Pippin files used.

A separate set of python scripts and tools are also provide to facilitate the use and reproduction of our results.

0- DATA
^^^^^^^

The light-curves are produced using the Scene Modelling Photometry pipeline described in Brout et al. 2019a and Sanchez et al. 2024 (in prep.).
The full set of light-curves will be released with Sanchez et al. 2024 (in prep.).

1- Simulations
^^^^^^^^^^^^^^
This folder includes the 25 DES mocks used for testing and validation of the DES cosmological pipeline. We provide both simulated Ia and non-Ia DES light-curves. See the folder for further details.

2- LCFIT_MODEL
^^^^^^^^^^^^^^

 - :file:`SALT3.DES5YR`: This is the SALT3 model used for the Nominal DES-SN5YR cosmological analysis
 - :file:`SALT3.DES5YR-SYS`: These are the 10 SALT3 models (SALT3.MODEL000 to SALT3.MODEL009) used to incorporate Calibration and LC fitting Systematics in the DES-SN5YR cosmological analysis

3 - CLASSIFICATION
^^^^^^^^^^^^^^^^^^

The file contains classification probabilities for the 1635 DES SNe used in the DES-SN5YR cosmological analysis.
  
  - :file:`PROB_SNNV19`: classification probabilities from SuperNNova algorithm trained on core-collapse tmplt by `Vincenzi et al 2019`_,
  - :file:`PROB_SNNJ17`: classification probabilities from SuperNNova algorithm trained on core-collapse tmplt by `Jones et al 2017`_,
  - :file:`PROB_SNNDESCC`: classification probabilities from SuperNNova algorithm trained on core-collapse tmplt built from DES core-collapse data,
  - :file:`PROB_SCONE`: classification probabilities from SCONE algorithm trained on core-collapse tmplt by `Vincenzi et al 2019`_,
  - :file:`PROB_SNIRF`: classification probabilities from SNIRF algorithm trained on core-collapse tmplt by `Vincenzi et al 2019`_.

4- DISTANCES_COVMAT
^^^^^^^^^^^^^^^^^^^

  - Data vector with redshifts (zHD) and distance modulii (MU) for the 1829 SNe (194 low-z + 1635 DES) used in the DES-SN5YR cosmological analysis.
  - STAT only covariance matrix
  - STAT+SYST covariance matrix
  - Single systematic covariance matrices (see README therein)

7- PIPPIN_FILES
^^^^^^^^^^^^^^^

This folder includes the pippin input files needed to reproduce DES simulations and cosmological analysis.


.. Data products
.. ------------------------------------------

..  - 01-FILTERS
..   - Filter Transmission Functions + Atmosphere [Download 42KB `01-FILTERS.tar.gz`_] 
..     Citation: `Burke et al. 2017 <http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1706.01542>`_
..  - 02-DATA_PHOTOMETRY
..   - 02.1-DIA_LIGHTCURVES
..   - 02.2-SMP_LIGHTCURVES
..  - 03-DATA_SPECTRA
..  - 04-SIM_BIASCOR
..  - 05-CLASSIFICATION
..  - 06-DISTANCES_COVMAT
..  - 07-LCFIT_MODEL


Software tools tutorial
=======================

.. toctree:: 
   :maxdepth: 3

   tutorial/index

Papers from DES-SN5YR
=====================
 

 - The Dark Energy Survey: Cosmology Results With ~1500 New High-redshift Type Ia Supernovae Using The Full 5-year Dataset 
   - `DES Collaboration (2024)`_
 - The Dark Energy Survey 5-year photometrically classified type Ia supernovae without host-galaxy redshifts 
   - `Möller et al (2024)`_
 - The Dark Energy Survey Supernova Program: Cosmological Analysis and Systematic Uncertainties 
   - `Vincenzi et al (2024)`_
 - The Dark Energy Survey Supernova Program: Corrections on Photometry Due to Wavelength-dependent Atmospheric Effects 
   - `Lee & Acevedo et al. (2023)`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. include:: _static/links.rst
