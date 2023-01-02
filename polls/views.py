from pyexpat.errors import messages

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question


def index(request):
    return HttpResponse("<html>"
                        "<body>"
                        "<form method = 'post' action='mailto:votreemail@email.com'>"
                        "<p><font size='15' color='BLUE'>Question</font></p>"
                        "<input type='checkbox' name='animal' value='proposition'/>Proposition1<br/>"
                        "<input type='checkbox' name='animal' value='proposition'/>Proposition2<br/>"
                        "<input type='submit' value='Submit'/>"
                        "</form>"
                         "</body>"
                        "</html>")

def take_quiz(request):
    questions = Question.text_question
    context = {'questions': questions}

    if request.method == 'GET':
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request, 'quiz.html', context)

    if request.method == 'POST':
        correct_user_answers = []
        user_answer = request.POST['option']
        correct_answer = request.POST.get('answerLabel') #Changer pour database
        print('correct answer ', correct_answer)
        print('user answer: ', user_answer)
        if user_answer == correct_answer:
            correct_user_answers.append(user_answer)
            messages.success(request, 'Correct answer')
            return HttpResponseRedirect(request.session['previous_page'])
        else:
            messages.warning(request, f'Wrong answer, Correct Answer is {correct_answer}')
            return HttpResponseRedirect(request.session['previous_page'])
