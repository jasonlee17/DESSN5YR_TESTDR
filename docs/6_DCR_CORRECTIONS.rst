###################
6 - DCR Corrections
###################

Overview
========

We release the photometrical corrections applied to our SNe and transients in generaal.

For the SHAPE effect, it takes the flux ratio values in the look up table to the SHAPE magnitude corrections. For the COORD effect, it takes the altitude shifts vs. g-i values to the COORD magnitude corrections.

Data Format
===========

Coordinate table
----------------

This is a 

Chains
======

The chain folder includes all the *cosmosis/emcee* chains (see file header) for the four cosmological models tested in our analysis:

- Flat :math:`\Lambda\rm{CDM}` (``flcdm`` sub-folder)
- :math:`\Lambda\rm{CDM}` (``lcdm`` sub-folder)
- Flat :math:`w\rm{CDM}`(``wlcdm`` sub-folder)
- Flat :math:`w_0 w_a \rm{CDM}` (``w0wacdm`` sub-folder)
  
And for the different probes combination

- DES-SN only
- DES-SN + CMB (from Planck Collaboration et al. 2020)
- DES-SN + BAO and 3x2pt
- DES-SN + BAO and 3x2pt + CMB

...........

.. include:: _static/links.rst

