# Create your models here.
import random
from .config import *

class Question():
    text_question : str
    def __str__(self):
        return self.text_question
    def __init__(self):
        self.text_question

#Each class has :
#__init__ with NameClass() without argument
#take_answer() without argument which gets an answer from the user and return the correction (with _make_verification)

#Adapt make_verification() of Open to be more flexible

class MultipleChoice(Question):
    text_choice : [str]
    solution : [int]
    id : int
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

    def actualise(self,question,choice,solution,id):
        self.text_question=question
        self.text_choice=choice
        self.solution=solution
        self.id=id

    def __init__(self):
        self.text_question=""
        self.text_choice=[]
        self.solution=[]
        self.answer=""
        self.id=0

    def take_answer(self,user_answer):
        self.answer=user_answer
        if self._make_verification():
            return(True)
        else:
            return(False)

    def insert(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM MCQ''') #read the table
        result = cur.fetchall()
        new_id=len(result)+1
        Insert_MCQ =f'''INSERT INTO MCQ(question,choice,solution,id) VALUES ("{self.text_question}","{list_to_str(self.text_choice)}","{intlist_to_str(self.solution)}","{new_id}")'''
        cur.execute(Insert_MCQ)
        conn.commit()
        conn.close()

    def get_byid(self,id_ref):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        command=f'''SELECT * FROM MCQ WHERE id={id_ref}'''
        cur.execute(command) #read the tableJ
        result = cur.fetchall()
        conn.close()
        self.recreate(result,0)

    def recreate(self,result,i):
        choice=str_to_list(result[i][1])
        solution=str_to_intlist(result[i][2])
        self.actualise(result[i][0],choice,solution,result[i][3])

    def get(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM MCQ''') #read the table
        result = cur.fetchall()
        conn.close()
        random_choice=random.randrange(len(result))
        self.recreate(result,random_choice)

    def quizz(self):
        list_html=[]
        list_html.append(self.text_question)
        list_html.append(self.text_choice)
        list_html.append(self.id)
        return list_html

class Open(Question):
    solution : str
    answer : str
    id : int
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
        self.id=0

    def ask_user(self):
        self._insert_question()
        self._insert_solution()

    def actualise(self,question,solution,id):
        self.text_question=question
        self.solution=solution
        self.id=id

    def take_answer(self,user_answer):
        self.answer=user_answer
        if self._make_verification():
            return(True)
        else:
            return(False)

    def insert(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM OPEN''') #read the table
        result = cur.fetchall()
        new_id=len(result)+1
        Insert_OPEN =f'''INSERT INTO OPEN(question,solution,id) VALUES ("{self.text_question}","{self.solution}","{new_id}")'''
        cur.execute(Insert_OPEN)
        conn.commit()
        conn.close()

    def recreate(self,result,i):
        solution=result[i][1]
        question=result[i][0]
        id=result[i][2]
        self.actualise(question,solution,id)

    def get(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM OPEN''') #read the table
        result = cur.fetchall()
        conn.close()
        random_choice=random.randrange(len(result))
        self.recreate(result,random_choice)

    def get_byid(self,id_ref):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        command=f'''SELECT * FROM OPEN WHERE id={id_ref}'''
        cur.execute(command) #read the table
        result = cur.fetchall()
        conn.close()
        self.recreate(result,0)

    def quizz(self):
        list_html=[]
        list_html.append(self.text_question)
        list_html.append(self.id)
        return list_html

class Number(Question):
    solution: float
    answer: str
    id : int

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
        self.id=0

    def ask_user(self):
        self._insert_question()
        self._insert_solution()

    def actualise(self,question,solution,id):
        self.text_question=question
        self.solution=solution
        self.id=id

    def take_answer(self,user_answer):
        self.answer = user_answer
        if self._make_verification():
            return(True)
        else:
            return(False)

    def insert(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM NUMBER''') #read the table
        result = cur.fetchall()
        new_id=len(result)+1
        Insert_NUMBER =f'''INSERT INTO NUMBER(question,solution,id) VALUES ("{self.text_question}","{str(self.solution)},"{new_id}")'''
        cur.execute(Insert_NUMBER)
        conn.commit()
        conn.close()

    def recreate(self,result,i):
        solution=float(result[i][1])
        question=result[i][0]
        id=result[i][2]
        self.actualise(question,solution,id)

    def get(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM NUMBER''') #read the table
        result = cur.fetchall()
        conn.close()
        random_choice=random.randrange(len(result))
        self.recreate(result,random_choice)

    def get_byid(self,id_ref):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        command=f'''SELECT * FROM NUMBER WHERE id={id_ref}'''
        cur.execute(command) #read the table
        result = cur.fetchall()
        conn.close()
        self.recreate(result,0)

    def quizz(self):
        list_html=[]
        list_html.append(self.text_question)
        list_html.append(self.id)
        return list_html

class Comparison(Question):
    choice : [str]
    solution : [int]
    answer : str
    id : int
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
        self.choice=choice

    def _insert_solution(self):
        print(self.choice)
        next_solution = input("Insert the number of solution : ")
        solution = []
        for element in next_solution:
            if not(element in [" ",",",";"]):#ajouter d'autres elements separateurs
                solution.append(int(element))
        self.solution = solution

    def __init__(self):
        self.text_question=""
        self.choice=""
        self.solution=[]
        self.answer=""
        self.id=0

    def ask_user(self):
        self._insert_question()
        self._insert_choice()
        self._insert_solution()

    def actualise(self,question,choice,solution,id):
        self.text_question=question
        self.choice=choice
        self.solution=solution
        self.id=id

    def take_answer(self,user_answer):
        self.answer=user_answer
        if self._make_verification():
            return(True)
        else:
            return(False)

    def insert(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM COMPARISON''') #read the table
        result = cur.fetchall()
        new_id=len(result)+1
        Insert_COMPARISON =f'''INSERT INTO COMPARISON(question,choice,solution,id) VALUES ("{self.text_question}","{list_to_str(self.choice)}","{intlist_to_str(self.solution)}","{new_id}")'''
        cur.execute(Insert_COMPARISON)
        conn.commit()
        conn.close()

    def recreate(self,result,i):
        choice=str_to_list(result[i][1])
        question=result[i][0]
        solution=str_to_intlist(result[i][2])
        id=result[i][3]
        self.actualise(question,choice,solution,id)

    def get(self):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM COMPARISON''') #read the table
        result = cur.fetchall()
        conn.close()
        random_choice=random.randrange(len(result))
        self.recreate(result,random_choice)

    def get_byid(self,id_ref):
        conn = sqlite3.connect(road)
        cur = conn.cursor()
        command=f'''SELECT * FROM NUMBER WHERE id={id_ref}'''
        cur.execute(command) #read the table
        result = cur.fetchall()
        conn.close()
        self.recreate(result,0)

    def quizz(self):
        list_html=[]
        list_html.append(self.text_question)
        list_html.append(self.choice)
        list_html.append(self.id)
        return list_html
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
        if a[i_char]=="]":
            None
        elif a[i_char]==";" or a[i_char]=="," or a[i_char]=="[":
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

##DATABASE part
import sqlite3
#conn = sqlite3.connect('db.sqlite3')
#cur = conn.cursor()
#Table_COMPARISON ='''CREATE TABLE IF NOT EXISTS NUMBER(question TEXT,solution TEXT,id INT)'''  #Create Table
#cur.execute(Table_COMPARISON)
#cur.execute("""DROP TABLE NUMBER""") #Destroy Table
#conn.commit()
#conn.close()

##Fonction finale
def create_empty_question():
    type_question=int(input("Which question do you want to create, enter 1 for MCQ, 2 for Open, 3 for Number, 4 for Comparison : "))
    if type_question==1:
        new_question=MultipleChoice()
    if type_question==2:
        new_question=Open()
    if type_question==3:
        new_question=Number()
    if type_question==4:
        new_question=Comparison()
    return new_question


def create_empty_precise_question(type_question):
    if type_question==1:
        new_question=MultipleChoice()
    if type_question==2:
        new_question=Open()
    if type_question==3:
        new_question=Number()
    if type_question==4:
        new_question=Comparison()
    return new_question

def insertion_question():
    question=create_empty_question()
    question.ask_user()
    question.insert()

def answer_question():
    question=get_question()
    question.take_answer()

def get_question():
    question=create_empty_question()
    question.get()
    return question

#Function for html

def quizz_mcq():
    question=create_empty_precise_question(1)
    question.get()
    return question.quizz()

def quizz_open():
    question=create_empty_precise_question(2)
    question.get()
    return question.quizz()

def quizz_number():
    question=create_empty_precise_question(3)
    question.get()
    return question.quizz()

def quizz_comparison():
    question=create_empty_precise_question(4)
    question.get()
    return question.quizz()

def listquizz_mcq(i):
    list_question=[]
    for j in range(i):
        newquestion=quizz_mcq()
        while (newquestion in list_question):
            newquestion=quizz_mcq()
        list_question.append(newquestion)
    return list_question

def listquizz_open(i):
    list_question=[]
    for j in range(i):
        newquestion=quizz_open()
        while (newquestion in list_question):
            newquestion=quizz_open()
        list_question.append(newquestion)
    return list_question

def listquizz_number(i):
    list_question=[]
    for j in range(i):
        newquestion=quizz_number()
        while (newquestion in list_question):
            newquestion=quizz_number()
        list_question.append(newquestion)
    return list_question

def listquizz_comparison(i):
    list_question=[]
    for j in range(i):
        newquestion=quizz_comparison()
        while (newquestion in list_question):
            newquestion=quizz_comparison()
        list_question.append(newquestion)
    return list_question

def find_solution_id_mcq(id_ref):  #return solution of the question with id = id_ref
    question=create_empty_precise_question(1)
    question.get_byid(id_ref)
    return question