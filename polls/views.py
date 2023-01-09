from pyexpat.errors import messages

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question
from . import models

def index(request):
    html_header = "<html><body>"
    html_footer = "</body></html>"
    html_response = ""
    for i in range(2):
        html_question=""
        V = models.quizz_mcq()
        L = len(V[1])
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend>" + str(V[0]) + "</legend>"
        html_question = html_question + "<form method='post' action='mailto:email@example.com'>"
        html_question = html_question + "<p>"
        for j in range(L):
            html_question = html_question  +  "<input type='checkbox' id='coding' name='interest' value='coding'>"
            html_question = html_question + "<label for='coding'>"+str(V[1][j])+"</label>"
            html_question = html_question + "</p>"

        html_response =  html_response + html_question
        html_response = html_response + "<input type='submit' value= 'Send email' />"
        html_response = html_response + "</form>"
        html_response = html_response + "</fieldset>"

    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)


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


#test