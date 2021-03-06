from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Test, User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
# Create your views here.

def question_detail(request, test_id, pk):
    test = get_object_or_404(Test, pk = test_id)
    count = test.question_set.count()
   
    if count >= pk:
        question = test.question_set.all()[pk-1:pk].get()
        return render(request, 'testing/question_detail.html', {'question': question, 'pk': pk})
    else:
        return HttpResponseRedirect(reverse('results', args = (test.id, )))


def test_list(request):
    test = Test.objects.all()
    return render(request, 'testing/test_list.html', {'test': test})


def test_detail(request, pk):
    test = get_object_or_404(Test, pk = pk)
    question = test.question_set.all()[:1].get()
    return render(request, 'testing/test_detail.html', {'test': test, 'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    test = get_object_or_404(Test, pk = question.test_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'testing/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",})
    else:
        #selected_choice.votes += 1
        #selected_choice.save()
        
        if selected_choice.votes == question.right_choice:
            test.bal += 1
            test.save()
        #question = test.question_set.all()[question_id:question_id+1].get()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('question_detail', args=(test.id, question.id + 1, )))

def zero(request, test_id, user_id):
    test = get_object_or_404(Test, pk = test_id)
    user = User.objects.get(pk = user_id)
    user.profile.test +=' |' + test.name +' - ' + str(test.bal) 
    user.save()
    test.bal = 0
    test.save()
    return HttpResponseRedirect(reverse('test_list'))


def bal(request, test_id):
    test = get_object_or_404(Test, pk = test_id)
    test.bal = 0
    test.save()
    return HttpResponseRedirect(reverse('test_list'))


def results(request, pk):
    test = get_object_or_404(Test, pk = pk)
    return render(request, 'testing/result.html', {'test': test})


def contact(request):
    return render (request, 'testing/contact.html')