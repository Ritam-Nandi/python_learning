questions=["Which animal is known as the 'Ship of the Desert?","How many days are there in a week?","How many hours are there in a day?","How many letters are there in the English alphabet?","Rainbow consist of how many colours?","How many days are there in a year?","How many minutes are there in an hour?"]
answers=["Camel","7","24","26","7","365","60"]

print("How many questions do you want to answer?")
q_nos=(int)(input("Select 1-7 "))

if (q_nos<1 or q_nos>len(questions)):
    quit()

answer_count=0

for i in range(q_nos):
    print(questions[i])
    ans=input("Enter your answer: ")
    if ans==answers[i]:
        answer_count = answer_count + 1
percent = (int)((answer_count*100)/q_nos)

print("Correct answer : %d" % (percent))