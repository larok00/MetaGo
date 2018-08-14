import openfoodfacts

#brands = openfoodfacts.facets.get_brands()
#codes = openfoodfacts.facets.get_packaging_codes()
#print(codes)

#status_code = openfoodfacts.products.upload_image(None, "front", "20180808_120011.jpg")
product = openfoodfacts.products.get_product('51000001')
print(product)

