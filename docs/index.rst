========================================
Dark Energy Survey Supernova Program 5YR
========================================

.. topic:: The DES Supernova Program 5-year Data release.
   
   The Dark Energy Survey Supernova Program (DES-SN) consisted on 5 years of observations using the Dark Energy Survey instrument, finding Type Ia Supernovae up to cosmological redshifts :math:`z>1.1`.

   This is the **full public data release** of DES-SN (DES-SN5YR) containing all data products used to compute the cosmological result from the full 5 years of photometrically classified supernovae (SNe) combined with a sample of low-redshift SNe. 


Overview of DES-SN 5-year Data release 
======================================

0 - DATA
  Transient light curves from DES-SN, measured with DIFFIMG and SMP photometry pipelines, and also including SALT3 model fitted curves.

1 - Simulations
  DES mocks used for testing and validation of the DES cosmological pipeline. 

2 - LCFIT_MODEL
  The trained SALT3 SED time-series used in DES-SN5YR cosmological analysis.

3 - CLASSIFICATION
  Classification probabilities for the DES SNe used in the DES-SN5YR cosmological analysis.

4 - DISTANCES_COVMAT
  Distances and Hubble Diagram, global SN sample parameters :math:`\alpha, \beta, \gamma, M_0`, and Statistical and Systematic covariance matrices.

5 - Cosmology
  Likelihood used, and obtained chains from CosmoMC_  and emcee_ 

7 - PIPPIN_FILES
  The PIPPIN_ input files for reproducing the cosmological SNIa analysis. 

Detail description of release Contents
======================================  

.. toctree::
  :maxdepth: 2

  0_DATA
  1_SIMULATIONS
  2_LCFIT_MODEL

.. releaseDetails
.. desSNprogram



DES 5YR Tutorials 
=================

.. toctree:: 
   :maxdepth: 2

   tutorial/01-load_data
   tutorial/02-dessn_fwcdm
   tutorial/03-load_lcplot
   tutorial/04-HubbleDiagram

.. tutorial/index

Used Public cosmology Codes  
===========================
 - PIPPIN_
 - CosmoSIS_
 - MontePython_
 - Cobaya_
 - CosmoMC_ 
 - emcee_ 

Papers from DES-SN5YR
=====================
 

 - `DES Collaboration (2024)`_ - The Dark Energy Survey: Cosmology Results With ~1500 New High-redshift Type Ia Supernovae Using The Full 5-year Dataset 
 - `Möller et al (2024)`_ - The Dark Energy Survey 5-year photometrically classified type Ia supernovae without host-galaxy redshifts 
 - `Vincenzi et al (2024)`_ - The Dark Energy Survey Supernova Program: Cosmological Analysis and Systematic Uncertainties 
 - `Lee & Acevedo et al. (2023)`_ - The Dark Energy Survey Supernova Program: Corrections on Photometry Due to Wavelength-dependent Atmospheric Effects 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. include:: _static/links.rst
