from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('subject', views.subjects, name="subject"),
    path('quiz', views.quizView, name="quiz"),
    path('score', views.scoreView, name="login"),
    path('signup', views.signUpView, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user', views.dashboardView, name="dashboard"),
    path('dashboard', views.dashboardView, name="ddd"),
    path('about', views.about, name="aboutus")

]
