import face_recognition
import pickle
import os

DATABASE_NAME="employee_database.pkl"
KNOWN_DATABASE=[]
ID_KEY="ID"
ENCODING_KEY="ENCODING"
unknown_images_path = os.path.join(os.getcwd(), "unknown_images")

class Person:
    def __init__(self, person_id, encoding, first=None, last=None):
        self.person_id=person_id
        self.first=first
        self.last=last
        self.encoding=encoding


def load_training_images():
    global unknown_images_path
    training_images_names=os.listdir(unknown_images_path)
    unknown_images_paths = [os.path.join(unknown_images_path, file_) for file_ in training_images_names]
    return unknown_images_paths


def load_emplydb(DATABASE_NAME):
    global KNOWN_DATABASE
    databasepkl=open(DATABASE_NAME, "rb")
    KNOWN_DATABASE=pickle.load(databasepkl)
    databasepkl.close()


def find_matches(image):
    global KNOWN_DATABASE
    matches=[]
    image_data=face_recognition.load_image_file(image)
    unknown_encoding=face_recognition.face_encodings(image_data)
    for encoding in unknown_encoding:
        for known_data in KNOWN_DATABASE:
            results = face_recognition.compare_faces([known_data[ENCODING_KEY]], encoding)
            matches.append([known_data[ID_KEY], results])
    return matches


if __name__=="__main__":
    unknown_images_path_list=load_training_images()
    load_emplydb(DATABASE_NAME)
    for image in unknown_images_path_list:
        matches=find_matches(image)
        print(image, matches)





