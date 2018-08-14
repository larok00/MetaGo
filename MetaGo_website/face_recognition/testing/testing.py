import face_recognition
import os


class Person:
    def __init__(self, person_id, first=None, Last=None, encoding):
        self.person_id=person_id
        self.first=first
        self.second=second
        self.encoding=encoding

# Create list with all file paths
unknown_images_path = os.path.join(os.getcwd(), "unknown_images")
known_images_path = os.path.join(os.getcwd(), "known_images")

known_images_names=os.listdir(known_images_path)
print(known_images_names)
known_images_paths = [os.path.join(known_images_path, file_) for file_ in known_images_names]
print(known_images_paths)
training_images_names=os.listdir(unknown_images_path)
unknown_images_paths = [os.path.join(unknown_images_path, file_) for file_ in training_images_names]
print(unknown_images_paths)


#Train the api with known images
kn=[]
for known_image in known_images_paths:
    # Load a sample picture and learn how to recognize it.
    image_data = face_recognition.load_image_file(known_image)
    print("Face data:", image_data)
    face_encoding = face_recognition.face_encodings(image_data)[0]
    print("Encoding:", face_encoding)
    known_encodings.append(face_encoding)


# Load unknown images and compare to known database
data_to_print=[]
print(unknown_images_paths)
for unknown_image in unknown_images_paths:
    print(unknown_image)
    image_data=face_recognition.load_image_file(unknown_image)
    print("unknown image:", image_data)
    unknown_encoding=face_recognition.face_encodings(image_data)[0]
    print("unknown encoding:", unknown_encoding)
    for index, known_encoding in enumerate(known_encodings):
        print("known encoding: ", known_encoding)
        results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        if results:
            print(results)
        data_to_print.append([unknown_image, results])

print(data_to_print)









