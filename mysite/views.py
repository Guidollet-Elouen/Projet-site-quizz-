from django.http import HttpResponse

def index(request):
    return HttpResponse("<html>"
                        "<head><title>INDEX</title></head>"
                        "<body>"
                        "<h1 align = 'center'> <font color ='Blue' size = 10 >INDEX</font></h1><ul>"
                        "<hr/><li>"
                        "<font size= 50 color = 'red'>"
                        "<a href='/polls/'>Questions à choix multiples</a>"
                        " </font>"
                        "</li>"
                        "<li><font size = 50 color= 'red' ><a href ='/quizz/'>Questions à choix unique</a></font></li>"
                        "<li><font size = 50 color = 'red'> <a href ='/open/'>Questions libres</a></font></li>"
                        "</ul>"
                        "</body>"
                        "</html>")
