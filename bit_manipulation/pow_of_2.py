"""
Use bit_manipulation to determine whether number is a power of 2.
"""
from datetime import datetime


def is_pow_2(num):
    res = num & (num-1)
    return res == 0


if __name__ == "__main__":
    start = datetime.utcnow()
    max_exp = 17

    pows = [2**i for i in range(max_exp)]
    non_pows = [i for i in range(2**max_exp) if 2**i != 0]

    for pow in pows:
        assert is_pow_2(pow)

    for non_pow in pows:
        assert is_pow_2(non_pow)

    stop = datetime.utcnow()
    seconds = (stop - start).total_seconds()

    print("Success!")
    print("Runtime: " + str(seconds))
    print("Size pows: " + str(len(pows)))
    print("Size non_pows: " + str(len(non_pows)))
