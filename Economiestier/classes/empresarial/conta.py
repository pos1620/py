class conta:
    salario=0;
    investimento=0;
    percentualDeNegocio=3/100;
    months="";
    tipoConta=None;
    tesouro=0;
    def __init__(self,salario,investimento,percentual,months,tipoConta):
        self.salario=salario;
        self.investimento=investimento;
        self.percentual=percentual;
        self.months=months;
        self.tipoConta=tipoConta;


    def __init__(self):
        self.salario="";
        self.investimento="";
        self.percentual="";
        self.months="";
        self.tipoConta="";


    #def __init__(self,salario="",investimento="",percentual="",months="",tipoConta=""):


    def getSalario(self):
        return self.salario;


    def setSalario(self,salario):
        self.salario=salario;


    def setInvestimento(self,investimento):
        self.investimento=float(investimento);


    def getInvestimento(self):
        return self.investimento;

    def setPercentualDeNegocio(self, PercentualDeNegocio):
        self.PercentualDeNegocio = PercentualDeNegocio;

    def getPercentualDeNegocio(self):
        return self.percentualDeNegocio;

    def setMonths(self,months):
        self.months=months

    def getMonths(self):
        return self.months-1;

    def setTipoConta(self, tipoConta):
        self.tipoConta = tipoConta;

    def getTipoConta(self):
        return self.tipoConta;

    def setTesouro(self,t):
        self.tesouro+=t
    
    def getTesouro(self):
        return self.tesouro

    def getTesouroDireto(self):
        return self.getTesouro()+self.JuroS()
   

    def getCDI(self):
        return

    def getCDB(self):
        return

    def getSELIC(self):
        return

    def JuroS(self):
        juro=self.getInvestimento()*self.getMonths()*self.getPercentualDeNegocio()
        montante=juro+self.getInvestimento()
        return montante;

    def JuroC(self):
        return self.getTesouro()*2