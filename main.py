import hashlib
from brute_force import combinaisons
import gpu
from numba import cuda
import numpy
import time
# import tensorflow as tf


HASH = 'a9993e364706816aba3e25717850c26c9cd0d89d'
mdp = numpy.empty(shape=0)

start = time.perf_counter()
#taille maximale que fait notre mdp
MAX_LENGTH = 15

for i in range(MAX_LENGTH): #Les différentes tailles de mdp à trouver
    combinaisons(mdp, 0, i, '', all, 'sha1')

    print("Tous les mots de passe de", i, "caractères ont été testé.")
end = time.perf_counter()
print("elapsed time before cuda implementation = {}s".format((end - start)))

d_HASH = cuda.to_device(HASH)
d_mdp = cuda.to_device(mdp)
start = time.perf_counter()
gpu.kernel_combinaisons[5,5](d_mdp, d_HASH)
end = time.perf_counter()
mdp = numpy.empty(shape=d_mdp.shape, dtype=d_mdp.dtype)
d_mdp.copy_to_host(mdp)
HASH = numpy.empty(shape=d_HASH.shape, dtype=d_HASH.dtype)
d_HASH.copy_to_host(HASH)
print(mdp)
print(HASH)
print("elapsed time before cuda implementation= {}s".format((end - start)))