from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):#passing the object and determining it's data type (QuizBrain)
        self.quiz = quiz_brain
        self.quiz_score = 0
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0/0", bg=THEME_COLOR, fg="white",font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF")
        self.question_text = self.canvas.create_text(150, 125, text="Quiz text, quiz text",width=250, font=("Arial", 15, "italic"),fill=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2,  pady=50)



        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)


        self.get_next_question()


        self.window.mainloop()#all of the codes must be above this, it makes the GUI not to terminate


    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_pressed(self):
        answer = "False"
        wrong_text = self.quiz.check_answer(answer)

        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.canvas.itemconfig(self.question_text, text=wrong_text)


        self.window.after(3000, self.get_next_question)

    def true_pressed(self):
        answer = "True"
        correct_text = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.canvas.itemconfig(self.question_text, text=correct_text)

        self.window.after(3000, self.get_next_question)


