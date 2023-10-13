# Muhammad Azmi Falah - 2206082285 - PBP B

**Tautan _Adaptable_**: [Azmuh Global](https://azmuhglobal.adaptable.app/main/)


----------
## Tugas 6

### Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.

_Asynchronous programming_ dan _synchronous programming_ adalah dua pendekatan yang berbeda dalam pemrograman. Berikut adalah perbedaan antara keduanya:

- **Asynchronous Programming** :
    - _Asynchronous programming_ adalah pendekatan pemrograman di mana tugas-tugas dapat dieksekusi secara independen tanpa harus menunggu tugas sebelumnya selesai.
    - Dalam _asynchronous programming_, tugas-tugas dapat dieksekusi secara bersamaan atau dalam urutan yang tidak terikat.
    - Proses eksekusi tugas dalam _asynchronous programming_ bersifat _non-blocking_, yang berarti tugas berikutnya dapat dimulai segera setelah tugas sebelumnya dimulai, tanpa harus menunggu tugas sebelumnya selesai.
    - _Asynchronous programming_ cocok untuk tugas yang kompleks, memerlukan waktu yang lama untuk dieksekusi, atau memerlukan akses ke sumber daya eksternal seperti jaringan atau database.

    Dalam _asynchronous programming_, umumnya digunakan konsep seperti _callback_, _promise_, _coroutine_, atau _async/await_ untuk mengelola tugas-tugas yang _asynchronou_. Ini memungkinkan pemrogram untuk menulis kode yang lebih efisien dan responsif, karena tugas-tugas yang memerlukan waktu lama dapat dieksekusi secara paralel atau di latar belakang tanpa menghentikan eksekusi tugas-tugas lainnya.

- **Synchronous Programming** :
    - _Synchronous programming_ adalah pendekatan pemrograman di mana setiap tugas dieksekusi secara berurutan, satu per satu.
    - Dalam _synchronous programming_, setiap tugas harus menunggu tugas sebelumnya selesai sebelum dapat dieksekusi.
    - Proses eksekusi tugas dalam _synchronous programming_ bersifat _blocking_, yang berarti tugas berikutnya tidak dapat dimulai sampai tugas sebelumnya selesai.
    - _Synchronous programming_ cocok untuk tugas yang sederhana dan tidak memerlukan waktu yang lama untuk dieksekusi.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _event-driven programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

*event-driven programming* adalah paradigma pemrograman komputer di mana aliran program ditentukan oleh peristiwa, seperti tindakan pengguna atau pemberitahuan dari sistem. Dalam paradigma ini, program menunggu peristiwa terjadi, lalu meresponsnya sesuai kejadian tersebut. JavaScript sangat cocok untuk _event-driven programming_ ini karena sifatnya yang asinkron, yang memungkinkan eksekusi kode tanpa pemblokiran.

Dalam konteks JavaScript dan AJAX, _event-driven programming_ digunakan untuk menangani interaksi pengguna dengan halaman web. Sebagai contoh, ketika seorang pengguna mengklik tombol, sebuah peristiwa dipicu, dan fungsi kustom dapat dieksekusi sebagai respons terhadap peristiwa tersebut. Hal ini memungkinkan pembuatan halaman web yang lebih interaktif dan responsif, karena pengguna dapat berinteraksi dengan elemen-elemen pada halaman dan mendapatkan respons sesuai dengan tindakan mereka.

Dalam tugas yang diberikan, salah satu contoh penerapan _event-driven programming_ adalah penggunaan _event listener_ untuk menangani interaksi pengguna dengan katalog buku. Setiap buku dalam katalog dapat memiliki tombol atau tautan yang terkait, dan ketika pengguna mengklik tombol atau tautan tersebut, sebuah peristiwa dipicu, dan fungsi kustom dapat dieksekusi untuk melakukan tindakan tertentu, seperti menampilkan informasi lebih lanjut tentang buku atau menambahkannya ke daftar bacaan pengguna. Hal ini meningkatkan pengalaman pengguna dan membuat aplikasi web lebih interaktif serta responsif.

### Jelaskan penerapan _asynchronous programming_ pada AJAX.

_Asynchronous programming_ diterapkan dalam AJAX (Asynchronous JavaScript and XML) untuk memungkinkan aplikasi web mengirim dan menerima data dari server tanpa harus me-_refresh_ seluruh halaman.

- **Asynchronous Communication**: AJAX menggunakan transfer data _asynchronous_ (permintaan HTTP) antara browser dan server web. Hal ini memungkinkan halaman web untuk memanggil informasi kecil atau seluruh data dari server tanpa me-_refresh_ halaman atau melakukan _postback_. Komunikasi _asynchronous_ memastikan bahwa halaman web tetap dapat diakses oleh pengguna sementara data diproses di latar belakang.

- **Objek XMLHttpRequest**: AJAX menggunakan objek XMLHttpRequest, yang merupakan fitur bawaan dalam JavaScript, untuk menangani komunikasi _asynchronous_ dengan server. Objek ini memungkinkan aplikasi web untuk mengirim permintaan ke server dan menerima tanggapan tanpa memblokir interaksi pengguna dengan halaman.

- **Event-driven Programming**: AJAX mengikuti model pemrograman berbasis _event_, di mana aplikasi web mendaftarkan _event handler_ untuk menangani tanggapan dari server. Hal ini memungkinkan aplikasi untuk terus menjalankan tugas lain sambil menunggu tanggapan dari server.

- **Callback Functions**: AJAX menggunakan _callback functions_ untuk menangani tanggapan dari server. Ketika tanggapan diterima, _callback function_ dieksekusi, memungkinkan aplikasi untuk memproses data dan memperbarui halaman web sesuai dengan tanggapan tersebut.

- **Format Data JSON**: Meskipun AJAX awalnya menggunakan XML untuk pertukaran data, pengembang telah mulai menggantinya dengan JSON karena kemiripannya dengan JavaScript. JSON adalah format data ringan yang dapat dengan mudah di-parse oleh JavaScript, sehingga lebih cocok untuk komunikasi _asynchronous_.

Dengan mengimplementasikan _asynchronous programming_, AJAX memungkinkan aplikasi web memberikan pengalaman yang lebih responsif dan ramah pengguna dengan memperbarui bagian-bagian tertentu dari halaman tanpa me-_refresh_ seluruh konten.


### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada _library_ jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Fetch API dan jQuery AJAX adalah dua teknologi yang digunakan untuk melakukan permintaan asinkron pada aplikasi web. Berikut adalah perbandingan antara kedua teknologi tersebut:

- **Fetch API**:
    - Fetch API adalah bagian dari JavaScript dan merupakan API bawaan dari browser.
    - Fetch API menggunakan _Promise_ untuk menangani respons dari server.
    - Fetch API lebih mudah digunakan dan memiliki sintaks yang lebih sederhana.
    - Fetch API lebih ringan dan lebih cepat daripada jQuery AJAX.
    - Fetch API tidak memerlukan _library_ tambahan.

- **jQuery AJAX**:
    - jQuery AJAX adalah _library_ JavaScript yang harus diunduh dan diinstal terlebih dahulu.
    - jQuery AJAX menggunakan _callback function_ untuk menangani respons dari server.
    - jQuery AJAX memiliki fitur yang lebih lengkap dan lebih banyak opsi konfigurasi.
    - jQuery AJAX lebih mudah digunakan untuk melakukan permintaan _cross-domain_.
    - jQuery AJAX lebih kompatibel dengan browser yang lebih lama.

Pilihan antara Fetch API dan jQuery AJAX tergantung pada kebutuhan dan preferensi pengembang. Jika pengembang ingin menggunakan teknologi yang lebih ringan dan lebih cepat, maka Fetch API adalah pilihan yang tepat. Namun, jika pengembang memerlukan fitur yang lebih lengkap dan lebih banyak opsi konfigurasi, maka jQuery AJAX adalah pilihan yang lebih baik. Selain itu, jika pengembang ingin mendukung browser yang lebih lama, maka jQuery AJAX adalah pilihan yang lebih kompatibel.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

- Menyesuaikan kode pada `views.py` dengan membuat fungsi `get_item_json` dan `add_item_ajax`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `get_item_json` dan `add_item_ajax` dan menambahkan path url-nya ke dalam `urlpatterns`
- Menyesuaikan kode pada `main.html` dengan menambahkan blok `<script>` dan membuat fungsi `getItems`, `refreshItems`, dan `addItems` di dalam blok kode `<scirpt>`
- Menyesuaikan kode pada `main.html` dengan menerapkan Cards data item yang dapat mendukung AJAX GET
- Menyesuaikan juga kode pada `views.py` dengan membuat fungsi `delete_item_ajax_`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `delete_item_ajax` dan menambahkan path url-nya ke dalam `urlpatterns`
- Menyesuaikan kode pada `main.html` dengan menambahkan fitur _delete_ yang dapat mendukung AJAX DELETE

----------
## Tugas 5

### Jelaskan manfaat dari setiap _element selector_ dan kapan waktu yang tepat untuk menggunakannya.

1. **Element Selector**
    -  *Manfaat*: Selector elemen digunakan untuk memilih dan mengatur tampilan semua elemen dengan tipe yang sama dalam dokumen HTML. Contohnya, dapat digunakan untuk mengubah semua elemen paragraf `<p>` menjadi berwarna merah.
    - *Penggunaan*: Selector elemen digunakan ketika ingin mengatur tampilan semua elemen dengan tipe yang sama di seluruh dokumen HTML.

2. **ID Selector**
    - *Manfaat*: Selector ID digunakan untuk memilih dan mengatur tampilan elemen dengan atribut ID yang unik dalam dokumen HTML. Setiap elemen hanya memiliki satu ID, sehingga berguna untuk mengatur tampilan elemen tertentu yang ingin dimodifikasi.
    - *Penggunaan*: Selector ID digunakan ketika ingin mengatur tampilan elemen tunggal dengan atribut ID yang unik dalam dokumen HTML.

3. **Class Selector**
    - *Manfaat*: Selector kelas digunakan untuk memilih dan mengatur tampilan elemen dengan atribut kelas yang sama dalam dokumen HTML. Digunakan untuk mengatur tampilan beberapa elemen yang memiliki atribut kelas yang sama secara bersamaan.
    - *Penggunaan*: Selector kelas digunakan ketika ingin mengatur tampilan beberapa elemen dengan atribut kelas yang sama dalam dokumen HTML.

4. **Attribute Selector**
    - *Manfaat*: Selector atribut digunakan untuk memilih dan mengatur tampilan elemen berdasarkan atribut atau nilai atributnya. Digunakan untuk memilih elemen dengan atribut tertentu atau elemen yang memiliki atribut dengan nilai tertentu.
    - *Penggunaan*: Selector atribut digunakan ketika ingin mengatur tampilan elemen berdasarkan atribut atau nilai atributnya dalam dokumen HTML.

5. **Pseudo-Class Selector**
    - **Manfaat*: Selector pseudo-class digunakan untuk memilih dan mengatur tampilan elemen berdasarkan keadaan atau statusnya. Digunakan untuk mengatur tampilan elemen saat diklik, saat diarahkan dengan kursor, atau saat berada dalam keadaan tertentu.
    - *Penggunaan*: Selector pseudo-class digunakan ketika ingin mengatur tampilan elemen secara dinamis berdasarkan keadaan atau statusnya dalam dokumen HTML.

6. **Pseudo-Element Selector**
    - *Manfaat*: Selector pseudo-element digunakan untuk memilih dan mengatur tampilan bagian-bagian tertentu dari elemen. Digunakan untuk mengatur tampilan teks yang berada dalam elemen `<p>` atau untuk menambahkan konten tambahan sebelum atau setelah elemen.
    - *Penggunaan*: Selector pseudo-element digunakan ketika ingin mengatur tampilan bagian-bagian tertentu dari elemen dalam dokumen HTML.


### Jelaskan HTML5 Tag yang kamu ketahui.

- `<header>`: Digunakan untuk mendefinisikan bagian header atau kepala dari sebuah dokumen atau sebuah elemen.
- `<nav>`: Digunakan untuk mendefinisikan bagian navigasi.
- `<section>`: Digunakan untuk mengelompokkan konten yang terkait menjadi bagian yang berbeda.
- `<main>`: Digunakan untuk menandai bagian konten utama.
- `<title>`: Digunakan untuk menentukan judul halaman yang akan ditampilkan.
- `<meta>`: Digunakan untuk menyediakan informasi meta tentang halaman, seperti deskripsi, kata kunci, dan sebagainya.
- `<style>`: Digunakan untuk menentukan gaya CSS secara internal dalam file HTML.
- `<body>`: Digunakan untuk memuat tempat konten utama halaman web berada, seperti teks, gambar, tautan, dan elemen-elemen lainnya.
- `<h1> - <h6>`: Digunakan untuk membuat judul atau kepala dengan tingkat kepentingan yang berbeda. `<h1>` adalah yang paling tinggi, sedangkan `<h6>` adalah yang paling rendah.
- `<p>`: Digunakan untuk menandai paragraf teks.
- `<a>`: Digunakan untuk membuat tautan ke halaman web lain atau resource seperti gambar atau dokumen.
- `<div>`: Digunakan untuk mengelompokkan dan memformat sejumlah elemen HTML.
- `<input>`: Digunakan dalam formulir untuk membuat berbagai jenis kontrol input.
- `<footer>`: Digunakan untuk menandai bagian bawah halaman web.


### Jelaskan perbedaan antara margin dan padding.

Margin dan padding adalah dua properti dalam CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML. Dalam konteks penggunaan, berikut adalah beberapa perbedaan dalam penggunaan margin dan padding:
- **Margin**: Digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya. Contoh penggunaan margin adalah untuk mengatur jarak antara blok teks dan elemen tetangganya, atau untuk mengatur jarak antara elemen dan tepi halaman.
- **Padding**: Digunakan untuk mengatur jarak antara konten elemen dan batas elemen itu sendiri. Contoh penggunaan padding adalah untuk mengatur jarak antara teks dan batas elemen, atau untuk memberikan ruang tambahan di sekitar elemen yang berisi gambar atau ikon.


### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

1. **Bootstrap**: Bootstrap adalah framework CSS yang lebih tua dan lebih besar dalam hal ukuran file. Ia menyediakan banyak komponen dan fitur siap pakai seperti tab navigasi contohnya. Bootstrap lebih fokus pada pengembangan komponen secara menyeluruh untuk penggunaan situs. Keuntungan menggunakan Bootstrap adalah kumpulan komponen yang luas, namun kekurangannya adalah ukuran file yang lebih besar dan kurangnya fleksibilitas dalam kustomisasi.

2. **Tailwind**: Tailwind adalah framework CSS yang lebih baru dan lebih ringkas dibandingkan dengan Bootstrap. Ia dibangun berdasarkan konsep utility class, di mana semua properti CSS telah ditulis sebelumnya sebagai class yang dapat diterapkan langsung ke elemen HTML. Tailwind dirancang untuk menghasilkan elemen UI yang fungsional, rapi, dan fleksibel. Keuntungan menggunakan Tailwind adalah waktu pemuatan yang lebih cepat dan fleksibilitas dalam kustomisasi, namun kekurangannya adalah kurangnya komponen siap pakai seperti yang ada di Bootstrap.

Kapan sebaiknya menggunakan Bootstrap daripada Tailwind, dan sebaliknya, tergantung pada kebutuhan proyek dan preferensi pengembang, berikut penjelasannya:
- **Bootstrap**: Cocok digunakan jika memerlukan kumpulan komponen yang luas dan siap pakai, serta jika ukuran file bukanlah masalah yang signifikan. Bootstrap juga dapat menjadi pilihan yang baik jika ingin mengembangkan situs dengan cepat dan tidak memerlukan tingkat kustomisasi yang tinggi.
- **Tailwind**: Cocok digunakan jika menginginkan fleksibilitas tinggi dalam kustomisasi tampilan situs web, serta jika peduli dengan waktu pemuatan yang cepat dan ukuran file yang lebih kecil. Tailwind juga dapat menjadi pilihan yang baik jika ingin membangun komponen UI yang unik dan tidak terikat dengan komponen siap pakai yang disediakan oleh Bootstrap.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

- Menyesuaikan kode pada `base.html` dengan menambahkan tag `<meta name="viewport">` agar tampilan halaman web dapat menyesuaikan ukuran dan perilaku perangkat _mobile_
- Menambahkan Bootstrap CSS dan JS pada `base.html`
- Menyesuaikan kode pada `views.py` dengan membuat fungsi `edit_item`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `edit_item` dan menambahkan path url-nya ke dalam `urlpatterns`
- Membuat file `edit_item.html`
- Menyesuaikan kode pada `main.html` agar tombol _edit_ dapat terlihat pada setiap baris tabel
- Menyesuaikan kode pada `views.py` dengan membuat fungsi `delete_item`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `delete_item` dan menambahkan path url-nya ke dalam `urlpatterns`
- Menyesuaikan kode pada `main.html` agar tombol _delete_ dapat terlihat pada setiap baris tabel

- Kustomisasi desain pada template html:
    - Menyesuaikan kode pada `main.html` agar tampilannya lebih menarik sesuai keinginan saya. Saya mengubah warna backgroundnya menjadi hitam, mengubah font yang digunakan dengan font _Futura_, kemudian menempatpan posisi tampilan menjadi di tengah.
    - Menyesuaikan kode pada `login.html`, `register.html`, `create_item.html`, dan `edit_item.html` dengan mengubah warna background menjadi hitam, mengubah font yang digunakan dengan font _Futura_, menempatkan posisi tampilan menjadi di tengah, kemudian mengubah tampilan button-button tersebut agar dapat berganti warna.

----------
## Tugas 4

 ### Apa itu `Django UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

- Django `UserCreationForm` adalah sebuah kelas yang disediakan oleh Django, sebuah kerangka kerja pengembangan web Python. `UserCreationForm` adalah formulir bawaan yang memudahkan proses pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan menggunakan `UserCreationForm`, pengembang dapat mengimplementasikan fungsionalitas pendaftaran pengguna dengan mudah tanpa harus menulis kode dari awal.

*Kelebihannya:*
- **Mudah Digunakan**: `UserCreationForm` menyediakan metode dan fungsi bawaan yang memudahkan pembuatan formulir pendaftaran pengguna. Ini mengurangi waktu dan usaha yang diperlukan untuk mengimplementasikan fungsionalitas pendaftaran pengguna.

- **Keamanan yang teruji**: `UserCreationForm` telah dirancang dengan memperhatikan praktik keamanan terbaik. Formulir ini menyertakan validasi bawaan untuk memastikan data yang diinput oleh pengguna valid dan aman.

- **Integrasi yang baik dengan Django**: `UserCreationForm` sangat terintegrasi dengan Django dan kerangka kerja lainnya yang dapat digunakan dalam pengembangan web dengan Django. Ini memudahkan penggunaan dan penggunaan formulir ini dalam proyek Django yang ada.

*Kekurangannya:*
- **Keterbatasan kustomisasi**: `UserCreationForm` menyediakan fungsi bawaan untuk pendaftaran pengguna, tetapi kustomisasi lebih lanjut mungkin memerlukan penyesuaian tambahan. Jika proyek kita membutuhkan logika pendaftaran pengguna yang kompleks atau kustom, kita mungkin perlu menyesuaikan atau mengubah formulir ini secara manual.

- **Tidak dapat memenuhi semua kebutuhan**: `UserCreationForm` dirancang untuk kasus penggunaan umum dalam pendaftaran pengguna. Namun, jika proyek kita memiliki kebutuhan khusus atau kompleks yang tidak dapat dipenuhi oleh UserCreationForm, kita mungkin perlu menggunakan pendekatan yang lebih kustom.


 ### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
 
- Autentikasi dan otorisasi adalah dua konsep penting dalam keamanan web. Autentikasi adalah proses mengidentifikasi pengguna, sedangkan otorisasi adalah proses menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu. Dalam konteks Django, autentikasi dan otorisasi dapat digunakan untuk melindungi aplikasi web dari akses yang tidak sah. *Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi*, sedangkan *otorisasi memastikan bahwa pengguna hanya memiliki izin untuk mengakses sumber daya yang mereka perlukan*.

Keduanya penting karena *autentikasi dan otorisasi bekerja bersama-sama untuk menciptakan lapisan keamanan yang komprehensif* dalam aplikasi web:

- Autentikasi memastikan bahwa pengguna yang mengakses aplikasi adalah pengguna yang sah, sehingga melindungi akun pengguna dari akses yang tidak sah.

- Otorisasi memastikan bahwa pengguna yang telah diautentikasi hanya memiliki akses ke sumber daya dan tindakan yang sesuai dengan izin mereka, sehingga melindungi data dan fungsionalitas aplikasi dari akses yang tidak sah atau tidak diinginkan.


 ### Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?

Dalam konteks aplikasi web, _cookies_ adalah file teks kecil yang disimpan di browser pengguna. _Cookies_ dapat digunakan untuk menyimpan berbagai informasi, seperti data sesi pengguna, preferensi pengguna, dan informasi pemasaran.

Berikut adalah cara Django menggunakan _cookie_ untuk mengelola data sesi pengguna:

- Saat pengguna masuk ke aplikasi web, Django membuat ID sesi pengguna baru. ID sesi pengguna adalah nilai unik yang digunakan untuk mengidentifikasi pengguna dalam sesi.
- Django menyimpan ID sesi pengguna dalam _cookie_ dan mengirimkan _cookie_ ke browser pengguna.
- Browser pengguna menyimpan _cookie_ di komputer pengguna.
- Setiap kali pengguna mengunjungi halaman di aplikasi web, browser pengguna mengirimkan _cookie_ ke server.
- Django menggunakan ID sesi pengguna untuk mengidentifikasi pengguna dan autentikasi pengguna.


 ### Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Pada dasarnya, penggunaan _cookie_ tidak aman secara default dalam pengembangan web. Ada beberapa risiko potensial yang harus diwaspadai, di antaranya:

- **Kebocoran data**: _Cookie_ dapat digunakan untuk mencuri informasi sensitif, seperti nama pengguna, kata sandi, dan informasi keuangan.
- **Pelacakan**: _Cookie_ dapat digunakan untuk melacak perilaku pengguna di situs web dan aplikasi web.
- **Kerusakan**: Cookie yang tidak valid atau berbahaya dapat menyebabkan kerusakan pada browser web atau perangkat pengguna.


 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

- Menjalankan virtual environment
- Menyesuaikan kode pada `views.py` dengan membuat fungsi `register` dan menambahkan beberapa import seperti `redirect`, `UserCreationForm`, dan `messages`
- Membuat file `register.html`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `register` dan menambahkan path url-nya ke dalam `urlpatterns`
- Menyesuaikan kode pada `views.py` dengan membuat fungsi `login_user` dan menambahkan beberapa import seperti `authenticate` dan `login`
- Membuat file `login.html`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `login_user` dan menambahkan path url-nya ke dalam `urlpatterns`
- Menyesuaikan kode pada `views.py` dengan membuat fungsi `logout_user` dan menambahkan import `logout`
- Mennyesuaikan koede pada `main.html` dengan menambahkan _button_ `logout`
- Menyesuaikan kode pada `urls.py` dengan menambahkan import `logout_user` dan menambahkan path url-nya ke dalam `urlpatterns`
- Menyesuaikan kode pada `views.py` dengan menambahkan import `login_required` dan menambahkan kode agar halaman _main_ dapat diakses dengan menambahkan kode baru di atas fungsi `show_main`
- Menyesuaikan kode pada `views.py` dengan menyesuaikan fungsi `login_user`, kemudian menambahkan beberapa import seperti `datetime`, `HttpResponseRedirect`, dan `reverse`, kemudian menambahkan kode baru pada variabel `context`, dan mengubah isi kode pada fungsi `logout_user`
- Menyesuaikan kode pada `main.html` dengan menambahkan kode baru untuk menampilkan data _last login_
- Menyesuaikan kode pada `models.py` dengan menambahkan import `user` dan menambahkan kode baru pada model `Item` untuk menghubungkan satu item dengan satu user
- Menyesuaikan kode pada `views.py` dengan mengubah kode dari fungsi `create_item` dan mengubah kode dari fungsi `show_main` agar item yang terdaftar sesuai dengan pengguna yang sedang login


----------
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


----------
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