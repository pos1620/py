from conta import conta;
class pessoa(conta):
    nome=None;
    endereco=None;
    phone=None;
    email=None;
    nasc=None;
    AnoAtual=2222;


    def __init__(self,nome,endereco,phone,email,nasc):
        self.nome=nome;
        self.endereco=endereco;
        self.phone=phone;
        self.email=email;
        self.nasc=nasc;

    def __init__(self):
        self


    def getIdade(self):
        return self.AnoAtual-self.nasc;


    def setEndereco(self,endereco):
        self.endereco=endereco;


    def getEndereco(self):
        return self.endereco;

    def setEmail(self,email):
        self.email=email;

    def getEmail(self):
        self.email=self.getNome()+"@Economiester.com"
        return self.email;


    def setPhone(self,phone):
        self.phone=phone;

    def getPhone(self):
        return self.phone;

    def setNome(self,nome):
        self.nome=nome;

    def getNome(self):
        return self.nome;



