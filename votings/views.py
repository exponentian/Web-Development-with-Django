from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def index(request):
    questions = Question.objects.all()
    return render(request, 'votings/index.html', {'questions': questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'votings/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    print(question.choice_set.all)
    return render(request, 'votings/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'votings/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('votings:results', args=(question.id,)))
