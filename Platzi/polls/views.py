from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id=None):
    # question = Question.objects.get(id=question_id) Merodo sencillo
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id=None):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")


def vote(request, question_id=None):
    return HttpResponse(f"Estas viendo los votos de la pregunta numero {question_id}")
