import argparse

BATCH_SIZE = 102400000  # Draw random pairs (x, y) in batches of BATCH_SIZE elements
N_BATCHES = 8  # Total number of batches
N = N_BATCHES * BATCH_SIZE  # Total number of random pairs (x, y)


def int_tuple(tuple_text):
    return tuple(map(int, tuple_text.split(",")))


parser = argparse.ArgumentParser(description="Monte Carlo method for computing Pi")
parser.add_argument(
    "--variant",
    help="Implementation variant",
    type=str.casefold,
    choices=["numpy", "numba", "dpnp", "numba-dpex"],
    default="numpy",
)

parser.add_argument(
    "--task-size",
    help=f"Batch size followed by a total number of batches, e.g. {BATCH_SIZE},{N_BATCHES} (default)",
    type=int_tuple,
    default=int_tuple(f"{BATCH_SIZE},{N_BATCHES}"),
)

args = parser.parse_args()

RUN_VERSION = args.variant
