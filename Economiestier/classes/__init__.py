#coding:utf-8
from empresarial import empresas,conta,pessoa,trabalhos;
from Pessoal.dividas import dividas;
import os;
import socket
import sys;


#from empresarial import conta;
#from empresarial import empresas;
#from empresarial.conta import conta;
#from empresarial.pessoa import pessoa;

#from empresarial.* import *;
#import sys
#sys.path.append('./Pessoal')
#from Pessoal.dividas

d1 = dividas();
p1 = pessoa.pessoa();
emp = empresas.empresas();
c1 = conta.conta();
t1= trabalhos.trabalhos();
diasUteis = 30;
diaria = 50.00;
prct=7.5/100.0
c1.setTesouro(5)
def cad(ob):
    if ob.__class__.__name__ == "conta":
        print sys.platform
        print prct

        # Users inormation
        # p1.setNome("alxsy mostovik")
        p1.setNome(raw_input("Nome do Usuario:"))
        #p1.setEmail(raw_input("Email do Usuario:"))
        # Account Information
        c1.setSalario(float(raw_input("Ganho mensal do Investidor:")));
        c1.setInvestimento(float(raw_input("Investimental mensal do Investidor:")));
        c1.setMonths(int(raw_input("quantidade de meses em investimento:")))
#        c1.setPercentualDeNegocio(float(raw_input("Percenteual de Negocio:")))
        c1.setTipoConta(raw_input("Tipo de conta:"));
        d1.setNomeConta(raw_input("Tipo da Conta a Pagar:"))
        d1.setValorConta(float(raw_input("Valor da Conta a Pagar:")))


    else:
        # Companies Information
        emp.setNome("GoldxEngenharia");
        emp.setPhone("98997-8887");
        emp.setEmail("GoldxEngenharia@gmail.com");
        # Account Information
        emp.setSalario(80000.00);
        emp.setInvestimento(2500.00);
        emp.setMonths(12)
        """
        emp.setPercentualDeNegocio(3)
        """
        emp.setTipoConta("basica");
        diasUteis = 30;
        diaria = 50.00;


def imp(ob):
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("cls")
    print "Welcome to Economiester,Gestão Financeira"
    print "\nNome:" + p1.getNome() + \
          "\nEmail:" + p1.getEmail()

    print "\nsalario:%.2f" % c1.getSalario() + \
          "\ninvestimento:%.2f" % c1.getInvestimento() + \
          "\nlucro estimado ao fim do prazo:%.2f" % (c1.getTesouroDireto() * c1.getMonths()) + \
          "\nfaturamento Mensal com TesouroDireto:%.2f" % c1.getTesouroDireto() + \
          "\nfaturamento Diario:%.2f" % (c1.JuroS() * c1.getMonths() / diasUteis)

    print "lucro estimado ao fim do prazo:%.2f" % (c1.JuroS() * c1.getMonths()) + \
          "\nfaturamento Mensal com JurosSimples:%.2f" % c1.JuroS() + \
          "\nfaturamento Diario:%.2f" % (c1.JuroS() * c1.getMonths() / diasUteis)

#c1.setSalario(c1.getSalario() - c1.getInvestimento() - d1.getValorConta())
#print "\nSaldo:%.2f" % c1.getSalario();
print "lucro com alugal de carros:%.2f"%(t1.Aluguel());

    # print  "sinceramente!,pessimo investimento" if(((c1.getSalario() - c1.getInvestimento()) / c1.getMonths()) / 30 < diaria) else "quem sabe pode valer a pena!";
   # print "cada dia equivale a {:.2f}".format(((c1.getSalario() - c1.getInvestimento()) / c1.getMonths()) / 30);

#main
cad(c1);
imp(c1);
