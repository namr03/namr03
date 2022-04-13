name = input("What's your name? ")
age = int(input("How old are you? "))
copies = int(input("How many copies do you want? "))
year = 2022+(100-age)
i=1
while i<=copies:
    i+=1
    print(name, "you will be 100 years old in: ", year,"y",'\n')
