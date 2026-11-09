from django.test import TestCase
from django.urls import reverse


class LearningViewsTest(TestCase):
    def test_home_page_status_and_content(self):
        """Memastikan halaman dashboard home bisa diakses dan memuat data topik."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/home.html")
        self.assertContains(response, "CodeQuest")
        self.assertContains(response, "Dasar Pemrograman Python")
        self.assertContains(response, "Variabel &amp; Tipe Data")

    def test_lesson_detail_page_success(self):
        """Memastikan halaman materi pertama berhasil dibuka beserta kuisnya."""
        response = self.client.get(reverse("lesson_detail", args=["variabel"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning/lesson.html")
        self.assertContains(response, "Variabel &amp; Tipe Data")
        self.assertContains(response, "Periksa Jawaban")
        # Memastikan data soal ter-serialisasi ke context
        self.assertIn("questions_json", response.context)

    def test_lesson_detail_page_not_found(self):
        """Memastikan modul yang tidak terdaftar menghasilkan 404."""
        response = self.client.get(reverse("lesson_detail", args=["modul-tidak-ada"]))
        self.assertEqual(response.status_code, 404)
