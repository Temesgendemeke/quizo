from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import Question, Quiz, Result, Subject
from django.contrib.auth.models import User


# Create your views here.
def homepage(request):
    subject = Subject.objects.all()
    quiz = Quiz.objects.all().order_by("-number")
    user = Result.objects.all().order_by("-score")[:5]
    return render(
        request, "quiz/home.html", {"subject": subject, "quizs": quiz, "leader": user}
    )


def about(request):
    return render(request, "quiz/about.html")


def subjects(request):
    quiz = Quiz.objects.filter(subject__name=request.GET["q"]).order_by("-number")
    return render(
        request, "quiz/subject.html", {"subject": quiz, "name": request.GET["q"]}
    )


def quizView(request):
    try:
        quiz = Quiz.objects.get(id=request.GET["q"]).order_by("-number")
        questions = quiz.question.all()
    except:
        return HttpResponseNotFound()
    return render(request, "quiz/quiz.html", {"quiz": quiz, "questions": questions})


def scoreView(request):
    if request.method == "POST":
        score = 0
        quiz_id = request.POST["quiz_id"][0]
        quiz = Quiz.objects.get(id=quiz_id)
        quiz.number += 1
        quiz.save()
        questions = quiz.question.all()
        for question in questions:
            user_quess = request.POST.get("answer-{}".format(str(question.id)))
            print(user_quess)
            if question.answer == user_quess:
                score += 1
        print(score, quiz.subject.name)
        Result.objects.create(subject=quiz.subject.name, score=score)
        if score > questions.count() - 1:
            msg = "you are wonderful 🎉"
        elif score >= questions.count() / 2:
            msg = "good 😉"
        else:
            msg = "come on you can do better than this 😫"
        print(quiz, score, questions)

        return render(
            request,
            "quiz/score.html",
            {
                "quiz_id": quiz_id,
                "score": score,
                "total": questions.count(),
                "msg": msg,
                "subject": quiz.subject.name,
            },
        )

    return render(
        request,
        "quiz/404.html",
    )


def signUpView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("quiz:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def dashboardView(request):
    user = User.objects.filter(id=1).first()
    quiz = Result.objects.filter(user__id=1)
    print(quiz)
    return render(request, "quiz/dashboard.html", {"user": user})
