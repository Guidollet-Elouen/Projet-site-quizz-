from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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

