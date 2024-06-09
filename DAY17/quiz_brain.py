class QuizBrain:
    def __init__(self,q_list):
        self.question_num=0
        self.question_list=q_list
        self.score=0
    
    def still_has_que(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False


    def nextQue(self):
        curr=self.question_list[self.question_num]
        self.question_num+=1
        user_ans=input(f"Q.{self.question_num}: {curr.text} (True/False)")
        self.check(user_ans,curr.answer)

    def check(self,user_ans,correct):
        if user_ans.lower()==correct.lower():
            print("CORRECT")
            self.score+=1
        else:
            print("WRONG!!")
        print(f"Correct Answer is: {correct}")
        print(f"Your current score is {self.score}/{self.question_num}")