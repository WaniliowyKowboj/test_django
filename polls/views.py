﻿# uwaga zmieniłam to:
from django.http import HttpResponse
#dodana linia o 404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question

#wkleilem aktualizacje widoku index z 3 czesci tutoriala
#zmiana konczy sie na return templaterender
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#dodane 3 linie o 404
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
