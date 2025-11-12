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

#Section 3.2
def build_bst(N: int) -> BinarySearchTree:
    tree = BinarySearchTree(less_than, None)
    if N <= 0:
      return tree
    values = random.sample(range(1000000), N)
    for v in values:
        tree = insert(tree, v)
    return tree

def time_to_insert_into_bst(N: int, TREES_PER_RUN: int) -> float:
    total_time = 0.0
    for _ in range(TREES_PER_RUN):
       tree = build_bst(N)
       insert_val = random.randint(0, 10000)
       start = time.perf_counter()
       new_tree = insert(tree, insert_val)
       end = time.perf_counter()
       total_time += (end - start)
    return total_time/TREES_PER_RUN

def avg_insertion_time(n_max: int, TREES_PER_RUN: int) -> float:
    Ns = np.linspace(0, n_max, 50, dtype=int)
    Ns = np.unique(Ns)
    times = []
    for N in Ns:
       avg_time = time_to_insert_into_bst(N, TREES_PER_RUN)
       times.append(avg_time)
    return Ns, times 

def plot_insertion_time_graph(Ns, times):
    plt.plot(Ns, times, marker='o', label='Average Insertion Time')
    plt.xlabel("Tree Size (N)")
    plt.ylabel("Insertion Time (s)")
    plt.title("Insertion Time vs. Tree Size")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

if __name__ == '__main__':
    Ns, times = avg_insertion_time(n_max=50, TREES_PER_RUN=10000)
    plot_insertion_time_graph(Ns, times)
