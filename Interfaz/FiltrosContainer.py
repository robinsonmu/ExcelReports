class FiltrosContainer():
    def __init__(self, ratName=""):
        self.ratName = ratName
        self.selected = True
        self.valoresTA = set()
        self.hitsMinimos = 0
        self.tomarMsPower = True
        self.msPowerInicial = None
        self.msPowerFinal = None
        # Valores last lac seleccionados
        self.valoresLastLac = dict()
    
    def getSelectedLastLacValues(self):
        return [l for l,v in self.valoresLastLac.items() if v is True]

    def __str__(self):
        return f"<FiltrosContainerValores Rat={self.ratName}, valores ta {self.valoresTA}, hits minimos {self.hitsMinimos} tomar ms power {self.tomarMsPower} valores last lac = {self.valoresLastLac}"