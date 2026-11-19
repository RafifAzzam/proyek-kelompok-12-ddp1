from django.test import TestCase
from django.urls import reverse
from .courses.base import Course, Lesson, Step, Topic
from .data import COURSES, LESSONS_DATA


class LearningViewsTest(TestCase):
    def test_home_page_status_and_content(self):
        """Memastikan halaman dashboard home bisa diakses dan memuat data topik DDP1 secara default."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/home.html")
        self.assertContains(response, "CodeQuest")
        self.assertContains(response, "Dasar Pemrograman Python")
        self.assertContains(response, "Variabel &amp; Tipe Data")
        self.assertContains(response, "Operator Aritmatika &amp; Logika")
        self.assertContains(response, "Logika &amp; Percabangan")
        # Memastikan dropdown option-box pemilih matkul ada di halaman
        self.assertContains(response, 'id="course-select"')
        self.assertContains(response, "CSGE601020")

    def test_home_page_with_course_param_matdis1(self):
        """Memastikan filter matkul ?course=matdis1 merender konten Matematika Diskret 1."""
        response = self.client.get(reverse("home"), {"course": "matdis1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Matematika Diskret 1")
        self.assertContains(response, "CSGE601010")
        self.assertContains(response, "Logika Proposisi &amp; Himpunan")
        self.assertContains(response, "Proposisi &amp; Tabel Kebenaran")

    def test_home_page_invalid_course_fallback(self):
        """Memastikan parameter matkul yang tidak valid fallback secara anggun ke DDP1."""
        response = self.client.get(reverse("home"), {"course": "matkul-gaib"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dasar Pemrograman Python")

    def test_lesson_detail_interleaved_steps_success(self):
        """Memastikan halaman materi selang-seling berhasil dibuka beserta steps datanya."""
        response = self.client.get(reverse("lesson_detail", args=["variabel"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/lesson.html")
        self.assertContains(response, "Variabel &amp; Tipe Data")
        self.assertIn("steps_json", response.context)

        # Validasi struktur data selang-seling modul 1
        steps = LESSONS_DATA["variabel"]["steps"]
        self.assertEqual(len(steps), 6)
        step_types = [s["type"] for s in steps]
        self.assertEqual(
            step_types, ["material", "quiz", "material", "quiz", "material", "quiz"]
        )

    def test_lesson_detail_operator_module_success(self):
        """Memastikan modul operator aritmatika & logika bisa diakses."""
        response = self.client.get(reverse("lesson_detail", args=["operator"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/lesson.html")
        self.assertContains(response, "Operator Aritmatika &amp; Logika")
        self.assertIn("steps_json", response.context)

    def test_lesson_detail_conditional_module_success(self):
        """Memastikan modul percabangan if-else (subbab berikutnya) bisa diakses."""
        response = self.client.get(reverse("lesson_detail", args=["kondisional-if"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/lesson.html")
        self.assertContains(response, "Percabangan if-else")
        self.assertIn("steps_json", response.context)

    def test_lesson_detail_matdis_module_success(self):
        """Memastikan modul Matematika Diskret 1 bisa diakses via lesson_detail."""
        response = self.client.get(reverse("lesson_detail", args=["matdis-prop-logic"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/lesson.html")
        self.assertContains(response, "Proposisi &amp; Tabel Kebenaran")
        self.assertIn("steps_json", response.context)
        # Pastikan tombol keluar mengarah kembali ke ?course=matdis1
        self.assertContains(response, "?course=matdis1")

    def test_lesson_detail_page_not_found(self):
        """Memastikan modul yang tidak terdaftar menghasilkan 404."""
        response = self.client.get(reverse("lesson_detail", args=["modul-tidak-ada"]))
        self.assertEqual(response.status_code, 404)

    def test_oop_classes_integrity(self):
        """Memastikan method to_dict(), steps_as_dict(), dan dictionary indexing berfungsi."""
        step = Step(id="s1", type="material", badge="Info", title="Intro", content_blocks=[])
        step_dict = step.to_dict()
        self.assertEqual(step_dict["id"], "s1")
        self.assertEqual(step["type"], "material")

        lesson = Lesson(
            id="l1",
            title="Lesson Test",
            duration="5 menit",
            summary="Ringkasan",
            steps=[step],
        )
        self.assertEqual(len(lesson.steps_as_dict()), 1)
        self.assertEqual(lesson["title"], "Lesson Test")
        self.assertEqual(lesson["steps"][0]["id"], "s1")
