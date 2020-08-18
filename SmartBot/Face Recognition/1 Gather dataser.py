import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

modelFile = "C:\\Users\\Junu\\Desktop\\OpenCV-Face-Recognition-master\\models\\res10_300x300_ssd_iter_140000.caffemodel"
configFile = "C:\\Users\\Junu\\Desktop\\OpenCV-Face-Recognition-master\\models\\deploy.prototxt.txt"

net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
face_id = input('\n enter user id end press <return> ==>  ')
count = 0
  
while(True):

    ret, img = cam.read()
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
    (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces = net.forward()
    #to draw faces on image
    for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2]
            if confidence > 0.5:
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
                count += 1                
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y1,x:x1])
                cv2.imshow('img', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 60: # take 60 samples 
          break


cam.release()
cv2.destroyAllWindows()





