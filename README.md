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

## Panduan Menambahkan Gambar pada Modul (Materi & Kuis)

Sistem CodeQuest mendukung penyisipan gambar/ilustrasi di dalam langkah pembelajaran (Materi) maupun pertanyaan latihan (Kuis).

### 1. Tempat Menyimpan File Gambar
Simpan semua aset gambar pada direktori static berikut:
```text
learning/static/learning/images/
```
Contoh: simpan file `diagram_venn.png` ke dalam folder tersebut, sehingga file dapat diakses melalui path:
```text
/static/learning/images/diagram_venn.png
```

---

### 2. Memasukkan Gambar ke Materi (`type="material"`)
Tambahkan blok bertipe `"image"` di dalam list `content_blocks` pada `Step`:

```python
Step(
    id="step-1",
    type="material",
    badge="Visualisasi",
    title="Diagram Irisan Himpunan",
    content_blocks=[
        {
            "type": "paragraph",
            "text": "Perhatikan daerah arsiran pada diagram Venn di bawah ini:",
        },
        {
            "type": "image",
            "src": "/static/learning/images/diagram_venn.png",
            "caption": "Gambar 1.1: Irisan antara himpunan A dan himpunan B (A ∩ B)",
        },
        {
            "type": "paragraph",
            "text": "Daerah yang diarsir merupakan elemen yang dimiliki bersama oleh himpunan A dan B.",
        },
    ],
)
```

- `src`: Path static gambar (misal `/static/learning/images/nama_file.png`) atau URL gambar online (`https://...`).
- `caption` *(opsional)*: Keterangan gambar yang akan muncul di bawah ilustrasi.

---

### 3. Memasukkan Gambar ke Kuis (`type="quiz"`)
Tambahkan argumen `image` (dan opsional `image_caption`) langsung saat menginisialisasi `Step` kuis:

```python
Step(
    id="step-2",
    type="quiz",
    badge="Latihan 1",
    question="Berdasarkan diagram relasi di bawah, manakah pernyataan yang benar?",
    image="/static/learning/images/diagram_relasi.png",
    image_caption="Diagram Panah Relasi Himpunan P ke Q",
    choices=[
        {"id": "A", "text": "Relasi merupakan fungsi injektif"},
        {"id": "B", "text": "Relasi bukan merupakan fungsi"},
        {"id": "C", "text": "Relasi merupakan fungsi surjektif"},
        {"id": "D", "text": "Relasi merupakan fungsi bijektif"},
    ],
    answer="A",
    explanation="Setiap elemen pada domain P berpasangan tepat satu dengan elemen unik di kodomain Q.",
)
```
Gambar soal akan otomatis ditampilkan tepat di bawah teks pertanyaan kuis dan di atas pilihan ganda.
