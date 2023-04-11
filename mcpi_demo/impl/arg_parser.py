import argparse


def int_tuple(tuple_str):
    return tuple(map(int, tuple_str.split(",")))


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Monte Carlo Pi")
    parser.add_argument(
        "--variant",
        help="Implementation variant",
        type=str.casefold,
        choices=["numpy", "numba", "dpnp", "numba-dpex"],
        default="numpy",
    )
    parser.add_argument(
        "--parallel",
        help="Keyword argument parallel= for @njit. Used along with --variant numba. Default --no-parallel",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    parser.add_argument(
        "--gui",
        help="Render the evolution of the grid or do computation only and "
        "print statistics in the end. Default --no-gui",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    batch_size = 102400000
    parser.add_argument(
        "--batch-size",
        help=f"Size of the grid. E.g. 102400000. Default {batch_size}",
        type=int,
        default=int(f"{batch_size}"),
    )
    n_batches = 8
    parser.add_argument(
        "--n-batches",
        help=f"Size of the grid. E.g. 8. Default {n_batches}",
        type=int,
        default=int(f"{n_batches}"),
    )

    args, _ = parser.parse_known_args(argv)
    return args
