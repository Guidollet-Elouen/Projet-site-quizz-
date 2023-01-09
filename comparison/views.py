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
    for i in range(2):
        html_question=""
        Question= models.quizz_comparison()
        Taille = len(Question)
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend title='Input the ranking'>" + str(Question[0]) + "</legend>"
        html_question = html_question + "<form method='post' action='mailto:email@example.com'>"
        html_question = html_question + "<p>"
        for j in range(Taille):
            html_question = html_question + "<label for='coding'>"+Question[1][j]+"</label>"
            html_question = html_question + "</p>"

        html_response =  html_response + html_question
        html_response = html_response + "Answer:<input type='text' name='Name' size='15' maxlength='15' /><br />"
        html_response = html_response + "</br>"
        html_response = html_response + "<input type='submit' value= 'Send email' />"
        html_response = html_response + "</form>"
        html_response = html_response + "</fieldset>"

    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)