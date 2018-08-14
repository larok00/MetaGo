import django
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MetaGo_website.settings")
django.setup()

from MetaGo.models import Employee

def barcode_to_product_dict(barcode=None):
    f = open("food_registry.txt", 'r')
    file_str = f.read()
    file_json = json.loads(file_str)
    f.close()
    return file_json[barcode]


def barcode_to_product_name(barcode=None):
    return barcode_to_product_dict(barcode=barcode)["name"]

"""
Example use (both lines do the same thing):

print(barcode_to_product_dict(barcode="51000001")["name"])
print(barcode_to_product_name(barcode="51000001"))
"""


def get_debt(person_id=None):
    debt = Employee.objects.get(person_id=person_id).debt
    return debt


def change_debt(person_id=None, person_balance=None):
    e = Employee.objects.get(person_id=person_id)
    e.debt = person_balance
    e.save()


def update(barcode=None, person_id=None):
    price = barcode_to_product_dict(barcode=barcode)["price"]
    debt = get_debt(person_id=person_id)
    change_debt(person_id=person_id, person_balance=debt+price)
