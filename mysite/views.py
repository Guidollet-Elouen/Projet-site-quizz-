from django.http import HttpResponse

def index(request):
    return HttpResponse("<html>"
                        "<head><title>INDEX</title></head>"
                        "<body>"
                        "<h1 align = 'center'> <font color ='Blue' size = 10 >INDEX</font></h1><ul>"
                        "<hr/><li>"
                        "<font size= 50 color = 'red'>"
                        "<a href='/MCQ/'>Multiple choice Questions </a>"
                        " </font>"
                        "</li>"
                        "<li><font size = 50 color= 'red' ><a href ='/comparison/'>Comparison Questions </a></font></li>"
                        "<li><font size = 50 color = 'red'> <a href ='/open/'>Open Questions </a></font></li>"
                        "<li><font size = 50 color = 'red'> <a href ='/number/'>Numeric Questions</a></font></li>"
                        "</ul>"
                        "</body>"
                        "</html>")
