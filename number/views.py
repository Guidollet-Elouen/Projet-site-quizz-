# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from polls import models


def index(request):
    html_header = "<html><body>"
    html_footer = "</body></html>"
    html_response = ""
    for i in range(20):
        html_question=""
        V = models.quizz_number()
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend>" + str(V[0]) + "</legend>"
        html_question = html_question + "<form method='post' action='mailto:email@example.com'>"
        html_question = html_question + "Answer:<input type='text' name='Name' size='15' maxlength='15' /><br />"
        html_question = html_question + "</br>"
        html_response =  html_response + html_question
        html_response = html_response + "<input type='submit' value= 'Submit' />"
        html_response = html_response + "</form>"
        html_response = html_response + "</fieldset>"

    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)