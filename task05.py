def numara_vocale(nume):
   
    # Funcția primește un șir de caractere și returnează numărul de vocale din acesta.

    vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contor = 0
    for caracter in nume:
        if caracter in vocale:
            contor += 1
    return contor

# Program principal
print("Introduceți numele clienților. Programul se oprește dacă introduceți un nume fără vocale.")

while True:
    nume_client = input("Introduceți un nume: ")
    numar_vocale = numara_vocale(nume_client)

    if numar_vocale == 0:
        print("Numele nu conține vocale. Programul se oprește.")
        break
    else:
        print(f"Numele '{nume_client}' conține {numar_vocale} vocale.")
