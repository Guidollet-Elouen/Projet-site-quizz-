# Create your models here.
import random

class Question():
    text_question : str
    def __str__(self):
        return self.text_question
    def __init__(self):
        self.text_question

#Each class has :
#__init__ with NameClass() without argument
#take_answer() without argument which gets an answer from the user and return the correction (with _make_verification)


#Make test, assertion, at each input to check if the answer returned is ok
#Adapt make_verification() of Open to be more flexible

class MultipleChoice(Question):
    text_choice : [str]
    solution : [int]
    answer : str

    def __str__(self):
        return [self.text_question,self.text_choice,self.solution]

    def _transformation(self):
        answer_list=[]
        for element in self.answer:
            if not(element in ["",",",";"]):#ajouter d'autres elements separateurs
                answer_list.append(int(element))
        return answer_list

    def _make_verification(self):
        transfo=self._transformation()
        for elem_transfo in transfo:
            if not(elem_transfo in self.solution):
                return False
        for elem_solu in self.solution:
            if not(elem_solu in transfo):
                return False
        return True

    def _insert_question(self):
        self.text_question = input("Insert the question : ")

    def _insert_choice(self):
        next_choice = input("Insert the first choice : ")
        choice = []
        i = 1
        while next_choice != "0":
            choice.append(str(i) + "." + next_choice)
            next_choice = input("Insert the next choice, if no more choice tap 0 : ")
            i += 1
        self.text_choice=choice

    def _insert_solution(self):
        print(self.text_choice)
        next_solution = int(input("Insert the number of the first solution : "))
        solution = []
        while next_solution != "0":
            solution.append(next_solution)
            next_solution = input("Insert the next solution, if no more choice tap 0 : ")
        self.solution = solution

    def ask_user(self):
        self._insert_question()
        self._insert_choice()
        self._insert_solution()

    def actualise(self,question,choice,solution):
        self.text_question=question
        self.text_choice=choice
        self.solution=solution

    def __init__(self):
        self.text_question=""
        self.text_choice=[]
        self.solution=[]
        self.answer=""

    def take_answer(self):
        print(self.text_question)
        print(self.text_choice)
        self.answer=input("Insert your answer : ")
        if self._make_verification():
            print(True)
        else:
            print(False)
            print("The correct answer was " + str(self.solution))

#firstquestion=MultipleChoice()
#firstquestion.take_answer()


class Open(Question):
    solution : str
    answer : str
    def _make_verification(self):
        return(self.solution==self._transformation())

    def _transformation(self):
        return self.answer
    def _insert_question(self):
        self.text_question=input("Insert your question : ")

    def _insert_solution(self):
        self.solution=input("insert your solution : ")

    def __init__(self):
        self.text_question=""
        self.solution=""
        self.answer=""

    def ask_user(self):
        self._insert_question()
        self._insert_solution()

    def actualise(self,question,solution):
        self.text_question=question
        self.solution=solution

    def take_answer(self):
        print(self.text_question)
        self.answer=input("Insert your answer : ")
        if self._make_verification():
            print(True)
        else:
            print(False)
            print("The correct answer was "+str(self.solution))

#openquestion=Open()
#openquestion.take_answer()


class Number(Question):
    solution: float
    answer: str

    def _make_verification(self):
        return (self.solution == self._transformation())

    def _transformation(self):
        answer=""
        for element in self.answer:
            if element in  [".", ",","1","2","3","4","5","6","7","8","9","0"]:# ajouter d'autres elements separateurs
                if element==",":
                    answer+="."
                else:
                    answer+=element
        return float(answer)

    def _insert_question(self):
        self.text_question = input("Insert your question : ")

    def _insert_solution(self):
        self.solution = float(input("insert your solution (float with . not ,) : "))

    def __init__(self):
        self.text_question=""
        self.solution=0.0
        self.answer=""

    def ask_user(self):
        self._insert_question()
        self._insert_solution()

    def actualise(self,question,solution):
        self.text_question=question
        self.solution=solution

    def take_answer(self):
        print(self.text_question)
        self.answer = input("Insert your answer : ")
        if self._make_verification():
            print(True)
        else:
            print(False)
            print("The correct answer was " + str(self.solution))

#numberquestion=Number()
#numberquestion.take_answer()

class Comparison(Question):
    choice : str
    solution : [int]
    answer : str
    def _transformation(self):
        answer_list = []
        for element in self.answer:
            if not(element in [" ",",",";"]):# ajouter d'autres elements separateurs
                answer_list.append(int(element))
        return answer_list

    def _make_verification(self):
        answer_list=self._transformation()
        return(self.solution==answer_list)

    def _insert_question(self):
        self.text_question = input("Insert the question : ")

    def _insert_choice(self):
        next_choice = input("Insert the first choice : ")
        choice = []
        i = 1
        while next_choice != "0":
            choice.append(str(i) + "." + next_choice)
            next_choice = input("Insert the next choice, if no more choice tap 0 : ")
            i += 1
        self.text_choice=choice

    def _insert_solution(self):
        print(self.text_choice)
        next_solution = input("Insert the number of solution : ")
        solution = []
        for element in next_solution:
            if not(element in [" ",",",";"]):#ajouter d'autres elements separateurs
                solution.append(int(element))
        self.solution = solution

    def __init__(self):
        self.text_question=""
        self.text_choice=""
        self.solution=[]
        self.answer=""

    def ask_user(self):
        self._insert_question()
        self._insert_choice()
        self._insert_solution()

    def actualise(self,question,choice,solution):
        self.text_question=question
        self.text_choice=choice
        self.solution=solution

    def take_answer(self):
        print(self.text_question)
        print(self.text_choice)
        self.answer=input("Insert your answer : ")
        if self._make_verification():
            print(True)
        else:
            print(False)
            print("The correct answer was "+str(self.solution))

#comparisonquestion=Comparison()
#comparisonquestion.take_answer()


def create_question(type_question):
    #type_question=int(input("Which question do you want to create, enter 1 for MCQ, 2 for Open, 3 for Number, 4 for Comparison : "))
    if type_question==1:
        new_question=MultipleChoice()
    if type_question==2:
        new_question=Open()
    if type_question==3:
        new_question=Number()
    if type_question==4:
        new_question=Comparison()
    new_question.ask_user()
    return new_question

#myquestion=create_question(1)
#myquestion.take_answer()

##Function to translate list to int/str

def list_to_str(L):
    a=""
    for l in L:
        a=a+";"+l
    return a
def intlist_to_str(L):
    a=""
    for l in L:
        a=a+";"+str(l)
    return a
def str_to_list(a):
    l=[]
    i_char=0
    j_list=-1
    while i_char<len(a):
        if a[i_char]==";":
            l.append("")
            j_list+=1
        else:
            l[j_list]+=a[i_char]
        i_char+=1
    return l
def str_to_intlist(a):
    L=str_to_list(a)
    L_end=[]
    for l in L:
        L_end.append(int(l))
    return L_end

def recreate_qcm(result,i):
    choice=str_to_list(result[i][1])
    solution=str_to_intlist(result[i][2])
    mcq=MultipleChoice()
    mcq.actualise(result[i][0],choice,solution)
    return mcq

def recreate_open(result,i):
    open=Open()
    solution=result[i][1]
    question=result[i][0]
    open.actualise(question,solution)
    return open

def recreate_number(result,i):
    number=Number()
    solution=float(result[i][1])
    question=result[i][0]
    number.actualise(question,solution)
    return number

def recreate_comparison(result,i):
    comparison=Comparison()
    choice=result[i][1]
    question=result[i][0]
    solution=str_to_intlist(result[i][2])
    comparison.actualise(question,choice,solution)
    return comparison

##DATABASE part
import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

#Table_COMPARISON ='''CREATE TABLE IF NOT EXISTS COMPARISON(question TEXT,choice TEXT,solution TEXT)'''  #Create Table
#cur.execute(Table_COMPARISON)
#conn.commit()
#cur.execute("""DROP TABLE OPEN""") #Destroy Table
#conn.commit()


##FONCTION CREATION ET REPONSE AUX QUESTIONS
def insert_mcq():#Insert an element in a table checker les doublons
    myquestion = create_question(1)
    Insert_MCQ =f'''INSERT INTO MCQ(question,choice,solution) VALUES ("{myquestion.text_question}","{list_to_str(myquestion.text_choice)}","{intlist_to_str(myquestion.solution)}")'''
    cur.execute(Insert_MCQ)
    conn.commit()

def take_mcq():
    cur.execute('''SELECT * FROM MCQ''') #read the table
    result = cur.fetchall()
    random_choice=random.randrange(len(result))
    recreate_qcm(result,random_choice).take_answer()

def insert_open():#Insert an element in a table
    myquestion = create_question(2)
    Insert_OPEN =f'''INSERT INTO OPEN(question,solution) VALUES ("{myquestion.text_question}","{myquestion.solution}")'''
    cur.execute(Insert_OPEN)
    conn.commit()

def take_open():
    cur.execute('''SELECT * FROM OPEN''') #read the table
    result = cur.fetchall()
    random_choice=random.randrange(len(result))
    recreate_open(result,random_choice).take_answer()

def insert_number():#Insert an element in a table
    myquestion = create_question(3)
    Insert_NUMBER =f'''INSERT INTO NUMBER(question,solution) VALUES ("{myquestion.text_question}","{str(myquestion.solution)}")'''
    cur.execute(Insert_NUMBER)
    conn.commit()

def take_number():
    cur.execute('''SELECT * FROM NUMBER''') #read the table
    result = cur.fetchall()
    random_choice=random.randrange(len(result))
    recreate_number(result,random_choice).take_answer()

def insert_comparison():#Insert an element in a table
    myquestion = create_question(4)
    Insert_COMPARISON =f'''INSERT INTO COMPARISON(question,choice,solution) VALUES ("{myquestion.text_question}","{myquestion.text_choice}","{intlist_to_str(myquestion.solution)}")'''
    cur.execute(Insert_COMPARISON)
    conn.commit()

def take_comparison():
    cur.execute('''SELECT * FROM COMPARISON''') #read the table
    result = cur.fetchall()
    random_choice=random.randrange(len(result))
    recreate_comparison(result,random_choice).take_answer()

##Fonction finale

def creation_question():
    type_question=int(input("Which question do you want to create, enter 1 for MCQ, 2 for Open, 3 for Number, 4 for Comparison : "))
    if type_question==1:
        insert_mcq()
    if type_question==2:
        insert_open()
    if type_question==3:
        insert_number()
    if type_question==4:
        insert_comparison()

def answer_question():
    type_question=int(input("Which question do you want to answer, enter 1 for MCQ, 2 for Open, 3 for Number, 4 for Comparison : "))
    if type_question==1:
        take_mcq()
    if type_question==2:
        take_open()
    if type_question==3:
        take_number()
    if type_question==4:
        take_comparison()
