from django.http import HttpResponse

def index(request):
    return HttpResponse("<html>"
                        "<head><title>INDEX</title></head>"
                        "<body>"
                        "<h1 align = 'center'> <font color ='Blue' size = 10 >INDEX</font></h1><ul>"
                        "<hr/><li>"
                        "<font size= 5 color = 'red'>"
                        "<a href='/polls/'>Questions à choix multiples</a>"
                        " </font>"
                        "</li>"
                        "<li><font size = 9 color= 'red' <a href = '/quizz/'>Questions à choix unique</a></font></li>"
                        "<li><font size = 9 color = 'red' <a href = '/open/'>Questions libres</a></font>/li>"
                        "</ul>"
                        "<img alt='image html exemple' src='/imgT2.jpg' width='120' height='75' />"
                       " <form method='post' action='mailto:votreemail@email.com'><p>Quelle couleur de chaussures vous préférez?</p>"
                        "<input type='checkbox' name='shoes' value='noires' /> Simple Noires <br/>"
	                    "<input type='checkbox' name='shoes' value='blanches' /> Simple Blanches <br/>"
	                    "<input type='checkbox' name='shoes' value='grises' /> Nuances de gris <br/>"
	                    "<input type='checkbox' name='shoes' value='noires&blanches' /> Noires et blanches<br/>"
	                    "<input type='submit' value='Menvoyer un Email' />"
                        "</form>"
                        "<textarea cols=50 rows=2>Zone de texte!</textarea>"
                        "</body>"
                        "</html>")



