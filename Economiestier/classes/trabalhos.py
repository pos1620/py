class trabalhos:
    valor=None;
    termino=None;
    inicio=None;
    tempo=None;


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




    def TempoServico(self):
        return (self.getTermino()-self.getInicio())