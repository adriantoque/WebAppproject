from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("profile/", views.profile, name="Profile"),
    path("quiz/", views.quiz_list, name="quiz_list"),
    path("quiz/<int:quiz_id>/<int:q_index>/", views.quiz_detail, name="quiz_detail"),
    path("quiz/<int:quiz_id>/<int:q_index>/<int:answer_id>/", views.answer_question, name="answer_question"),


]
