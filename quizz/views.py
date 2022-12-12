from django.http import HttpResponse

def index(request):
    return HttpResponse("<html>"
                        "<body>"
                        " <form method='post' action='mailto:votreemail@email.com'>"
                        "<p><font size = '15' color='BLUE' >Question</font></p>"
                        "<select name='question'><option>Choisir</option>"
                        "<option>Option1</option>"
                        "<option>Option2</option>"
                        "</select><br/>"
                        "<input type='submit' value='Submit'/>"
                        "</form>"
                        "</body>"
                        "</html>")


#jsdhukivehui h