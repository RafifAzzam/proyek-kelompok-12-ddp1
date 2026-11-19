"""
Kelas dasar OOP (Object-Oriented Programming) untuk arsitektur pembelajaran CodeQuest.
Mendukung hirarki: Course -> Topic -> Lesson -> Step.
"""


class Step:
    """
    Mewakili satu langkah interaktif dalam pelajaran.
    Bisa berupa tipe 'material' (penjelasan materi) atau 'quiz' (latihan kuis interaktif).
    """

    def __init__(
        self,
        id,
        type,
        badge,
        title=None,
        content_blocks=None,
        question=None,
        choices=None,
        answer=None,
        explanation=None,
        image=None,
        image_caption=None,
    ):
        self.id = id
        self.type = type
        self.badge = badge
        self.title = title
        self.content_blocks = content_blocks or []
        self.question = question
        self.choices = choices or []
        self.answer = answer
        self.explanation = explanation
        self.image = image
        self.image_caption = image_caption

    def to_dict(self):
        """
        Mengonversi objek Step menjadi dictionary untuk serialisasi JSON ke frontend.
        """
        data = {
            "id": self.id,
            "type": self.type,
            "badge": self.badge,
        }
        if self.type == "material":
            data["title"] = self.title
            data["content_blocks"] = self.content_blocks
        elif self.type == "quiz":
            data.update(
                {
                    "question": self.question,
                    "choices": self.choices,
                    "answer": self.answer,
                    "explanation": self.explanation,
                    "image": self.image,
                    "image_caption": self.image_caption,
                }
            )
        return data

    def __getitem__(self, item):
        """Mempertahankan kompatibilitas akses gaya dictionary (step['type'])."""
        if item == "content_blocks":
            return self.content_blocks
        if item == "choices":
            return self.choices
        return getattr(self, item)


class Lesson:
    """
    Mewakili satu modul pembelajaran atau kuis utuh bergaya Duolingo interleaved.
    """

    def __init__(
        self,
        id,
        title,
        duration,
        summary,
        xp_reward=50,
        is_locked=True,
        steps=None,
        topic_id=None,
        topic_title=None,
        course_id=None,
    ):
        self.id = id
        self.title = title
        self.duration = duration
        self.summary = summary
        self.xp_reward = xp_reward
        self.is_locked = is_locked
        self.steps = steps or []
        self.topic_id = topic_id
        self.topic_title = topic_title
        self.course_id = course_id

    def steps_as_dict(self):
        """Mengembalikan seluruh steps dalam bentuk dictionary murni untuk json.dumps()."""
        return [s.to_dict() if isinstance(s, Step) else s for s in self.steps]

    def __getitem__(self, item):
        """Mempertahankan kompatibilitas akses gaya dictionary (lesson['steps'])."""
        if item == "steps":
            return self.steps_as_dict()
        return getattr(self, item)

    def get(self, item, default=None):
        """Mempertahankan dukungan method .get() seperti pada dictionary."""
        try:
            return self[item]
        except AttributeError:
            return default


class Topic:
    """
    Mewakili kelompok subbab materi dalam suatu mata kuliah (contoh: Dasar Python, String, dsb).
    """

    def __init__(self, id, title, description, badge, lessons=None):
        self.id = id
        self.title = title
        self.description = description
        self.badge = badge
        self.lessons = lessons or []

    def __getitem__(self, item):
        return getattr(self, item)


class Course:
    """
    Mewakili satu mata kuliah utuh (contoh: DDP1, Matematika Diskret 1, dsb).
    """

    def __init__(self, id, name, code, icon, description, topics=None):
        self.id = id
        self.name = name
        self.code = code
        self.icon = icon
        self.description = description
        self.topics = topics or []

    def get_lessons_map(self):
        """
        Menghasilkan pemetaan dict {lesson_id: Lesson} untuk seluruh pelajaran di matkul ini.
        Sekaligus memastikan referensi course_id, topic_id, dan topic_title terisi.
        """
        lessons_map = {}
        for topic in self.topics:
            for lesson in topic.lessons:
                lesson.course_id = self.id
                lesson.topic_id = topic.id
                lesson.topic_title = topic.title
                lessons_map[lesson.id] = lesson
        return lessons_map

    def __getitem__(self, item):
        return getattr(self, item)
