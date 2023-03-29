MCPI - Monte Carlo estimation of Pi using numpy, numba, dpnp, numba-dpex
************************************************************************

This is a "Hello, World" application in Monte Carlo methods. It stresses random number generation along with some other math required for implementation of the Acceptance-Rejection technique.

How to run
----------
`python mcpi [options]`

The following options are allowed:
* `--variant [numpy, numba, dpnp, numba-dpex]` (default `numpy`): Implementation variant
* `--task-size` (default 102400000, 8): Batch size followed by a total number of batches
