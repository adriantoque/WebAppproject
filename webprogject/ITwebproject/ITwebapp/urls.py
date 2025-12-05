from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("lesson_list/", views.lesson_list, name="lesson_list"),
    path("lesson_view/<int:lesson_id>/", views.lesson_view, name="lesson_view"),
    path("quiz/", views.quiz_list, name="quiz_list"),
    path("quiz/<int:quiz_id>/<int:q_index>/", views.quiz_detail, name="quiz_detail"),
    path("quiz/<int:quiz_id>/<int:q_index>/<int:answer_id>/", views.answer_question, name="answer_question"),


]
