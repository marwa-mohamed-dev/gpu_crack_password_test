import hashlib
from brute_force import bf
import gpu
from numba import cuda
import numpy
import time
# import tensorflow as tf


HASH = 'a9993e364706816aba3e25717850c26c9cd0d89d'
mdp = numpy.empty()
d_HASH = cuda.to_device(HASH)
d_mdp = cuda.to_device(mdp)
start = time.perf_counter()
gpu.kernel_combinaisons[5,5](d_mdp, d_HASH)
end = time.perf_counter()
mdp = numpy.empty(shape=d_mdp.shape, dtype=d_mdp.dtype)
d_mdp.copy_to_host(mdp)
print(mdp)
print("Elapsed (after compilation) = {}s".format((end - start)))