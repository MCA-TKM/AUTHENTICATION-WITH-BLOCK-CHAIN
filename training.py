import os
import cv2
import numpy as np
from PIL import Image

Base_Dir=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(Base_Dir,"dataSet")
recognizer=cv2.createLBPHFaceRecognizer();
#recognizer=cv2.face.createLBPHFaceRecognizer();
#recognizer=cv2.face.LBPHFaceRecognizer_create();
#recognizer=EigenFaceRecognizer_create();
path='dataSet'

'''for root,dirs,files in os.walk(image_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path=os.path.join(root,file)
                print(path)'''
def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    print(imagePaths)
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert("L");
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return IDs,faces
Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
#recognizer.write()
cv2.destroyAllWindows()
recognizer
        
        
