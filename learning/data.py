"""
Data materi dan kuis untuk CodeQuest (Milestone 1 - Duolingo Interleaved Mode).
Materi dan latihan disusun selang-seling (Materi -> Latihan -> Materi -> Latihan).
"""

TOPICS = [
    {
        "id": "dasar-python",
        "title": "Dasar Pemrograman Python",
        "description": "Pelajari pondasi dasar bahasa Python dari variabel hingga logika perhitungan.",
        "badge": "🐍",
        "lessons": [
            {
                "id": "variabel",
                "title": "Variabel & Tipe Data",
                "duration": "5 menit",
                "summary": "Memahami cara menyimpan data ke dalam variabel dan mengenal tipe data dasar (int, float, str, bool).",
                "is_locked": False,
            },
            {
                "id": "operator",
                "title": "Operator Aritmatika & Logika",
                "duration": "7 menit",
                "summary": "Melakukan operasi matematika, perbandingan nilai, dan evaluasi logika dalam Python.",
                "is_locked": True,
            },
            {
                "id": "input-output",
                "title": "Input & Output Sederhana",
                "duration": "5 menit",
                "summary": "Membaca masukan pengguna dengan input() dan mencetak hasil berformat dengan print().",
                "is_locked": True,
            },
        ],
    },
    {
        "id": "logika-dasar",
        "title": "Logika & Percabangan",
        "description": "Mengambil keputusan dalam kode menggunakan if, elif, dan else.",
        "badge": "⚡",
        "lessons": [
            {
                "id": "kondisional-if",
                "title": "Percabangan if-else",
                "duration": "7 menit",
                "summary": "Menjalankan blok kode tertentu hanya saat suatu kondisi bernilai True.",
                "is_locked": True,
            },
            {
                "id": "kondisi-boolean",
                "title": "Kondisi & Logika Boolean",
                "duration": "10 menit",
                "summary": "Memahami truthy/falsy, perbandingan berantai, dan short-circuit untuk menyusun kondisi.",
                "is_locked": True,
            },
            {
                "id": "percabangan-bersarang",
                "title": "Percabangan Bersarang",
                "duration": "8 menit",
                "summary": "Menggabungkan keputusan bertingkat serta membedakan beberapa if dengan if-elif.",
                "is_locked": True,
            },
        ],
    },
    {
        "id": "perulangan",
        "title": "Perulangan",
        "description": "Mengulang instruksi dengan while dan for, mengatur alurnya, serta membuat perulangan bersarang.",
        "badge": "🔁",
        "lessons": [
            {
                "id": "while-loop",
                "title": "Perulangan while",
                "duration": "8 menit",
                "summary": "Mengulang berdasarkan kondisi, menghindari infinite loop, dan menggunakan nilai penghenti.",
                "is_locked": True,
            },
            {
                "id": "for-range",
                "title": "Perulangan for & range()",
                "duration": "8 menit",
                "summary": "Menelusuri urutan dan membuat rentang angka dengan start, stop, serta step.",
                "is_locked": True,
            },
            {
                "id": "kontrol-perulangan",
                "title": "break, continue & Loop else",
                "duration": "8 menit",
                "summary": "Menghentikan loop, melewati satu putaran, dan memahami else pada perulangan.",
                "is_locked": True,
            },
            {
                "id": "perulangan-bersarang",
                "title": "Perulangan Bersarang",
                "duration": "8 menit",
                "summary": "Menelusuri loop di dalam loop dan membuat pola bintang sederhana.",
                "is_locked": True,
            },
        ],
    },
]

LESSONS_DATA = {
    # -------------------------------------------------------------------------
    # Modul 1: Variabel & Tipe Data
    # -------------------------------------------------------------------------
    "variabel": {
        "id": "variabel",
        "topic_id": "dasar-python",
        "topic_title": "Dasar Pemrograman Python",
        "title": "Variabel & Tipe Data",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Konsep Dasar",
                "title": "Apa Itu Variabel?",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Bayangkan sebuah <strong>variabel</strong> seperti wadah atau kotak berlabel di memori komputer. Kamu bisa menyimpan data di dalamnya dan menggunakannya kapan saja di dalam program.",
                    },
                    {
                        "type": "code",
                        "code": '# Menyimpan data ke dalam variabel\nnama = "Budi"\numur = 18\n\nprint("Halo,", nama)',
                    },
                    {
                        "type": "callout",
                        "title": "Aturan Penting Penamaan Variabel di Python:",
                        "items": [
                            "Harus diawali huruf (a-z, A-Z) atau garis bawah (<em>underscore</em> <code>_</code>).",
                            "Tidak boleh menggunakan spasi (gunakan <em>snake_case</em>, contoh: <code>total_skor</code>).",
                            "Tidak boleh diawali angka (contoh salah: <code>1nama</code>).",
                            "Python bersifat <em>case-sensitive</em>: <code>umur</code> dan <code>Umur</code> berbeda.",
                        ],
                    },
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Di antara pilihan nama variabel berikut, manakah yang VALID menurut aturan Python?",
                "choices": [
                    {"id": "A", "text": "2_skor_pemain"},
                    {"id": "B", "text": "skor-pemain"},
                    {"id": "C", "text": "skor_pemain"},
                    {"id": "D", "text": "skor pemain"},
                ],
                "answer": "C",
                "explanation": "Pilihan C benar! Nama variabel di Python boleh memakai huruf dan underscore. Tidak boleh memakai spasi (D), tanda hubung minus (B), atau diawali angka (A).",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Tipe Data",
                "title": "Mengenal 4 Tipe Data Dasar",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Python secara otomatis menentukan jenis tipe data berdasarkan nilai yang kamu masukkan ke dalam variabel:",
                    },
                    {
                        "type": "code",
                        "code": 'jumlah = 20        # int (bilangan bulat)\nberat = 55.5       # float (bilangan desimal/pecahan)\nnama = "Ayu"       # str (teks / string)\nlulus = True       # bool (kebenaran: True atau False)',
                    },
                    {
                        "type": "callout",
                        "title": "Tips Mengenali Tipe Data:",
                        "items": [
                            "Angka dengan titik pecahan desimal (seperti <code>3.14</code> atau <code>10.0</code>) selalu bertipe <strong>float</strong>.",
                            "Teks selalu diapit oleh tanda petik tunggal <code>'...'</code> atau ganda <code>\"...\"</code>.",
                            "Boolean hanya bernilai <code>True</code> atau <code>False</code> dengan huruf kapital di awal.",
                        ],
                    },
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Perhatikan kode berikut:\n\nnilai = 3.14\n\nApakah tipe data dari variabel `nilai`?",
                "choices": [
                    {"id": "A", "text": "int (Integer)"},
                    {"id": "B", "text": "float (Floating Point)"},
                    {"id": "C", "text": "str (String)"},
                    {"id": "D", "text": "bool (Boolean)"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Bilangan yang memiliki titik desimal di Python dikelompokkan sebagai tipe data float.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Operasi Variabel",
                "title": "Mengubah & Menimpa Nilai Variabel",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Nilai dalam variabel dapat diganti (*re-assigned*) kapan saja. Tanda sama dengan tunggal <code>=</code> berarti <em>menugaskan/mengisi</em> nilai di sisi kanan ke wadah di sisi kiri.",
                    },
                    {
                        "type": "code",
                        "code": 'skor = 10\nprint(skor)  # Output: 10\n\nskor = 25    # Nilai 10 ditimpa menjadi 25\nprint(skor)  # Output: 25',
                    },
                    {
                        "type": "callout",
                        "title": "Menyalin Antar Variabel:",
                        "items": [
                            "Perintah <code>a = b</code> berarti: ambil isi nilai dari variabel <code>b</code>, lalu masukkan ke dalam variabel <code>a</code>.",
                        ],
                    },
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Apa output dari kode Python berikut jika dijalankan?\n\na = 10\nb = 5\na = b\nprint(a)",
                "choices": [
                    {"id": "A", "text": "10"},
                    {"id": "B", "text": "5"},
                    {"id": "C", "text": "15"},
                    {"id": "D", "text": "Error"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Perintah `a = b` mengisi variabel `a` dengan nilai yang dimiliki `b` (yaitu 5). Sehingga saat dicetak, hasilnya adalah 5.",
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Modul 2: Operator Aritmatika & Logika
    # -------------------------------------------------------------------------
    "operator": {
        "id": "operator",
        "topic_id": "dasar-python",
        "topic_title": "Dasar Pemrograman Python",
        "title": "Operator Aritmatika & Logika",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Aritmatika",
                "title": "Operator Aritmatika Khusus Python",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Selain penambahan (<code>+</code>) dan pengurangan (<code>-</code>), Python memiliki operator pembagian khusus yang sangat sering dipakai di kuliah DDP1:",
                    },
                    {
                        "type": "code",
                        "code": '# Pembagian biasa (hasil selalu float)\nprint(7 / 2)   # Hasil: 3.5\n\n# Pembagian bulat / Floor division (//)\nprint(7 // 2)  # Hasil: 3\n\n# Sisa bagi / Modulo (%)\nprint(7 % 2)   # Hasil: 1 (karena 7 = 3 * 2 + 1)',
                    },
                    {
                        "type": "callout",
                        "title": "Ingat Perbedaan Pembagian:",
                        "items": [
                            "<code>//</code> membuang angka di belakang koma (dibulatkan ke bawah).",
                            "<code>%</code> (modulo) mencari sisa pembagian.",
                        ],
                    },
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Berapakah hasil evaluasi dari ekspresi `14 % 4` dalam Python?",
                "choices": [
                    {"id": "A", "text": "3"},
                    {"id": "B", "text": "2"},
                    {"id": "C", "text": "3.5"},
                    {"id": "D", "text": "0"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! 14 dibagi 4 adalah 3 dengan sisa 2 (karena 4 × 3 = 12, dan 14 - 12 = 2). Operator % mengambil nilai sisa tersebut.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Perbandingan",
                "title": "Operator Perbandingan (Relasional)",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Operator perbandingan digunakan untuk membandingkan dua nilai dan selalu menghasilkan nilai boolean (<code>True</code> atau <code>False</code>).",
                    },
                    {
                        "type": "code",
                        "code": 'x = 10\ny = 20\n\nprint(x == y)  # False (Apakah x sama dengan y?)\nprint(x != y)  # True  (Apakah x TIDAK sama dengan y?)\nprint(x < y)   # True  (Apakah x lebih kecil dari y?)',
                    },
                    {
                        "type": "callout",
                        "title": "Jangan Tertukar:",
                        "items": [
                            "<code>=</code> adalah penugasan nilai ke variabel.",
                            "<code>==</code> adalah pengecekan apakah dua nilai bernilai sama.",
                        ],
                    },
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Perhatikan baris kode berikut:\n\na = 15\nb = 15\nprint(a != b)\n\nApa output yang dicetak ke terminal?",
                "choices": [
                    {"id": "A", "text": "True"},
                    {"id": "B", "text": "False"},
                    {"id": "C", "text": "15"},
                    {"id": "D", "text": "Error"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Operator != menanyakan 'apakah a TIDAK SAMA dengan b?'. Karena nilai keduanya sama-sama 15, pernyataan tersebut salah (False).",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Logika Boolean",
                "title": "Operator Logika: and, or, not",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Operator logika menggabungkan beberapa kondisi boolean:",
                    },
                    {
                        "type": "code",
                        "code": '# and: Bernilai True HANYA jika KEDUA kondisi True\nprint(True and False)  # Output: False\n\n# or: Bernilai True jika MINIMAL SALAH SATU kondisi True\nprint(True or False)   # Output: True\n\n# not: Membalikkan nilai (True jadi False, False jadi True)\nprint(not True)        # Output: False',
                    },
                    {
                        "type": "callout",
                        "title": "Trik Cepat Menghafal:",
                        "items": [
                            "<code>and</code> rewel: satu saja False, hasilnya pasti False.",
                            "<code>or</code> santai: satu saja True, hasilnya pasti True.",
                            "<code>not</code> kebalikan: memutarbalikkan kenyataan.",
                        ],
                    },
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Apa output dari ekspresi Python berikut?\n\nprint(not (5 > 10))",
                "choices": [
                    {"id": "A", "text": "True"},
                    {"id": "B", "text": "False"},
                    {"id": "C", "text": "None"},
                    {"id": "D", "text": "Error"},
                ],
                "answer": "A",
                "explanation": "Pilihan A benar! Ekspresi di dalam kurung (5 > 10) menghasilkan False. Operator not membalikkan nilai False tersebut menjadi True.",
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Modul 3: Input & Output Sederhana
    # -------------------------------------------------------------------------
    "input-output": {
        "id": "input-output",
        "topic_id": "dasar-python",
        "topic_title": "Dasar Pemrograman Python",
        "title": "Input & Output Sederhana",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Input Pengguna",
                "title": "Membaca Masukan dengan input()",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Fungsi <code>input()</code> digunakan untuk menerima masukan teks dari pengguna lewat terminal.",
                    },
                    {
                        "type": "code",
                        "code": 'nama = input("Masukkan nama: ")\nprint("Halo,", nama)',
                    },
                    {
                        "type": "callout",
                        "title": "PENTING di DDP1:",
                        "items": [
                            "Fungsi <code>input()</code> <strong>SELALU</strong> mengembalikan tipe data <code>str</code> (String), meskipun pengguna mengetikkan angka!",
                            "Jika ingin digunakan untuk hitungan matematika, kamu wajib mengubahnya dengan <code>int()</code> atau <code>float()</code>.",
                        ],
                    },
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Jika pengguna mengetik angka 25 pada baris berikut:\n\numur = input('Berapa umurmu? ')\n\nApakah tipe data dari variabel `umur`?",
                "choices": [
                    {"id": "A", "text": "int (Integer)"},
                    {"id": "B", "text": "str (String)"},
                    {"id": "C", "text": "float (Float)"},
                    {"id": "D", "text": "number (Number)"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! input() selalu mengembalikan data dalam bentuk String (str). Jika ingin menjadi integer, harus dibungkus int(input(...)).",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Format String",
                "title": "Mencetak dengan f-string yang Rapi",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Cara paling modern dan rapi di Python untuk menggabungkan teks dan variabel adalah dengan <strong>f-string</strong> (huruf <code>f</code> sebelum tanda kutip).",
                    },
                    {
                        "type": "code",
                        "code": 'nama = "Citra"\nskor = 95\n\n# f-string menyisipkan variabel langsung di dalam kurung kurawal {}\npesan = f"Pemain {nama} memperoleh skor {skor}!"\nprint(pesan)',
                    },
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Perhatikan kode berikut:\n\nitem = 'Apel'\nharga = 5000\nprint(f'{item}: Rp{harga}')\n\nApa output yang tercetak?",
                "choices": [
                    {"id": "A", "text": "Apel: Rp5000"},
                    {"id": "B", "text": "{item}: Rp{harga}"},
                    {"id": "C", "text": "Apel Rp5000"},
                    {"id": "D", "text": "Error"},
                ],
                "answer": "A",
                "explanation": "Pilihan A benar! Tanda {item} digantikan dengan 'Apel', dan {harga} digantikan dengan 5000.",
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Modul 4: Percabangan if-else (Topik: Logika & Percabangan)
    # -------------------------------------------------------------------------
    "kondisional-if": {
        "id": "kondisional-if",
        "topic_id": "logika-dasar",
        "topic_title": "Logika & Percabangan",
        "title": "Percabangan if-else",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Percabangan Dasar",
                "title": "Pernyataan if di Python",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Pernyataan <code>if</code> digunakan untuk membuat program mengambil keputusan. Blok kode di dalam <code>if</code> hanya akan dijalankan jika kondisinya bernilai <code>True</code>.",
                    },
                    {
                        "type": "code",
                        "code": 'nilai = 85\n\nif nilai >= 75:\n    print("Selamat, kamu lulus!")  # Dijalankan karena 85 >= 75 bernilai True',
                    },
                    {
                        "type": "callout",
                        "title": "Aturan Indentasi (Spasi Menjorok):",
                        "items": [
                            "Di Python, blok kode di dalam <code>if</code> <strong>wajib menjorok</strong> (indentasi 4 spasi atau 1 tab).",
                            "Jangan lupa tanda titik dua <code>:</code> di akhir baris <code>if</code>.",
                        ],
                    },
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Perhatikan kode berikut:\n\nskor = 60\nif skor > 70:\n    print('Hebat')\nprint('Selesai')\n\nApa output yang tercetak ke terminal?",
                "choices": [
                    {"id": "A", "text": "Hebat\nSelesai"},
                    {"id": "B", "text": "Selesai"},
                    {"id": "C", "text": "Hebat"},
                    {"id": "D", "text": "Tidak mencetak apa pun"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Karena skor > 70 bernilai False (60 tidak lebih besar dari 70), blok 'Hebat' dilewati. Kode langsung mencetak baris berikutnya: 'Selesai'.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Alternatif if",
                "title": "Pernyataan if-else",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Bagian <code>else</code> menjadi 'rencana cadangan'. Blok <code>else</code> akan dieksekusi ketika kondisi pada <code>if</code> bernilai <code>False</code>.",
                    },
                    {
                        "type": "code",
                        "code": 'umur = 15\n\nif umur >= 17:\n    print("Boleh membuat KTP")\nelse:\n    print("Belum cukup umur")',
                    },
                    {
                        "type": "callout",
                        "title": "Catatan else:",
                        "items": [
                            "<code>else</code> tidak memerlukan kondisi tambahan.",
                            "Tepat satu cabang (antara <code>if</code> atau <code>else</code>) yang pasti dieksekusi.",
                        ],
                    },
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Apa output dari kode Python berikut?\n\nx = 10\nif x % 2 == 0:\n    print('Genap')\nelse:\n    print('Ganjil')",
                "choices": [
                    {"id": "A", "text": "Genap"},
                    {"id": "B", "text": "Ganjil"},
                    {"id": "C", "text": "Genap\nGanjil"},
                    {"id": "D", "text": "Error"},
                ],
                "answer": "A",
                "explanation": "Pilihan A benar! 10 % 2 menghasilkan sisa 0, sehingga 0 == 0 bernilai True. Blok if yang mencetak 'Genap' dijalankan.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Banyak Kondisi",
                "title": "Multi-kondisi dengan elif",
                "content_blocks": [
                    {
                        "type": "paragraph",
                        "text": "Jika kamu memiliki lebih dari 2 kemungkinan kondisi, gunakan <code>elif</code> (singkatan dari <em>else if</em>).",
                    },
                    {
                        "type": "code",
                        "code": 'nilai = 78\n\nif nilai >= 85:\n    grade = "A"\nelif nilai >= 70:\n    grade = "B"  # Kondisi ini True pertama kali, maka cabang ini dipilih\nelif nilai >= 55:\n    grade = "C"\nelse:\n    grade = "D"\n\nprint(f"Grade: {grade}")',
                    },
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Perhatikan kode berikut:\n\na = 5\nif a < 3:\n    print('Kecil')\nelif a <= 5:\n    print('Sedang')\nelif a <= 10:\n    print('Besar')\nelse:\n    print('Sangat Besar')\n\nApa outputnya?",
                "choices": [
                    {"id": "A", "text": "Kecil"},
                    {"id": "B", "text": "Sedang"},
                    {"id": "C", "text": "Sedang\nBesar"},
                    {"id": "D", "text": "Besar"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Python mengevaluasi dari atas ke bawah. Saat 'elif a <= 5' bernilai True (karena 5 <= 5), blok tersebut dieksekusi ('Sedang') dan seluruh cabang elif berikutnya langsung diabaikan.",
            },
        ],
    },
    # Materi lanjutan diadaptasi dari slide DDP1 Topic 3.1:
    # Conditionals/Selection (Lintang Matahari Hasani dan Lia Sadita).
    "kondisi-boolean": {
        "id": "kondisi-boolean",
        "topic_id": "logika-dasar",
        "topic_title": "Logika & Percabangan",
        "title": "Kondisi & Logika Boolean",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Nilai Kebenaran",
                "title": "Kondisi Tidak Harus Ditulis sebagai True atau False",
                "content_blocks": [
                    {"type": "paragraph", "text": "Di dalam kondisi, Python menafsirkan nilai sebagai benar (<em>truthy</em>) atau salah (<em>falsy</em>). Angka nol, teks kosong, koleksi kosong, <code>None</code>, dan <code>False</code> termasuk falsy. Angka bukan nol dan teks yang tidak kosong termasuk truthy."},
                    {"type": "code", "code": 'nama = ""\nif nama:\n    print("Nama terisi")\nelse:\n    print("Nama masih kosong")\n\nprint(bool(0))    # False\nprint(bool("0"))  # True: teks ini tidak kosong'},
                    {"type": "callout", "title": "Perhatikan jenis datanya", "items": ["Angka <code>0</code> berbeda dengan teks <code>\"0\"</code>.", "Fungsi <code>bool()</code> membantu melihat nilai kebenaran suatu nilai."]},
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Apa output kode berikut?\n\nteks = '0'\nif teks:\n    print('Terisi')\nelse:\n    print('Kosong')",
                "choices": [{"id": "A", "text": "Kosong"}, {"id": "B", "text": "Terisi"}, {"id": "C", "text": "0"}, {"id": "D", "text": "Error"}],
                "answer": "B",
                "explanation": "Pilihan B benar! '0' adalah teks yang tidak kosong sehingga bernilai truthy. Yang falsy adalah angka 0 atau teks kosong ''.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Menyusun Kondisi",
                "title": "Perbandingan Berantai dan Urutan Operator",
                "content_blocks": [
                    {"type": "paragraph", "text": "Perbandingan menghasilkan <code>True</code> atau <code>False</code>. Python bisa memeriksa rentang dengan perbandingan berantai: <code>0 &lt;= nilai &lt;= 100</code> setara dengan <code>0 &lt;= nilai and nilai &lt;= 100</code>."},
                    {"type": "code", "code": 'nilai = 80\nprint(70 <= nilai < 85)  # True\n\n# and dikerjakan sebelum or\nprint(True or False and False)    # True\nprint((True or False) and False)  # False'},
                    {"type": "callout", "title": "Urutan yang perlu diingat", "items": ["Operasi aritmatika, lalu perbandingan, lalu <code>not</code>, <code>and</code>, dan <code>or</code>.", "Gunakan tanda kurung agar maksud kondisi lebih mudah dibaca.", "Ubah input angka dengan <code>int()</code> sebelum membandingkannya dengan bilangan; <code>'1' &lt; 2</code> menimbulkan TypeError."]},
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Apa hasil ekspresi berikut?\n\nprint(0 <= 5 < 10 and not (5 == 5))",
                "choices": [{"id": "A", "text": "True"}, {"id": "B", "text": "5"}, {"id": "C", "text": "False"}, {"id": "D", "text": "Error"}],
                "answer": "C",
                "explanation": "Pilihan C benar! Rentang 0 <= 5 < 10 bernilai True, tetapi not (5 == 5) bernilai False. True and False menghasilkan False.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Short-Circuit",
                "title": "Python Bisa Berhenti Memeriksa Lebih Awal",
                "content_blocks": [
                    {"type": "paragraph", "text": "Pada <code>and</code>, operand kanan hanya dievaluasi jika operand kiri truthy. Pada <code>or</code>, operand kanan hanya dievaluasi jika operand kiri falsy. Ini disebut <em>short-circuit</em>."},
                    {"type": "code", "code": 'pembagi = 0\n# Bagian kanan dilewati: tidak terjadi pembagian dengan nol\nprint(pembagi != 0 and 10 / pembagi > 2)  # False\n\n# and/or mengembalikan operand, tidak selalu bool\nprint("" or "Tamu")  # Tamu\nprint(0 and 99)      # 0'},
                    {"type": "callout", "title": "Nilai sama atau objek sama?", "items": ["<code>==</code> membandingkan nilai. <code>is</code> memeriksa apakah keduanya merujuk ke objek yang sama.", "Gunakan <code>==</code> untuk membandingkan angka atau teks; gunakan <code>is None</code> untuk memeriksa None."]},
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Apa output berikut?\n\npembagi = 0\nprint(pembagi != 0 and 10 / pembagi > 2)",
                "choices": [{"id": "A", "text": "False"}, {"id": "B", "text": "True"}, {"id": "C", "text": "ZeroDivisionError"}, {"id": "D", "text": "10"}],
                "answer": "A",
                "explanation": "Pilihan A benar! Kondisi pembagi != 0 sudah False. Operator and melewati bagian kanan sehingga pembagian dengan nol tidak dijalankan.",
            },
        ],
    },
    "percabangan-bersarang": {
        "id": "percabangan-bersarang",
        "topic_id": "logika-dasar",
        "topic_title": "Logika & Percabangan",
        "title": "Percabangan Bersarang",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Keputusan Bertingkat",
                "title": "if di Dalam if",
                "content_blocks": [
                    {"type": "paragraph", "text": "Percabangan bersarang (<em>nested if</em>) adalah percabangan di dalam cabang lain. Kondisi di dalam hanya diperiksa jika alur program masuk ke cabang luarnya."},
                    {"type": "code", "code": 'punya_tiket = True\numur = 15\n\nif punya_tiket:\n    if umur >= 17:\n        print("Masuk reguler")\n    else:\n        print("Perlu pendamping")\nelse:\n    print("Beli tiket dahulu")'},
                    {"type": "callout", "title": "Baca dari luar ke dalam", "items": ["Pertama periksa tiket. Jika tiket ada, baru periksa umur.", "Pada contoh ini hasilnya <code>Perlu pendamping</code>."]},
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Apa output berikut?\n\npunya_tiket = False\numur = 20\nif punya_tiket:\n    if umur >= 17:\n        print('Masuk')\n    else:\n        print('Perlu pendamping')\nelse:\n    print('Beli tiket')",
                "choices": [{"id": "A", "text": "Masuk"}, {"id": "B", "text": "Perlu pendamping"}, {"id": "C", "text": "Beli tiket"}, {"id": "D", "text": "Masuk\nBeli tiket"}],
                "answer": "C",
                "explanation": "Pilihan C benar! punya_tiket bernilai False, sehingga seluruh cabang if luar dilewati. Umur tidak diperiksa dan else luar mencetak Beli tiket.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Indentasi",
                "title": "else Ini Milik if yang Mana?",
                "content_blocks": [
                    {"type": "paragraph", "text": "Indentasi menentukan struktur percabangan. <code>else</code> sejajar dengan <code>if</code> pasangannya. Gunakan 4 spasi untuk setiap tingkat dan jangan mencampurkan tab dengan spasi."},
                    {"type": "code", "code": 'nilai = 80\nhadir = False\n\nif nilai >= 75:\n    if hadir:\n        print("Lulus lengkap")\n    else:  # Pasangan if hadir\n        print("Lengkapi kehadiran")\nelse:      # Pasangan if nilai >= 75\n    print("Perbaiki nilai")\n\nprint("Pemeriksaan selesai")'},
                    {"type": "callout", "title": "Di luar semua cabang", "items": ["Baris terakhir tidak menjorok, sehingga tetap dijalankan setelah percabangan selesai."]},
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Apa output berikut?\n\nx = 8\nif x > 5:\n    if x > 10:\n        print('Besar')\n    else:\n        print('Sedang')\nprint('Selesai')",
                "choices": [{"id": "A", "text": "Besar\nSelesai"}, {"id": "B", "text": "Sedang\nSelesai"}, {"id": "C", "text": "Selesai"}, {"id": "D", "text": "Sedang"}],
                "answer": "B",
                "explanation": "Pilihan B benar! x > 5 benar, tetapi x > 10 salah sehingga else dalam mencetak Sedang. Baris di luar percabangan lalu mencetak Selesai.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Memilih Struktur",
                "title": "Beberapa if Berbeda dengan if-elif",
                "content_blocks": [
                    {"type": "paragraph", "text": "Beberapa <code>if</code> terpisah diperiksa satu per satu, sehingga lebih dari satu blok bisa berjalan. Pada satu rangkaian <code>if-elif-else</code>, hanya cabang pertama yang kondisinya benar yang dipilih."},
                    {"type": "code", "code": 'nilai = 90\n\n# Dua pemeriksaan terpisah: mencetak A dan B\nif nilai >= 85:\n    print("A")\nif nilai >= 70:\n    print("B")\n\n# Satu rangkaian: hanya mencetak A\nif nilai >= 85:\n    print("A")\nelif nilai >= 70:\n    print("B")'},
                    {"type": "callout", "title": "Pilih sesuai tujuan", "items": ["Gunakan if-elif untuk kategori yang saling menggantikan, seperti satu nilai huruf.", "Gunakan beberapa if jika setiap kondisi perlu diperiksa secara mandiri."]},
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Apa output berikut?\n\nx = 0\nif x == 0:\n    x += 1\n    print('Pertama')\nif x == 1:\n    print('Kedua')",
                "choices": [{"id": "A", "text": "Pertama"}, {"id": "B", "text": "Kedua"}, {"id": "C", "text": "Tidak ada output"}, {"id": "D", "text": "Pertama\nKedua"}],
                "answer": "D",
                "explanation": "Pilihan D benar! if pertama mengubah x menjadi 1. Karena if kedua adalah pemeriksaan terpisah, kondisinya juga benar dan Kedua ikut dicetak. Jika if kedua diganti elif, cabang itu dilewati.",
            },
        ],
    },

    # -------------------------------------------------------------------------
    # Topik: Perulangan. Diadaptasi dari slide DDP1 Topic 3.2: Repetition
    # (Lintang Matahari Hasani dan Lia Sadita). Contoh dan soal ditulis ulang.
    # -------------------------------------------------------------------------
    "while-loop": {
        "id": "while-loop",
        "topic_id": "perulangan",
        "topic_title": "Perulangan",
        "title": "Perulangan while",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Konsep Perulangan",
                "title": "Mengulang Selama Kondisi Benar",
                "content_blocks": [
                    {"type": "paragraph", "text": "Perulangan menjalankan blok kode berulang kali. <code>while</code> memeriksa kondisi sebelum setiap putaran (iterasi). Jika kondisi benar, blok dijalankan; jika salah, loop berakhir. Kondisi yang salah sejak awal membuat blok tidak dijalankan sama sekali."},
                    {"type": "code", "code": 'sisa = 3\nwhile sisa > 0:\n    print(sisa)\n    sisa -= 1\nprint("Mulai!")\n# Output: 3, 2, 1, lalu Mulai! pada baris terpisah'},
                    {"type": "callout", "title": "Tiga bagian penting", "items": ["Inisialisasi: beri nilai awal sebelum loop.", "Kondisi: tentukan kapan loop boleh berjalan.", "Pembaruan: ubah nilai agar kondisi akhirnya menjadi salah. Gunakan indentasi 4 spasi untuk blok loop."]},
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Apa output kode berikut?\n\nn = 3\nwhile n > 0:\n    n -= 1\n    print(n)",
                "choices": [{"id": "A", "text": "3\n2\n1"}, {"id": "B", "text": "2\n1\n0"}, {"id": "C", "text": "3\n2\n1\n0"}, {"id": "D", "text": "Tidak ada output"}],
                "answer": "B",
                "explanation": "Pilihan B benar! n dikurangi sebelum dicetak. Putaran terakhir dimulai saat n masih 1, lalu n menjadi 0 dan dicetak. Pemeriksaan berikutnya menghentikan loop.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Menghindari Infinite Loop",
                "title": "Pastikan Ada Jalan Keluar",
                "content_blocks": [
                    {"type": "paragraph", "text": "<em>Infinite loop</em> terjadi ketika loop terus berjalan tanpa mencapai penghenti. Misalnya, nilai penghitung tidak berubah atau berubah menjauhi batas. Periksa nilai awal, kondisi, dan pembaruannya bersama-sama."},
                    {"type": "code", "code": '# Versi yang berhenti\nangka = 1\nwhile angka <= 3:\n    print(angka)\n    angka += 1\n\n# Tanpa angka += 1, kondisi selalu benar\n# dan angka 1 akan terus dicetak.'},
                    {"type": "callout", "title": "Saat mencoba di terminal", "items": ["Jika program terjebak loop, tekan Ctrl+C di terminal untuk menghentikannya.", "Perhatikan batas: <code>&lt; 3</code> berbeda dengan <code>&lt;= 3</code>. Letak pembaruan sebelum atau sesudah print juga memengaruhi output."]},
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Kode ini seharusnya mencetak 1, 2, dan 3 lalu berhenti. Baris apa yang perlu ditambahkan di dalam loop setelah print?\n\nn = 1\nwhile n <= 3:\n    print(n)",
                "choices": [{"id": "A", "text": "n -= 1"}, {"id": "B", "text": "n = 1"}, {"id": "C", "text": "n += 1"}, {"id": "D", "text": "print('Selesai')"}],
                "answer": "C",
                "explanation": "Pilihan C benar! n += 1 menaikkan n setiap putaran. Setelah mencetak 3, n menjadi 4 sehingga kondisi n <= 3 salah. Pilihan lain tidak membuat loop ini berhenti.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Sentinel Loop",
                "title": "Berhenti Ketika Nilai Khusus Dimasukkan",
                "content_blocks": [
                    {"type": "paragraph", "text": "<em>Sentinel</em> adalah nilai khusus untuk mengakhiri perulangan, misalnya teks <code>selesai</code>. Polanya: baca input awal, periksa apakah sentinel, proses input biasa, lalu baca input berikutnya. Nilai sentinel tidak ikut diproses."},
                    {"type": "code", "code": 'pesan = input("Pesan (selesai untuk keluar): ")\nwhile pesan != "selesai":\n    print("Pesanmu:", pesan)\n    pesan = input("Pesan berikutnya: ")\nprint("Sampai jumpa!")'},
                    {"type": "callout", "title": "Kapan memakai while?", "items": ["Cocok saat jumlah putaran belum diketahui, seperti menunggu masukan tertentu.", "Input baru di dalam loop penting agar nilai yang diperiksa bisa berubah."]},
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Pengguna memasukkan 'halo', lalu 'selesai'. Berapa kali baris print(pesan) dijalankan?\n\npesan = input()\nwhile pesan != 'selesai':\n    print(pesan)\n    pesan = input()",
                "choices": [{"id": "A", "text": "0 kali"}, {"id": "B", "text": "1 kali"}, {"id": "C", "text": "2 kali"}, {"id": "D", "text": "Tidak berhenti"}],
                "answer": "B",
                "explanation": "Pilihan B benar! halo diproses satu kali. Saat input berikutnya adalah selesai, kondisi menjadi salah dan sentinel tidak dicetak.",
            },
        ],
    },
    "for-range": {
        "id": "for-range",
        "topic_id": "perulangan",
        "topic_title": "Perulangan",
        "title": "Perulangan for & range()",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Menelusuri Urutan",
                "title": "for Mengambil Elemen Satu per Satu",
                "content_blocks": [
                    {"type": "paragraph", "text": "<code>for</code> menelusuri elemen suatu <em>iterable</em>, yaitu sesuatu yang bisa diambil elemennya satu per satu. Contohnya teks, list, dan range. Variabel loop otomatis menerima elemen berikutnya pada setiap putaran."},
                    {"type": "code", "code": 'for huruf in "Aku":\n    print(huruf)\n# Output: A, k, u pada baris terpisah\n\n# List adalah kumpulan nilai dalam kurung siku\nfor buah in ["apel", "jeruk"]:\n    print(buah)'},
                    {"type": "callout", "title": "for atau while?", "items": ["Gunakan for untuk menelusuri urutan atau mengulang sejumlah kali dengan range().", "Gunakan while saat penghentian bergantung pada kondisi yang bisa berubah. Keduanya sering bisa menyelesaikan tugas yang sama."]},
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Apa output kode berikut?\n\nfor huruf in 'Hi':\n    print(huruf)",
                "choices": [{"id": "A", "text": "Hi"}, {"id": "B", "text": "0\n1"}, {"id": "C", "text": "H\ni"}, {"id": "D", "text": "H\nH"}],
                "answer": "C",
                "explanation": "Pilihan C benar! for mengambil karakter H, lalu i. Setiap print membuat baris baru.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Batas Range",
                "title": "range(start, stop, step)",
                "content_blocks": [
                    {"type": "paragraph", "text": "<code>range()</code> mewakili urutan bilangan bulat. <code>range(stop)</code> mulai dari 0 dengan langkah 1. <code>range(start, stop)</code> memakai awal pilihanmu. Batas <code>stop</code> tidak ikut diambil."},
                    {"type": "code", "code": 'for i in range(3):\n    print(i)  # 0, 1, 2: tiga putaran\n\nfor i in range(2, 5):\n    print(i)  # 2, 3, 4\n\nfor i in range(1, 7, 2):\n    print(i)  # 1, 3, 5'},
                    {"type": "callout", "title": "Cek batas akhir", "items": ["Untuk mencetak 1 sampai 5, gunakan <code>range(1, 6)</code>.", "<code>range(3, 3)</code> kosong. Nilai step tidak boleh 0 karena akan menimbulkan ValueError."]},
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Angka apa saja yang dicetak?\n\nfor i in range(2, 9, 3):\n    print(i)",
                "choices": [{"id": "A", "text": "2\n5\n8"}, {"id": "B", "text": "2\n5\n8\n9"}, {"id": "C", "text": "3\n6\n9"}, {"id": "D", "text": "2\n3\n4\n5\n6\n7\n8"}],
                "answer": "A",
                "explanation": "Pilihan A benar! Mulai dari 2 dan tambah 3 setiap putaran: 2, 5, 8. Nilai berikutnya 11 sudah melewati batas 9.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Langkah Negatif & Akumulasi",
                "title": "Menghitung Mundur dan Menjumlahkan Nilai",
                "content_blocks": [
                    {"type": "paragraph", "text": "Step negatif membuat urutan menurun; elemen diambil selama masih lebih besar dari stop. Untuk menghitung total, siapkan variabel akumulator sebelum loop dan tambahkan nilai di dalam loop."},
                    {"type": "code", "code": 'total = 0\nfor angka in range(6, 0, -2):\n    total += angka\nprint(total)  # 6 + 4 + 2 = 12\n\n# Arah tidak cocok: tidak ada putaran\nfor angka in range(1, 5, -1):\n    print(angka)'},
                    {"type": "callout", "title": "Letak inisialisasi", "items": ["Letakkan <code>total = 0</code> sebelum loop agar total tidak direset pada setiap putaran.", "Batas stop tetap tidak termasuk, baik step positif maupun negatif."]},
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Berapa total yang dicetak?\n\ntotal = 0\nfor angka in range(5, 0, -2):\n    total += angka\nprint(total)",
                "choices": [{"id": "A", "text": "15"}, {"id": "B", "text": "8"}, {"id": "C", "text": "0"}, {"id": "D", "text": "9"}],
                "answer": "D",
                "explanation": "Pilihan D benar! range(5, 0, -2) memberikan 5, 3, dan 1. Totalnya 9; batas 0 tidak ikut diambil.",
            },
        ],
    },
    "kontrol-perulangan": {
        "id": "kontrol-perulangan",
        "topic_id": "perulangan",
        "topic_title": "Perulangan",
        "title": "break, continue & Loop else",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Berhenti Lebih Awal",
                "title": "break Mengakhiri Loop",
                "content_blocks": [
                    {"type": "paragraph", "text": "<code>break</code> langsung keluar dari loop terdekat yang membungkusnya. Sisa kode di dalam loop dilewati, lalu program melanjutkan kode setelah loop. Perintah ini dapat dipakai pada while maupun for."},
                    {"type": "code", "code": 'for angka in range(1, 6):\n    if angka == 3:\n        break\n    print(angka)\nprint("Selesai")\n# Output: 1, 2, Selesai pada baris terpisah'},
                    {"type": "callout", "title": "Letak break berpengaruh", "items": ["Angka 3 tidak dicetak karena break dijalankan sebelum print.", "Gunakan saat tujuan sudah tercapai, misalnya nilai yang dicari ditemukan."]},
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Apa output berikut?\n\nn = 4\nwhile n > 0:\n    n -= 1\n    if n == 2:\n        break\n    print(n)\nprint('Akhir')",
                "choices": [{"id": "A", "text": "3\n2\nAkhir"}, {"id": "B", "text": "3\nAkhir"}, {"id": "C", "text": "4\n3\nAkhir"}, {"id": "D", "text": "Akhir"}],
                "answer": "B",
                "explanation": "Pilihan B benar! Putaran pertama mencetak 3. Pada putaran kedua n menjadi 2 dan break menghentikan loop sebelum print(n). Kode setelah loop tetap mencetak Akhir.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Melewati Satu Putaran",
                "title": "continue Melanjutkan ke Putaran Berikutnya",
                "content_blocks": [
                    {"type": "paragraph", "text": "<code>continue</code> melewati sisa kode pada putaran saat ini. Pada for, loop mengambil elemen berikutnya. Pada while, kondisi diperiksa kembali. Berbeda dari break, continue tidak mengakhiri seluruh loop."},
                    {"type": "code", "code": 'n = 0\nwhile n < 4:\n    n += 1\n    if n == 2:\n        continue\n    print(n)\n# Output: 1, 3, 4 pada baris terpisah'},
                    {"type": "callout", "title": "Hati-hati dengan while", "items": ["Pastikan pembaruan penghitung tidak terus dilewati oleh continue. Contoh ini memperbarui n sebelum continue.", "Gunakan break dan continue secukupnya agar alur tetap mudah dibaca."]},
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Apa output berikut?\n\nfor n in range(1, 5):\n    if n % 2 == 0:\n        continue\n    print(n)",
                "choices": [{"id": "A", "text": "2\n4"}, {"id": "B", "text": "1"}, {"id": "C", "text": "1\n3"}, {"id": "D", "text": "1\n2\n3\n4"}],
                "answer": "C",
                "explanation": "Pilihan C benar! Angka genap 2 dan 4 memicu continue sehingga print dilewati. Angka ganjil 1 dan 3 tetap dicetak.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Loop else",
                "title": "else Berjalan Jika Loop Selesai Tanpa break",
                "content_blocks": [
                    {"type": "paragraph", "text": "Loop while dan for bisa mempunyai <code>else</code>. Bagian ini berjalan ketika while selesai karena kondisinya salah, atau for kehabisan elemen. Jika loop dihentikan oleh break, else dilewati. continue tidak mencegah else berjalan ketika loop akhirnya selesai normal."},
                    {"type": "code", "code": 'n = 2\nwhile n > 0:\n    print(n)\n    n -= 1\nelse:\n    print("Hitungan selesai")\n\nfor angka in range(3):\n    if angka == 1:\n        break\nelse:\n    print("Baris ini dilewati")'},
                    {"type": "callout", "title": "Pasangan loop", "items": ["else sejajar dengan while atau for pasangannya, bukan dengan if di dalam loop.", "else juga berjalan jika sejak awal loop tidak mempunyai putaran, selama tidak ada break yang dijalankan."]},
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Apa output kode berikut?\n\nfor n in range(3):\n    if n == 1:\n        break\nelse:\n    print('Lengkap')\nprint('Selesai')",
                "choices": [{"id": "A", "text": "Selesai"}, {"id": "B", "text": "Lengkap\nSelesai"}, {"id": "C", "text": "Lengkap"}, {"id": "D", "text": "Tidak ada output"}],
                "answer": "A",
                "explanation": "Pilihan A benar! break saat n bernilai 1 membuat else loop dilewati. print setelah seluruh loop tetap mencetak Selesai.",
            },
        ],
    },
    "perulangan-bersarang": {
        "id": "perulangan-bersarang",
        "topic_id": "perulangan",
        "topic_title": "Perulangan",
        "title": "Perulangan Bersarang",
        "xp_reward": 50,
        "steps": [
            {
                "id": "step-1",
                "type": "material",
                "badge": "Nested Loop",
                "title": "Satu Loop di Dalam Loop Lain",
                "content_blocks": [
                    {"type": "paragraph", "text": "Perulangan bersarang memiliki loop dalam dan loop luar. Setiap putaran loop luar menjalankan loop dalam dari awal. Jika loop luar memiliki 2 putaran dan loop dalam selalu 3 putaran, blok terdalam berjalan 2 × 3 = 6 kali."},
                    {"type": "code", "code": 'for baris in range(1, 3):\n    for kolom in range(1, 4):\n        print(baris, kolom)\n# Pasangan: 1 1, 1 2, 1 3, 2 1, 2 2, 2 3'},
                    {"type": "callout", "title": "Baca per tingkat", "items": ["Loop dalam diindentasi satu tingkat di bawah loop luar.", "Perkalian jumlah putaran berlaku jika banyak putaran loop dalam tetap dan tidak ada penghentian lebih awal."]},
                ],
            },
            {
                "id": "step-2",
                "type": "quiz",
                "badge": "Latihan 1",
                "question": "Berapa kali kata Halo dicetak?\n\nfor i in range(3):\n    for j in range(2):\n        print('Halo')",
                "choices": [{"id": "A", "text": "2 kali"}, {"id": "B", "text": "3 kali"}, {"id": "C", "text": "5 kali"}, {"id": "D", "text": "6 kali"}],
                "answer": "D",
                "explanation": "Pilihan D benar! Loop luar berjalan 3 kali dan masing-masing menjalankan 2 putaran loop dalam. Totalnya 3 × 2 = 6 kali.",
            },
            {
                "id": "step-3",
                "type": "material",
                "badge": "Nested while",
                "title": "Reset Penghitung Loop Dalam",
                "content_blocks": [
                    {"type": "paragraph", "text": "Pada nested while, penghitung loop dalam perlu dikembalikan ke nilai awal setiap putaran loop luar. Jika tidak, setelah loop dalam selesai sekali, kondisinya bisa tetap salah pada putaran luar berikutnya."},
                    {"type": "code", "code": 'baris = 1\nwhile baris <= 2:\n    kolom = 1  # Reset untuk setiap baris\n    while kolom <= 2:\n        print(baris, kolom)\n        kolom += 1\n    baris += 1'},
                    {"type": "callout", "title": "Dua penghitung, dua pembaruan", "items": ["kolom bertambah di dalam loop dalam, sedangkan baris bertambah setelah loop dalam selesai.", "Jika memakai break pada loop dalam, hanya loop dalam itu yang dihentikan; loop luar tetap melanjutkan putarannya."]},
                ],
            },
            {
                "id": "step-4",
                "type": "quiz",
                "badge": "Latihan 2",
                "question": "Agar loop dalam mencetak dua kolom pada setiap baris, di mana kolom = 1 sebaiknya diletakkan?",
                "choices": [{"id": "A", "text": "Sekali saja sebelum loop luar"}, {"id": "B", "text": "Di dalam loop luar, tepat sebelum loop dalam"}, {"id": "C", "text": "Setelah semua loop selesai"}, {"id": "D", "text": "Di dalam loop dalam, pada setiap putaran"}],
                "answer": "B",
                "explanation": "Pilihan B benar! Penghitung kolom direset setiap kali baris baru dimulai. Jika direset pada setiap putaran loop dalam, penghitung justru bisa tidak pernah mencapai batas keluar.",
            },
            {
                "id": "step-5",
                "type": "material",
                "badge": "Pola Bintang",
                "title": "Membuat Segitiga dengan Nested for",
                "content_blocks": [
                    {"type": "paragraph", "text": "Loop luar menentukan baris, sedangkan loop dalam menentukan berapa bintang pada baris itu. Jumlah putaran loop dalam boleh bergantung pada nilai loop luar."},
                    {"type": "code", "code": 'tinggi = 3\nfor baris in range(1, tinggi + 1):\n    for kolom in range(baris):\n        print("*", end="")\n    print()\n# Output:\n# *\n# **\n# ***'},
                    {"type": "callout", "title": "Mengatur pergantian baris", "items": ["<code>end=\"\"</code> membuat print tidak berpindah baris setelah mencetak bintang.", "<code>print()</code> setelah loop dalam membuat baris baru. Di sini total bintang adalah 1 + 2 + 3, bukan 3 × 3."]},
                ],
            },
            {
                "id": "step-6",
                "type": "quiz",
                "badge": "Latihan 3",
                "question": "Berapa total bintang yang dicetak oleh kode ini?\n\nfor baris in range(1, 5):\n    for kolom in range(baris):\n        print('*', end='')\n    print()",
                "choices": [{"id": "A", "text": "4"}, {"id": "B", "text": "16"}, {"id": "C", "text": "10"}, {"id": "D", "text": "15"}],
                "answer": "C",
                "explanation": "Pilihan C benar! range(1, 5) memberikan baris 1, 2, 3, dan 4. Jumlah bintang per baris mengikuti nilai baris, sehingga totalnya 1 + 2 + 3 + 4 = 10.",
            },
        ],
    },
}
