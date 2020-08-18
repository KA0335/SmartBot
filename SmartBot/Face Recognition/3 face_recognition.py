import cv2
import numpy as np
import time


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

modelFile = "C:\\Users\\Junu\\Desktop\\OpenCV-Face-Recognition-master\\models\\res10_300x300_ssd_iter_140000.caffemodel"
configFile = "C:\\Users\\Junu\\Desktop\\OpenCV-Face-Recognition-master\\models\\deploy.prototxt.txt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

font = cv2.FONT_HERSHEY_TRIPLEX
font1= cv2.FONT_HERSHEY_DUPLEX

#iniciate id counter
id = 0


names = ['None', 'Kushagra', 'W', 'X', 'Y', 'Z'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')   
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]
    s=time.time()
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
    (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces = net.forward()
    print(time.time()-s)
    for i in range(faces.shape[2]):
        confidence = faces[0, 0, i, 2]
        if confidence > 0.5:
            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
                       
            id, confidence = recognizer.predict(gray[y:y1,x:x1])
            

        # Check confidence
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
        
           
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1) 
              
        fps = cam.get(cv2.CAP_PROP_FPS)
        text= str(fps)
        cv2.putText(img, text, (50,50), font1, 1, (255,230,230), 4)
                      
        cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
