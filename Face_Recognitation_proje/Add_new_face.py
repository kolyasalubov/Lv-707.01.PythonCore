import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import joblib
import numpy as np
import time
from PIL import Image
from mtcnn.mtcnn import MTCNN
from tensorflow.keras.models import load_model
from tensorflow.keras import backend
from sklearn.preprocessing import Normalizer, LabelEncoder
from sklearn.ensemble import RandomForestClassifier


MAX_TAKING_OF_PHOTOS = 200
MAX_TAKING_OF_PHOTOS_TRAIN = 150
MAX_TAKING_OF_PHOTOS_VAL = 150
ESCAPE_KEY = 27

######### if these directories doesn't exist, make them #######
try: os.makedirs('faces')
except FileExistsError: "This directory exist"

try: os.makedirs('faces/train')
except FileExistsError: "This directories exist"

try: os.makedirs('faces/val')
except FileExistsError: "This directories exist"


############### take name and roll no as input #################
name = input('Enter your name --> ')
roll = input('Enter your roll no --> ')

name = name+'-'+roll


######### make face folders in train and val ##################
if name in os.listdir('faces/train'):
    print('User already exist in faces')

else:    
    os.makedirs('faces/train/'+name)
    os.makedirs('faces/val/'+name)
    
    #open the default camera using default API
    cap = cv2.VideoCapture(0)
    i = 0
    print()
    for i in range(5):
        print(f"Capturing starts in {5-i} seconds...")
        time.sleep(1)
    print('Taking photos...')
    while i<=MAX_TAKING_OF_PHOTOS:
        ret,frame = cap.read()
        print(f"Rate is: {ret}, Frame is: {frame}")
    
        # show live and wait for a key with timeout long enough to show images
        cv2.imshow('taking your pictures',frame)
        if i%5==0 and i<=MAX_TAKING_OF_PHOTOS_TRAIN and i!=0:
            cv2.imwrite('faces/train/'+name+'/'+str(i)+'.png',frame)
        elif i%5==0 and i>MAX_TAKING_OF_PHOTOS_VAL:
            cv2.imwrite('faces/val/'+name+'/'+str(i)+'.png',frame)
        i+=1
            
        if cv2.waitKey(1)==ESCAPE_KEY:  #Escape Key
            break

    cv2.destroyAllWindows()
    cap.release()
    print('Successfully taken your photos...')




#### Below part is just training the model with the newly added face. Here we are creating model.
ckpt_path = 'xception_cl_fus_aspp_imp1k_10kl-3cc0.1mse-5nss5bc_bs4_ep30_valloss-2.5774_full.h5'
embedding_model = load_model(ckpt_path, custom_objects={"K": backend})
print('Embedding Model Loaded')

# making a a mtcnn instance for detecting faces
detector = MTCNN()

def find_face(img,img_size=(160,160)):
    img = cv2.imread(img)
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
        return face
    return None


def embed(face):
    face = face.astype('float32')
    fm,fs = face.mean(),face.std()
    face = (face-fm)/fs # standardizing the data 
    face = np.expand_dims(face,axis=0) # flattening it
    embs = embedding_model.predict(face)
    return embs[0]



def load_dataset(path):
    FACE_EMBEDINGS= []
    names_our_users = []
    for people in os.listdir(path):
        for people_images in os.listdir(path+people):
            face = find_face(path+people+'/'+people_images)
            if face is None:continue
            emb = embed(face)
            FACE_EMBEDINGS.append(emb)
            names_our_users.append(people)
        print('Loaded {} images of {}'.format(len(os.listdir(path+'/'+people)),people)) 
    return np.asarray(FACE_EMBEDINGS),np.asarray(names_our_users)



########### Loading training and testing data using functions defined above #############
print('Loading train data...')
FACE_EMBEDINGS_train, names_our_users_train = load_dataset('faces/train/')

print(f"First trains data_set are: {FACE_EMBEDINGS_train} and Second trains data_set are: {names_our_users_train}")

print('Loading test data...')
FACE_EMBEDINGS_test, names_our_users_test = load_dataset('faces/val/')


# l2 normalizing the data
l2_normalizer = Normalizer('l2')

X_train = l2_normalizer.transform(FACE_EMBEDINGS_train)
X_test  = l2_normalizer.transform(FACE_EMBEDINGS_test)

#label encoding the y data
label_enc = LabelEncoder()
y_train = label_enc.fit_transform(names_our_users_train)
y_test = label_enc.transform(names_our_users_test)


############ Training SVC (Support Vector Classifier) for predicting faces ########
# svc = SVC(kernel='linear',probability=True)
# svc.fit(X_train,y_train)

rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)

joblib.dump(rfc,'models/face_prediction_model.sav')
print()

print('Random Forest Model saved successfully!!')
