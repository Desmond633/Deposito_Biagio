# 1 definizione della classe Prodotto
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome  # nome del prodotto
        self.costo_produzione = costo_produzione  # costo di produzione
        self.prezzo_vendita = prezzo_vendita  # prezzo di vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione  # restitutzione profitto