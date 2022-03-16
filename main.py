from task_template import TEXTS
from collections import Counter

oddelovac = ("=" * 50)

users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

login = input("Enter your username: ")
if login in users:
    heslo = input("Enter your password: ")
    if (login, heslo) in users.items():
           print(oddelovac)
           print("Welcome to the app", login)
           print("We have 3 texts to be analyzed.")
           print(oddelovac)
    else:
        print("Incorrect password, terminating the program...")
        quit()
else:
    print(login, "is unregistered user, terminating the program..")
    quit()

vyber= ("1","2","3")
while True:
    vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
    if vyber_textu not in vyber:
        print("Incorrect number. Try again number btw. 1 and 3.")
    else:
        break


list_textu = list(TEXTS)
vybrany_text = list(list_textu[int(vyber_textu) -1].split())

cista_slova = []

for slovo in vybrany_text:
    ciste_slovo = slovo.strip(",.!?")
    cista_slova.append(ciste_slovo)


list_cistych_slov = list(filter(None, cista_slova))


print(oddelovac)

pocet_slov = 0
title_slova = []
uppercase_slova = []
lowercase_slova = []
ciselne_stringy = []

pocet_slov += len(list(list_cistych_slov ))

print("There are", pocet_slov, "words in the text.")

for slovo in list(list_cistych_slov):
    if slovo.istitle():
        title_slova.append(slovo)
    elif slovo.isupper():
        uppercase_slova.append(slovo)
    elif slovo.islower():
        lowercase_slova.append(slovo)
    elif slovo.isnumeric():
        ciselne_stringy.append(slovo)

print("There are", len(title_slova), "titlecase words")
print("There are", len(uppercase_slova), "uppercase words")
print("There are", len(lowercase_slova), "lowercase words")
print("There are", len(ciselne_stringy), "numeric strings")

list_cisel = []
for cislo in ciselne_stringy:
    list_cisel.append(int(cislo))
print("The sum of all numbers is", sum(list_cisel))
print(oddelovac)
print("LEN", "|", "occurencies", "|", "NR.")
print(oddelovac)

konverze_textu = list(list_cistych_slov )
pouze_slova = []
for slovo in konverze_textu:
    ciste_slovo = slovo.lower()
    pouze_slova.append(len(ciste_slovo))

counts = Counter(pouze_slova)

for key in sorted(counts):
    print("%2s| %s" % (key, counts[key]*"*"), "|", counts[key])