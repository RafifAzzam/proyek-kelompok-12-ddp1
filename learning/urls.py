from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pelajaran/<str:lesson_id>/", views.lesson_detail, name="lesson_detail"),
]
