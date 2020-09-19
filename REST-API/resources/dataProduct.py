from flask import Flask, Blueprint, jsonify
from flask_restful import Resource, Api, abort, reqparse

import models
import datetime

# Post new products
dataProduct_post_args = reqparse.RequestParser()
dataProduct_post_args.add_argument("product_name",
                                   type=str,
                                   help="nama produk harus diisi",
                                   required=True, location=['form', 'json'])
dataProduct_post_args.add_argument("product_description",
                                   type=str,
                                   help="deskripsi produk harus diisi",
                                   required=True, location=['form', 'json'])
dataProduct_post_args.add_argument("product_price",
                                   type=str,
                                   help="harga produk harus diisi",
                                   required=True, location=['form', 'json'])
dataProduct_post_args.add_argument("product_image_url",
                                   type=str,
                                   help="deskripsi produk harus diisi",
                                   required=True, location=['form', 'json'])
dataProduct_post_args.add_argument("user_id",
                                   type=str,
                                   required=True, location=['form', 'json'])


class DataProduct(Resource):
    def get(self):
        data_product = {}
        query = models.Data_product.select().join(models.Data_user)
        print(query)
        for row in query:
            data_product[row.row_id] = {
                'product_name': row.product_name,
                'product_description': row.product_description,
                'product_price': row.product_price,
                'product_image': row.product_image_url,
                'users': {
                    'nama': str(lambda: (models.Data_user.select(models.Data_user.nama_lengkap_user).where(models.Data_user.rowid == row.user_id))),
                    'alamat': str(lambda: models.Data_user.select(models.Data_user.alamat_user).where(models.Data_user.rowid == row.user_id))
                }
            }

        return jsonify({'status': 200, 'data': data_product})

    def post(self):
        datenow = datetime.datetime.now()
        product_code = "A001"
        args = dataProduct_post_args.parse_args()
        product_name = args["product_name"]
        product_description = args["product_description"]
        product_price = int(args["product_price"])
        product_image_url = args["product_image_url"]
        user_id = int(args["user_id"])
        product_id = product_code
        new_product_data = {
            "product_id": product_id,
            "product_name": product_name,
            "product_description": product_description,
            "product_price": product_price,
            "product_image_url": product_image_url,
            "user_id": user_id
        }
        models.Data_product.create(**new_product_data)
        return jsonify({'Success': True, 'Status': 200})


dataProduct_api = Blueprint('resources.dataProduct', __name__)
api = Api(dataProduct_api)

api.add_resource(DataProduct, '/product',
                 endpoint='data_product')
