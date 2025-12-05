from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, Answer, Lesson

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, "lesson/lesson_list.html", {"lessons": lessons})

def lesson_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, "lesson/lesson_view.html", {"lessons": lesson})

def profile(request):
    return render(request, 'profile.html')


def quiz_list(request):
    quizzes = Quiz.objects.all()
    # store scores in session
    scores = request.session.get("scores", {})
    for quiz in quizzes:
        correct = scores.get(str(quiz.id), 0)
        total = quiz.questions.count()
        quiz.score_display = f"{correct} / {total}"
    return render(request, "quiz/quiz_list.html", {"quizzes": quizzes, "scores": scores})


def quiz_detail(request, quiz_id, q_index=0):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    
    if q_index == 0:
        scores = request.session.get("scores", {})
        scores[str(quiz_id)] = 0
        request.session["scores"] = scores
    
    if q_index >= len(questions):
        return redirect("quiz_list")

    question = questions[q_index]
    return render(request, "quiz/quiz_detail.html", {
        "quiz": quiz,
        "question": question,
        "q_index": q_index,
        "total": len(questions),
    })


def answer_question(request, quiz_id, q_index, answer_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    question = questions[q_index]
    answer = get_object_or_404(Answer, id=answer_id)

    # initialize score tracking
    scores = request.session.get("scores", {})
    if str(quiz_id) not in scores:
        scores[str(quiz_id)] = 0

    if answer.is_correct:
        scores[str(quiz_id)] += 1

    request.session["scores"] = scores
    return redirect("quiz_detail", quiz_id=quiz_id, q_index=q_index+1)
