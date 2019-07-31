import imutils
import math
import numpy as np
import cv2
import copy
import rotatingandtranslating as rt
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
roi=np.zeros((84,100),dtype="uint8")
i=0
m=0
n=0
for j in range(20,780):
    while (rot[i][j]<=15):
        i+=1
    roi[m][n]=rot[i][j]
    roi[m+1][n]=rot[i+1][j]
    roi[m+2][n]=rot[i+2][j]
    roi[m+3][n]=rot[i+3][j]
    n+=1
    if(n%100==0):
        n=0
        m+=4
    i=0
i=274
for j in range(20,780):
    while(rot[i][j]<=15):
        i-=1
    roi[m][n] = rot[i][j]
    roi[m + 1][n] = rot[i - 1][j]
    roi[m + 2][n] = rot[i - 2][j]
    roi[m + 3][n] = rot[i - 3][j]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
    i=274
j=0
for i in range(20,260):
    while(rot[i][j]<=15):
        j+=1
    roi[m][n] = rot[i][j]
    roi[m + 1][n] = rot[i][j+1]
    roi[m + 2][n] = rot[i][j+2]
    roi[m + 3][n] = rot[i][j+3]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
    j=0
j=798
for i in range(20,260):
    while(rot[i][j]<=15):
        j-=1
    roi[m][n] = rot[i][j]
    roi[m + 1][n] = rot[i][j-1]
    roi[m + 2][n] = rot[i][j-2]
    roi[m + 3][n] = rot[i][j-3]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
    j=798
#corners
#up left
i=0
j=0
while(rot[i][j]<=15):
    i+=1
    j+=1
for k in range(-7,7):
    roi[m][n] = rot[i-k][j+k]
    roi[m + 1][n] = rot[i-k+1][j+k+1]
    roi[m + 2][n] = rot[i -k+ 2][j+k+2]
    #roi[m + 3][n] = rot[i -k+ 3][j+k+3]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
#down right
i=279
j=799
while(rot[i][j]<=15):
    i-=1
    j-=1
for k in range(-6,6):
    roi[m][n] = rot[i-k][j+k]
    roi[m + 1][n] = rot[i -k- 1][j+k-1]
    roi[m + 2][n] = rot[i -k- 2][j+k-2]
    #roi[m + 3][n] = rot[i -k- 3][j+k-3]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
#up right
i=0
j=799
while(rot[i][j]<=15):
    i+=1
    j-=1
for k in range(-7,7):
    roi[m][n] = rot[i-k][j-k]
    roi[m + 1][n] = rot[i-k+1][j-k-1]
    roi[m + 2][n] = rot[i -k+ 2][j-k-2]
   # roi[m + 3][n] = rot[i -k+ 3][j-k-3]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
#down left
i=279
j=0
while(rot[i][j]<=15):
    i-=1
    j+=1
for k in range(-7,7):
    roi[m][n] = rot[i-k][j-k]
    roi[m + 1][n] = rot[i -k- 1][j-k+1]
    roi[m + 2][n] = rot[i-k-2][j-k+2]
   # roi[m + 3][n] = rot[i-k-3][j-k+3]
    n += 1
    if (n % 100 == 0):
        n = 0
        m += 4
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
