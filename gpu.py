from numba import cuda
import hashlib
import numpy as np

@cuda.jit
def kernel_combinaisons(hash):
    all_chars = np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','[',']','^','_','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','{','}','<','>','=','|','~','?'])
    mdp = np.empty(0, dtype=np.dtype('U15')) # define the data type of the array
    MAX_LENGTH = 15
    for y in range (0,MAX_LENGTH):
        for i in range(len(all_chars)):
            new_mdp = np.concatenate([mdp, np.array([all_chars[i]], dtype=np.dtype('U15'))])
            new_mdp_str = ''.join(new_mdp) # convert the array to string
            if(hashlib.sha1(new_mdp_str.encode()).hexdigest() == hash) :
                print("Le mot de passe est : ", new_mdp_str)
                return new_mdp_str
            else:
                mdp = new_mdp # update the array


# from numba import cuda
# import hashlib
# import numpy as np
# @cuda.jit
# def kernel_combinaisons(hash):
#     mdp=''
#     all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','[',']','^','_','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','{','}','<','>','=','|','~','?']
#     # tx = cuda.threadIdx.x
#     # bx = cuda.blockIdx.x
#     # bw = cuda.blockDim.x
#     # i = tx + bx * bw
#     #taille maximale que fait notre mdp
#     MAX_LENGTH = 15
    
#     #if i <MAX_LENGTH: #Les différentes tailles de mdp à trouver
#     for y in range (0,MAX_LENGTH) : 
#         for i in range(len(all)):
#             mdp = np.concatenate(mdp,all[i])
#             if(hashlib.sha1(mdp.encode()).hexdigest() == hash) :
#                 print("Le mot de passe est : ", mdp)
#                 return mdp
        
#         #kernel_combinaisons( mdp,  hash) #Recursion avec caractère suivant)