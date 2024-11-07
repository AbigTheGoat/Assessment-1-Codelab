
Dictionar = {
"Name": str(input('what is your name?' )),
    
    "Age": str(input('How old are you?' )),

    "Hometown": str(input('wheres your hometown?' ))
}

for key, value in Dictionar.items():
    print(f"{key}, {value}")
