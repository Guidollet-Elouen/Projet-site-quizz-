from pyexpat.errors import messages

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from polls import models
from polls.models import Question

def index(request):
    html_header = "<html><body>"
    html_footer = "</body></html>"
    html_response = ""
    for i in range(1):
        html_question=""
        Question= models.quizz_comparison()
        Taille = len(Question[1])
        question_id=Question[2]
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend title='Input the ranking'>" + str(Question[0])+ "</legend>"
        html_question = html_question + "<form method='get' action='take_quiz/'>"
        html_question = html_question + "<p>"
        for j in range(Taille):
            html_question = html_question + "<label for='coding'>"+Question[1][j]+"</label>"
            html_question = html_question + "</p>"


        html_question = html_question + f"Answer:<input type='text' name='Name' size='15' maxlength='15' /><br />"
        html_question = html_question + "</br>"
        html_response =  html_response + html_question
        html_response = html_response + f"<input type='submit' name='{question_id}' value= 'Submit' />"
        html_response = html_response + "</form>"
        html_response = html_response + "</fieldset>"

    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)


def take_quiz(request):
    affichage=[]
    questions = []
    answers_str=request.GET.get('Name')
    answers=[]
    for i in answers_str:
        if i!=' ':
            answers.append(i)
    print(answers)
    question_id=1
    find_id=request.GET.get(str(question_id))
    while find_id==None and question_id<5:
        question_id+=1
        find_id=request.GET.get(str(question_id))
    print(question_id)
    for i in range(1):
        questions.append(models.find_solution_id_comparison(question_id)) #Indice de question
    if request.method == 'GET':
        user_answer = answers
        print("user_answer=",user_answer)
        for i in range(1):
            if questions[i].take_answer(answers):
                affichage.append("Correct")
            else:
                affichage.append("Wrong")
        return HttpResponse(affichage)