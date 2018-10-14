import random

slowa = ("gdynia","gdansk","sopot")

word = random.choice(slowa)

print("Witaj w grze 'Zgadnij słowo'!")
print("Masz 5 szans na zadanie pytania o obecność litery w wylosowanym słowie\n!")

licznik = 0

while (licznik < 5):
	pytanie = input("Zadaj pierwsze pytanie (literę): ")
	for i in len(word):