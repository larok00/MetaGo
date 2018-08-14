import csv
import sys
import pickle

import face_recognition
import os


class User:
    def __init__(self, inits, first, last, person_id, encoding):
        self.initials = inits
        self.first = first
        self.last = last
        self.person_id = person_id
        self.encoding = encoding


def save_all_images():
    csv.field_size_limit(sys.maxsize)
    users = []
    with open(os.path.join('resources', 'raw_employees.csv'), 'r') as inf:
        freader = csv.DictReader(inf,
                                 fieldnames=['payroll', 'initials', 'title', 'known_as', 'first_name', 'middle_initial',
                                             'last_name', 'bu_id', 'unit', 'photo', 'person_id'])
        for row in freader:
            if row['photo']:
                path = os.path.join('resources','directory',row['initials'] + '.jpg')
                with open(path, 'wb') as ouf:
                    ouf.write(eval(row['photo']))
                print("Calculating encoding for " + row['initials'])
                fr_image = face_recognition.load_image_file(path)
                encoding = face_recognition.face_encodings(fr_image)
                users.append(User(row['initials'],row['known_as'],row['last_name'],row['person_id'],encoding))


def calc_first_order_distances():
    with open(os.path.join('resources', 'users.pickle'), 'rb') as inf:
        users = pickle.load(inf)
    distances = {}
    for user in users:
        u_dists = face_recognition.face_distance([u.encoding for u in users], user.encoding)
        distances[user.initials] = {other.initials: u_dists[i] for i, other in enumerate(users)}

    return distances

import csv
import sys
import pickle

import face_recognition
import os


class User:
    def __init__(self, inits, first, last, person_id, encoding):
        self.initials = inits
        self.first = first
        self.last = last
        self.person_id = person_id
        self.encoding = encoding


def save_all_images():
    csv.field_size_limit(sys.maxsize)
    users = []
    with open(os.path.join('resources', 'raw_employees.csv'), 'r') as inf:
        freader = csv.DictReader(inf,
                                 fieldnames=['payroll', 'initials', 'title', 'known_as', 'first_name', 'middle_initial',
                                             'last_name', 'bu_id', 'unit', 'photo', 'person_id'])
        for row in freader:
            if row['photo']:
                path = os.path.join('resources','directory',row['initials'] + '.jpg')
                with open(path, 'wb') as ouf:
                    ouf.write(eval(row['photo']))
                print("Calculating encoding for " + row['initials'])
                fr_image = face_recognition.load_image_file(path)
                encoding = face_recognition.face_encodings(fr_image)
                users.append(User(row['initials'],row['known_as'],row['last_name'],row['person_id'],encoding))


def calc_first_order_distances():
    with open(os.path.join('resources', 'users.pickle'), 'rb') as inf:
        users = pickle.load(inf)
    distances = {}
    for user in users:
        u_dists = face_recognition.face_distance([u.encoding for u in users], user.encoding)
        distances[user.initials] = {other.initials: u_dists[i] for i, other in enumerate(users)}

    return distances
