# proyek-kelompok-12-ddp1
# CodeQuest

Website pembelajaran materi Fasilkom dengan Django.

## Persiapan

- Instal Python VERSI_PYTHON.
- Instal Git dan VS Code.
- Perintah berikut digunakan pada Windows.

## Pertama kali mengambil proyek

Buka terminal, lalu jalankan:

```powershell
git clone URL_REPO
cd NAMA_FOLDER_REPO
```

Buka folder tersebut di VS Code melalui File → Open Folder.
Buka terminal VS Code, lalu jalankan perintah berikut satu per satu:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Buka http://127.0.0.1:8000/ di browser.

Tidak perlu menjalankan startproject atau startapp lagi.

## Menjalankan proyek pada hari berikutnya

Buka terminal di folder yang berisi manage.py, lalu jalankan:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Untuk menghentikan server, tekan Ctrl + C.

## Mengambil pembaruan dari GitHub

Selesaikan dan commit pekerjaan lokal terlebih dahulu.
Hentikan server, lalu jalankan satu per satu:

```powershell
git pull
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Jika muncul konflik saat git pull, selesaikan konflik sebelum melanjutkan.