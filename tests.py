from unittest import TestCase, main as unittest_main, mock
from flask import Flask
from app import app
from bson.objectid import ObjectId

sample_sneaker_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_sneaker = {
    'title': 'Sneaker',
    'image': 'https://wwws.dior.com/couture/ecommerce/media/catalog/product/cache/1/cover_image_mobile_2/715x773/17f82f742ffe127f42dca9de82fb58b1/U/0/1557402302_3SH118YQC_H563_E02_GHC.jpg',
    'price': "$300"
}
sample_form_data = {
    'title': sample_sneaker['title'],
    'image': sample_sneaker['image'],
    'price': sample_sneaker['price']
}

if __name__ == '__main__':
    unittest_main()
