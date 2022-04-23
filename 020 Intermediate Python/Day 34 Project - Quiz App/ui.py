THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.window=Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white",highlightthickness=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.score=Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)

        self.quiz = quiz_brain

        self.question_text=self.canvas.create_text(150, 120, width=280,text="", font=("Arial", 20, "normal"))
        self.canvas.grid(column=0, row=1,columnspan=2,pady=50)
        self.true_button=Button(image=true_img,command=self.check_true)
        self.true_button.grid(column=1, row=3)
        self.false_button = Button(image=false_img,command=self.check_false)
        self.false_button.grid(column=0, row=3)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question=self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text=f"{question}")
        else:
            self.canvas.itemconfig(self.question_text,text=f"Game Over")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        








