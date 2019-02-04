class conta:
    salario =None;
    investimento=None;
    percentualDeNegocio=1;
    months="";
    tipoConta=None;



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
