import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten,MaxPooling2D,Dropout
from keras.optimizers import SGD
from keras.models import load_model
from keras.models import save_model
import tkinter

coordinates=[]
images=[]


for i in range(30706):
    img=cv2.imread(r"D:\Facultate\Licenta\RoiDataSet\roi"+str(i)+".jpg",cv2.IMREAD_GRAYSCALE)
    img=np.array(img)
    images.append(img)

images=np.array(images)
images=images.reshape(30706,84,100,1)
print(np.shape(images))
images=images.astype("float32")
images /= 255
labels=np.zeros((30706,205))
for k in range(0,8160,204):
    j=1
    for i in range(20,224):
        labels[k+i][j]=1
        j+=1
    labels[k+223][204]=1
m=1
j=2
for k in range(10000,30706):
     labels[k][m]=1
     labels[k][j]=1
     j=j+1
     if(j==205):
         m+=1
         j=m+1
for i in range(20):
    labels[i][0]=1
for i in range(8180,10000):
    labels[i][0]=1


model = Sequential()
model.add(Conv2D(32,(7,7),input_shape=(images.shape[1], images.shape[2], 1),padding='same',strides=1, activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3),strides=2))
model.add(Conv2D(64,(5,5),padding='same',strides=1, activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3),strides=2))
model.add(Conv2D(128, (3,3),padding='same',strides=1,activation='relu'))
model.add(Conv2D(128, (3,3),padding='same',strides=1,activation='relu'))
model.add(Conv2D(64, (3,3),padding='same',strides=1,activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=2))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(1000,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1000,activation='relu'))
model.add(Dense(205,activation='softmax'))
sgd =SGD(lr=0.001, momentum=0.5)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

model.fit(images,labels,epochs=100,batch_size=10)


model.save_weights('faultrec_weights.h5')

# Save the model architecture
with open('faultrec_architecture.json', 'w') as f:
    f.write(model.to_json())

