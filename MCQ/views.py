from django.http import HttpResponse, HttpResponseRedirect

from polls import models

def index(request):
    html_header = "<html><body>"
    html_footer = "</body></html>"
    html_response = ""
    Questions = models.listquizz_mcq(1)
    for i in range(1):
        html_question = ""
        Taille = len(Questions[i][1])
        Index = Questions[i][2]
        html_question = html_question + "<fieldset>"
        html_question = html_question + "<legend>" + str(Questions[i][0]) + "</legend>"
        html_question = html_question + "<form method='get' action='take_quiz/'>"
        html_question = html_question + "<p>"
        for j in range(Taille):
            html_question = html_question + f"<input type='checkbox' name={'user_answer'+str(j)} value='{[j+1,Index]}' >"
            html_question = html_question + "<label for='coding'>" + str(Questions[i][1][j]) + "</label>"
            html_question = html_question + "</p>"


        html_response = html_response + html_question
        html_response = html_response + "<input type='submit' value= 'Submit' />"
        html_response = html_response + "</form>"
        html_response = html_response + "</fieldset>"

    http_response = html_header + html_response + html_footer
    return HttpResponse(http_response)


"""
def get_request_field(request, field_name):
    if field_name in request.args:
        return request.args[field_name]
    elif field_name in request.form:
        return request.form[field_name]
    else:
        return None
"""

def find_numberchoice(request):
    answers=[]
    i=0
    answers.append(request.GET.get('user_answer' + str(i)))
    while(answers[i]==None):
        i+=1
        answers.append(request.GET.get('user_answer' + str(i)))
    test = models.str_to_list(answers[i])
    question_id=test[1]
    question=models.find_solution_id_mcq(question_id)
    return len(question.text_choice)

#qezfzeqfqez
def take_quiz(request):
    questions = []
    a = 0
    affichage=[]
    answers=[]
    answer_user=[]
    longueur_choix=find_numberchoice(request)
    number_choice=longueur_choix
    for j in range(number_choice):#Trouver comment trouver le nombre de choix de la question
        answers.append(request.GET.get('user_answer'+str(j)))
    for j in range(number_choice):
        if answers[j]==None:
            None
        else:
            test = models.str_to_list(answers[j])
            answer_user.append(test[0])
            question_id=test[1]
    #test=models.str_to_list(answers)
    #answer_user=test[0]
    #question_id=test[1]
    for i in range(1):
        questions.append(models.find_solution_id_mcq(int(question_id))) #Indice de question
    if request.method == 'GET':
        user_answer = answer_user # Id de la box sur laquelle l'user clique
        print("user_answer=",user_answer)
        for i in range(1):
            if questions[i].take_answer(user_answer):
                a += 1
                affichage.append("Correct")
            else:
                affichage.append("Wrong")
        return HttpResponse(affichage)