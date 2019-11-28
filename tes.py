from function import DBManager
import requests
import json

info = requests.get('http://3.227.193.57:8000/users/all')
# DBManager.add_account(info.json())
print(DBManager.get_account())
# dict = {'nim': '18217041', 'email': '182@gmail.com', 'password': 'test', 'nama': 'wealthtan',
#         'no_telepon': '081234567890', 'usia': 20, 'jurusan': 'STI', 'semester': 5,
#         'gpa': 3.8, 'pendapatan': 99999999, 'berkas': 'lengkap', 'username': 'wealth'}
# info = json.dumps(dict)
# print(DBManager.inserttoMahasiswa(info))
