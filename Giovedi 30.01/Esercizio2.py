# Definiamo tre funzioni per calcolare l'area di triangoli, quadrati e rettangoli

def area_triangolo(base, altezza):
    return (base * altezza) / 2  # Moltiplica base e altezza e divide per 2

def area_quadrato(lato):
    return lato * lato  # Eleva il lato al quadrato

def area_rettangolo(base, altezza):
    return base * altezza  # Moltiplica base per altezza

# Definiamo la funzione principale che gestisce il menu e le interazioni con l'utente
def calcolo_area():
    while True:  # Ciclo infinito per far ripetere il menu fino a quando l'utente sceglie di uscire
        print("Benvenuto! Scegli la forma geometrica per calcolare l'area:")
        print("1. Triangolo")
        print("2. Quadrato")
        print("3. Rettangolo")
        print("4. Esci")  # Opzione per terminare il programma

        # L'utente inserisce un numero per selezionare un'opzione
        scelta = int(input("Cosa scegli? (1-4): "))  # L'input viene convertito in un intero

        if scelta == 1:  # Se l'utente ha scelto "1", calcoliamo l'area di un triangolo
            base = float(input("Inserisci la base del triangolo: "))  # Convertiamo l'input in float per i decimali
            altezza = float(input("Inserisci l'altezza del triangolo: "))
            area = area_triangolo(base, altezza)  # Chiamiamo la funzione area_triangolo con i valori inseriti
            print("L'area del triangolo è:", area)  # Stampiamo il risultato
        
        elif scelta == 2:  # Se l'utente ha scelto "2", calcoliamo l'area di un quadrato
            lato = float(input("Inserisci il lato del quadrato: "))
            area = area_quadrato(lato)
            print("L'area del quadrato è:", area)

        elif scelta == 3:  # Se l'utente ha scelto "3", calcoliamo l'area di un rettangolo
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            area = area_rettangolo(base, altezza)
            print("L'area del rettangolo è:", area)

        elif scelta == 4:  # Se l'utente ha scelto "4", usciamo dal programma
            print("Hai deciso di uscire. Arrivederci!")
            break  # Il comando break interrompe il ciclo while e termina la funzione

        else:
            # Se l'utente ha inserito un numero non compreso tra 1 e 4, mostriamo un messaggio di errore
            print("Errore: devi inserire un numero tra 1 e 4. Riprova!")

# Chiamata della funzione per avviare il programma
calcolo_area()
