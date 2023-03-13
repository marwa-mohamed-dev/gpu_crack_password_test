import numpy as np
from numba import cuda, uint32
import hashlib
import time 
@cuda.jit
def generate_passwords_kernel(chars, n_chars, length, passwords):
    """
    CUDA kernel to generate all possible passwords of a given length
    """
    # Get the thread ID
    tid = cuda.grid(1)
    
    # Calculate the number of possible passwords
    n_passwords = n_chars ** length
    
    # Generate the passwords
    if tid < n_passwords:
        password = ""
        for i in range(length):
            idx = (tid // n_chars ** i) % n_chars
            password += chars[idx]
        passwords[tid] = password

@cuda.jit
def hash_passwords_kernel(passwords, n_passwords, target_hash, hashes):
    """
    CUDA kernel to hash all the passwords and compare them to the target hash
    """
    # Get the thread ID
    tid = cuda.grid(1)
    
    # Hash the passwords and compare them to the target hash
    if tid < n_passwords:
        hash_value = hash_password(passwords[tid])
        if hash_value == target_hash:
            hashes[tid] = 1

def hash_password(password):
    """
    Hashes a password using the SHA-256 algorithm
    """
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.digest()

def crack_password(target_hash, chars, length):
    # Convert the character set to a NumPy array
    chars = np.array(list(chars), dtype=np.uint32)
    
    # Calculate the number of characters in the character set
    n_chars = len(chars)
    
    # Calculate the number of possible passwords
    n_passwords = n_chars ** length
    
    # Allocate memory on the GPU for the password candidates and the hashes
    passwords = cuda.device_array(n_passwords, dtype=np.object_)
    hashes = cuda.device_array(n_passwords, dtype=np.uint32)
    
    # Generate all possible passwords
    threads_per_block = 256
    blocks_per_grid = (n_passwords + threads_per_block - 1) // threads_per_block
    generate_passwords_kernel[blocks_per_grid, threads_per_block](chars, n_chars, length, passwords)
    
    # Hash the passwords and compare them to the target hash
    threads_per_block = 256
    blocks_per_grid = (n_passwords + threads_per_block - 1) // threads_per_block
    hash_passwords_kernel[blocks_per_grid, threads_per_block](passwords, n_passwords, target_hash, hashes)
    
    # Copy the results back from the GPU
    hashes = hashes.copy_to_host()
    
    # Find the password that matches the target hash
    idx = np.nonzero(hashes)[0][0]
    password = passwords[idx]
    
    return password
def main():
    # Target hash to crack
    target_hash = b"\xfd\xd7\xa8\xf0\x1d\xc3\xf2\x2c\x9e\x18\x61\x62\x48\xa9\xfd\x3a"
    
    # Character set to use for generating passwords
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="
    
    # Maximum password length
    max_length = 8
    
    # Start the timer
    start_time = time.time()
    
    # Crack the password
    password = crack_password(target_hash, chars, max_length)
    
    # Stop the timer
    end_time = time.time()
    
    # Print the results
    if password:
        print(f"Password: {password}")
    else:
        print("Password not found")
        
    print(f"Time elapsed: {end_time - start_time:.2f} seconds")
