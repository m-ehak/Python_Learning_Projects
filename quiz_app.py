import random
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the smallest prime number?": "2",
    "In which year did the Titanic sink?": "1912",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the largest continent by area?": "Asia",
    "How many continents are there on Earth?": "7"
}

score = 0
print("Let's Play a Quiz!")
while True:
    question = random.choice(list(quiz_questions.keys()))
    print(question)
    answer = input("Ans: ")
    if answer == quiz_questions[question]:
        print("Correct Answer!")
        score +=1
        
    else:
       print("Wrong Answer!") 
    print("Your score is now :" , score)    
    cont = input("Do you want to continue playing? : ").lower()
    if cont == "no":
        break
        
    
    