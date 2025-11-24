import random

class FruitQuiz:

    def __init__(self):

        #Create a dictionary of fruits as keys and color as value
        self.fruits={'apple':'red', 'orange':'orange', 'watermelon':'green', 'banana':'yellow'}

    #Function for the quiz, here a fruit wiil be chosen randomly

    def quiz(self):
        while(True):

            fruit,color=random(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))

            user_answer=input()

            if(user_answer.lower()==color):
                print("Correct answer")
            else:
                print("wrong answer")

            option=int(input("Enter 0, if you want to play again otherwise enter 1 :"))
            if (option):
                break

print("Welcome to fruit quiz")
fq=FruitQuiz()
fq.quiz()