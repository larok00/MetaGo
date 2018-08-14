
import face_recognition
import pickle
import django
import os

os.chdir("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MetaGo_website.settings")
django.setup()
os.chdir("MetaGo")
from MetaGo.models import Employee

HOST_KEY="HOST"
USER_KEY="USER"
PORT_KEY="PORT"
PASSWORD_KEY="PASSWORD"
DATBASE_KEY="DATABASE"
ID_KEY="ID"
ENCODING_KEY="ENCODING"
root_directory=os.getcwd()
PERSONEL_INFO_FILE_NAME="data_dictionary.pkl"
known_images_path = os.path.join(os.getcwd(), "known_images")



class Person:
    def __init__(self, person_id, encoding, first=None, last=None):
        self.person_id=person_id
        self.first=first
        self.last=last
        self.encoding=encoding

def load_personel_data():
    return pickle.load(open(PERSONEL_INFO_FILE_NAME))

def collect_filepaths():
    global known_images_path
    # Create list with all file paths
    known_images_names=os.listdir(known_images_path)
    print("images names: ", known_images_names)
    known_images_paths = [os.path.join(known_images_path, file_) for file_ in known_images_names]
    print("images paths: ", known_images_paths)
    known_images=[[filename, file_path] for filename, file_path in zip(known_images_names, known_images_paths)]
    print("list that will be traversed: ", known_images)
    return known_images


def populate_database(known_images):
    global root_directory
    known_database=[]
    #Train the api with known images
    for known_image in known_images:
        # Load a sample picture and learn how to recognize it.
        image_data = face_recognition.load_image_file(known_image[1])
        face_encoding = face_recognition.face_encodings(image_data)[0]
        person={}
        person[ID_KEY]=known_image[0]
        person[ENCODING_KEY]=face_encoding
        Employee_info = Employee(person_id=person[ID_KEY], face_encoding=person[ENCODING_KEY])
        known_database.append(person)
    print(person)

if __name__=="__main__":
    print(load_personel_data)
    known_images=collect_filepaths()
    populate_database(known_images)













