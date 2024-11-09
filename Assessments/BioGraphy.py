#Mark Hanherly Abig Cybersec year 1
Dictionar = { #Dictionary is composed of Keys and values that are able to be called out
"Name": str(input('what is your name?' )),
    
    "Age": str(input('How old are you?' )),

    "Hometown": str(input('wheres your hometown?' ))
} 

for key, value in Dictionar.items():
    print(f"{key}, {value}")
