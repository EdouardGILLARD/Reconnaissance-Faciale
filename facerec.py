# facerec.py
# ----------------
# Ce programme lance la reconnaissance faciale 
# On compare avec toutes les image contenue dans le dossier
# lienPhoto. 
# Elle n'est pas reconnue -> on l'a supprime !
# La personne est reconnue -> on fait une pause et on supprime toutes les photos. 
# En effet, dans notre cas, la camera prend plusieurs photos de la meme personne.
# ----------------

#VARIABLE A RENTRER :
#Lien ou prendre les photos à comparer
lienPhoto= 'XXXXXXXXXXXXXXXXX'


import cv2, sys, numpy, os
import glob
import requests
import time

size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'att_faces'

# Part 1: Create fisherRecognizer
print('Training...')
# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)


# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]

# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face'
model = cv2.face.createFisherFaceRecognizer()
model.train(images, lables)


# Part 2: Use fisherRecognizer on image
haar_cascade = cv2.CascadeClassifier(fn_haar)


while (True) :
		list = glob.glob(lien + '/*.*')
		longueur = len(list)
		
		if longueur != 0 :
		#for i in range(0,longueur) :
			time.sleep(3)
			webcam = cv2.imread(list[0])
			#while True:
			p=1
			if p == 1 :
			    #(rval, frame) = webcam.read()
			    frame = webcam
			    frame=cv2.flip(frame,1,0)
			    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			    mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
			    faces = haar_cascade.detectMultiScale(mini)
			    if len(faces) == 0 : 
				os.remove(list[0])
			    for i in range(len(faces)):
				face_i = faces[i]
				(x, y, w, h) = [v * size for v in face_i]
				face = gray[y:y + h, x:x + w]
				face_resize = cv2.resize(face, (im_width, im_height))

				# Try to recognize the face
				prediction = model.predict(face_resize)
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

				# Write the name of recognized face
				#600 c'est le seuil de prediction qu'on fixe
				
				if prediction[1]<600:
				     cv2.putText(frame,'%s - %.0f' % (names[prediction[0]],prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
				     name = names[prediction[0]]
				     print name
				     time.sleep(1.5)
				     listb= glob.glob(lien + '/*.*')
				     longueurb = len(listb)
				     for h in range(0,longueurb) :
					os.remove(listb[h])
				     #time.sleep(3.5)
				     break
				     
				     

				else:
				     cv2.putText(frame,'Unknown',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
				     print name
				     os.remove(list[0])
				     
	
				cv2.imshow('OpenCV', frame)			

			longueur =0

	key = cv2.waitKey(10)
	# On attend que l'utilisateur presse une touche
	cv2.waitKey(0)
	# Destruction de la fenetre
	cv2.destroyAllWindows()


			
	

			
			

