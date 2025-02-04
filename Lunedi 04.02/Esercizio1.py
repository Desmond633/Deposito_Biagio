# 1 definizione della classe Prodotto
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome  # nome del prodotto
        self.costo_produzione = costo_produzione  # costo di produzione
        self.prezzo_vendita = prezzo_vendita  # prezzo di vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione  # restitutzione profitto
# classe parallela Elettronica che eredita da Prodotto
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)  # Iattributi della classe base
        self.garanzia = garanzia  # nuovo attributo specifico per elettronica

# classe parallela Abbigliamento che eredita da Prodotto
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)  # attributi della classe base
        self.materiale = materiale  # nuovo attributo specifico per abbigliamento