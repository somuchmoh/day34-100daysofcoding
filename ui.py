from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill="Black",
                                                     font=("Arial", 23, 'italic'), width=270)
        self.canvas.grid(row=2, column=1, columnspan=2)

        self.true = Button()
        true_image = PhotoImage(file="images/true.png")
        self.true.config(image=true_image, highlightthickness=0, borderwidth=0, command=self.answer_true)
        self.true.grid(row=3, column=1)

        self.false = Button()
        false_image = PhotoImage(file="images/false.png")
        self.false.config(image=false_image, highlightthickness=0, borderwidth=0, command=self.answer_false)
        self.false.grid(row=3, column=2, pady=20)

        self.score = Label()
        self.score.config(text="Score: 0", fg="White", bg=THEME_COLOR, font=("Arial", 16), pady=20)
        self.score.grid(row=1, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")

        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
