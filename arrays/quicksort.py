"""Implement quicksort."""
import random

values_sorted = [i for i in range(100)]
values_rev_sorted = [i for i in range(100, 1, -1)]
values_random_pos = [int(random.uniform(1, 1000)) for i in range(100)]
values_random_signed = [int(random.uniform(-999, 999)) for i in range(100)]
values_none = []
values_one = [5]

