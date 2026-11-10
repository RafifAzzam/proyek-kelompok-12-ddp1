--------------------
Side Question: tapi ntar yg keliatan commitnya aku doang dong.. temen2ku gimana

Ini kekhawatiran yang sangat wajar (dan penting!), apalagi dosen dan asdos sering mengecek tab **Contributors / Insights** di GitHub untuk menilai keaktifan masing-masing anggota.

Ada **2 cara terbaik** untuk mengatasi ini:

---

### Cara 1: Gunakan Fitur Resmi GitHub `Co-authored-by` (Bisa untuk commit tadi)
GitHub punya fitur resmi untuk mencatat bahwa satu commit dikerjakan bersama-sama oleh lebih dari satu orang. 

Jika format pesan commit menyertakan tag `Co-authored-by:`, **foto profil dan nama teman-temanmu otomatis muncul berdampingan dengan akunmu di GitHub**, dan commit tersebut dihitung ke riwayat kontribusi mereka.

Contoh format di pesan commit:
```text
Implementasi Milestone 1: Pelajaran pertama dan kuis interaktif

Co-authored-by: Nama Teman 1 <email_teman1@ui.ac.id>
Co-authored-by: Nama Teman 2 <email_teman2@ui.ac.id>
```
*(Catatan: harus ada satu baris kosong sebelum baris `Co-authored-by`, dan email yang digunakan adalah email akun GitHub mereka).*

Jika kamu mau, commit terakhir di branch `solusi` tadi bisa kita ubah (*amend*) agar langsung mencantumkan nama dan email GitHub teman-temanmu.

---

### Cara 2: Pembagian Tugas Riil per Laptop (Paling Direkomendasikan untuk Kuliah)
Pekerjaan yang kita buat di branch `solusi` ini anggap saja sebagai **"fondasi awal"**. Supaya kontribusi teman-temanmu banyak di GitHub, bagi pekerjaan berikutnya agar mereka yang melakukan commit dari laptop masing-masing:

1. **Push branch `solusi` ini ke GitHub**:
   ```bash
   git push -u origin solusi
   ```
2. **Teman A (Penanggung Jawab Materi)**:
   - Di laptopnya, dia berpindah ke branch `solusi`:
     ```bash
     git fetch origin
     git checkout solusi
     ```
   - Tugas dia: Buka [`learning/data.py`](file:///Users/rafif/Documents/Kuliah/Semester%201/DDP1/hands_on/project/proyek-kelompok-12-ddp1/learning/data.py), lalu tambahkan pelajaran ke-2 (*Operator Aritmatika*) lengkap dengan 3 soal kuis dan pembahasannya.
   - Dia yang melakukan commit dan push dari laptopnya:
     ```bash
     git commit -m "Tambah materi dan kuis modul Operator Aritmatika"
     git push
     ```
   - Commit ini 100% tercatat atas nama dia.

3. **Teman B (Penanggung Jawab Logika / Pengujian)**:
   - Mengambil perubahan terbaru, lalu menambahkan test case baru di `tests.py` atau menyempurnakan aturan scoring.
   - Dia commit dan push dari laptopnya sendiri:
     ```bash
     git commit -m "Tambah validasi scoring dan unit test"
     git push
     ```

Dengan cara ini:
- Kamu dapat commit untuk arsitektur/setup awal.
- Teman A dapat commit untuk penulisan materi dan soal.
- Teman B dapat commit untuk pengujian dan logika tambahan.

Riwayat commit kelompok kalian di GitHub akan terlihat sangat aktif, merata, dan profesional di mata dosen/asdos!
--------------------
Side Question: bagaimana cara aku dan temanku menambahkan mateeri, modul, subbab, kuis, etc?

Semua materi, subbab, modul, dan kuis dikelola di **satu file saja**: 
👉 [`learning/data.py`](file:///Users/rafif/Documents/Kuliah/Semester%201/DDP1/hands_on/project/proyek-kelompok-12-ddp1/learning/data.py)

Kalian tidak perlu menyentuh database atau HTML setiap kali menambah konten baru. Cukup tambahkan data Python dengan format berikut:

---

### 1. Daftarkan Modul/Subbab di `TOPICS`
Di dalam list `TOPICS`, kalian bisa menambah subbab baru atau modul baru ke subbab yang sudah ada:

```python
# Di dalam TOPICS = [ ... ]
{
    "id": "perulangan",                 # ID unik subbab
    "title": "Perulangan (Looping)",    # Judul subbab
    "description": "Mengulang instruksi dengan for dan while loop.",
    "badge": "🔁",                      # Emoji badge
    "lessons": [
        {
            "id": "for-loop",           # ID unik modul (harus sama dengan di LESSONS_DATA)
            "title": "For Loop Dasar",
            "duration": "6 menit",
            "summary": "Mengenal perulangan menggunakan for dan range().",
            "is_locked": True,          # Biarkan True (akan otomatis terbuka setelah modul sebelumnya selesai)
        },
    ],
},
```

---

### 2. Isi Materi & Kuis di `LESSONS_DATA`
Di dalam dictionary `LESSONS_DATA`, buat entri baru sesuai `id` modul (misal `"for-loop"`):

```python
# Di dalam LESSONS_DATA = { ... }
"for-loop": {
    "id": "for-loop",
    "topic_id": "perulangan",
    "topic_title": "Perulangan (Looping)",
    "title": "For Loop Dasar",
    "xp_reward": 50,
    "steps": [
        # --- LANGKAH MATERI ---
        {
            "id": "step-1",
            "type": "material",
            "badge": "Konsep Dasar",
            "title": "Apa itu For Loop?",
            "content_blocks": [
                {
                    "type": "paragraph",
                    "text": "For loop digunakan untuk <strong>mengulang</strong> kode sejumlah kali tertentu.",
                },
                {
                    "type": "code",
                    "code": 'for i in range(3):\n    print("Halo ke-", i)',
                },
                {
                    "type": "callout",
                    "title": "Ingat:",
                    "items": [
                        "<code>range(3)</code> menghasilkan angka: 0, 1, 2.",
                    ],
                },
            ],
        },

        # --- LANGKAH KUIS ---
        {
            "id": "step-2",
            "type": "quiz",
            "badge": "Latihan 1",
            "question": "Berapa kali kata 'Halo' dicetak oleh kode: `for i in range(5): print('Halo')`?",
            "choices": [
                {"id": "A", "text": "4 kali"},
                {"id": "B", "text": "5 kali"},
                {"id": "C", "text": "6 kali"},
                {"id": "D", "text": "Tak terhingga"},
            ],
            "answer": "B",  # Kunci jawaban yang benar
            "explanation": "Pilihan B benar! range(5) menghasilkan 5 angka (0, 1, 2, 3, 4), sehingga diulang 5 kali.",
        },
    ],
},
```

---

### 💡 Apa yang Terjadi Secara Otomatis?
Begitu kalian menyimpan file [`learning/data.py`](file:///Users/rafif/Documents/Kuliah/Semester%201/DDP1/hands_on/project/proyek-kelompok-12-ddp1/learning/data.py):
1. **Dashboard langsung ter-update**: Kartu modul baru langsung muncul di homepage.
2. **Buka Kunci Otomatis**: Jika pengguna sudah menyelesaikan modul sebelumnya, modul baru ini otomatis terbuka kuncinya.
3. **Efek Suara & Progres**: Format selang-seling, efek suara *ting* / *buzz*, bilah progres, dan reward `+50 XP` langsung bekerja tanpa perlu coding tambahan!
--------------------
### **1. Ringkasan Proyek & Konsep**

  
- **Nama Proyek**: **CodeQuest**
- **Mata Kuliah**: DDP1 (Dasar-Dasar Pemrograman 1), Semester 1 Fasilkom.
- **Tim & Waktu**: 3 orang anggota, durasi pengerjaan 5 minggu.
- **Konsep Utama**: Website belajar materi Fasilkom bergaya *Duolingo* (materi singkat →\rightarrow→ latihan/kuis interaktif →\rightarrow→ *instant feedback* →\rightarrow→ pencatatan progres).
- **Tech Stack**: **Django (Python)** untuk backend/routing, HTML/CSS/JavaScript untuk frontend.
- **Fitur MVP (Tanpa Login)**:
  
  
- Progres pengguna (materi selesai, skor, XP) disimpan di sisi browser menggunakan **`localStorage`** agar praktis dan cepat untuk MVP.
- Target konten awal: **2 Topik ×\times× 3 Pelajaran ×\times× 3–5 Soal** (Total 6 pelajaran, misalnya *Dasar Pemrograman Python* dan *Logika Dasar*).

---

### **2. Pembagian Peran Tim (3 Orang)**

  AnggotaPeran UtamaTanggung Jawab**Anggota A****Materi**Menulis materi ringkas, soal kuis pilihan ganda, kunci jawaban, dan pembahasannya.**Anggota B****Logika**Menulis fungsi logika Python untuk pemeriksaan jawaban, aturan skor, dan syarat kelulusan/mengulang.**Anggota C****Integrasi & Pengujian**Menghubungkan Django, template HTML/JS, menjalankan server, dan mencatat perbaikan/bug.

---

### **3. Rencana Kerja 4 Minggu (Milestones)**

  
- **Minggu 1 (Fokus saat ini)**: Membuat satu pelajaran berjalan penuh (*Dashboard →\rightarrow→ Buka Materi →\rightarrow→ Jawab Kuis →\rightarrow→ Cek Benar/Salah*).
- **Minggu 2**: Alur kuis lengkap & penyimpanan progres ke `localStorage` (skor tidak hilang saat *refresh* atau ganti halaman).
- **Minggu 3**: Pengisian seluruh konten (6 pelajaran), poles UI/CSS (tema ungu & responsif di HP/laptop), uji coba ke teman luar tim.
- **Minggu 4**: Pengujian akhir, laporan tugas, slide presentasi, dan latihan demo.
--------------------
Saya telah membaca dan menganalisis seluruh isi percakapan dari tautan tersebut ("Ringkasan Memori Project").

Berikut adalah rangkuman lengkap status proyek, kesepakatan, dan langkah berikutnya:

1. Ringkasan Proyek & Konsep
Nama Proyek: CodeQuest
Mata Kuliah: DDP1 (Dasar-Dasar Pemrograman 1), Semester 1 Fasilkom.
Tim & Waktu: 3 orang anggota, durasi pengerjaan 5 minggu.
Konsep Utama: Website belajar materi Fasilkom bergaya Duolingo (materi singkat 
→
→ latihan/kuis interaktif 
→
→ instant feedback 
→
→ pencatatan progres).
Tech Stack: Django (Python) untuk backend/routing, HTML/CSS/JavaScript untuk frontend.
Fitur MVP (Tanpa Login):
Progres pengguna (materi selesai, skor, XP) disimpan di sisi browser menggunakan localStorage agar praktis dan cepat untuk MVP.
Target konten awal: 2 Topik 
×
× 3 Pelajaran 
×
× 3–5 Soal (Total 6 pelajaran, misalnya Dasar Pemrograman Python dan Logika Dasar).
2. Pembagian Peran Tim (3 Orang)
Anggota	Peran Utama	Tanggung Jawab
Anggota A	Materi	Menulis materi ringkas, soal kuis pilihan ganda, kunci jawaban, dan pembahasannya.
Anggota B	Logika	Menulis fungsi logika Python untuk pemeriksaan jawaban, aturan skor, dan syarat kelulusan/mengulang.
Anggota C	Integrasi & Pengujian	Menghubungkan Django, template HTML/JS, menjalankan server, dan mencatat perbaikan/bug.
3. Rencana Kerja 4 Minggu (Milestones)
Minggu 1 (Fokus saat ini): Membuat satu pelajaran berjalan penuh (Dashboard 
→
→ Buka Materi 
→
→ Jawab Kuis 
→
→ Cek Benar/Salah).
Minggu 2: Alur kuis lengkap & penyimpanan progres ke localStorage (skor tidak hilang saat refresh atau ganti halaman).
Minggu 3: Pengisian seluruh konten (6 pelajaran), poles UI/CSS (tema ungu & responsif di HP/laptop), uji coba ke teman luar tim.
Minggu 4: Pengujian akhir, laporan tugas, slide presentasi, dan latihan demo.
--------------------

--------------------
--------------------
--------------------
