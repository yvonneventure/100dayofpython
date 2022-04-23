class QuestionBrain:
    def __init__(self,list):
        self.number = 0
        self.score = 0
        self.list = list

    def still_has_question(self):
        # if self.number < len(self.list):
        #     return True
        # else:
        #     return False
        return self.number < len(self.list)


#new_qestion is to get the question_bank list
    def new_question(self):
        current = self.list[self.number]  #current is now getting the first object
        self.number+=1
        uanswer = input(f" Q. {self.number}: {current.text} (True/False): ")
        self.check_answer(uanswer,current.answer)

    def check_answer(self,uanswer, correct):
        if uanswer.lower()==correct.lower():
            print("You got it")
            self.score += 1

        else:
            print("You lose.")
            print(f"correct answer is {correct}")
        print(f"current score is {self.score}/{self.number}")
