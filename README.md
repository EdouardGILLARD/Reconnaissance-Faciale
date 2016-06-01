# Reconnaissance-Faciale

-----------------------------------
PROGRAMME DE RECONNAISSANCE FACIALE
-----------------------------------

Ce programme, compare un dossier d'image avec notre base de donnée d'image afin de trouver le nom
de la personne se trouvant devant la caméra. 


Expliquations : 
Ce document regroupe la notice d'utilisation du programme de reconnaissance Faciale. 
Il est composé de 3 script : 
	- rennomer.py : Permet de renommer les images d'un dossier en nombre.JPG = Utile pour la suite
		-> Il faut rentrer comme variable dans le script le lien du dossier ou se trouvent les images
	- train.py : Permet de prendre nos images rennommées, de reconnaitre les visages et de les unifier dans un même format
		-> Il faut rentrer comme variable "nombre" le numéro de la dernière photo
	- facerec.py : Lance la reconnaissance Faciale
		-> Il faut rentrer dans le programme, le lien du dossier où sont les photos


Architecture : 

.
├── att_faces
│   ├── edouard
│   │   ├── 10.png
│   │   ├── 11.png
│   │   ├── 12.png
│   │   ├── 13.png
│   │   ├── 14.png
│   │   ├── 15.png
│   │   ├── 16.png
│   │   ├── 17.png
│   │   ├── 18.png
│   │   ├── 19.png
│   │   ├── 1.png
│   │   ├── 20.png
│   │   ├── 21.png
│   │   ├── 22.png
│   │   ├── 23.png
│   │   ├── 24.png
│   │   ├── 25.png
│   │   ├── 26.png
│   │   ├── 27.png
│   │   ├── 28.png
│   │   ├── 29.png
│   │   ├── 2.png
│   │   ├── 30.png
│   │   ├── 31.png
│   │   ├── 32.png
│   │   ├── 33.png
│   │   ├── 34.png
│   │   ├── 35.png
│   │   ├── 36.png
│   │   ├── 37.png
│   │   ├── 38.png
│   │   ├── 39.png
│   │   ├── 3.png
│   │   ├── 40.png
│   │   ├── 41.png
│   │   ├── 42.png
│   │   ├── 43.png
│   │   ├── 4.png
│   │   ├── 5.png
│   │   ├── 6.png
│   │   ├── 7.png
│   │   ├── 8.png
│   │   └── 9.png
│   ├── fatou
│   │   ├── 10.png
│   │   ├── 11.png
│   │   ├── 12.png
│   │   ├── 13.png
│   │   ├── 14.png
│   │   ├── 15.png
│   │   ├── 16.png
│   │   ├── 17.png
│   │   ├── 18.png
│   │   ├── 1.png
│   │   ├── 2.png
│   │   ├── 3.png
│   │   ├── 4.png
│   │   ├── 5.png
│   │   ├── 6.png
│   │   ├── 7.png
│   │   ├── 8.png
│   │   └── 9.png
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
│   ├── edouard
│   │   ├── 10.JPG
│   │   ├── 11.JPG
│   │   ├── 12.JPG
│   │   ├── 13.JPG
│   │   ├── 14.JPG
│   │   ├── 15.JPG
│   │   ├── 16.JPG
│   │   ├── 17.JPG
│   │   ├── 18.JPG
│   │   ├── 19.JPG
│   │   ├── 1.JPG
│   │   ├── 20.JPG
│   │   ├── 21.JPG
│   │   ├── 22.JPG
│   │   ├── 23.JPG
│   │   ├── 24.JPG
│   │   ├── 25.JPG
│   │   ├── 26.JPG
│   │   ├── 27.JPG
│   │   ├── 28.JPG
│   │   ├── 29.JPG
│   │   ├── 2.JPG
│   │   ├── 30.JPG
│   │   ├── 31.JPG
│   │   ├── 32.JPG
│   │   ├── 33.JPG
│   │   ├── 34.JPG
│   │   ├── 35.JPG
│   │   ├── 36.JPG
│   │   ├── 37.JPG
│   │   ├── 38.JPG
│   │   ├── 39.JPG
│   │   ├── 3.JPG
│   │   ├── 40.JPG
│   │   ├── 41.JPG
│   │   ├── 42.JPG
│   │   ├── 43.JPG
│   │   ├── 4.JPG
│   │   ├── 5.JPG
│   │   ├── 6.JPG
│   │   ├── 7.JPG
│   │   ├── 8.JPG
│   │   └── 9.JPG
│   └── fatou
│       ├── 0.JPG
│       ├── 1.JPG
│       ├── 2.JPG
│       ├── 3.JPG
│       └── 4.JPG
├── readMe.txt
├── facerec.py
├── haarcascade_frontalface_default.xml
├── rennomer.py
├── suppressionftp.sh
└── train.py

