'''
A dummy db storaing faces in memory
Feel free to make it fancier like hooking with postgres or whatever
This model here is just for simple demo app under apps
Don't use it for production.
'''
from utils.utils_insightface import compare_faces
import numpy as np


class Model(object):

    
    def add_face(self, face_img, face_description,name):
        self.faces.append(face_img)
        self.faces_discriptions.append(face_description)
        self.faces_names.append(name)

    def load_database(model_name):
        print("[LOG] Loading Encoded faces ...")
        file = np.load('data/encodings/encoding_'+model_name+'.npz')
        known_face_encodings=file["encodings"]
        known_face_names = file["names"]
        database={"names":known_face_names,"encodings":known_face_encodings}
        return database
    
    def drop_all(self):
        self.faces = []
        self.faces_discriptions = []

    def get_all(self):
        return self.faces, self.faces_discriptions

    def get_similar_faces(self, face_description):
        print('[Face DB] Looking for similar faces in a DataBase of {} faces...'.format(len(self.faces)))
        if len(self.faces) == 0:
            return []
        # Use items in Python 3*, below is by default for Python 2*
        similar_face_idx = compare_faces(self.faces_discriptions, face_description)
        similar_faces = np.array(self.faces)[similar_face_idx]
        num_similar_faces = len(similar_faces)
        print('[Face DB] Found {} similar faces in a DataBase of {} faces...'.format(num_similar_faces, len(self.faces)))
        return similar_faces