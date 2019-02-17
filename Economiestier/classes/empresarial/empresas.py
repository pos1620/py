from empresarial.conta import conta;
class empresas(conta):
    nome=None;
    endereco=None;
    email=None;
    phone=None;



    def __init__(self,nome,endereco,email,phone):
        self.nome=nome;
        self.endereco=endereco;
        self.email=email;
        self.phone=phone;



    def __init__(self):
        self.nome;
        self.endereco;
        self.email;
        self.phone;



    def setNome(self,nome):
        self.nome=nome;

    def getNome(self):
        return self.nome;


    def setEndereco(self,endereco):
        self.endereco=endereco;

    def getEndereco(self):
        return self.endereco;

    def setEmail(self,email):
        self.email=email;

    def getEmail(self):
        return self.email;

    def setPhone(self,phone):
        self.phone=phone;

    def getPhone(self):
        return self.phone;
