from django.http import HttpResponse, HttpResponseRedirect
from polls import models
from polls import config
import sqlite3

def index(request):
    html_header = "<html><body>"
    html_footer = "</body></html>"
    html_response = ""
    nb_question=config.nb_question
    Question = models.listquizz_comparison(nb_question)
    for i in range(nb_question):
        html_question=""
        Taille = len(Question[i][1])
        question_id=Question[i][2]
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend title='Input the ranking'>" + str(Question[i][0])+ "</legend>"
        html_question = html_question + "<form method='get' action='take_quiz/'>"
        html_question = html_question + "<p>"
        for j in range(Taille):
            html_question = html_question + "<label for='coding'>"+Question[i][1][j]+"</label>"
            html_question = html_question + "</p>"
        html_question = html_question + f"Answer:<input type='text' name={'Name'+str(i)+str(question_id)} size='15' maxlength='15' /><br />"
        html_question = html_question + "</br>"
        html_question = html_question + "</fieldset>"
        html_response =  html_response + html_question
    html_response = html_response + f"<input type='submit' name='submit' value= 'Submit' />"
    html_response = html_response + "</form>"
    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)


def take_quiz(request):
    nb_questioninbase=models.nb_question_comparison()
    nb_question=config.nb_question
    affichage=[]
    score=0
    for k in range(nb_question):
        question_id=1
        find_id=request.GET.get('Name'+str(k)+str(question_id))
        while find_id==None and question_id<nb_questioninbase+1:
            question_id+=1
            find_id=request.GET.get('Name'+str(k)+str(question_id))
        answers_str=request.GET.get('Name'+str(k)+str(question_id))
        answers=[]
        for i in answers_str:
            if i!=' ':
                answers.append(i)
        question=models.find_solution_id_comparison(question_id) #Find the question with id=question_id
        if request.method == 'GET':
            message="Votre réponse à la question "+str(k+1)
            if question.take_answer(answers):
                 affichage.append(message+" est vraie")
                 score+=1
            else:
                affichage.append(message+" est fausse")
            affichage.append("</p>")
    affichage.append("Votre score est "+str(score)+"/"+str(nb_question))
    return HttpResponse(affichage)