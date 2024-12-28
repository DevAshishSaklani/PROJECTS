def correctanswer(correct):
    if(A==correct):
        print('The answer is correct')
    else:
        print('the answer is wrong')

money=0

q1=['question of prize rupees 10000','In python list is..........',
'(a)mutable', '(b)immutable','(c)both a and b','(d) none of these' ]
correct1='a' 

for i in range(0,6):
    print(q1[i])
    
A=input("enter the crrect answer:\n")

correctanswer(correct1)

amt1=10000
if(A==correct1):
    money=amt1

q2=['question of prize rupees 30000','In python tuple is .........',
'(a)mutable','(b)immutable','(c)both a and b','(d)none of these']
correct2='b'
for i in range(0,6):
    print(q2[i])
    

A=input("enter the correct :\n")
correctanswer(correct2)
amt2=30000
if(A==correct2):
    money=money+amt2
q3=['question of rupees 50000','what is the capital of India?',
'(a)Bengaluru','(b)Kolakata','(c)Hyderabad','(d)Delhi']

for i in range (0,6):
    print(q3[i])
    

correct3='d'
A=input("enter the correct answer:\n")
correctanswer(correct3)
amt3=50000
if(A==correct3):
    money=money+amt3

print('your won ruppees',money)