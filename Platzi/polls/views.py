from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Estas en la pagina Principal")


def detail(request, question_id=None):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")


def results(request, question_id=None):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")


def vote(request, question_id=None):
    return HttpResponse(f"Estas viendo los votos de la pregunta numero {question_id}")
