from conta import conta;
from empresas import empresas;

#Users Information
c1 = conta();
c1.setSalario(float(4000));
c1.setMonths(12)
c1.setPercentualDeNegocio(round(3,2))
c1.setInvestimento(round(2500,2));
dias=30;
real=180/9;
diaria=50;

#Companies Information
emp= empresas();

print "Welcome the Economiestier"

print "salario:" + str(c1.getSalario()) + \
      "\ninvestimento:" + str(c1.getInvestimento()) + \
      "\nlucro em " + str(c1.getMonths()) + " meses:" + str(c1.getSalario() - c1.getInvestimento()) + \
      "\nfaturamento mensal:%.2f" % ((c1.getSalario() - c1.getInvestimento()) / c1.getMonths());



print str(c1.months)+" meses,equivalente a "+str(c1.months*dias)+" dias,onde tudo pode occurer!";
if (((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30<diaria):
    print "sinceramente!,pessimo investimento";
else:
    print "quem sabe pode valer a pena!";

print "cada dia equivale a {:.2f}".format(((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30);

