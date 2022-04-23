from question_model import Question
from data import question_data
from question_brain import QuestionBrain

question_bank = []
#question_bank is a list, question_data is also a list of dictionary
for i in question_data:
    q=i["text"]
    a=i["answer"]
    new_q = Question(q, a) # now new_q is an object
    question_bank.append(new_q)  # now question bank is a list of object

question = QuestionBrain(question_bank)
while question.still_has_question():
    question.new_question()
print(f"Your final score is {question.score}/{question.number}")
