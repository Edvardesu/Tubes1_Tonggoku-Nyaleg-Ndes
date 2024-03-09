# **Tubes 1 Strategi Algoritma : Diamonds**
Repositori ini mengandung program untuk sebuah bot untuk permainan Diamonds
sebagai Tugas besar 1 mata kuliah Strategi dan Algoritma 2024.

## Authors
**Kelompok Tonggoku Nyaleg Ndes**
| Nama | NIM |
| ---- | --- |
| Eduardus Alvito Kristiadi | 13522004 |
| Zachary Samuel Tobing | 13522016 |
| Dimas Bagoes Hendrianto | 13522112 |

##** Latar Belakang**
Diamonds merupakan suatu _programming challenge_ yang mempertandingkan bot yang
anda buat dengan bot dari para pemain lainnya. Setiap pemain akan memiliki sebuah bot
dimana tujuan dari bot ini adalah mengumpulkan diamond sebanyak-banyaknya. Cara
mengumpulkan _diamond_ tersebut tidak akan sesederhana itu, ada beberapa objek
yang membuat permainan ini lebih kompleks.

## **Kebutuhan Program**
* Node.js
* Docker desktop
* Yarn

## **Cara Build**
Bot dapat di _build_ dengan menggunakan `npm run build` ada _folder_ _**tubes1-IF2110-game-engine-1.1.0**_

## **Cara Menjalankan Program**
1. Download _source code_ pada [release game engine](https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0)
   untuk _game engine_ dan [release bot starter pack](https://github.com/haziqam/tubes1-IF2211-bot-starter-pack/releases/tag/v1.0.1)
   untuk _bot starter pack_
2. Setup _default environment variable_ dengan menjalankan `./scripts/copy-env.bat` untuk Windows dan `chmod +x ./scripts/copy-env.sh
./scripts/copy-env.sh` untuk Linux
3. Nyalakan aplikasi _docker_ kemudian jalankan `docker compose up -d database`, diikuti dengan `./scripts/setup-db-prisma.bat` untuk Windows
   dan `chmod +x ./scripts/setup-db-prisma.sh ./scripts/setup-db-prisma.sh` untuk Linux
4. Program kemudian dapat di _run_ dengan `npm run start` pada folder _**tubes1-IF2110-game-engine-1.1.0**_ dan `python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo`
   pada folder _**tubes1-IF2110-bot-starter-pack-1.0.1**_
5. Program juga dapat menjalankan beberapa bot sekaligus dengan `./run-bots.bat` untuk Windows dan `./run-bots.sh` untuk Linux dengan
   mengubah _file_ _run-bots.bat_
6. _Frontend_ permainan dapat dilihat pada [http://localhost:8082/](http://localhost:8082/)

## **Algoritma**
Algoritma _Greedy_ yang kami gunakan yaitu:
1. Bot akan mencari _diamond_ terdekat dengan melihat semua diamond yang ada dan lewat jalur biasa maupun _teleporter_
2. Bot akan mengambil _diamond_ merah jika jarak pada _diamond_ merah terdekat lebih kecil dari jarak pada _diamond_ biru terdekat
3. Bot akan mempertimbangkan diamond dengan jarak terdekat dan yang menuju _base_ tanpa mempertimbangkan jenis _diamond_ jika jumlah _diamond_ yang dimiliki masih kurang dari 4
4. Jika bot sudah memiliki 4 _diamond_, bot hanya mempertimbangkan _diamond_ biru terdekat
5. Jika bot sudah memiliki 5 _diamond_, bot akan menuju _base_
6. Bot akan menuju tombol _red button_ atau _diamond button_ jika jumlah _diamond_ kurang dari 17, jarak ke tombol kurang dari 5, dan _diamond_ yang dimiliki kurang dari 4
7. Bot juga akan mengecek jika ada _portal_ yang berada di tengah _base_ dan _bot_ agar tidak terjadi _looping_ atau penjauhan dari _base_
