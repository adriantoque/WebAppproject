from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet
from .models import Quiz, Question, Answer, Lesson, LessonContent


# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4   # show 4 empty slots by default
    min_num = 4 # enforce at least 4 answers
    max_num = 4 # lock to exactly 4 answers


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class LessonInline(admin.TabularInline):
    model = LessonContent
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz")
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct",)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [LessonInline]

@admin.register(LessonContent)
class LessonContentAdmin(admin.ModelAdmin):
    list_display = ("content", "lesson")