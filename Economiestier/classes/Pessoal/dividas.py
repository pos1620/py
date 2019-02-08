class dividas():
    nomeConta=None
    valorConta=None
    percentualDeNegocio = 3 / 100;

    def __init__(self,nomeConta,valorConta):
        self.nomeConta=nomeConta
        self.valorConta=valorConta

    def __init__(self):
        self

    def setNomeConta(self,nomeConta):
        self.nome=nomeConta

    def getNomeConta(self):
        return self.nomeConta


    def setValorConta(self,valorConta):
        self.valorConta=valorConta

    def getValorConta(self):
        return self.valorConta


    def FaturaMensal(self):
        return self.getValorConta()+(self.getValorConta()*self.percentualDeNegocio)