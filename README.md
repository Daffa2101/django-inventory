"# django-inventory" 

#### TUGAS 2 #####

Link aplikasi adaptable : google.com


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    pertama-tama saya membuat proyek django baru dengan menginstall requirement yang dibutuhkan untuk project ini, kemudian menambahkan repositori lokal ini ke repositaru github saya (sudah ada .gitignore). 
    
    Setelah itu saya membuat app main melalui terminal dan menambahkannya ke settings.py pada direktori proyek.

    Setelah itu saya membuat file template HTML yang berisi judul aplikasi, nama dan kelas saya ( untuk nama dan kelas mengambil data dari context pada views.py). 

    Setelah membuat template, saya membuat model baru bernama Item yang memiliki atribut name, amount, description, dan category. 
    
    setelah model dibuat saya melalkukan migrasi model melalui terminal. 

    setelah migrasi berhasil, saya membuat sebuah function pada views.py untuk menampilkan template html yang telah dibuat.
    
    Kemudian setelah itu, saya melakukan routing melalui urls.py pada app main untuk mengarahkan ke fungsi yang telah saya buat pada views.py

    setelah itu, saya memasukkan routing kedalam urls.py pada direktori proyek.

    setelah semua selesai, saya memelakukan git add, commit, dan push untuk selanjutnya melakukan deploy ke adaptable.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan  tersebut kaitan antara urls.py, views.py, models.py, dan berkas HTML.

    ![Client Request Chart](images\chart.jpg)

    Kaitan antara urls.py, views.py, models.py, dan berkas HTML:
    
    -> urls.py berfungsi untuk mengarahkan Request client ke View yang dinginkan
    -> models.py berfungsi sebagai perantara antara database dan View pada saat mengolah data dari database.
    -> views.py melakukan logika bisnis dengan bantuan model dan template (HTML)
    -> Berkas HTML menyediakan template sebagai tampilan untuk data yang didapat pada View



3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Alasan kita menggunakan virtual environment adalah untuk mendapatkan fleksibilitas pada manajemen dependensi yang kita butuhkan. Dengan begitu kita dapat terhindar dari konflik versi dari package global pada pc kita.

    Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, akan tetapi akan memiliki kekurangan serta resiko akan hal hal yang disebutkan sebelumnnya.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC, MVT, dan MVVM merupakan kerangka / pola arsitektur software dalam pengembangan aplikasi untuk melakukan pemisahan antara logika bisnis, tampilan dan interaksi pengguna. Hal ini bertujuan untuk memudahkan pengembangan software serta mempermudah melakukan testing selama pengembangan software berlangsung.

Perbedaan ketiganya adalah seperti berikut : 
-> MVC (Model-View-Controller)
    flow / cara kerja arsitektur MVC:
        1. user berinteraksi dengan view dengan melakukan suatu action.
        2. action kemudian diteruskan ke Controller, pada Controller action tersebut diproses sesuai kebutuhan aplikasi.
        3. Controller akan berinteraksi dengan Model untuk mengambil atau mengubah data pada Model.
        4. Setelah berinteraksi dengan Model, Controller akan  mengupdate data yang akan ditampilkan dan mengirimkan ke View.
        5. View menerima data dari Controller kemudian mengupdate tampilan interface.

- MVT (Model-View-Template)
    flow / cara kerja arsitektur MVT:
        1. User mengakses salah satu suatu URL
        2. Django akan menjadi pola URL yang sesuai pada urls.py dan menentukan View yang akan menerima request
        3. View menerima request dan melakukan logika bisnis yang diperlukan aplikasi
        4. Jika View memerlukan dat dari database, View mengakses memlalui perantara Model.
        5. Setelah proses pada databse oleh Model selesai, View akan menggunakan template (HTML) untuk melakukan render data tersebut ke tampilan yang dinginkan.
        6. Setelah Template selesai mengatur tampilan, View akan akan menghasilkan page HTML yang sudah dirender beserta HTTP response yang sesuai.
        7. HTTP Response berisi halaman HTML yang di request oleh user.

- MVVM (Model-View-ViewModel)
    flow / cara kerja arsitektur MVVM:
        1. user berinteraksi dengan View dengan melakukan suatu action.
        2. Action yang didapat oleh View diteruskan ke ViewModel
        3. ViewModel mengelola logika bisnis aplikasi dan menjadi perantara antara View dan Model.
        4.Jika butuh menggunakan database, Model akan yang akan berinteraksi dengan database.
        5. Setelah data dari database didapatkan, Model meneruskan ke ViewModel.
        6. ViewModel kemudian melakukan proses yang dibutuhkan aplikasi pada data yang didapat sebelum diteruskan kepada View.
        7. Setelah data yang telah diproses diteruskan ke View, View akan merender tampilan sesuai yang dinginkan.
        8. Setelah itu user dapat melihat tampilan yang telah diperbarui dan siap melakukan interaksi lainnya.
