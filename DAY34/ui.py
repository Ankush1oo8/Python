THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *
class QuizzInterface:

    def __init__(self,quiz_brain :QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("QUIZZ MASTER")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score=Label(text="SCORE: 0",fg="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,
                                                    width=280,
                                                    text="Some Question Text",
                                                    fill=THEME_COLOR,
                                                    font=("Arial",20,"italic"))
        self.canvas.grid(pady=50,column=0,row=1,columnspan=2)
        
        true_img=PhotoImage(file="DAY34/images/true.png")
        self.ture_button=Button(image=true_img,command=self.true_pressed)
        self.ture_button.grid(column=0,row=3)

        false_img=PhotoImage(file="DAY34/images/false.png")
        self.false_button=Button(image=false_img,command=self.false_pressed)
        self.false_button.grid(column=1,row=3)


        self.get_next_que()

        self.window.mainloop()
    
    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="YOU HAVE REACHED THE END!!!")
            self.ture_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_que)