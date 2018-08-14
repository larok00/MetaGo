from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import face_recognition
import pickle

def face_test(image):
    image_data=face_recognition.load_image_file(image)
    face_encoding=face_recognition.face_encodings(image_data)
    pickle.dump(face_encoding,open("test.pkl", "wb"))     
    return face_encoding

def index(request):
    context = {}
    return render(request, 'MetaGo/index.html', context)

def photo_id(request):
    if request.method == "POST":
        return face_test(request.POST["img"])
    else:
        return HttpResponseRedirect(reverse('MetaGo:index'))
