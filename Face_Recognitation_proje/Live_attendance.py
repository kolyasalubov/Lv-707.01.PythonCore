import numpy as np
import cv2
from mtcnn.mtcnn import MTCNN
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import joblib
import pandas as pd
from PIL import Image
import datetime
import time
from mtcnn.mtcnn import MTCNN
from tensorflow.keras.models import load_model
from tensorflow.keras import backend


ckpt_path = 'xception_cl_fus_aspp_imp1k_10kl-3cc0.1mse-5nss5bc_bs4_ep30_valloss-2.5774_full.h5'
embedding_model = load_model(ckpt_path, custom_objects={"K": backend})
print('Embedding Model Loaded')

ML_model = joblib.load('models/face_prediction_model.sav')
print('Loaded ML Model')

detector = MTCNN()

def find_face(img,img_size=(160,160)):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = np.asarray(img) # converting our image obj to numpy array
    faces = detector.detect_faces(img)
    if faces:
        first_image,second_image,third_image,fourth_image = faces[0]['box']
        first_image,second_image=abs(first_image),abs(second_image)
        face = img[second_image:second_image+fourth_image,first_image:first_image+third_image]
        face = Image.fromarray(face) # converting it to image object to resize it
        face = face.resize(img_size) # resizing it
        face = np.asarray(face)      # converting it back to array
        return face,x,y,w,h
    return None,None,None,None,None



def embed(face):
    face = face.astype('float32')
    fm,fs = face.mean(),face.std()
    face = (face-fm)/fs
    face = np.expand_dims(face,axis=0)
    embs = embedding_model.predict(face)
    return embs[0]


#for converting ids to names
def id2name(id):
    x = os.listdir('faces/train/')
    return x[id]


def mark_attendance(name,roll):

    roll_list = []
    
    if not os.path.isdir('Attendance'):
        os.makedirs('Attendance')
        
    date=time.asctime()[8:10]
    month=time.asctime()[4:7]
    year=time.asctime()[-4:]
    tim=time.asctime()[11:16]
    
    # if csv of current date doesn't exist, make it
    if (date+'-'+month+'-'+year+'.csv')  not in os.listdir('Attendance/'):
        att = pd.DataFrame(columns=['Roll','Name','Time'])
        att.to_csv('Attendance/'+date+'-'+month+'-'+year+'.csv')
        
    # here we are just selecting these 3 columns everytime and ignoring the index column    
    att = pd.DataFrame(pd.read_csv('Attendance/'+date+'-'+month+'-'+year+'.csv'))
    att = att[['Roll','Name','Time']]
    
    for i in range(len(att)):
        roll_list.append(str(att.loc[i]['Roll']))
    

    if roll not in roll_list:
        att1 = pd.DataFrame({'Name':[name], 'Roll':[roll], 'Time':[datetime.datetime.now().strftime("%H:%M:%S")]})
        att = att.append(att1,ignore_index=False)
        print(f'Attendance marked for {name} whose roll no is {roll}.')

    else:
        prev_time = att[att['Roll']==int(roll)]['Time'].iloc[-1]
        curr_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        #here we are just checking the time difference between previous timestamp and current time
        if datetime.datetime.strptime(curr_time, '%H:%M:%S') - datetime.datetime.strptime(prev_time, '%H:%M:%S') > datetime.timedelta(minutes=5):
            att1 = pd.DataFrame({'Name':[name], 'Roll':[roll], 'Time':[datetime.datetime.now().strftime("%H:%M:%S")]})
            att = att.append(att1,ignore_index=False)
            print(f'Attendance marked for {name} whose roll no is {roll}.')

    att.to_csv('Attendance/'+date+'-'+month+'-'+year+'.csv')


cap = cv2.VideoCapture(0)
i = 0

while 1:
    i+=1
    ret,frame = cap.read()
    if i>10:
        face,first_image,second_image,third_image,fourth_image = find_face(frame)
        if face is not None:
            face_emb = embed(face)
            pred = ML_model.predict(face_emb.reshape(1,-1))
            name = str(id2name(pred[0]))
            if name:
                mark_attendance(name.split('-')[0],name.split('-')[1])
                cv2.rectangle(frame,(first_image,second_image),(first_image+third_image,second_image+fourth_image),(178,88,239),1)
                cv2.putText(frame,name,(first_image,second_image-10),cv2.FONT_HERSHEY_TRIPLEX,0.8,(178,88,239),1,cv2.LINE_AA)
        cv2.imshow('live',frame)
    
    if cv2.waitKey(1)==27:
        break
        
cap.release()
cv2.destroyAllWindows()
