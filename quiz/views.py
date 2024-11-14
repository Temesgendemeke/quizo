from types import NoneType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import Question, Quiz, Result, Subject
from django.contrib.auth.models import User
from .forms import UserCreationCustom, UserForm
from django.contrib.auth import authenticate


# Create your views here.
def homepage(request):
    subject = Subject.objects.all()
    quiz = Quiz.objects.all().order_by("-number")
    user_results = Result.objects.all().order_by("-score")[:5]

    unique_user = []
    seen_user = set()

    for result in user_results:
        if result.user.id not in seen_user:
            unique_user.append(result)
            seen_user.add(result.user.id)

        if len(unique_user) == 0:
            break

    return render(
        request,
        "quiz/home.html",
        {"subject": subject, "quizs": quiz, "leaders": unique_user},
    )


def about(request):
    return render(request, "quiz/about.html")


def subjects(request):
    quiz = Quiz.objects.filter(subject__name=request.GET["q"]).order_by("-number")
    return render(
        request, "quiz/subject.html", {"subject": quiz, "name": request.GET["q"]}
    )


def subjectMenuView(request):
    subject = Subject.objects.all()

    return render(request, "quiz/subject_page.html", {"subjects": subject})


def quizView(request):
    try:
        quiz = Quiz.objects.get(id=request.GET["q"])
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

        if request.user.is_authenticated:
            Result.objects.create(
                user=request.user, subject=quiz.subject.name, score=score, quiz=quiz
            )
        if score > questions.count() - 1:
            msg = "you are wonderful 🎉"
        elif score >= questions.count() / 2:
            msg = "good 😉"
        else:
            msg = "come on you can do better than this 😫"

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
        form = UserCreationCustom(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("quiz:login")
    else:
        form = UserCreationCustom()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def dashboardView(request):
    user = User.objects.filter(id=request.user.id).first()
    quiz = Result.objects.filter(user__id=request.user.id).order_by("-score")
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()

    return render(
        request, "quiz/dashboard.html", {"user": user, "quizs": quiz, "form": form}
    )
