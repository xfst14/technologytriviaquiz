from tkinter import *
from quiz_brain import QuizBrain

themecolor = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Time!")
        self.window.geometry("350x500")
        self.window.config(padx=20, pady=20, bg=themecolor)

        # Score label, centered across top row
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=themecolor,
            font=("Arial", 16, "bold")
        )
        self.score_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Canvas for question
        self.canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            150,
            width=280,
            text="Some Question Text",
            fill=themecolor,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Configure columns for even button spacing
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        # True button
        self.true_image = PhotoImage(file="true.png")
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0, sticky="ew", padx=20, pady=20)

        # False button
        self.false_image = PhotoImage(file="false.png")
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1, sticky="ew", padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

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
