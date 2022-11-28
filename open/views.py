from django.http import HttpResponse

def index(request):
    return HttpResponse("<html>" 
                        "<body>"
                        "<p><font size='15'color ='blue' >Question"
                        "</font></p>"
                        "<form method='post' action='mailto:email@example.com' > "
                        "Answer :<input type='text' name='Answer' size = 15 maxlenght='18'/><br/> "
                        "<input type='submit' value='Submit'/>"
                        "</form>"
                        "</body>"
                        "</html>")