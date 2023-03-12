import hashlib
import sys
from verification import verification_sha1 
from verification import verification_MD5
from numba import cuda

#mdp_test est le mot de passe créé à partir des combinaisons de lettre AVANT de passer dans l'algo de hash

def bf (type_hash, mdp) :
  #le hash que la personne souhaite casser
  '''if type_hash == 'sha1' :
    MDP = hashlib.sha1(mdp.encode()).hexdigest() #cette ligne sert a tester le code

  else : 
    MDP = hashlib.md5(mdp.encode()).hexdigest() #cette ligne sert a tester le code

  hash = MDP'''

  #tableaux avec les caractères des combinaisons qu'on doit tester
  all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','[',']','^','_','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','{','}','<','>','=','|','~','?']
#  number = ['0','1','2','3','4','5','6','7','8','9']
#  symbols =['@','[',']','^','_','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','{','}','<','>','=','|','~','?']
#  AZ = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#  az = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#  
#  gpu.kernel_AZ[1, 1](AZ)
#  gpu.kernel_az[1, 1](az)
#  gpu.kernel_symbols[1, 1](symbols)
#  gpu.kernel_number[1, 1](number)
  
# gpu.combinaisons[5,5](all, mdp, type_hash)
  
#  #taille maximale que fait notre mdp
#  MAX_LENGTH = 15
#
#  for i in range(MAX_LENGTH): #Les différentes tailles de mdp à trouver
#      combinaisons(mdp, 0, i, '', all, type_hash)
#
#      print("Tous les mots de passe de", i, "caractères ont été testé.")


def combinaisons (hash, currentlength, maxlength, mdp_test, all, type_hash) : #boucle de création des combinaisons
    # if currentlength > maxlength:

    #     return

    # for i in range(len(all)):

    #   if type_hash == 'sha1' :
    #      verification_sha1(hash, mdp_test+all[i]) #on vérifie si la string obtenue est notre mdp
    #   #    mdp_test += all[i]
    #   #    if(hashlib.sha1(mdp_test.encode()).hexdigest() == hash) :
    #   #     print("Le mot de passe est : ", mdp_test+all[i])
    #   #     return mdp_test
    #   # # elif type_hash == 'MD5' :
    #   #   verification_MD5(hash, mdp_test+all[i]) #on vérifie si la string obtenue est notre mdp

    #   combinaisons (hash, currentlength+1, maxlength, mdp_test, all, type_hash) #Recursion avec caractère suivant
    if currentlength > maxlength:
      return
    for i in range(len(all)):
      if type_hash == 'sha1' :
         verification_sha1(hash, mdp_test+all[i]) #on vérifie si la string obtenue est notre mdp

      elif type_hash == 'MD5' :
        verification_MD5(hash, mdp_test+all[i]) #on vérifie si la string obtenue est notre mdp

      combinaisons (hash, currentlength+1, maxlength, mdp_test+all[i], all, type_hash) #Recursion avec caractère suivant
