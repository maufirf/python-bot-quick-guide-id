# Bot Quick Guide (ID)
Ini adalah panduan cepat untuk membuat bot Facebook, Twitter, dan Discord. Panduan ini Berbahasa Indonesia. Kunjungi semua bot sosial media yang saya buat di [maufirf.me/Bottlemin-Bots](http://maufirf.me/Bottlemin-Bots).

_Disklaimer: Panduan ini tidak sepenuhnya menggunakan istilah dalam Bahasa Indonesia karena kadang kata-kata yang dipaksakan untuk diserap ke dalam Bahasa Indonesia terlihat bodoh atau sulit diucapkan. Contohnya "Grayscale image" menjadi "Citra Skala Keabuan". Jujur saja itu terdengar bodoh di telinga saya. Ditambah, saya juga tidak akan sepenuhnya mengikuti PUEBI dan menulis panduan ini sesuka hati saya._

_Saya dengan senang hati jika anda memiliki pertanyaan, namun biasakan diri anda untuk membaca terlebih dahulu. Saya akan lampirkan server Discord saya di sini ketika sudah dibuka untuk publik._

-------------

**Selamat datang di panduan cepat membuat bot sosial media ini!**<br/>
Panduan ini tidak membahas lengkap tentang pembuatan bot sampai ke akar, karena tujuan utama dari panduan ini adalah untuk mendeploy bot secara cepat kurang dari 3 jam. Pengembangan bot akan diserahkan sepenuhnya kepada pembaca. Panduan lengkap akan dibuat di situs ini, ketika panduan lengkap sudah dirilis, saya akan memberi kabar di [akun Facebook pribadi saya](https://fb.me/auficertepaja).

Outline panduan pembuatan bot ini melingkupi:
- Pemrograman di **Python**;
- Menggunakan _developer tools_ yang disediakan **Facebook**, **Twitter**, atau **Discord**;
- Menyambungkan akun sosial media bot dengan programnya;
- Menaruh program bot di tempat hosting **Heroku** agar tidak perlu menyalakan dan menggoreng komputer anda karena harus nyala 24 jam x 7 hari; dan
- Moderasi posting.

Prasyarat pembuatan bot ini adalah (syarat-syarat ini terserah mau anda penuhi atau tidak kalau punya preferensi sendiri, tapi ya kalau mau ikutin panduan ini, ini yang saya pake):
- Pengetahuan dasar pemrograman dengan bahasa **Python** berserta Pythonnya sendiri di komputer anda. Python dapat anda unduh [di situsnya](https://www.python.org/downloads/), namun saya juga menyarankan untuk lebih memilih [mengunduh Anaconda](https://www.anaconda.com/distribution/) dibanding Python biasa, karena Anaconda adalah Python biasa namun sebagian besar tools sudah lengkap bersama unduhannya.
- Akun di salah satu situs tujuan deployment anda, **[Facebook](https://fb.com)**, **[Twitter](https://twitter.com)**, atau **[Discord](https://discordapp.com)**.
- Akun di tempat hosting **[Heroku](https://heroku.com)**
- _(OPSIONAL)_ Pengetahuan dasar **pemrograman berbasis objek**. Sebenarnya nggak perlu banget sih, tapi kalau bisa yah lebih enak jelasinnya.
- _(OPSIONAL)_ Kartu debit dengan saldo setidaknya Rp.16.000,00. Kalau lebih mah terserah, kalau pake kartu kredit mah silahkan, mau teriak ke saya ***"PERSETAN KARO ATURAN, AKU IKI WONG SUGIH"*** mah saya terima. CATATAN: tidak akan menggunakan saldo yang ada miliki kok, kecuali kalau anda wong sugih ya, sila...
- <sub><sub>_(OPSIONAL, TAPI BENERAN NGGAK PENTING-PENTING BANGET)_ Kartu x-card jenius. belum punya? silahkan ke [situsnya](https://www.jenius.com/) buat bikin yha~</sub></sub>

--------

## Python: pengenalan dan persiapan

Dalam panduan ini, saya mencoba untuk menurunkan knowledge base saya sebawah mungkin agar panduan ini dapat diikuti sekalipun anda bukan ~~wibu ilkom~~ programmer.

<spoiler>aaaaaaa</spoiler>
