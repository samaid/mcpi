from init import RUN_VERSION

if RUN_VERSION == "numpy".casefold():
    import numpy as np
elif RUN_VERSION == "dpnp".casefold():
    import dpnp as np
elif RUN_VERSION == "numba".casefold():
    from numba import njit, prange
elif RUN_VERSION == "numba-dpex".casefold():
    from numba_dpex import dpjit as njit
    from numba_dpex import prange

if RUN_VERSION == "numba" or RUN_VERSION == "numba-dpex":
    @njit(parallel=True)
    def monte_carlo_pi_batch(batch_size):
        x = np.random.random(batch_size)
        y = np.random.random(batch_size)
        acc = 0
        for i in prange(batch_size):
            if x[i] * x[i] + y[i] * y[i] <= 1.0:
                acc += 1
        return 4.0 * acc / batch_size
else:
    def monte_carlo_pi_batch(batch_size):
        x = np.random.random(batch_size)
        y = np.random.random(batch_size)
        # acc = np.count_nonzero(x * x + y * y <= np.asarray(1.0))  # Preferred alternative to where
        acc = np.where(x * x + y * y <= 1.0, 1, 0).sum()
        return 4.0 * acc / batch_size


def monte_carlo_pi(batch_size, n_batches):
    s = 0.0
    for i in range(n_batches):
        print(f"Batch #{i}")
        s += monte_carlo_pi_batch(batch_size)
    return s/n_batches
