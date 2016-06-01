# rennomer.py
# ----------------
# Ce programme permet de renommer les elements d'un dossier 
# de maniere i.JPG
# Cela est necessaire pour lancer la fonction train.py
# ----------------

#VARIABLE A RENTRER :
#Lien du dossier : 
lien = "XXXXXXXXXXXXXXXXXXXXXXXXX"


import cv2, sys, numpy, os
import glob

list = glob.glob(lien + '/*.*')
longueur = len(list)

for i in range (0,longueur) :
	os.rename(list[i], lien + '/' + str(i) + '.JPG')

print 'Bien renomme ! '


