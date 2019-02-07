class dividas:
    nomeConta=None
    valorConta=None


    def __init__(self):
        pass

    def __init__(self,nomeConta,valorConta):
        self.nomeConta=nomeConta
        self.valor=valorConta

    def setNome(self,nomeConta):
        self.nome=nomeConta

    def getNome(self):
        return self.nomeConta


    def setValor(self,valorConta):
        self.valorConta=valorConta

    def getValor(self):
        return self.valorConta