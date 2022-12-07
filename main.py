#Décodeur...


code = "!',-./0127:?ABCEFJMNPSTUXabcdefghijlmnopqrstuvxyàèéêëô "
print("Entre les deux chiffres collés, sans espaces. La programme renverra le caractère.")
while True:
    try:
        print(code[int(input())])
    except:
        print("Oh oh. La référence n'est pas correcte.")
