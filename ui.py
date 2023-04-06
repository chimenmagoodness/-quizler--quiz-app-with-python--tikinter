from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from data import parameters


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quiz App")
        self.windows.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_text = Label(text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_text.grid(row=0, column=1)


        # White Background
        self.canvas = Canvas(width=300,  height=300, background="white")
        # Text on the white Background
        self.question_text = self.canvas.create_text(
            150,
            150,
            width=240,
            text="new_question",
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Buttons
        check_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_button_img, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        cancel_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cancel_button_img, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_text.config(text=f"Questions: {self.quiz.question_number}/50")
        if self.quiz.still_has_questions():
            a_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=a_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz \nYour final Score was: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.canvas.itemconfig(self.question_text, fill="white")
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.windows.after(1000, self.get_next_question)