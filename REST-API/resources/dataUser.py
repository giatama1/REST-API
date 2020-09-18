from flask import jsonify, Blueprint
from flask_restful import Resource, Api, abort, reqparse

import models

# Melakukan request penginputan data yang diperlukan ketika user ingin meng-input data user yang baru
dataUser_post_args = reqparse.RequestParser() 
dataUser_post_args.add_argument("nama_user", 
                                type=str, 
                                help="Nama pengguna harus di isi", 
                                required=True, 
                                location= ['form','json'])
dataUser_post_args.add_argument("alamat_user", 
                                type=str, 
                                help="Alamat pengguna harus di isi", 
                                required=True, 
                                location= ['form','json'])
dataUser_post_args.add_argument("noHp_user", 
                                type=str, 
                                help="Nomor handphone pengguna harus di isi", 
                                required=True, 
                                location= ['form','json'])
dataUser_post_args.add_argument("email_user", 
                                type=str, 
                                help="Email pengguna harus di isi", 
                                required=True, 
                                location= ['form','json'])

# Melakukan request penginputan data yang diperlukan ketika user ingin meng-update data user 
dataUser_update_args = reqparse.RequestParser()
dataUser_update_args.add_argument("nama_user", type=str, help="Nama pengguna harus di isi")
dataUser_update_args.add_argument("alamat_user", type=str, help="Alamat pengguna harus di isi")
dataUser_update_args.add_argument("noHp_user", type=str, help="Nomor Handphone pengguna harus di isi")
dataUser_update_args.add_argument("email_user", type=str, help="Email pengguna harus di isi")

#resource_fields = {
#	'rowid': fields.Integer,
#	'nama_user': fields.String,
#	'alamat_user': fields.String,
#	'noHp_user': fields.String,
#   'alamat_user':fields.String
#}

# Kelas yang berisi method-method yang dijalankan tanpa menggunakan paramater. ex:id,username,dll.
class DataUserList(Resource):  
    def get(self): # Method GET yang berfungsi untuk membaca data
        data_user = {}
        query = models.Data_user.select()
        for row in query:
            data_user[row.rowid] = {'nama_user' : row.nama_user,
                                    'alamat_user' : row.alamat_user,
                                    'noHp_user' : row.noHp_user,
                                    'email_user' : row.email_user}
        return jsonify({'data_user':data_user})

    def post(self): # Method POST yang berfungsi untuk meng-input data
        args = dataUser_post_args.parse_args()
        models.Data_user.create(**args)
        return jsonify({'Success':True})
    
    #def put(self):
    #    args = dataUser_update_args.parse_args()
    #    models.Data_user.create(**args)
    #    return jsonify({'Success':True})


# Kelas yang berisi method-method yang dijalankan menggunakan paramater. ex:id,username,dll.
class DataUser(Resource):
    def get(self,user_id):  # Method GET yang berfungsi untuk membaca data menggunakan parameter ID.
        #Ambil data dari database
        data_user = {}
        query = models.Data_user.select()
        resultQuery = query.filter(rowid=user_id)
        
        if not resultQuery:
            abort(404, message="Cannot find data user with that id")
        else:
            for row in resultQuery:
                data_user[row.rowid] = {'nama_user' : row.nama_user,
                                        'alamat_user' : row.alamat_user,
                                        'noHp_user' : row.noHp_user,
                                        'email_user' : row.email_user}
            return jsonify({'data_user':data_user})
        
    def delete(self, user_id):  # Method DELETE yang berfungsi untuk menghapus data menggunakan parameter ID.
        data_user = {}
        query = models.Data_user.select()
        resultQuery = query.filter(rowid=user_id)
        
        if not resultQuery:
            abort(404, message="Cannot find data user with that id")
        else:
            models.Data_user.delete_by_id(user_id)
            return jsonify({'Succes':True})


dataUser_api = Blueprint('resources.dataUser', __name__)
api = Api(dataUser_api)

api.add_resource(DataUserList, '/data_user', endpoint='data_user') # Mendefinisikan URL untuk di akses oleh CLIENT
api.add_resource(DataUser, '/data_user/<int:user_id>', endpoint='DataUser') # Mendefinisikan URL untuk di akses oleh CLIENT berdasarkan parameter pencarian 
