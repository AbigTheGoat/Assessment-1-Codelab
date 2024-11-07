Dictionary = {'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
month = input('Input a Month Number: ')
days = Dictionary.get(month)

if month == '2':
    answer = input('Is it a leap year? yes or no: ')
    answer = answer.lower()
    if answer == 'no':
        days = days - 1
    else:
        days = days

print(days)
