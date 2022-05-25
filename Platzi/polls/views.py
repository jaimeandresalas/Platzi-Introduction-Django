from ast import Try
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

"""def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id=None):
    # question = Question.objects.get(id=question_id) Merodo sencillo
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})"""

# Vista creada por funciones para usar generalized


"""def results(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/results.html', {'question': question})
"""
# Vista basadas en clases Clases Based views


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.Post["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            "error_message": "No elegiste una respuesta"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
