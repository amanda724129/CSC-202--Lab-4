import sys
import unittest
from typing import *
from dataclasses import dataclass
import math 
import matplotlib.pyplot as plt
import numpy as np
import random
import time
sys.setrecursionlimit(10**6)
from bst import *
TREES_PER_RUN : int = 10000 
# Return True if a comes before b and False otherwise.
def comes_before(a, b):
    return a < b

# Return a BinarySearchTree containing n random floats in [0,1).
def random_tree(n):
    bst = BinarySearchTree(comes_before, None)
    for _ in range(n):
        bst = insert(bst, random.random())
    return bst

# Compute BST height from a root node.
def height_of_root(root):
    def h(node):
        if node is None:
            return -1
        return 1 + max(h(node.left), h(node.right))
    return h(root)

# Find n_max from 1.5-2.5 seconds.
def find_n_max():
    n = 1
    while True:
        t0 = time.perf_counter()
        for _ in range(TREES_PER_RUN):
            t = random_tree(n)
            root = t.tree
            _ = height_of_root(root)
        elapsed = time.perf_counter() - t0

        print("n = {n}, time = {elapsed:.2f} seconds")

        match elapsed:
            case t if 1.5 <= t <= 2.5:
                print("Found n_max = {n}")
                return n
            case t if t < 1.5:
                n *= 2
            case _:
                n = max(1, n // 2)

# Average height over TREES_PER_RUN random trees of size n
def average_height_for_n(n):
    total = 0
    for _ in range(TREES_PER_RUN):
        t = random_tree(n)
        total += height_of_root(t.tree)
    return total / TREES_PER_RUN

# Return k integers evenly spaced from 0 to n_max.
def evenly_spaced_ints(n_max, k=50):
    if k <= 1:
        return [int(n_max)]
    vals = []
    for i in range(k):
        v = int(round(i * (n_max / float(k - 1))))
        if not vals or v != vals[-1]:
            vals.append(v)
    if vals[0] != 0:
        vals.insert(0, 0)
    if vals[-1] != n_max:
        vals.append(int(n_max))
    return vals

# A graph of average tree height as a function of N.
def graph_average_height(n_max):
    Ns = evenly_spaced_ints(n_max, 50)
    Ys = [average_height_for_n(n) for n in Ns]

    plt.plot(Ns, Ys, marker='o', linewidth=1, label='avg height')
    plt.xlabel("N (number of keys)")
    plt.ylabel("Average height (edges)")
    plt.title("Average BST Height vs N")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    n_max = find_n_max()
    print("n_max =", n_max)
    graph_average_height(n_max)
