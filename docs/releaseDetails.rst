The 5-year Data release 
=======================

This is the full public data release of the Dark Energy Survey Supernova Program, DES-SN5YR, consisting of data products used to compute the cosmological result from the full 5 years of photometrically classified supernovae (SNe) combined with a sample of low-redshift SNe. 

We provide both real and simulated data used in the cosmological analysis, the Machine Learning classification probabilities, the distances obtained for each SN event with the covariance matrix, the CosmoSIS input and obtained chains.
Additionally, we provide the analysis tools used to orchestrate this large analysis stage, this is the Pippin files used.

A separate set of python scripts and tools are also provide to facilitate the use and reproduction of our results.

Data Release file descriptions
------------------------------

.. toctree::
   :maxdepth: 1

   release/0_DATA
   release/1_SIMULATIONS

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
