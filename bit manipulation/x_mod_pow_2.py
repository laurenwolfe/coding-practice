"""
Use bit manipulation to determine whether number is a power of 2.
"""
from datetime import datetime
from statistics import mean

NUMBERS = 100000
TRIALS = 10


def bitwise_mod(num, power):
    """Returns num % power using only bitwise operators."""
    return num & ((1 << power) - 1)


def library_mod(num, power):
    """Returns num % power using Python library."""
    return num % 2 ** power


def trial(test_func, test_values):
    """Runs benchmarking tests."""
    start = datetime.utcnow()

    for val in test_values:
        num = val[0]
        power = val[1]

        test_func(num, power)

        """ Test commented out for for benchmarking.
        assert test_func(num, power) == (num % 2 ** power)
        """

    stop = datetime.utcnow()
    return (stop - start).total_seconds()


if __name__ == "__main__":
    test_vals_24 = [(num, power) for num in range(NUMBERS) for power in range(24)]
    test_vals_16 = [(num, power) for num in range(NUMBERS) for power in range(16)]
    test_vals_8 = [(num, power) for num in range(NUMBERS) for power in range(8)]

    results = {"bitwise": ([], [], []), "library": ([], [], [])}  # idx 0 = 2^8 tests, 1 = 2^16 tests, 2 = 2^24 tests

    for i in range(TRIALS):
        results["bitwise"][0].append(trial(bitwise_mod, test_vals_8))
        results["bitwise"][1].append(trial(bitwise_mod, test_vals_16))
        results["bitwise"][2].append(trial(bitwise_mod, test_vals_24))
        results["library"][0].append(trial(library_mod, test_vals_8))
        results["library"][1].append(trial(library_mod, test_vals_16))
        results["library"][2].append(trial(library_mod, test_vals_24))

    print("-- Benchmarking Results -- ")
    print("The bitwise function is: ")
    print("{1:.4f}s faster on average for {0} power trial".
          format("2^8", mean(results["library"][0]) - mean(results["bitwise"][0])))
    print("{1:.4f}s faster on average for {0} power trial".
          format("2^16", mean(results["library"][1]) - mean(results["bitwise"][1])))
    print("{1:.4f}s faster on average for {0} power trial".
          format("2^24", mean(results["library"][2]) - mean(results["bitwise"][2])))

    """
    For 10 trials of 100000 * n values each, where n refers to 2^n powers tested: 

    -- Benchmarking Results -- 
    Bitwise function is: 
    0.2556s faster on average for 2^8 power trial
    0.4863s faster on average for 2^16 power trial
    0.6749s faster on average for 2^24 power trial

    Not surprising. Python's % operator has to handle more than just powers of 2. Still, neat!  
    """
