#encoding utf-8
from conta import conta;
from empresas import empresas;
from pessoa import pessoa;


#Users inormation
p1=pessoa();
p1.setNome("alxsy mostovik")
p1.setEmail("alxsyMostovik@asapo.pt")
#Account Information
c1 = conta();
c1.setSalario(4000.00);
c1.setInvestimento(2500.00);
c1.setMonths(12)
c1.setPercentualDeNegocio(3)
c1.setTipoConta("basica");
diasUteis=30;
diaria=50.00;


#Companies Information
emp= empresas();
emp.setNome("GoldxEngenharia");
emp.setPhone("98997-8887");
emp.setEmail("GoldxEngenharia@gmail.com");
#Account Information
emp.setSalario(80000.00);
emp.setInvestimento(2500.00);
emp.setMonths(12)
emp.setPercentualDeNegocio(3)
emp.setTipoConta("basica");
diasUteis=30;
diaria=50.00;

#main
print "Welcome to Economiester,Gestão Financeira"
print "Nome:"+p1.getNome()+"\nEmail:"+p1.getEmail()
print "salario:" + str(c1.getSalario())+ \
      "\ninvestimento:" + str(c1.getInvestimento()) + \
      "\nlucro em " + str(c1.getMonths()) + " meses:" + str(c1.getSalario() - c1.getInvestimento()) + \
      "\nfaturamento mensal:%.2f" % ((c1.getSalario() - c1.getInvestimento()) / c1.getMonths());



print str(c1.months)+" meses,equivalente a "+str(c1.months*diasUteis)+" diasUteis,onde tudo pode occurer!";
if (((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30<diaria):
    print "sinceramente!,pessimo investimento";
else:
    print "quem sabe pode valer a pena!";

print "cada dia equivale a {:.2f}".format(((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30);

