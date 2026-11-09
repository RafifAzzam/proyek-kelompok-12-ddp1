import json
from django.http import Http404
from django.shortcuts import render
from .data import TOPICS, LESSONS_DATA


def home(request):
    """
    Menampilkan dashboard utama berisi daftar topik dan materi CodeQuest.
    """
    context = {
        "topics": TOPICS,
    }
    return render(request, "learning/home.html", context)


def lesson_detail(request, lesson_id):
    """
    Menampilkan materi dan kuis interaktif untuk pelajaran tertentu.
    """
    lesson = LESSONS_DATA.get(lesson_id)
    if not lesson:
        raise Http404("Pelajaran tidak ditemukan.")

    context = {
        "lesson": lesson,
        # Serialisasi soal untuk engine kuis JavaScript di frontend
        "questions_json": json.dumps(lesson["questions"]),
    }
    return render(request, "learning/lesson.html", context)
