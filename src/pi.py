from impl import monte_carlo_pi
from init import args

import time


def main():
    batch_size, n_batches = args.task_size
    print(f"Estimating Pi with {args.variant} for {n_batches} batches of size {batch_size}...")
    t1 = time.time()
    pi = monte_carlo_pi(batch_size, n_batches)
    t2 = time.time()
    print("Pi =", pi)
    print("Done in ", t2 - t1, "seconds...")


if __name__ == "__main__":
    main()
