# Create your models here.

class Question():
    text_question : str
    def __str__(self):
        return self.text_question

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
        return self.answer

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

    def __init__(self):
        self._insert_question()
        self._insert_choice()
        self._insert_solution()

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
        self._insert_question()
        self._insert_solution()

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
    solution: float #liste de taille 2 solution[0] la partie entiere et solution[1] la partie decimale
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
        self._insert_question()
        self._insert_solution()

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
        self._insert_question()
        self._insert_choice()
        self._insert_solution()

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


def create_question():
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

myquestion=create_question()
myquestion.take_answer()