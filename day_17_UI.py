from tkinter import *
from day_17_quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, fg="White")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Text", font=("Arial",20,"italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_image = PhotoImage(file="right.png")
        self.rigt_button = Button(image=check_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.rigt_button.grid(column=0, row=2)

        cross_image = PhotoImage(file="cancel.png")
        self.cancel_btn = Button(image=cross_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.cancel_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz")
            self.rigt_button.config(state="disabled")
            self.cancel_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    
        














