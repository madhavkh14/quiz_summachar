from django.urls import path
from .views import *

urlpatterns = [
    path('quiz/add', CreateQuiz.as_view()),
    path('quiz/<str:pk>/change', ChangeQuiz.as_view()),
    path('quiz/<str:pk>/delete', DeleteQuiz.as_view()),
    path('quiz', GetQuiz.as_view()),
    path('quiz/attempt', AttemptQuiz.as_view()),
    path('question/add', CreateQuestion.as_view()),
]