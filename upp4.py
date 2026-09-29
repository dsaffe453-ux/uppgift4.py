# UPPGIFT 2
while True:
    text = input("Skriv något (q för att avsluta): ")

    if text == "q":
        break

    print(text)


# UPPGIFT 3
text = input("Skriv något: ")

for i in range(10):
    print(text)


# UPPGIFT 4
for i in range(1, 11):
    print(i)


# UPPGIFT 5
y = int(input("Skriv ett tal: "))

for i in range(1, y + 1):
    print(i)


# UPPGIFT 6
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()


# UPPGIFT 7
tal = int(input("Skriv ett tal: "))
potens = int(input("Skriv exponenten: "))

resultat = 1

for i in range(potens):
    resultat = resultat * tal

print("Svar:", resultat)