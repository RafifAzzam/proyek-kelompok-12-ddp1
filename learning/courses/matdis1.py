"""
Data materi dan kuis untuk Matematika Diskret 1 (Matdis 1).
Disusun menggunakan arsitektur OOP CodeQuest.
"""
from .base import Course, Topic, Lesson, Step


# =============================================================================
# Modul 1: Proposisi & Tabel Kebenaran
# =============================================================================
steps_prop_logic = [
    Step(
        id="step-1",
        type="material",
        badge="Konsep Dasar",
        title="Apa Itu Proposisi?",
        content_blocks=[
            {
                "type": "paragraph",
                "text": "Dalam logika matematika, <strong>proposisi</strong> adalah sebuah kalimat deklaratif yang bernilai <em>benar (True / T)</em> atau <em>salah (False / F)</em>, tetapi tidak bisa bernilai keduanya sekaligus.",
            },
            {
                "type": "callout",
                "title": "Contoh Proposisi vs Bukan Proposisi:",
                "items": [
                    "✅ <code>2 + 3 = 5</code> &rarr; Proposisi bernilai <strong>Benar (True)</strong>.",
                    "✅ <code>Jakarta adalah ibukota Australia</code> &rarr; Proposisi bernilai <strong>Salah (False)</strong>.",
                    "❌ <code>Jam berapa sekarang?</code> &rarr; Bukan proposisi (kalimat tanya).",
                    "❌ <code>x + 2 = 10</code> &rarr; Bukan proposisi (kalimat terbuka yang nilai kebenarannya belum pasti).",
                ],
            },
        ],
    ),
    Step(
        id="step-2",
        type="quiz",
        badge="Latihan 1",
        question="Di antara kalimat-kalimat berikut, manakah yang merupakan sebuah PROPOSISI?",
        choices=[
            {"id": "A", "text": "Tolong ambilkan buku itu di atas meja!"},
            {"id": "B", "text": "Bulan November memiliki 30 hari."},
            {"id": "C", "text": "Berapa hasil dari 15 dikali 4?"},
            {"id": "D", "text": "x - 5 > 0"},
        ],
        answer="B",
        explanation="Pilihan B benar! 'Bulan November memiliki 30 hari' adalah pernyataan deklaratif dengan nilai kebenaran pasti (True). Pilihan A adalah perintah, C adalah pertanyaan, dan D adalah kalimat terbuka.",
    ),
    Step(
        id="step-3",
        type="material",
        badge="Operator Logika",
        title="Negasi, Konjungsi, dan Disjungsi",
        content_blocks=[
            {
                "type": "paragraph",
                "text": "Kita dapat menggabungkan proposisi tunggal menjadi proposisi majemuk menggunakan kata perangkai logika dasar:",
            },
            {
                "type": "code",
                "code": "Negasi (~p)       : NOT - Membalik nilai kebenaran (True -> False, False -> True)\nKonjungsi (p ^ q) : AND - Bernilai True HANYA JIKA kedua p dan q bernilai True\nDisjungsi (p v q) : OR  - Bernilai True JIKA SALAH SATU atau kedua p dan q bernilai True",
            },
            {
                "type": "callout",
                "title": "Kunci Mudah Mengingat:",
                "items": [
                    "<strong>Konjungsi (AND)</strong> bersifat 'ketat': ada 1 saja yang False, hasilnya langsung False.",
                    "<strong>Disjungsi (OR)</strong> bersifat 'ramah': ada 1 saja yang True, hasilnya langsung True.",
                ],
            },
        ],
    ),
    Step(
        id="step-4",
        type="quiz",
        badge="Latihan 2",
        question="Diketahui proposisi p bernilai True dan proposisi q bernilai False. Berapakah nilai kebenaran dari: p AND (NOT q)?",
        choices=[
            {"id": "A", "text": "True"},
            {"id": "B", "text": "False"},
            {"id": "C", "text": "Tidak dapat ditentukan"},
            {"id": "D", "text": "Sama dengan nilai q"},
        ],
        answer="A",
        explanation="Pilihan A benar! Karena q = False, maka (NOT q) = True. Sehingga p AND (NOT q) menjadi True AND True = True.",
    ),
    Step(
        id="step-5",
        type="material",
        badge="Implikasi",
        title="Implikasi Kondisional (Jika p maka q)",
        content_blocks=[
            {
                "type": "paragraph",
                "text": "Kondisional atau <strong>implikasi</strong> dilambangkan dengan <code>p &rarr; q</code> ('Jika p maka q'). Proposisi p disebut premis/hipotesis, dan q disebut konklusi/kesimpulan.",
            },
            {
                "type": "callout",
                "title": "Aturan Emas Implikasi:",
                "items": [
                    "Implikasi <code>p &rarr; q</code> bernilai <strong>False</strong> HANYA KETIKA premis <code>p = True</code> tetapi konklusi <code>q = False</code>.",
                    "Jika premis <code>p = False</code>, maka implikasi secara otomatis <strong>selalu bernilai True</strong> apa pun nilai q (kebenaran hampa / <em>vacuous truth</em>).",
                ],
            },
        ],
    ),
    Step(
        id="step-6",
        type="quiz",
        badge="Latihan 3",
        question="Jika premis p bernilai False dan konklusi q bernilai False, maka nilai kebenaran dari implikasi p -> q adalah...",
        choices=[
            {"id": "A", "text": "False"},
            {"id": "B", "text": "True"},
            {"id": "C", "text": "Tidak terdefinisi"},
            {"id": "D", "text": "Error logika"},
        ],
        answer="B",
        explanation="Pilihan B benar! Saat premis bernilai False, implikasi p -> q selalu bernilai True (vacuous truth).",
    ),
]

lesson_prop_logic = Lesson(
    id="matdis-prop-logic",
    title="Proposisi & Tabel Kebenaran",
    duration="6 menit",
    summary="Memahami pengertian proposisi, nilai kebenaran, negasi, konjungsi, disjungsi, dan implikasi.",
    xp_reward=50,
    is_locked=False,
    steps=steps_prop_logic,
    topic_id="logika-proposisi",
    topic_title="Logika Proposisi & Himpunan",
    course_id="matdis1",
)

lesson_set_basics = Lesson(
    id="matdis-set-basics",
    title="Dasar Operasi Himpunan",
    duration="7 menit",
    summary="Mengenal himpunan, diagram Venn, operasi irisan, gabungan, komplemen, dan hukum De Morgan.",
    xp_reward=50,
    is_locked=True,
    steps=[
        Step(
            id="step-1",
            type="material",
            badge="Konsep Dasar",
            title="Pengertian Himpunan",
            content_blocks=[
                {
                    "type": "paragraph",
                    "text": "<strong>Himpunan</strong> adalah kumpulan objek-objek berbeda yang terdefinisi dengan jelas (well-defined). Objek dalam himpunan disebut elemen atau anggota.",
                }
            ],
        )
    ],
    topic_id="logika-proposisi",
    topic_title="Logika Proposisi & Himpunan",
    course_id="matdis1",
)

topic_logika = Topic(
    id="logika-proposisi",
    title="Logika Proposisi & Himpunan",
    description="Fondasi logika matematika simbolik, tabel kebenaran, perangkai logika, dan relasi himpunan.",
    badge="🧠",
    lessons=[lesson_prop_logic, lesson_set_basics],
)

course_matdis1 = Course(
    id="matdis1",
    name="Matematika Diskret 1",
    code="CSGE601010",
    icon="📐",
    description="Pelajari logika matematika, pembuktian formal, teori himpunan, relasi, dan fungsi di Fasilkom.",
    topics=[topic_logika],
)
