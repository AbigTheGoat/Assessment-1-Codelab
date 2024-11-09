from operator import index

people = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]


question = input('which person would you like to rizz? ')
question = question.capitalize()
question = people.index(question)
question = people[question]
print(question)
