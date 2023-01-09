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
        V = models.quizz_comparison()
        L = len(V)
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