"""
Data Registry utama untuk CodeQuest.
Menyediakan mapping seluruh mata kuliah, topik, dan pelajaran (lessons)
berbasis arsitektur OOP.
"""
from .courses.base import Course, Topic, Lesson, Step
from .courses.ddp1 import course_ddp1
from .courses.matdis1 import course_matdis1

# Registry seluruh mata kuliah yang terdaftar di CodeQuest
COURSES = {
    "ddp1": course_ddp1,
    "matdis1": course_matdis1,
}

# Kompatibilitas mundur untuk kode/test lama yang mengimpor TOPICS (default DDP1)
TOPICS = course_ddp1.topics

# Menggabungkan seluruh lessons dari setiap mata kuliah ke dalam mapping lookup cepat
LESSONS_DATA = {}
for course in COURSES.values():
    LESSONS_DATA.update(course.get_lessons_map())
