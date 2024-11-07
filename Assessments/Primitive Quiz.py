answer = str(input("What is the capital of France? "))
answer = answer.lower()
if answer == 'paris':
    print('Nice youre correct!')
else:
    print('WRONG')
#gotta complete 2nd part (advanced req)
print('Quiz Time!!')

dictionary ={
    "What is the capital of Albania?": 'tirana',
    "What is the capital of Austria?": 'vienna',
    "What is the capital of Belarus?": 'minsk',
    "What is the capital of Belgium?": 'brussels',
    "What is the capital of Bulgaria?": 'sofia',
    "What is the capital of the Czech Republic?": 'prague',
    "What is the capital of Denmark?": 'copenhagen',
    "What is the capital of Finland?": 'helsinki',
    "What is the capital of Germany?": 'berlin',
    "What is the capital of Greece?": 'athens',
    "What is the capital of Ireland?": 'dublin'
}

#assigns values to the things in dictionary
def questionsanswers (question,correct_answer):
    answers = input(question)
    answers = answers.lower() #makes sure that what ever they answer is lowercased
    if answers == correct_answer:
        print('Good job u did amazing!')
    else:
        print('Nuh uh this is WRONG!')

for keys,value in dictionary.items():
    questionsanswers(keys,value)