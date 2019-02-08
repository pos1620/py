class conta:
    salario=None;
    investimento=None;
    percentualDeNegocio=3/100;
    months="";
    tipoConta=None;

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
        return self.PercentualDeNegocio;

    def setMonths(self,months):
        self.months=months

    def getMonths(self):
        return self.months;

    def setTipoConta(self, tipoConta):
        self.tipoConta = tipoConta;

    def getTipoConta(self):
        return self.tipoConta;


    def getLP(self):
        return self.getInvestimento()*self.getPercentualDeNegocio()/100;

    def Trial(self):
        return (self.getLP()+self.getSalario());


    def DiasInvest(self,dias):
        return self.getMonths()*dias;



    def getTesouroDireto(self):
        return (self.getInvestimento()+(self.getInvestimento()*self.percentualDeNegocio));

    def getCDI(self):
        return

    def getCDB(self):
        return

    def getCELIC(self):
        return