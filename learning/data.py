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
                "summary": "Melakukan operasi matematika dan perbandingan nilai dalam Python.",
                "is_locked": True,
            },
            {
                "id": "input-output",
                "title": "Input & Output Sederhana",
                "duration": "5 menit",
                "summary": "Membaca masukan pengguna dengan input() dan mencetak hasil dengan print().",
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
        ],
    },
]

LESSONS_DATA = {
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
    }
}
