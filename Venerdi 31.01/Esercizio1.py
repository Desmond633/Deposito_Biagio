utenti = []

while True:
    print("\nRegistrazione Account")
    username = input("Inserisci un username: ")
    password = input("Inserisci una password (min 6 caratteri, almeno una lettera e un numero): ")
    conferma_password = input("Conferma la password: ")
    
    conta_caratteri = 0
    ha_numero = False
    ha_lettera = False
    
    for char in password:
        conta_caratteri += 1
        if "0" <= char <= "9":
            ha_numero = True
        if ("a" <= char <= "z") or ("A" <= char <= "Z"):
            ha_lettera = True
    
    if password == conferma_password:
        if conta_caratteri >= 6 and ha_lettera and ha_numero:
            utenti.append((username, password))
            print("Registrazione completata con successo!")
        else:
            print("La password non soddisfa i requisiti.")
    else:
        print("Le password non coincidono.")
    
    scelta = input("Vuoi registrare un altro account? (sì/no): ").strip().lower()
    if scelta == "no":
        break

print("\nUtenti registrati:")
for user, pwd in utenti:
    password_oculta = ""
    for _ in pwd:
        password_oculta += "*"
    print("Username: " + user + ", Password: " + password_oculta)
