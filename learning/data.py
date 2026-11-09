"""
Data materi dan kuis untuk CodeQuest (Milestone 1).
Dikelola di sini agar mudah diedit bersama tim tanpa memicu konflik migrasi database di awal.
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
        "content_blocks": [
            {
                "type": "paragraph",
                "text": "Dalam Python, <strong>variabel</strong> diibaratkan seperti wadah berlabel untuk menyimpan nilai atau data di memori komputer.",
            },
            {
                "type": "code",
                "code": '# Membuat variabel dan menyimpan nilai\nnama = "Budi"       # Tipe data teks (String / str)\numur = 18           # Tipe data bilangan bulat (Integer / int)\ntinggi = 172.5      # Tipe data desimal (Float / float)\nis_mahasiswa = True # Tipe data kebenaran (Boolean / bool)\n\nprint("Halo,", nama)',
            },
            {
                "type": "callout",
                "title": "Aturan Penting Penamaan Variabel di Python:",
                "items": [
                    "Harus diawali huruf (a-z, A-Z) atau garis bawah (<em>underscore</em> <code>_</code>).",
                    "Tidak boleh diawali angka (contoh salah: <code>1nama</code>).",
                    "Tidak boleh menggunakan spasi (gunakan format <em>snake_case</em>, misalnya: <code>total_skor</code>).",
                    "Python bersifat <em>case-sensitive</em>: <code>umur</code> dan <code>Umur</code> adalah dua variabel yang berbeda.",
                ],
            },
        ],
        "questions": [
            {
                "id": 1,
                "question": "Di antara pilihan nama variabel berikut, manakah yang VALID menurut aturan Python?",
                "choices": [
                    {"id": "A", "text": "2_skor_pemain"},
                    {"id": "B", "text": "skor-pemain"},
                    {"id": "C", "text": "skor_pemain"},
                    {"id": "D", "text": "skor pemain"},
                ],
                "answer": "C",
                "explanation": "Pilihan C benar! Nama variabel di Python boleh menggunakan huruf dan underscore, tidak boleh memakai spasi (D), tanda hubung minus (B), atau diawali angka (A).",
            },
            {
                "id": 2,
                "question": "Perhatikan baris kode berikut:\n`nilai = 3.14`\nApakah tipe data dari variabel `nilai`?",
                "choices": [
                    {"id": "A", "text": "int (Integer)"},
                    {"id": "B", "text": "float (Floating Point)"},
                    {"id": "C", "text": "str (String)"},
                    {"id": "D", "text": "bool (Boolean)"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Angka yang memiliki koma/titik desimal di Python dikelompokkan sebagai tipe data `float`.",
            },
            {
                "id": 3,
                "question": "Apa output dari kode Python berikut jika dijalankan?\n\na = 10\nb = 5\na = b\nprint(a)",
                "choices": [
                    {"id": "A", "text": "10"},
                    {"id": "B", "text": "5"},
                    {"id": "C", "text": "15"},
                    {"id": "D", "text": "Error"},
                ],
                "answer": "B",
                "explanation": "Pilihan B benar! Perintah `a = b` menimpa nilai variabel `a` dengan nilai yang ada pada `b` (yaitu 5). Sehingga saat dicetak, nilainya adalah 5.",
            },
        ],
    }
}
