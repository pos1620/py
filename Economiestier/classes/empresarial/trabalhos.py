class trabalhos:
    valor=None;
    termino=None;
    inicio=None;
    tempo=None;
    veiculo=2;
    aluguel = 350

    def __init__(self,valor,inicio,termino):
        self.valor=valor;
        self.inicio=inicio;
        self.terminno=termino;



    def __init__(self):
        self.valor;
        self.inicio;
        self.termino;


    def setValor(self,valor):
        self.valor=self;

    def getValor(self):
        return self.valor


    def setTermino(self,termino):
        self.termino=termino;

    def getTermino(self):
        return self.termino;


    def setInicio(self,inicio):
        self.inicio=inicio;

    def getInicio(self):
        return self.inicio;


    def setTempo(self,tempo):
        self.tempo=tempo

    def getTempoo(self):
        return self.tempo

    def setAluguel(self, aluguel):
        self.aluguel = aluguel;

    def getAluguel(self):
        return self.aluguel;

    def setVeiculo(self, veiculo):
        self.veiculo = veiculo;

    def getVeiculo(self):
        return self.veiculo;

    def TempoServico(self):
        return (self.getTermino()-self.getInicio())

    #Alugel pickup
    def Aluguel(self):
        return (self.getVeiculo()*self.getAluguel());