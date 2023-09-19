# Muhammad Azmi Falah - 2206082285 - PBP B

**Tautan _Adaptable_**: [Azmuh Global](https://azmuhglobal.adaptable.app/main/)

## Tugas 3:


### Apa perbedaan antara form `POST` dan `form` GET dalam Django?

- Form `POST`: Metode `POST` digunakan untuk mengirim data form ke server sebagai bagian dari body permintaan HTTP. Data yang dikirim dengan metode `POST` tidak terlihat dalam URL dan dienkripsi saat dikirimkan. Metode `POST` umumnya digunakan ketika kita ingin mengirim data yang sensitif atau ketika kita ingin melakukan operasi yang mempengaruhi perubahan pada server, seperti membuat, mengubah, atau menghapus data.

- Form `GET`: Metode `GET` digunakan untuk mengirim data form ke server sebagai parameter yang ditambahkan ke URL. Data yang dikirim dengan metode `GET` terlihat dalam URL dan tidak dienkripsi. Metode `GET` umumnya digunakan ketika kita ingin mengambil data dari server tanpa melakukan perubahan pada server, seperti saat melakukan pencarian atau menampilkan halaman yang hanya menampilkan data.

Jadi, perbedaan utama antara form `POST` dan form `GET` adalah:

- **Tujuan Penggunaan**: Form `POST` digunakan untuk mengirim data yang mempengaruhi perubahan pada server, sementara form `GET` digunakan untuk mengambil data dari server tanpa mempengaruhi perubahan pada server.

- **Pengiriman Data**: Data yang dikirim dengan form `POST` tidak terlihat dalam URL dan dienkripsi, sedangkan data yang dikirim dengan form `GET` terlihat dalam URL dan tidak dienkripsi.


### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- **XML (Estensible Markup Language)**: XML, yang merupakan singkatan dari Extensible Markup Language, memiliki desain yang bertujuan agar dapat menjelaskan dirinya sendiri. Dengan membaca XML, kita dapat dengan jelas memahami informasi yang terkandung dalam data tersebut. XML sering digunakan dalam berbagai aplikasi web dan mobile untuk tujuan penyimpanan dan pengiriman data. Dalam XML, data disusun dengan cara ditempatkan dalam elemen-elemen yang diapit oleh _tag_. Untuk berinteraksi dengan data dalam XML, diperlukan penulisan program yang khusus dirancang untuk mengirim, menerima, menyimpan, atau menampilkan informasi yang terkandung dalam format XML.

- **JSON (JavaScript Object Notaioon)**: JSON, yang merupakan singkatan dari JavaScript Object Notation, memiliki desain yang bertujuan agar formatnya dapat secara jelas menjelaskan data yang berisi. JSON sangat mudah dimengerti dan sering digunakan dalam berbagai aplikasi web dan mobile untuk keperluan penyimpanan dan pengiriman data. Sintaks JSON mirip dengan struktur objek dalam bahasa pemrograman JavaScript. Namun, yang membedakan JSON adalah bahwa data dalam format ini disusun dalam bentuk teks, sehingga banyak tersedia kode dalam berbagai bahasa pemrograman yang memungkinkan pembacaan dan pembuatan data dalam format JSON.

- **HTML (Hypertext Markup Language)**: HTML, yang merupakatan singkatan dari Hypertext Markup Language, merupakan bahasa markup yang digunakan untuk menciptakan halaman web yang dapat ditampilkan di browser. Dengan menggunakan tag-tag atau elemen-elemen khusus, HTML memungkinkan pengembang web untuk menandai berbagai jenis konten seperti teks, gambar, tautan, dan elemen lainnya, serta mengontrol tampilan dan struktur halaman web. Dalam HTML, informasi diatur dalam hierarki dengan penggunaan tag dan atribut, yang menjelaskan cara kontennya harus ditampilkan dan berinteraksi di browser. Kemudahan interpretasi dan rendering oleh browser membuat HTML menjadi bahasa utama untuk menyampaikan konten di web dan merupakan dasar dari banyak situs web yang ada saat ini.

Perbedaan utama antara ketiganya terletak pada tujuan dan sintaks yang digunakan. XML dan JSON digunakan untuk data yang memiliki struktur terstruktur, sementara HTML digunakan untuk membuat tampilan halaman web. XML memiliki sintaks yang kompleks, JSON memiliki sintaks yang lebih sederhana, dan HTML memiliki sintaks yang khusus untuk tampilan konten di browser.


### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON (JavaScript Object Notation) adalah format data yang sering digunakan dalam pertukaran data di aplikasi web modern. Berikut adalah beberapa alasan utama mengapa JSON begitu populer:

1. **Kesederhanaan Sintaksis:** JSON memiliki struktur yang sederhana dan mudah dimengerti, membuatnya sangat user-friendly bagi pengembang. Sintaksis JSON dirancang untuk mudah dibaca dan ditulis.

2. **Ringan:** JSON memiliki ukuran yang ringan, sehingga dapat dengan cepat ditransmisikan melalui jaringan. Kecepatan dan kinerja adalah aspek penting dalam aplikasi web, dan JSON memenuhi kebutuhan ini.

3. **Kompatibilitas Lintas Bahasa:** JSON dapat digunakan dengan berbagai bahasa pemrograman, termasuk JavaScript, Python, PHP, dan Ruby. Ini membuatnya sangat fleksibel dan dapat digunakan dalam berbagai konteks.

4. **Mudah Diparsing:** JSON dapat dengan mudah diparsing, memungkinkan data untuk dengan cepat diubah menjadi struktur yang dapat diproses oleh program. Ini sangat penting untuk aplikasi web yang harus bekerja dengan sejumlah besar data dengan efisien.

5. **Kemudahan dalam Membaca:** JSON adalah format yang mudah dibaca, memudahkan pemahaman bagi pengembang dan pihak terkait lainnya. Kemudahan ini juga membantu dalam proses debugging dan troubleshooting aplikasi web yang menggunakan JSON.

Secara keseluruhan, JSON sering digunakan dalam pertukaran data di aplikasi web modern karena kesederhanaan, ringannya, kompatibilitas lintas bahasa, kemudahan parsing, dan mudah dibaca, semua faktor ini menjadikannya pilihan yang kuat untuk pertukaran data yang efisien dalam ekosistem web.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

- Menjalankan virtual environment
- Mengubah _path_ `main/` menjadi ` ` pada `urlpatterns` pada file `urls.py` dalam folder `AzmuhGlobal`
- Membuat file `base.html` sebagai kerangka umum untuk halaman web pada folder `AzmuhGlobal/templates`
- Menyesusaikan kode pada `settings.py` agar file `base.html` dapat terdeteksi
- Menyesusaikan kode pada `main.html` yang ada pada folder `main/templates`
- Membuat file `forms.py` sebagai struktur _form_ yang dapat menerima data item baru
- Menyesuaikan kode pada `views.py` dengan menambahkan beberapa import, membuat fungsi `create_item`, dan mengubah isi dari fungsi `show_main`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import fungsi `create_item` dan menambahkan path url-nya ke dalam `urlpatterns`
- Membuat file `create_item` pada folder `main/templates`
- Menyesuaikan kode pada `main.html` untuk menampilkan data item derta tombol _Add New Item_ dengan menambahkan kode pada `{% block content %}`
- Menyesuaikan kode pada `views.py` dengan menambahkan beberapa import dan membuat fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` dan mebambahkan path url keempat fungsi tersebut ke dalam `urlpatterns`

1. **HTML**
<img src= '/assets/postman_html.png'>

2. **XML**
<img src= '/assets/postman_xml.png'>

3. **JSON**
<img src= '/assets/postman_json.png'>

4. **XML by ID**
<img src= '/assets/postman_xml-by-id.png'>

5. **JSON by ID**
<img src= '/assets/postman_json-by-id.png'>


## Tugas 2:


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