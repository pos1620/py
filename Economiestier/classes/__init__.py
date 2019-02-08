#coding:utf-8
#from empresarial import conta;
from empresarial.empresas import empresas;
from empresarial.conta import conta;
from empresarial.pessoa import pessoa;
from Pessoal.dividas import dividas;

#from empresarial.* import *;
#import sys
#sys.path.append('./Pessoal')
#from Pessoal.dividas

d1 = dividas();
p1 = pessoa();
emp = empresas();
c1 = conta();
diasUteis = 30;
diaria = 50.00;



def cad(ob):
    if ob.__class__.__name__ == "conta":
        # Users inormation
        # p1.setNome("alxsy mostovik")
        p1.setNome(raw_input("Nome do Usuario:"))
        p1.setEmail(raw_input("Email do Usuario:"))
        # Account Information
        c1.setSalario(float(raw_input("Ganho mensal do Investidor:")));
        c1.setInvestimento(float(raw_input("Investimental mensal do Investidor:")));
        c1.setMonths(int(raw_input("quantidade de meses em investimento:")))
        c1.setPercentualDeNegocio(float(raw_input("Percenteual de Negocio:")))
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
        emp.setPercentualDeNegocio(3)
        emp.setTipoConta("basica");
        diasUteis = 30;
        diaria = 50.00;

cad(c1);

#main
print "Welcome to Economiester,Gestão Financeira"
print "Nome:"+p1.getNome()+\
      "\nEmail:"+p1.getEmail()
print "salario:%.2f" %c1.getSalario()+ \
      "Saldo:%.2f"%(c1.getSalario()-d1.getValorConta())+\
      "\ninvestimento:%.2f" %c1.getInvestimento() + \
      "\nlucro em " + str(c1.getMonths()) + " meses:%.2f"%(c1.getSalario() - c1.getInvestimento()) + \
      "\nfaturamento mensal:%.2f" % ((c1.getSalario() - c1.getInvestimento()) / c1.getMonths());







#user
#print str(c1.months)+" meses,equivalente a "+str(c1.months*diasUteis)+" diasUteis,onde tudo pode occurer!";
#print "sinceramente!,pessimo investimento" if (((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30<diaria)else"quem sabe pode valer a pena!";
print  (((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30<diaria) and "sinceramente!,pessimo investimento" or "quem sabe pode valer a pena!";
print "cada dia equivale a {:.2f}".format(((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30);

#company

"""
if (((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30<diaria):
    print d1.getNome()
else:
    print "quem sabe pode valer a pena!";
"""

