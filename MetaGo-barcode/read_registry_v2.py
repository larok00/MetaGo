import json


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