from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.quote_text = self.canvas.create_text(300 / 2, 250 / 2, text="quote", fill=THEME_COLOR,
                                                  font=("Arial", 20, "italic"), width=280)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        check_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=check_img, highlightthickness=0, command=self.press_true)
        self.right_button.grid(column=0, row=2)

        cross_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=cross_img, highlightthickness=0, command=self.press_false)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            return

        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quote_text, text=q_text)

    def press_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
