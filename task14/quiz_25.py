# Quiz Game in Python
class Quiz:
    def __init__(self,question,option,answer):
        self.question = question
        self.option  = option
        self.answer = answer

    def displayOptions(self):
        for i,option in enumerate(self.option, start=1):
            print(f"{chr(ord('A') + i - 1)}. {option}")

    def askQuestions(self):
        print("\n",self.question)
        self.displayOptions()
        while True:
            choice = input("Enter the answer as A/B/C/D:").upper()
            if choice in ['A','B','C','D']:
                break
            else:
                print("Invalid entry, re-enter")
            # choice = input("Enter the answer as A/B/C/D:").upper()

        return choice == self.answer
    
def playQuiz(questions, name):
    score = 0
    for question in questions:
        if question.askQuestions():
            print("\nCorrect Answer")
            score += 1
        else:
            print("Wrong Answer")
    print(f"{name} scored:{score}")

name = input("Enter the name of the candidate:")
question1 = Quiz("National flower of India?",['Lotus','Lilly','Rose','Jasmin'],'A')
question2 = Quiz("National Animal of India?",['Lion','Elephant','Cheetah','Tiger'],'D')
question3 = Quiz("Official language of India?",['English','Hindi','Malayalam','Marathi'],'B')
question4 = Quiz("Largest Mammal in the Planet",['Elephant','Lion','Blue Whale','Platypus'],'C')
question5 = Quiz("Larest Mountain in the World",['Mount k2','Mount Everest','Kilimanjaro','Elbrus'],'B')

quiz_Questions = [question1,question2,question3,question4,question5]
playQuiz(quiz_Questions, name)