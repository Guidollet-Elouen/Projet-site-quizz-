from django.http import HttpResponse

def index(request):
    return HttpResponse("<html>"
                        "<head><title>INDEX</title></head>"
                        "<body>"
                        "<h1 align = 'center' >INDEX</h1><ol>"
                        "<li bgcolor = 'rgb(255,0,0)' >Questions à choix multiples</li>"
                        "<li>Questions à choix unique</li>"
                        "<li>Questions libres</li>"
                        "</ol>"
                        
                        "</body>"
                        "</html>")
    '''return HttpResponse("<html><body><h1><a href='/polls/'>Hello, world.</a></h1> You're at the polls index.</body></html>")
'''
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)'''

