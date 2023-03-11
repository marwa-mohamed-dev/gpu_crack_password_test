from numba import cuda
import brute_force as b


@cuda.jit 
def kernel_combinaisons(mdp, type_hash):
    all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','[',']','^','_','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','{','}','<','>','=','|','~','?']
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    bw = cuda.blockDim.x
    i = tx + bx * bw
    #taille maximale que fait notre mdp
    MAX_LENGTH = 15
    
    if i < mdp.size: #Les différentes tailles de mdp à trouver
        b.combinaisons(mdp, 0, i, '', all, type_hash)
        print("Tous les mots de passe de", i, "caractères ont été testé.")