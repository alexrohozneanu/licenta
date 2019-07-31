import numpy as np
import cv2
def roiExtraction:
        img=cv2.imread(r"D:\Facultate\Licenta\TestSet\test"+str(y)+".jpg",cv2.IMREAD_GRAYSCALE)
        img=cv2.resize(img,(800,280))
        roi=np.zeros((84,100),dtype="uint8")
        #up
        i=0
        m=0
        n=0
        for j in range(20,780):
            while (img[i][j]<=15):
               i+=1
            roi[m][n]=img[i][j]
            roi[m+1][n]=img[i+1][j]
            roi[m+2][n]=img[i+2][j]
            roi[m+3][n]=img[i+3][j]
            n+=1
            if(n%100==0):
                n=0
                m+=4
            i=0
        #down
        i=279
        for j in range(20,780):
            while(img[i][j]<=15):
               i-=1
            roi[m][n] = img[i][j]
            roi[m + 1][n] = img[i - 1][j]
            roi[m + 2][n] = img[i - 2][j]
            roi[m + 3][n] = img[i - 3][j]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
            i=279
        #left
        j=0
        for i in range(20,260):
            while(img[i][j]<=15):
                j+=1
            roi[m][n] = img[i][j]
            roi[m + 1][n] = img[i][j+1]
            roi[m + 2][n] = img[i][j+2]
            roi[m + 3][n] = img[i][j+3]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
            j=0
        #right
        j=799
        for i in range(20,260):
            while(img[i][j]<=15):
                j-=1
            roi[m][n] = img[i][j]
            roi[m + 1][n] = img[i][j-1]
            roi[m + 2][n] = img[i][j-2]
            roi[m + 3][n] = img[i][j-3]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
            j=799
        #corners
        #up left
        i=0
        j=0
        while(img[i][j]<=15):
            i+=1
            j+=1
        for k in range(-10,10):
            roi[m][n] = img[i-k][j+k]
            roi[m + 1][n] = img[i-k+1][j+k+1]
            roi[m + 2][n] = img[i -k+ 2][j+k+2]
            roi[m + 3][n] = img[i -k+ 3][j+k+3]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
        #down right
        i=279
        j=799
        while(img[i][j]<=15):
            i-=1
            j-=1
        for k in range(-6,6):
            roi[m][n] = img[i-k][j+k]
            roi[m + 1][n] = img[i -k- 1][j+k-1]
            roi[m + 2][n] = img[i -k- 2][j+k-2]
            roi[m + 3][n] = img[i -k- 3][j+k-3]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
        #up right
        i=0
        j=799
        while(img[i][j]<=15):
            i+=1
            j-=1
        for k in range(-10,10):
            roi[m][n] = img[i-k][j-k]
            roi[m + 1][n] = img[i-k+1][j-k-1]
            roi[m + 2][n] = img[i -k+ 2][j-k-2]
            roi[m + 3][n] = img[i -k+ 3][j-k-3]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
        #down left
        i=279
        j=0
        while(img[i][j]<=15):
            i-=1
            j+=1
        for k in range(-10,10):
            roi[m][n] = img[i-k][j-k]
            roi[m + 1][n] = img[i -k- 1][j-k+1]
            roi[m + 2][n] = img[i-k-2][j-k+2]
            roi[m + 3][n] = img[i-k-3][j-k+3]
            n += 1
            if (n % 100 == 0):
                n = 0
                m += 4
       return roi


