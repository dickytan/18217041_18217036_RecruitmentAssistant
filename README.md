# Tugas Besar Teknologi Sistem Terintegrasi

## Anggota
1. Dicky / 18217041
2. Johanes Antonius / 18217036

## API yang digunakan
1. To-do List API (Dicky 18217041)
2. LinkedIn API (Nicholaus DY 18217028)

## Apa itu Recruitment Assistant?
Aplikasi yang ditujukan untuk memudahkan recruiter dalam mendapatkan data calon pekerja seperti data nama, jabatan, daerah, jabatan, dan tempat kerja seseorang menggunakan API LinkedIn. Aplikasi ini juga memudahkan recruiter untuk mengelola daftar tugas yang harus dikerjakan dalam periode waktu tertentu selama proses pencarian calon pekerja seperti pengaturan jadwal komunikasi, tes psikologi, tes wawancara, dll.

## Mengapa menggunakan Recruitment Assistant?
Recruitment Assistant memudahkan pengguna (Human Resource) untuk mendapatkan data-data calon pekerja yang berpotensi untuk di-approach berdasarkan latar belakang edukasi atau domisili. Selain itu, aplikasi ini juga terintegrasi dengan fitur to-do List sehingga tugas-tugas selama proses pencarian calon pekerja dapat dikelola dengan baik oleh pengguna. Kedepannya, aplikasi ini dapat dikembangkan lebih lanjut sehingga fitur pencarian tidak hanya berdasarkan latar belakang edukasi dan domisili, melainkan pengguna (Human Resource) bisa mendapatkan suggested person berdasarkan riwayat pencarian orang sebelumnya dengan mengimplementasikan Recommender System (Artificial Intelligence) pada fitur pencariannya.

## Aplikasi Recruitment Assistant dapat diakses di sini: 
Recruitment Assistant: http://3.227.193.57:5001/

## Cara penggunaan aplikasi: 
1. Pada halaman utama, pengguna (Human Resource) dapat memilih scout people atau to-do list
   > scout people untuk mendapatkan data calon pekerja yang berpotensi untuk di-approach dan
   > to-do list untuk melihat daftar tugas pengguna
2. Jika pengguna memilih scout people, maka pengguna dapat memilih untuk mencari data calon pekerja berdasarkan region atau education
3. Setelah mendapatkan data calon pekerja menggunakan API LinkedIn, Human Resource dapat membuat tugas yang harus dilakukan terhadap orang yang ingin di-approach dengan mengisi data HR ID, to-do/task dan deadline to-do/task.
4. Setelah menambahkan daftar tugas, pengguna dapat melihat tugas yang baru ditambahkan dengan memilih menu TO DO pada header
5. Setelah menekan menu TO DO, pengguna dapat memilih untuk melihat daftar tugas HR1, HR2, dan HR3 (Asumsi: HR di perusahaan berjumlah 3 orang) // Jika pengguna adalah HR dengan nomor ID 1, maka daftar tugas pengguna tersebut terdapat di HR1
6. Setelah masuk ke daftar tugas, pengguna dapat melihat daftar tugas, menambah daftar tugas, mengupdate status tugas menjadi telah selesai, dan menghapus daftar tugas tertentu.

## Dokumentasi API dapat diakses di sini:
https://orange-water-4285.postman.co/collections/9500366-9af4e0f7-a337-44f8-8c7f-74ee1bf53984?version=latest&workspace=187e2795-93e3-4d51-8989-cb9833937da0#3c85eae8-d209-4ac4-8aea-505358cd9177

## Method API (file: endpoint.py dan function.py)
### To-do List API
|Method |Link  	                                                          |Deskripsi  	                                             |
|---	  |---	                                                             |---	                                                      |
|GET    |http://3.227.193.57:5000/task                                      |Mengembalikan seluruh daftar tugas                        |
|GET    |http://3.227.193.57:5000/task/hrid/<hr_id>                         |Mengembalikan daftar tugas berdasarkan ID HR              |
|GET    |http://3.227.193.57:5000/task/hrid/<hr_id>/uid/<user_id>           |Mengembalikan daftar tugas berdasarkan HR ID dan User ID  |
|POST   |http://3.227.193.57:5000/task/hrid/<hr_id>/uid/<user_id>           |Membuat daftar tugas berdasarkan HR ID dan User ID        |
|PUT    |http://3.227.193.57:5000/task/<task_id>/hrid/<hr_id>/uid/<user_id> |Mengubah daftar tugas berdasarkan Task ID, HR ID, User ID |
|DELETE |http://3.227.193.57:5000/task/<task_id>/uid/<user_id>              |Menghapus daftar tugas berdasarkan task ID, HR ID, User ID|

#### Contoh pemanggilan pada browser:
1. http://3.227.193.57:5000/task
2. http://3.227.193.57:5000/task/hrid/1
3. http://3.227.193.57:5000/task/hrid/1/uid/6b00ab158

### LinkedIn API
|Method |Link 	                                                             |Deskripsi  	                                             |
|---	  |---	                                                             |---	                                                      |
|GET    |http://3.227.193.57:5000/account                                   |Mengembalikan data calon pekerja (pengguna LinkedIn)      |
|GET    |http://3.227.193.57:5000/account/education/<education>             |Mengembalikan data calon pekerja dengan edukasi tertentu  |
|GET    |http://3.227.193.57:5000/account/region/<region>                   |Mengembalikan data calon pekerja dengan edukasi tertentu  |
|POST   |http://3.227.193.57:5000/account                                   |Melakukan request ke API LinkedIn          `              |

#### Contoh pemanggilan pada browser:
1. http://3.227.193.57:5000/account
2. http://3.227.193.57:5000/account/education/Institut%20Teknologi%20Bandung
3. http://3.227.193.57:5000/account/region/Jakarta

## Log
|Nama   	        |Aktivitas Commit   	                                      |Tanggal  	                |
|---	            |---	                                                      |---	                      |
|Dicky & Johanes  |Designed API integration                                   |12 November 2019          	|
|Dicky & Johanes  |Revised API integration Design                             |14 November 2019          	|
|Dicky   	        |Created remote repository (Github)                         |14 November 2019          	|
|Dicky   	        |Created local database (postgreSQL)                        |14 November 2019          	|
|Dicky   	        |Integrated API Todo with API LinkedIn                      |14 November 2019          	|
|Dicky   	        |Updated API's DELETE method                                |15 November 2019   	      |
|Dicky   	        |Updated API's PUT method                                   |24 November 2019    	      |
|Dicky   	        |Created API's documentation                                |24 November 2019  	        |
|Johanes          |Created Apps' Interface                    	              |27 November 2019         	|
|Johanes          |Created Logic for Apps' Interface (GET and POST method)    |27 November 2019         	|
|Dicky            |Deployed API to the testing environment                	  |28 November 2019         	|
|Johanes          |Created Logic for Apps' Interface (PUT and DELETE method)  |28 November 2019         	|
|Dicky & Johanes  |Tested back-end and front-end integration                 	|29 November 2019         	|
|Dicky            |Deployed App                   	                          |30 November 2019         	|
|Dicky            |Created Progress Report (README.md)                   	    |30 November 2019         	|
|Dicky            |Finalized Progress Report (README.md)                  	  |2  Desember 2019         	|
