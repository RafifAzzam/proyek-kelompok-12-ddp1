import json
from django.http import Http404
from django.shortcuts import render
from .data import COURSES, LESSONS_DATA, TOPICS


def home(request):
    """
    Menampilkan dashboard utama berisi daftar topik dan materi CodeQuest.
    Mendukung penyaringan mata kuliah via query parameter (?course=<course_id>).
    """
    course_id = request.GET.get("course", "ddp1")
    selected_course = COURSES.get(course_id)
    if not selected_course:
        selected_course = COURSES.get("ddp1")

    context = {
        "courses": list(COURSES.values()),
        "selected_course": selected_course,
        "topics": selected_course.topics if selected_course else [],
    }
    return render(request, "learning/home.html", context)


def lesson_detail(request, lesson_id):
    """
    Menampilkan alur selang-seling (materi & kuis) bergaya Duolingo.
    """
    lesson = LESSONS_DATA.get(lesson_id)
    if not lesson:
        raise Http404("Pelajaran tidak ditemukan.")

    steps_data = lesson.steps_as_dict() if hasattr(lesson, "steps_as_dict") else lesson["steps"]
    context = {
        "lesson": lesson,
        "steps_json": json.dumps(steps_data),
    }
    return render(request, "learning/lesson.html", context)
