#coding:utf-8
#from empresarial import empresas,conta,pessoa,trabalhos;
import os;
import socket
import sys;




from Pessoal.dividas import dividas;
from empresarial import conta,empresas,pessoa,trabalhos

'''
from empresarial.conta import conta;
from empresarial.empresas import empresas;
from empresarial.conta import conta;
from empresarial.pessoa import pessoa;
from empresarial import trabalhos;
'''

#pacote pessoal
d1 = dividas();


#pacote empresarial
'''
c1 = conta();
emp = empresas();
p1 = pessoa();
t1= trabalhos.trabalhos();
'''
c1 = conta.conta();
emp = empresas.empresas();
p1 = pessoa.pessoa();
t1= trabalhos.trabalhos();




diasUteis = 30;
diaria=None;
def cad(ob):
    if ob.__class__.__name__ == "conta":
        diaria=10.00

        # Users inormation
        # p1.setNome("alxsy mostovik")
        p1.setNome(input("Nome do Usuario:"))
        p1.setEmail(input("Email do Usuario:"))
        p1.setPhone(input("Contato:"))
        
        # Account Information
        c1.setSalario(float(input("Ganho mensal do Investidor:")));
        c1.setInvestimento(float(input("Investimental mensal do Investidor:")));
        c1.setMonths(int(input("quantidade de meses em investimento:")))
        c1.setTipoConta(input("Tipo de conta:"));
        if c1.getTipoConta()=="basica":
            c1.setTesouro(15)
        else:
            c1.setTesouro(55);        


    else:
        # Companies Information
        diaria=50.00
        emp.setNome(input("Nome da Enpresa:"))
        emp.setEmail(input("Email da Enpresa:"))
        emp.setPhone(input("Contato:"))
        # Account Information
        emp.setSalario(float(input("Ganho mensal do Investidor:")));
        emp.setInvestimento(float(input("Investimental mensal do Investidor:")));
        emp.setMonths(int(input("quantidade de meses em investimento:")))
        emp.setTipoConta(input("Tipo de conta:"));

            
        

def imp(ob):
    print ("Welcome to Economiester,Gestão Financeira")
    print ("\nNome:" + p1.getNome() + \
          "\nEmail:" + p1.getEmail()+ \
          "\nContato:"+ p1.getPhone())

    print ("\nsalario:%.2f" % c1.getSalario() + \
          "\ninvestimento:%.2f" % c1.getInvestimento() + \
          "\nlucro estimado ao fim do prazo:%.2f" % (c1.getTesouroDireto() * c1.getMonths()) + \
          "\nfaturamento Mensal com TesouroDireto:%.2f" % c1.getTesouroDireto() + \
          "\nfaturamento Diario:%.2f" % (c1.JuroS() * c1.getMonths() / diasUteis))

    print ("lucro estimado ao fim do prazo:%.2f" % (c1.JuroS() * c1.getMonths()) + \
          "\nfaturamento Mensal com JurosSimples:%.2f" % c1.JuroS() + \
          "\nfaturamento Diario:%.2f" % (c1.JuroS() * c1.getMonths() / diasUteis)+ \
          "\nlucro com alugal de carros:%.2f"%(t1.AluguelComNegocio("carro")));

#main
cad(c1);
imp(c1);
