from tkinter import *
from quiz_brain import QuizBrain

themecolor = "#375362"

class quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quiz time!")
        self.window.config(padx=20, pady=20, bg=themecolor)

        self.score_label=Label(text="Score: 0", fg="white", bg=themecolor)
        self.score_label.grid(row=0, column=1)
        self.canvas= Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text(150, 125, width=285, text="Some Question Text", fill=themecolor, font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueimage=PhotoImage(file="true.png")
        self.true_button = Button(image=trueimage, highlightthickness=0, command=self.truepressed)
        self.true_button.grid(row=2, column=0)

        falseimage=PhotoImage(file="false.png")
        self.false_button = Button(image=falseimage, highlightthickness=0, command=self.falsepressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def truepressed(self):
        self.givefeedback(self.quiz.check_answer("True"))

    def falsepressed(self):
        self.givefeedback(self.quiz.check_answer("False"))

    def givefeedback(self, isright):
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)