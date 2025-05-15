questions = ("What is the coldest planet ","What is the fastest land animal","What is the largest mammal","Who is the father of computer","WHo is the founder of microsoft","Who is the founder of Space x","Who is the father of physics")

options = (("A. Neptune","B. Saturn","C. Jupiter","D. Mars"),("A. Cheetah","B. Lion","C. Tiger","D. Elephant"),("A. Blue Whale","B. Elephant","C. Giraffe","D. Hippo"),("A. Charles Babbage","B. Alan Turing","C. John von Neumann","D. Ada Lovelace"),("A. Bill Gates","B. Steve Jobs","C. Elon Musk","D. Jeff Bezos"),("A. Elon Musk","B. Jeff Bezos","C. Richard Branson","D. Larry Page"),("A. Isaac Newton","B. Albert Einstein","C. Galileo Galilei","D. Niels Bohr"))

answers = ("A","A","A","A","A","A","A")
question_num = 0
score = 0
guesses = []

for question in questions:
    print("-------------------------")
    print(question)
    print("--------------------------")
    for option in options[question_num]:
        print(option)
    
    
    guess = input("Choose an option(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == "Q":
        break
    elif guess == answers[question_num]:
        print("Correct!!")
        score += 1
    else: 
        print("Incorrect!!")
        print(f"Correct answer: {answers[question_num]}")
    question_num += 1
    
    
for guess in guesses:
    print(guess,end=" ")
    
print()
for answer in answers:
    print(answer,end=" ")
    
score = (score / len(questions)) * 100

print("------------------------")
print(f"Result:{score:.2f}")
print("-------------------------")