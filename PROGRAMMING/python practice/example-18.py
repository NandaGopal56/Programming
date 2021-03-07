class Question:
    def __init__(self,qid,option,score):
        self.questionId=qid
        self.option=option
        self.score=score
        self.status='Not Answered'

class QuestionPaper:
    def __init__(self,paperid,questions):
        self.paperid=paperid
        self.questionList=questions
    def checkSolutions(self,answers):
        for quid in answers:
            for i in self.questionList:
                if i.questionId==quid:
                    if answers[quid]==i.option:
                        i.status='Correct'
                    else:
                        i.status='Incorrect'

    def findResult(self):
        total=0
        for i in self.questionList:
            if i.status=='Correct':
                total=total+i.score
            elif i.status == 'Incorrect':
                total=total - (i.score*0.1)
        total_mark=0
        for i in self.questionList:
            total_mark+=i.score
        percentage=(total/total_mark)*100

        if percentage > 80:
            return "Pass"
        return "Fail"
    

if __name__ == '__main__':
    count = int(input())
    questions = []            
    for i in range(count):
        qid = int(input())
        option = int(input())
        score = int(input())
        questions.append(Question(qid,option,score))
    q = QuestionPaper(12398,questions)
    answers={}
    ans = int(input())
    for i in range(ans):
        ques = int(input())
        option = int(input())
        answers.update({ques:option})
    q.checkSolutions(answers)
    for question in q.questionList:
        print(question.questionId,question.status)
    print(q.findResult())