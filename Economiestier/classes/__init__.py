from conta import conta;

c1 = conta();
c1.setSalario(float(3255));
c1.setMonths(12)
c1.setPercentualDeNegocio(round(3,2))
c1.setInvestimento(round(800,2));
dias=30;
real=180/9;


print "Welcome the Economiestier"

print "salario:" + str(c1.getSalario()) + \
      "\ninvestimento:" + str(c1.getInvestimento()) + \
      "\nlucro em " + str(c1.getMonths()) + " meses:" + str(c1.getSalario() - c1.getInvestimento()) + \
      "\nfaturamento mensal:%.2f" % ((c1.getSalario() - c1.getInvestimento()) / c1.getMonths());

'''
print "seus investimento a longo prazo retornara:"+str(c1.Trial());
print "\nInvestindo "+str(c1.getInvestimento())+" seus investimento no prazo de "+str(c1.months)+" meses,seu lucro retornara:"+str(c1.Trial()+c1.months*4);
print str(c1.getSalario()-c1.getInvestimento())+" a mais do que foi investido";
'''


print str(c1.months)+" meses,equivalente a "+str(c1.months*dias)+" dias,onde tudo pode occurer!";
if (((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30<50):
    print "sinceramente!,pessimo investimento";
else:
    print "quem sabe pode valer a pena!";

print "cada dia equivale a {:.2f}".format(((c1.getSalario() - c1.getInvestimento()) / c1.getMonths())/30);

#print "%.2f"%((c1.getSalario()-c1.getInvestimento())/c1.getMonths());

'''
print str(float(real))+" meses";
print "%.2f"%real;
%((c1.getSalario()-c1.getInvestimento())/c1.getMonths());
print ".:{%.2f}".format(salario);

      "\nfaturamento mensal:"+str((c1.getSalario()-c1.getInvestimento())/c1.getMonths())

'''

