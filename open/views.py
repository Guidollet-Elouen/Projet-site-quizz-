from django.http import HttpResponse, HttpResponseRedirect
from polls import models
from polls import config
import sqlite3

def index(request):
    html_header = "<html><body>"
    html_footer = "</body></html>"
    html_response = ""
    nb_question=1
    Question = models.listquizz_open(nb_question)
    for i in range(nb_question):
        html_question=""
        question_id=Question[i][1]
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend>" + str(Question[i][0]) + "</legend>"
        html_question = html_question + "<form method='get' action='take_quiz/'>"
        html_question = html_question + f"Answer:<input type='text' name='Name' size='15' maxlength='15' /><br />"
        html_question = html_question + "</br>"
        html_response =  html_response + html_question
        html_response = html_response + f"<input type='submit' name='{question_id}' value= 'Submit' />"
        html_response = html_response + "</form>"
        html_response = html_response + "</fieldset>"

    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)

def take_quiz(request):
    nb_questioninbase=models.nb_question_open()
    answers=request.GET.get('Name')
    question_id=1
    find_id=request.GET.get(str(question_id))
    while find_id==None and question_id<nb_questioninbase+1:#find the question id
        question_id+=1
        find_id=request.GET.get(str(question_id))
    question=models.find_solution_id_open(question_id)#Find the question which has id=question_id
    if request.method == 'GET':
        if question.take_answer(answers):
            return HttpResponse("Correct")
        else:
            return HttpResponse("Wrong")
