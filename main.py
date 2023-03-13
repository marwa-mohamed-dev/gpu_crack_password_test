import hashlib
from brute_force import bf
import gpu
from numba import cuda
import numpy as np
import time

# import tensorflow as tf


HASH = 'a9993e364706816aba3e25717850c26c9cd0d89d'
mdp = np.empty(shape=0)
length = 15
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','[',']','^','_','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','{','}','<','>','=','|','~','?']
start = time.perf_counter()
bf(HASH)
end = time.perf_counter()
print("elapsed time before cuda implementation = {}s".format((end - start)))

# Calculate the number of characters in the character set
num_chars = len(chars)


# Calculate the maximum number of passwords to check
max_passwords = num_chars ** length

d_HASH = cuda.to_device(HASH)
d_mdp = cuda.to_device(mdp)
# Launch the brute-force kernel
threads_per_block = 128
blocks_per_grid = (max_passwords + (threads_per_block - 1)) // threads_per_block
start = time.perf_counter()
gpu.kernel_combinaisons[blocks_per_grid, threads_per_block](d_HASH)
cuda.syncthreads()
end = time.perf_counter()
mdp = np.empty(shape=d_mdp.shape, dtype=d_mdp.dtype)
d_mdp.copy_to_host(mdp)
HASH =np.empty(shape=d_HASH.shape, dtype=d_HASH.dtype)
d_HASH.copy_to_host(HASH)
print(mdp)
print(HASH)
print("elapsed time before cuda implementation= {}s".format((end - start)))