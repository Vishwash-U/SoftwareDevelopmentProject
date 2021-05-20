
from django.http import HttpResponse
from django.template import loader

from .models import Question, Quote


from django.http import Http404
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index2.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


# Leave the rest of the views (detail, results, vote) unchanged


def processquote(request):

	print(request.POST)
	Quote(product=request.POST['product'],quantity=request.POST['quantity'],price=request.POST['price'],hospital=request.POST['hospital']).save()
	return HttpResponse("thank you")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

