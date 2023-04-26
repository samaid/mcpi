# MCPI - Monte Carlo estimation of Pi using numpy, numba, dpnp, numba-dpex

This is a "Hello, World" application in Monte Carlo methods. It stresses random number generation along with some other math required for implementation of the Acceptance-Rejection technique.

## How to run

`python -m mcpi_demo [options]`

Demo can be invoked in several ways:

1. Cloning Github repo and running `python mcpi.py [options]`
2. Cloning Github repo and running `python -m mcpi_demo [options]`
3. Installing conda package and invoking executable
   * `conda install -c pycoddiy/label/dev mcpi-demo`
   * `mcpi [options]`

### Options

The following options are allowed:
* `--variant [numpy, numba, dpnp, numba-dpex]` (default `numpy`): Implementation variant
* `--batch-size`: Number of trial points in the batch
* `--n-batches`:  Number of batches
