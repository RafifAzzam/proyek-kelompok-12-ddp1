from django.test import TestCase
from django.urls import reverse
from .data import LESSONS_DATA


class LearningViewsTest(TestCase):
    def test_home_page_status_and_content(self):
        """Memastikan halaman dashboard home bisa diakses dan memuat data topik."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/home.html")
        self.assertContains(response, "CodeQuest")
        self.assertContains(response, "Dasar Pemrograman Python")
        self.assertContains(response, "Variabel &amp; Tipe Data")
        self.assertContains(response, "Operator Aritmatika &amp; Logika")
        self.assertContains(response, "Logika &amp; Percabangan")

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
        self.assertEqual(step_types, ["material", "quiz", "material", "quiz", "material", "quiz"])

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

    def test_lesson_detail_page_not_found(self):
        """Memastikan modul yang tidak terdaftar menghasilkan 404."""
        response = self.client.get(reverse("lesson_detail", args=["modul-tidak-ada"]))
        self.assertEqual(response.status_code, 404)
