from questions import glossary

def check_ans(question, ans, attempts, score):
	"""Takes the arguments, and confirms if the answer provided by user is correct.
	Converts all answers to lower case to make sure the glossary is not case sensitive."""
   
	if glossary[question]['answer'].lower() == ans.lower():
		print(f"Correct Answer! \nYour score is {score + 1}!")
		return True
	else:
		print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
		return False

def print_glossary():
	for question_id, ques_answer in glossary.items():
		for key in ques_answer:
			print(key + ':', ques_answer[key])

print("Capital City Quiz!!")

def intro_msg():
	#Introductory message for the game
	print("Welcome to this fun Capital City Quiz! \nLets see how many capitals of the world you know.")
	print("There are a total of 6 questions, you can skip at any time by typing 'skip.'")
	intro_answer = input("Press any key to play or type 'leave' to leave. ")
	intro_answer = intro_answer.lower()
	if intro_answer == "leave":
		quit()
	else:
		return True

intro = intro_msg()
while True:
	score = 0
	for question in glossary:
		attempts = 3
		while attempts > 0:
			print(glossary[question]['question'])
			answer = input("Enter Answer (To move to the next question, type 'skip') : ")
			answer = answer.lower()
			if answer == "skip":
				break
			check = check_ans(question, answer, attempts, score)
			if check:
				score += 1
				break
			attempts -= 1

	break

print(f"Your final score is {score}!\n")
if score < 6:
	print("In case you want to know the correct answers, they will be below this message.")
	print_dictionary()
else:
	print("Congratulations!")
print("Thanks for playing")
