-----------------------------------
PROGRAMME DE RECONNAISSANCE FACIALE
-----------------------------------

Prérequis : 
	Avoir installé la bibliothèque openCv et les contribs
	Python 2.7

		-> http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/

	Pour avoir les imports, lire chaque début de programme et installer les packages. 
		exemple : import glob 
		faire : sudo pip install glob 
		etc..


Ce programme, compare un dossier d'image avec notre base de donnée d'image afin de trouver le nom
de la personne se trouvant devant la caméra. 


Expliquations : 
Ce document regroupe la notice d'utilisation du programme de reconnaissance Faciale. 
Il est composé de 3 script : 
	- rennomer.py : Permet de renommer les images d'un dossier en nombre.JPG = Utile pour la suite
		-> Il faut rentrer comme variable dans le script le lien du dossier ou se trouvent les images
	- train.py : Permet de prendre nos images rennommées, de reconnaitre les visages et de les unifier dans un même format
		-> Il faut rentrer comme variable "nombre" le numéro de la dernière photo + le lien ou sont les images
	- facerec.py : Lance la reconnaissance Faciale
		-> Il faut rentrer dans le programme, le lien du dossier où sont les photos


Il reste quoi à faire ? 
	Prend des photos de toi (minimum une 15aine), et met les dans le dossier Personne/ton nom. 
	Lance le rennomer.py dans ce fichier
	lance le train.py
	Met des images dans le dossier avec lequel tu veux comparer et met le ds facerec.py et lance ce script
	Bingo ! 


Architecture : 

.
├── att_faces
│   ├── edouard
│   │   ├── 0.png
│   │   ├── 1.png
│   │   └── 2.png
│   ├── s1
│   │   ├── 10.pgm
│   │   ├── 1.pgm
│   │   ├── 2.pgm
│   │   ├── 3.pgm
│   │   ├── 4.pgm
│   │   ├── 5.pgm
│   │   ├── 6.pgm
│   │   ├── 7.pgm
│   │   ├── 8.pgm
│   │   └── 9.pgm
│   ├── s2
│   │   ├── 10.pgm
│   │   ├── 1.pgm
│   │   ├── 2.pgm
│   │   ├── 3.pgm
│   │   ├── 4.pgm
│   │   ├── 5.pgm
│   │   ├── 6.pgm
│   │   ├── 7.pgm
│   │   ├── 8.pgm
│   │   └── 9.pgm
│   └── s3
│       ├── 10.pgm
│       ├── 1.pgm
│       ├── 2.pgm
│       ├── 3.pgm
│       ├── 4.pgm
│       ├── 5.pgm
│       ├── 6.pgm
│       ├── 7.pgm
│       ├── 8.pgm
│       └── 9.pgm
├── Personne
│    ── edouard
│       ├── r.JPG
│       ├── f.JPG
│       └── h.JPG
├── readMe.txt
├── facerec.py
├── haarcascade_frontalface_default.xml
├── rennomer.py
├── suppressionftp.sh
└── train.py

