#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order , along with answer keys
import random
QList={'1 x 21': 21,
 '1 x 28': 28,
 '10 x 1': 10,
 '10 x 19': 190,
 '11 x 11': 121,
 '11 x 4': 44,
 '13 x 11': 143,
 '13 x 12': 156,
 '13 x 18': 234,
 '14 x 15': 210,
 '14 x 21': 294,
 '15 x 23': 345,
 '15 x 5': 75,
 '16 x 13': 208,
 '16 x 26': 416,
 '18 x 29': 522,
 '19 x 11': 209,
 '19 x 22': 418,
 '19 x 6': 114,
 '2 x 23': 46,
 '2 x 24': 48,
 '20 x 2': 40,
 '20 x 7': 140,
 '21 x 12': 252,
 '21 x 21': 441,
 '22 x 1': 22,
 '22 x 11': 242,
 '22 x 19': 418,
 '22 x 3': 66,
 '24 x 24': 576,
 '25 x 22': 550,
 '26 x 24': 624,
 '27 x 20': 540,
 '27 x 24': 648,
 '28 x 12': 336,
 '28 x 16': 448,
 '28 x 19': 532,
 '28 x 21': 588,
 '28 x 28': 784,
 '30 x 28': 840,
 '30 x 8': 240,
 '4 x 30': 120,
 '5 x 18': 90,
 '5 x 2': 10,
 '6 x 9': 54,
 '7 x 12': 84,
 '8 x 16': 128,
 '8 x 18': 144,
 '9 x 7': 63,
 '4 x 12':48}

for quizNum in range(35):
    #create the quiz and answer key files
    quizFile=open('MathQuiz%s.txt'%(quizNum+1),'w')
    answerKeyFile=open('MathQuiz_answers%s.txt'%(quizNum+1),'w')

    #write header for quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+'.'+'Math Multiplication Quiz (Form %s)'.center(200,'.')%(quizNum +1))
    quizFile.write('\n\n')


    #Shuffle questions
    questions=list(QList.keys())
    random.shuffle(questions)

    
    for questionNum in range(50):
        #lopp through all 50 questions
        correctAnswers=QList[questions[questionNum]]
        wrongAnswers=list(QList.values())   
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswers]
        random.shuffle(answerOptions)
        quizFile.write('%s. What is the value of %s\n\n'%(questionNum+1,questions[questionNum]))
        for i in range(4):
            quizFile.write('%s.%s'%('ABCD'[i],answerOptions[i]))
            
            quizFile.write('\n\n')

        answerKeyFile.write('%s.%s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswers)]))
    quizFile.close()
    answerKeyFile.close()

   
    

    
        
    
    
    




    
    


