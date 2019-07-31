import imutils
import math
import numpy as np
import cv2
import copy
import rotatingandtranslating as rt
import dynamicroiextraction as dre
from keras.models import model_from_json
coordinates=[]
for i in range(0,760,10):
    coordinates.append((25+i,6))
coordinates.append((786,12))
for i in range(0,240,10):
    coordinates.append((793,26+i))
coordinates.append((787,267))
for i in range(0,760,10):
    coordinates.append((776-i,273))
coordinates.append((14,268))
for i in range(0,240,10):
    coordinates.append((7,256-i))
coordinates.append((13,13))
rot=rt.rotAndTrans(img)
roi=dre.roiExtraction(rot)
with open('faultrec_architecture.json', 'r') as f:
    model = model_from_json(f.read())
# Load weights into the new model
model.load_weights('faultrec_weights.h5')
cv2.imshow("roi",roi)
roi=roi.reshape((1,84,100,1))
roi=roi.astype("float32")
roi /= 255
out=model.predict(roi)
out=out.reshape(205)
rot=cv2.cvtColor(rot,cv2.COLOR_GRAY2RGB)
if out[0]>0.3:
    cv2.imshow("Input", img)
    img2 = cv2.resize(rot, (originalSize[1], originalSize[0]))
    cv2.imshow("No mistakes found!", img2)
else:
 for i in range(1,np.size(out)):
    if(out[i]>0.1):
        cv2.circle(rot,coordinates[i-1],10,(0,0,255))
        cv2.imshow("Input",img)
        img2=cv2.resize(rot,(originalSize[1],originalSize[0]))
        cv2.imshow("Mistakes found!",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(np.argmax(out))
print(out)
