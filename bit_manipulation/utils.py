
BITS = 16  # format 2's complement binary

def to_bin_str(n):
    s = bin(n & int("1" * BITS, 2))[2:]
    return ("{0:0>%s}" % BITS).format(s)
