from dictionnaire import dico
from brute_force import bf
import gpu
from numba import cuda
# import tensorflow as tf
import gc

open('motnombre.txt', 'w').close()
open('perso1.txt', 'w').close()
open('test.txt', 'w').close()

answer = input(
    "Bonjour !\nConnaissez-vous quel algorithme a été utilisé ?\n\t1. Oui\n\t2. Non\n\nVeuillez entrer le chiffre correspondant. "
)

if answer == '1':
	HASH = ''
	TYPE_HASH = input(
	    "\nVeuillez choisir\n\t1. Sha1\n\t2. MD5\n\t3. Autre\n\nVeuillez entrer le chiffre correspondant. "
	)

	if TYPE_HASH == '1':
		HASH = 'sha1'

	elif TYPE_HASH == '2':
		HASH = 'MD5'

	else:
		print(
		    "\nDésolé mais nous ne pouvons pas casser votre mdp pour le moment."
		)

tf.config.list_physical_devices('GPU')

mdp = input(
	    "\nVeuillez entrer votre hash. "
	)  #il ne faut pas mettre un hash pour l'instant car version test juste mettre des mots ou lettres random

Mode = input(
	    "\nQuelle méthode voulez-vous utiliser ?\n\t1. Brute force\n\t2. Dictionnaire\n\nVeuillez entrer le chiffre correspondant. "
	)

if Mode == '1' :
	#bf(HASH, mdp)
	

	gc.collect()

	
	d_HASH = cuda.to_device(HASH)
	d_mdp = cuda.to_device(mdp)
	gpu.kernel_combinaisons[5,5](d_mdp, d_HASH)
	torch.cuda.empty_cache()	

elif Mode == '2':
    dico(HASH, mdp)
    
else:
	  print("Veuillez choisir parmis les chiffres proposés.")
