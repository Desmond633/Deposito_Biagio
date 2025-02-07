class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome}: L'unità si sta muovendo.")
    def attacca(self):
        print(f"{self.nome}: L'unità sta attaccando.")

    def ritira(self):
        print(f"{self.nome}: L'unità si sta ritirando.")

class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome}: Costruzione di difese temporanee.")

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome}: Calibrando i pezzi di artiglieria per una maggiore precisione.")
        
class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome}: Esplorazione del territorio in corso.")
        
class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome}: Rifornimento e manutenzione delle unità.")
        
class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome}: Missione di sorveglianza in corso.")