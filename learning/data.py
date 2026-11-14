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
]

LESSONS_DATA = {
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
}
