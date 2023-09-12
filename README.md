# Nama    : Muhammad Azmi Falah
## NPM     : 2206082285
## Kelas   : PBP-B

**Tautan _Adaptable_**: [Azmuh Global](https://azmuhglobal.adaptable.app/main/)

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

- Membuat direktori baru bernama AzmuhGlobal
- Membuat virtual environment dengan command: `python3 -m venv env`
- Mengaktifkan virtual environment dengan command: `source env/bin/activate`
- Membuat file `requirements.txt` dan menambahkan beberapa dependencies berikut:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
- Memasang dependencies dengan command: `pip install -r requirements.txt`
- Membuat proyek Django AzmuhGlobal dengan command: `django-admin startproject AzmuhGlobal .`
- Mengubah variabel `ALLOWED_HOSTS` pada `settings.py` agar dapat diakses oleh semua host seperti berikut:`ALLOWED_HOSTS = ["*"]`
- Membuat aplikasi `main` dalam proyek AzmuhGlobal dengan command: `python3 manage.py startapp main`
- Mendaftarkan aplikasi main ke dalam proyek AzmuhGlobal dengan mengubah variabel `INSTALLED_APPS` pada `settings.py` seperti berikut: `INSTALLED_APPS = [...,'main',...]`
- Membuat file `main.html` dalam direktori `templates` dalam direktori `main` dengan contoh seperti yang sudah saya terapkan dalam file `main.html`
- Mengubah isi file `models.py` dengan membuat dengan nama Item serta memiliki atribut `name`, `amount`, dan `description`
- Membuat migrasi model dengan command: `python3 manage.py makemigrations`
- Menerapkan migrasi model dengan command: `python3 manage.py migrate`
- Mengimport `render` dan menambahkan fungsi `show_main` pada `views.py` dengan contoh seperti yang sudah saya terapkan dalam file `views.py`
- Membuat routing pada `urls.py` pada aplikasi `main` dengan mengisi file `urls.py` dalam direktori `main` dengan contoh seperti yang sudah saya terapkan dalam file `urls.py`
- Membuat routing pada `urls.py` pada direktori `AzmuhGlobal` dengan mengimpor fungsi `include` dari `django.urls` dan mengubah variabel `urlpatterns` seperti berikut: `urlpatterns = [...,path('main/', include('main.urls')),...]`
- Menonaktifkan virtual environment dengan command: `deactivate`
- Membuat file `.gitignore` untuk menentukan file dan direktori yang harus diabaikan oleh Git
- Membuat repositori github baru bernama AzmuhGlobal
- Menginisiasi repositori baru dengan command: `git init`
- Mengonfigurasikan nama pengguna dan email git dengan command: `git config user.name "myusername"` dan `git config user.email "myemail@email.com"`
- Membuat branch utama bernama main dengan command: `git branch -M main`
- Menghubungkan direktori lokal dengan repositori github dengan command: `git remote add origin https://github.com/azmifal/AzmuhGlobal.git`
- Menambahkan perubahan-perubahan yang dilakukan untuk dipush ke repositori github dengan command: `git add .`
- Memberikan comment pada perubahan-perubahan tersebut dengan command: `git commit -m "mycomment"`
- Melakukan push ke repositori github dengan command: `git push origin -u origin main`
- Melakukan deployment pada adaptable.io dengan menghubungkan repositori github AzmuhGlobal
- Memilih Python App Template dan PostGreSQL sebagai template dan basis data yang digunakan
- Menambahkan perintah berikut pada bagian Start Command: `python manage.py migrate && gunicorn AzmuhGlobal.wsgi`
- Mencentang bagian HTTP Listener on PORT
- Selesai deploying dan link adaptable sudah dapat diakses


### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

<img src='/assets/BaganTugas2.png'>


### Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?

Virtual environment merupakan tools yang dapat digunakan dalam pengembangan perangkat lunak Python, termasuk aplikasi web berbasis Django. Program python yang kita berjalan dalam virtualenv memiliki modul-modulnya sendiri dan tidak dapat diakses oleh program dari luar. Dengan virtualenv, kita dapat memiliki program python yang berbeda untuk setiap proyek atau aplikasi yang kita buat. Misal, kita memiliki proyek Django yang berjalan pada Django versi 1.1 dan proyek lain yang memerlukan Django versi 4.0. Melalui virtualenv, setiap proyek yang kita buat akan memiliki versi Django yang sesuai dan tidak bentrok antar proyeknya.

Sebenernya, kita dapat saja membuat aplikasi web berbasis Django tanpa menggunakan virtualenv, tetapi praktik ini kurang dianjurkan. Penggunaan virtualenv sangat berguna untuk mengisolasi package dan dependensi dari sebuah aplikasi serta mencegah konflik dengan versi lain dari proyek-proyek yang kita miliki.


### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC, yang merupakan singkatan dari Model-View-Controller, merupakan konsep arsitektur yang digunakan dalam pengembangan perangkat lunak. Dalam arsitektur MVC, aplikasi dibagi menjadi tiga komponen utama. Pertama, Model, yang bertanggung jawab untuk mengelola data dan logika aplikasi. Kedua, View, yang menampilkan informasi kepada pengguna. Dan yang ketiga, Controller, yang mengatur interaksi antara Model dan View. Konsep ini memungkinkan pemisahan yang jelas antara logika aplikasi, tampilan, dan pengaturan interaksi, sehingga memudahkan pengembangan, pemeliharaan, dan pengujian aplikasi.

MVT, yang merupakan singkatan dari Model-View-Template, adalah konsep arsitektur yang digunakan dalam pengembangan web. Dalam arsitektur MVT, aplikasi dibagi menjadi tiga komponen utama. Pertama, Model, yang bertanggung jawab untuk mengelola data dan logika aplikasi. Kedua, View, yang menampilkan informasi kepada pengguna. Dan yang terakhir, Template, yang merupakan bagian yang mengatur tampilan dan struktur halaman web secara terpisah dari logika aplikasi. Tujuan dari konsep ini adalah untuk memisahkan komponen-komponen utama dalam sebuah aplikasi web. Hal ini membantu pengembang web dalam mengatur dan mengelola kode dengan lebih terstruktur dan terorganisir.

MVVM, yang merupakan singkatan dari Model-View-ViewModel, merupakah sebuah konsep arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis user interface (UI). Dalam MVVM, Model mirip dengan konsep Model dalam MVC dan MVT, yang bertanggung jawab untuk mengelola data dan logika aplikasi. View adalah representasi visual dari antarmuka pengguna atau user interface, tetapi perbedaannya terletak pada ViewModel, yang berperan sebagai perantara antara Model dan View. ViewModel bertanggung jawab untuk mengelola logika tampilan dan menyediakan data yang akan ditampilkan di View. Hal ini memungkinkan pemisahan yang kuat antara tampilan dan logika aplikasi, serta memfasilitasi pengembangan antarmuka pengguna yang lebih dinamis.

MVC, MVT, dan MVVM adalah tiga konsep arsitektur yang berbeda dalam pengembangan perangkat lunak. MVC memisahkan aplikasi menjadi tiga komponen utama, yaitu Model (data dan logika aplikasi), View (tampilan pengguna), dan Controller (pengendali aksi). MVT, yang digunakan dalam kerangka kerja Django, mirip dengan MVC, tetapi mengganti Controller dengan Template untuk tampilan yang lebih dinamis. MVVM, di sisi lain, memisahkan aplikasi menjadi Model, View, dan ViewModel sebagai penghubung antara Model dan View. MVVM memungkinkan pengembangan antarmuka pengguna yang lebih reaktif. Jadi, perbedaan utamanya terdapat pada bagaimana komponen-komponen tersebut berinteraksi dan dipisahkan dalam struktur aplikasi.